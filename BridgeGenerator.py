from collections import deque

from ES6Visitor import ES6Visitor
import os.path


#TODO: add list of disallowed method names to overrides (C# keywords)
#method names: object
#TODO: add list of disallowed field names
#field names: private
#TODO: Bug, generating same method stub multiple times

class BridgeGenerator(ES6Visitor):


    def __init__(self,outputPath,packageName,overrides):
        super().__init__()
        self.outputpath=outputPath
        self.packageName = packageName
        self.rootOut = outputPath+"/"+packageName
        self.inClass=False
        self.inBody=False
        self.inConstructor = False;
        self.overrides = overrides
        if (not os.path.exists(self.rootOut)):
            os.makedirs(self.rootOut)

    def DoEnterClassDeclaration(self,node):
        filePath = self.outputpath+"/"+node.id.name+".cs"
        self.currentClassname = node.id.name
        self.classVariables = set()
        self.classMethods = set()
        self.fout = open(filePath,"w")
        self.fout.write("""
using Bridge;
using System;
        
        """)
        self.fout.write("""
namespace """+self.packageName)
        self.fout.write("""
{
        """)
        self.fout.write("""
    [External]
    [Namespace(false)] """)
        self.fout.write("""   
    public class """+node.id.name+"""{
""")
        self.inClass=True

    def DoExitClassDeclaration(self,node):
        self.fout.write("""
    }
        """)
        self.fout.write("""
}""")
        self.fout.flush()
        self.fout.close()
        self.inClass = False

    def DoEnterClassBody(self,node):
        self.inBody=True

    def DoExitClassBody(self,node):
        self.inBody=False

    def CheckSymbolOverride(self, pname):
        if ("symbols" in self.overrides):
            if (pname in self.overrides["symbols"]):
                pname =  self.overrides["symbols"][pname]
        return pname

    def GetParamName(self,node):
        if (node.type=="Identifier"):
           return "dynamic "+self.CheckSymbolOverride(node.name)
        elif node.type=="AssignmentPattern":
            return self.GetParamName(node.left)
        elif node.type=="MethodDefinition":
            return self.GetParamName(str(node.key))
        elif node.type=="ObjectExpression":
            return "dynamic optionsObject"
        elif node.type == "ObjectPattern":
            return "dynamic optionsObject"
        elif node.type=="RestElement":
            return "params dynamic[] "+self.CheckSymbolOverride(node.argument.name)
        else:
            raise Exception("Unknown param node type: "+str(node.type))

    def DoEnterMethodDefinition(self,node):
        self.classVariables = set()
        if node.kind == "constructor":
            self.inConstructor = True
        #do override check
        if ("methods" in self.overrides):
            if(self.currentClassname in self.overrides["methods"]):
                if(node.key.name in self.overrides["methods"][self.currentClassname]): # overridden
                    self.fout.write("       "+
                                    self.overrides["methods"][self.currentClassname][node.key.name]+
                                    "\n")

                    return
        #do generation
        if node.key.type=="Identifier":
            if (self.inConstructor):
                self.fout.write("       public "+ self.currentClassname + "(")
            else:
                pname=node.key.name
                altname = self.CheckSymbolOverride(str(pname))
                if (altname!=pname): #need to set alt name
                    self.fout.write("       [Name(\"" +pname +"\")]\n")
                    pname=altname
                self.fout.write("       public dynamic "+pname+"(")
            first=True
            for param in node.value.params:
                if not first:
                    self.fout.write(", ")
                pname = self.GetParamName(param)
                self.fout.write(str(pname))
                first = False
            if self.inConstructor:
                self.fout.write("){}//dummy body\n")
            else:
                self.fout.write("){return null;}//dummy return\n")
        elif node.key.type=="MemberExpression":
            if node.key.object.name=="Symbol":
                if node.key.property.name=="iterator":
                    self.fout.write("       public dynamic this[int i]{ get { return null; } }\n")
                else:
                    raise Exception("Unknown symbol name: "+node.key.property.name)
        else:
            raise Exception("Unknown method type: " + node.key.property.name)
    def DoExitMethodDefinition(self,node):
        if node.kind == "constructor":
            self.inConstructor = False
            for varname in self.classVariables:
                self.fout.write("       public dynamic " + self.CheckSymbolOverride(str(varname)) + ";\n")

    def DoAssignmentExpression(self,node):
        if(self.inConstructor):
            if(node.left.type=="MemberExpression"):
                if(node.left.object.type=="ThisExpression"):
                    self.classVariables.add(node.left.property.name)

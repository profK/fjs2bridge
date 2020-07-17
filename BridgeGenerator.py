from collections import deque

from ES6Visitor import ES6Visitor
import os.path

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

    def GetParamName(self,node):
        if (node.type=="Identifier"):
           return "dynamic "+node.name
        elif node.type=="AssignmentPattern":
            return self.GetParamName(node.left)
        elif node.type=="MethodDefinition":
            return self.GetParamName(str(node.key))
        elif node.type=="ObjectExpression":
            return "optionsObject"
        elif node.type == "ObjectPattern":
            return "optionsObject"
        elif node.type=="RestElement":
            return "params dynamic[] "+node.argument.name
        else:
            raise Exception("Unknown param node type: "+str(node.type))

    def DoEnterMethodDefinition(self,node):
        if node.kind == "constructor":
            self.inConstructor = True
            self.classVariables = set()
        else:
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
                self.fout.write("       public dynamic "+str(node.key.name)+"(")
                first=True
                for param in node.value.params:
                    if not first:
                        self.fout.write(", ")
                    self.fout.write(str(self.GetParamName(param)))
                    first = False
                self.fout.write("){return null;}//dummy return\n")
            elif node.key.type=="MemberExpression":
                if node.key.object.name=="Symbol":
                    if node.key.property.name=="iterator":
                        self.fout.write("       public dynamic this[int i]{get;set;}\n")
                    else:
                        raise Exception("Unknown symbol name: "+node.key.property.name)
            else:
                raise Exception("Unknown method type: " + node.key.property.name)
    def DoExitMethodDefinition(self,node):
        if node.kind == "constructor":
            self.inConstructor = False
            for varname in self.classVariables:
                self.fout.write("       public dynamic " + str(varname) + ";\n")

    def DoAssignmentExpression(self,node):
        if(self.inConstructor):
            if(node.left.type=="MemberExpression"):
                if(node.left.object.type=="ThisExpression"):
                    self.classVariables.add(node.left.property.name)

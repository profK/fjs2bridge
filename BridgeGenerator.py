from collections import deque

from ES6Visitor import ES6Visitor
import os.path

class BridgeGenerator(ES6Visitor):


    def __init__(self,outputPath,packageName):
        super().__init__()
        self.outputpath=outputPath
        self.packageName = packageName
        self.rootOut = outputPath+"/"+packageName
        if (not os.path.exists(self.rootOut)):
            os.makedirs(self.rootOut)

    def DoEnterClassDeclaration(self,node):
        filePath = self.outputpath+"/"+node.id.name+".cs"
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

    def DoExitClassDeclaration(self,node):
        self.fout.write("""
    }
        """)
        self.fout.write("""
}
        """)
        self.fout.flush()
        self.fout.close()
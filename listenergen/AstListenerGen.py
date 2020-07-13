
import os
import sys
from contextlib import redirect_stdout

import hjson

global nodeTypes
nodeTypes= set()
global indent
indent=""

def Indent():
    global indent
    indent+="    "

def Unindent():
    global indent
    indent = indent[:len(indent)-4]
def Print(text):
    global indent
    print(indent + text)

def MakeVisit():
    global indent
    Print("def Visit(self,node):")
    for typename in nodeTypes:
        Print(" if (node.type == \""+typename+"\"):")
        Indent()
        Print("self.DoEnter"+typename + "(node)")
        Print("self.Do" +typename+"(node)")
        Print("self.DoExit" +typename + "(node)")
        Unindent();
def VisitNode(node):
    global indent
    if (not node["type"] in nodeTypes):
        nodeTypes.add(node["type"])
        Print("def DoEnter"+node["type"]+"(self,node):")
        Print("    self.EnterNode("+node["type"]+")")
        Print("def DoExit" + node["type"] + "(self,node):")
        Print("    self.ExitNode(" + node["type"] + ")")
        Print("def Do"+node["type"]+"(self,node):")
        indent+="    "

        for key in node:
            if(isinstance(node[key],dict)):
                VisitNode(node[key])
            elif(isinstance(node[key],list)):
                for subnode in node[key]:
                    VisitNode(subnode)
            else:
              Print("self.Print("+key+":"+"node."+key)

#make astlistener
with open(sys.argv[1],"r",encoding="utf-8") as fin:
    root = hjson.load(fin)
with open(sys.argv[2],"w") as fout:
    with redirect_stdout(fout):
        Print("class "+os.path.splitext(sys.argv[2])[0])
        indent+="    "
        Print("def __init__(self):")
        indent+="    "
        Print("self.indent=\"\"")
        indent = indent[:len(indent)-4]
        Print("""
        def EnterNode(self,name):
            self.Print("Entering "+name)
            self.indent = self.indent+"    "

        def ExitNode(self,name):
            self.indent = self.indent[:len(self.indent)-4]
            self.Print("Exiting "+name)
        """)
        VisitNode(root)
        MakeVisit()
    

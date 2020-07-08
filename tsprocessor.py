import os
import sys

import esprima
import jsonpickle


def do_ts_file(namespace,infilename,inputpath,outputpath):
    try:
        with open(inputpath+"/"+infilename,'r',encoding="utf-8") as fin:
            with open('ast.json','w') as fout:
                ast = esprima.parseScript(fin.read())
                ostdout = sys.stdout
                sys.stdout = fout
                print(ast)
                sys.stdout=ostdout
    except Exception as ex:
        print(ex)

def ProcessTypeScriptFiles(namespaceroot,inputpath,outputpath,extlist=[".ts"],excludelist=[]):
    dirlist = os.listdir(inputpath)
    for entryname in dirlist:
        fileinpath = inputpath+"/"+entryname
        fileoutpath = outputpath + "/"+entryname
        if (os.path.isfile(fileinpath)):
            ext = os.path.splitext(entryname)[1]
            if (ext in extlist):
                if (not entryname in excludelist):
                    do_ts_file(namespaceroot,entryname,inputpath,outputpath)
        elif (os.path.isdir(fileinpath)):
            if (not os.path.isdir(fileoutpath)):
                os.mkdir(fileoutpath)
                ProcessTypeScriptFiles(namespaceroot+"."+entryname,fileoutpath,extlist,excludelist)


import json
import os
import string
import file_utils
from pprint import pprint
from tsprocessor import ProcessTypeScriptFiles;

config = json.load(open('config.json'))

pprint(config)

#make output dir
outputdir=config["outpath"]+"/"+config["namespace"].replace(".","/")
if(not os.path.isdir(outputdir)):
    os.makedirs(outputdir)

ProcessTypeScriptFiles(config["namespace"],config["inputpath"],
                       outputdir,config["extensions"], config["exclude"])
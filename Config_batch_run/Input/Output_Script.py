import os
import commands
import sys
import subprocess
import random
import os.path
import filecmp
import shutil

result=[]
result.append("File Location ---------------------------------> File Status \n")
a=sys.argv[1]
b=sys.argv[2]
DIR=a
OUTPUT_PATH='C:\Users\KANAK\Desktop\Batch_Processing\NetSim_Batch_Automation\NetSim_Batch_Automation_v10.1'
NETSIM_PATH='"'+ b + '"'
os.chdir(DIR)

def filecheck(line):
        name=line+"_Results"
        DIR_C=OUTPUT_PATH + "\\Output\\" + name
        
        if not os.path.exists(DIR_C):
            os.makedirs(DIR_C)
        shutil.copy2(line,DIR_C)
        shutil.copy2('NetSim_Params.bat',DIR_C)
        os.chdir(DIR_C)
        original=line
        overwrite="configuration.netsim"
        os.rename(original,overwrite)
        command = 'NetSim_Params.bat ' + NETSIM_PATH + ' ' + '"' + DIR_C + '"'
        os.system(command)
        os.rename(overwrite,original)
        os.chdir(DIR)
        
with open("filetext.txt") as files:
    content = files.read().splitlines()
    for line in content:
        filecheck(line)
       


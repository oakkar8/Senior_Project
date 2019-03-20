#!/usr/bin/python
import os
path='.'

files = os.listdir(path)

for name in files:
    if name.endswith((".apk","_files")):
        fileName = name[0:len(name)-4] +"_permission.txt"
        checkFileExist = os.path.isfile(fileName)
        if checkFileExist:
            print(fileName+" already exist")
        else:
            os.system("aapt dump permissions "+ name + "> " + fileName) 




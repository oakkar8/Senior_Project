#!/usr/bin/python
import csv
import os
import re


collected_file_path='../final_data/permission_total.csv'
path='../permissionTextFile/'

with open (collected_file_path) as csvfile:
    permissionlist=csv.reader(csvfile,delimiter=',')
    permisison_list=next(permissionlist)

filenames=os.listdir(path)
app_permission_list=[]
for name in filenames:
    name=name.rstrip()
    name=path+name
    f=open(name,'r')
    for line in f:
        line = line.rstrip()
        if(line.startswith("package")):
            line=line.split()[-1]
            app_permission_list.append(line)
        else:
           # if(len(re.findall('[0-9]',line))>0):
            line=line.replace('\'',' ')
            temp=line
            line= line.split()[-1]
            if(len(line)<5):
                line=temp.split()[-3]
            app_permission_list.append(line)
    print app_permission_list[0]
    app_permission_list=[]


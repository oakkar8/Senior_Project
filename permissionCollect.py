#!/usr/bin/python

import os
import csv

path='./permissionTextFile/'
f= open("permissionList.txt","r")
permission_list=set()
for line in f:
    line=line.rstrip()
    permission_list.add(line)

files = os.listdir(path)
write_file=open('test.txt','w')
for name in files:
    name=name.rstrip()
    name=path+name
    f=open(name,"r")
    for line in f:
        line=line.rstrip()
        if("package" in line):
            continue
        else:
            permission_list.add(line)
count=0
permission_list=list(permission_list)
for i in permission_list:
    print(i)
    if(len(i)==0):
        count=count+1


print count
with open('permissionList.csv','w') as csvfile:
    wr = csv.writer(csvfile, dialect='excel')
    wr.writerow(permission_list)

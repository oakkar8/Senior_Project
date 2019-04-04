#!/usr/bin/python

import os
import csv

path='./permissionTextFile/'
permission_list=set()
with open("permissionList.txt","r") as f:
	for line in f:
    		line=line.rstrip()
    		permission_list.add(line)

files = os.listdir(path)
write_file=open('test.txt','w')
for name in files:
   # print(name)
    name=name.rstrip()
    name=path+name
    f=open(name,"r")
    for line in f:
        line=line.rstrip()
        if("package" in line):
            continue
        else:
            if(len(line)!=0):
                permission_list.add(line)
permission_list=list(permission_list)
<<<<<<< HEAD
for i in permission_list:
   # print(i)
    if(len(i)==0):
        count=count+1
	print "count"
=======
print len(permission_list)
permission_list=filter(None,permission_list)
print len(permission_list)
print permission_list[0]
with open('text.txt','w') as txtfile:
    for item in permission_list:
        txtfile.write(item)
        txtfile.write('\n')
>>>>>>> b63855aca7f27e4d0045e01e250be1afb1a9e694
with open('permissionList.csv','w') as csvfile:
    wr = csv.writer(csvfile, dialect='excel')
    wr.writerow(permission_list)

print permission_list

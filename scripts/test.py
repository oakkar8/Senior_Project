#!/usr/bin/python
import re
import os
import csv
path='../permissionTextFile/'
collected_file_path='../collected_permisison/permissionList.txt'
save_file_name='permission_total.txt'
collected_file=open(collected_file_path,'r')

permission_set=set()
for line in collected_file:
    line=line.rstrip()
    permission_set.add(line)

filenames=os.listdir(path)
for name in filenames:
    name=name.rstrip()
    name=path+name
    f=open(name,'r')
    for line in f:
        line=line.rstrip()
        if ("package" in line):
            continue
        else:
           # if(len(re.findall('[0-9]',line))>0):
            line=line.replace('\'',' ')
            temp=line
            line= line.split()[-1]
            if(len(line)<5):
                line=temp.split()[-3]
            permission_set.add(line)
print len(permission_set)
with open(save_file_name,'w') as txtfile:
    for item in permission_set:
        txtfile.write(item)
        txtfile.write('\n')

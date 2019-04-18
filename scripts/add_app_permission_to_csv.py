#!/usr/bin/python
import csv
import os
import re


collected_file_path='../final_data/permission_total_with_malware.csv'
path='../malware_permissions/'
#path='../permissionTextFile/'
cw=csv.writer(open(collected_file_path,'a'))
isBenign=0
def check_permission(permissionlist,app_permission_list,cw):
    permission_list=[0]*len(permissionlist)
    permission_list[0]=app_permission_list[0]
    permission_list[1]=isBenign
    for permission in app_permission_list[1:]:
        index=permissionlist.index(permission)
        permission_list[index]=1

    cw.writerow(permission_list)


with open (collected_file_path,'r') as csvfile:
        print (collected_file_path)
        permissionlist=csv.reader(csvfile,delimiter=',')
        print permissionlist
        permission_list=next(permissionlist)
        #print len(permission_list)
       # print "permisison size"

#print len(permission_list)
#print "outside of open"
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
    check_permission(permission_list,app_permission_list,cw)
    app_permission_list=[]


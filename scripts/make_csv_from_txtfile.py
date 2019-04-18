#!/usr/bin/python
import re
import os
import csv
path='../permissionTextFile/'
malware_path='../malware_permissions/'
collected_file_path='../final_data/permissionList.txt'
collected_file_path2='../final_data/permission_total.txt'
save_file_name='../final_data/permission_total_with_maleware'
collected_file=open(collected_file_path2,'r')

permission_set=set()
for line in collected_file:
    line=line.rstrip()
    permission_set.add(line)

filenames=os.listdir(malware_path)
for name in filenames:
    name=name.rstrip()
    name=malware_path+name
    f=open(name,'r')
    print(name)
    for line in f:
        line=line.rstrip()
        if (line.startswith("package")):
            continue
        else:
            line=line.replace('\'',' ')
            temp=line
            line= line.split()[-1]
            if(len(line)<5):
                line=temp.split()[-3]
            permission_set.add(line)

def save_into_csv_file():
    cw=csv.writer(open(save_file_name+'.csv','w'))
    permission_list=list(permission_set)
    permission_list=["app/title"]+["isBenign"]+permission_list
    print(len(permission_list))
    cw.writerow(permission_list)

def save_into_txt_file():
    with open(save_file_name+'.txt','w') as txtfile:
        for item in permission_set:
            txtfile.write(item)
            txtfile.write('\n')
print("everything Work fine")
#save_into_txt_file()
save_into_csv_file()

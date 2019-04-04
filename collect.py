#!/usr/bin/python

import os
import csv

permissionList = list()
with open("permissionList.txt","r") as f: 
	for line in f: 
		line = line.rstrip()
		permissionList.append(line)

path='./permissionTextFile/'
txtFiles = os.listdir(path)

for name in txtFiles:
	name=name.rstrip()
	name=path+name
	with open(name,"r") as file:
		for line in file:
			line=line.rstrip()
			if("package" in line):
				continue
			elif("TOKEN" in line):
				continue
			elif line in permissionList:
				continue
			else:
				permissionList.append(line)
			
permissionList = filter(None,permissionList)

for i in permissionList:
	print(i)

print(len(permissionList))

with open('permissionList.csv','w') as csvfile:
    wr = csv.writer(csvfile, dialect='excel')
    wr.writerow(permissionList)


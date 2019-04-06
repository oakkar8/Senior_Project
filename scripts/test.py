#!/usr/bin/python

path='../permissionTextFile/'

filename='com.microblink.photomath_permission.txt'

f=open(path+filename,'r')

for line in f:
    line=line.rstrip()
    if ("package" in line):
        continue
    else:
       # print(line)
        line=line.replace('\'',' ')
        line= line.split()[-1]
        print(line)

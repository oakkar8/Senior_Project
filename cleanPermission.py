#!/usr/bin/python
import os
path='.'

files = os.listdir(path)

for name in files:
	if name.endswith((".txt","_files")):
		file = name[0:len(name)-4]
		f = open(name,"r+")
		
		for x in f:
			y = x.replace("uses-permission: name='","")
			z = y.replace("'","")
			
			f.write(z)
		f.close()

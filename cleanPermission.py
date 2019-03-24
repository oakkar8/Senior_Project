#!/usr/bin/python
import os
path='.'

files = os.listdir(path)

for name in files:
	if name.endswith((".txt","_files")):
		file = name[0:len(name)-4]
		with open(name,"r+") as f:
			for x in f:
				y=x.replace("uses-permission: name='","")
				z=y.replace("'","")
				a=z.replace("uses-permission-sdk-23: name=","")
				open(name,'w').close()
			#	wr.write(z)
				f.write(a)

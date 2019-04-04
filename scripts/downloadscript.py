#!/usr/bin/python

import os
path='applicationlink.txt'
gplaycli='~/Documents/Senior_Project/gplaycli-master/gplaycli'
os.system('pwd')
f = open(path,"r")
for line in f:
	line=line.rstrip()
	os.system(gplaycli+" -d " + line + " -f app -p")


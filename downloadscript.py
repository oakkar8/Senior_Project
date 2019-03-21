#!/usr/bin/python

import os
f = open("a.txt","r")

for line in f:
	line=line.rstrip()
	os.system("/anaconda3/envs/py3/bin/gplaycli -d " + line + " -f test")


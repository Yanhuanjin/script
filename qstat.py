#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Date2017年3月7日10:22:27
import os
import time
print(" ---------------------------------------"'\n'
      "| qstat.py_Beta_1.0build by Jinyanhuan  |" '\n'
      " ---------------------------------------"'\n'
       " 2017年3月7日10:55:35\n")
filename = r'./1.txt'
if os.path.exists(filename):
    print("file already exists! contunue.")
    pass
else:
    os.mknod("1.txt")
time.sleep(1.5)
os.system('qstat -f|grep Output_Path|cat > 1.txt')
f = open("1.txt","r")
line = f.readlines()
f.close()
for a in line:
    a = a.strip()
    print(a)
os.remove("1.txt")

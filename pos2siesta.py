#!/usr/bin/env python3
import os 
filename = r'POSCAR'
i=-9
f = open(filename)
with open('constrain_information','a') as g:
    g.write("#Usage: Copy following lines to the end of the 'Input.fdf' to fix the atoms.    # Yan-Huan Jin @ jinyanhuan@gmail.com"
            +"\n%block GeometryConstraints\n")
    g.close()
for line in f.readlines():
    i+=1
    if line.find('F')>0:
        if i>0:
#           print(i)
            with open('constrain_information','a') as g:
                g.write("position from " + str(i)+" to " + str(i) + "\n")
with open('constrain_information','a') as g:
    g.write("%endblock GeometryConstraints")
    g.close()

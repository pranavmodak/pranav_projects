# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:08:43 2020

@author: modak
"""
import time

friend=["meena,ved,jass,arya"]

marks=[60,50,80,99]

addition=0
print("meena-60")
time.sleep(2)
print("ved-50")
time.sleep(2)
print("jass-80")
time.sleep(2)
print("arya-99")
time.sleep(2)
for i in range(4):
    addition=addition+marks[i]
print(addition)

print("I did the total")

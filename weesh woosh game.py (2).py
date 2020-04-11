# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:55:22 2020

@author: alokmodak
"""
num=0

while num<=50:
    num=num+1
    
    if num%3 ==0 and num%5 ==0:
        print("weesh woosh")
    elif num%3 ==0:
        print ("weesh")
    elif num%5 ==0:
        print(num)

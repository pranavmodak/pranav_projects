# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:38:47 2020

@author: pranav modak
"""
usernum= int(input("enter a number: "))
num=0


while num<=50:
    num=num+1
    
    if num%3 ==0 and num%5 ==0:
        print("weesh woosh")
    elif num%3 ==0:
        print ("weesh")
    elif num%5 ==0:
        print(num)
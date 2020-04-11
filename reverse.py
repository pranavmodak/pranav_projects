# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:46:06 2020

@author:pranav modak
"""

print("tell me any numbers and I will make it in reverse order")
input = input("Enter numbers: ")

print("Reverse is: ")
for num in range(len(input)-1, -1, -1):
    print("" + input[num])
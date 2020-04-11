# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:11:10 2020

@author: pranav modak
"""

print("Tell me any three number, I will tell which is the biggest")
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
largest=num1
if num2>largest:
    largest =num2
if num3>largest:
    largest =num3
    
print("The largest number is " + str(largest))
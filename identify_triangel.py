# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:49:59 2020

@author: pranav modak
"""

print ("I will identify the type of triangle for you")
side1=int(input("tell dimention of the side1: "))
side2=int(input("tell dimention of the side2: "))
side3=int(input("tell dimention of the side3: "))
if  side1==side2==side3:
    print ("it is equilateral triangle")
elif side1==side2 or side2==side3 or side1==side3:
    print("it is a isosceles triangle")
if side1!=side2!=side3:
    print("it is a scalene triangle")
    
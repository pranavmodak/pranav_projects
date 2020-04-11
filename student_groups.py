# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:40:26 2020

@author:pranav modak
"""

print("there are 20 students,the teacher needs to divide them in five groups")
rollno=int(input("enter rollno"))
if rollno  in range (1, 5):
    print("you are in group 1")
if rollno  in range (5, 9):
    print("you are in group 2")
if rollno  in range (9, 13):
    print("you are in group 3")
if rollno  in range (13, 17):
    print("you are in group 4")
if rollno  in range (17, 21):    
    print("you are in group 5")
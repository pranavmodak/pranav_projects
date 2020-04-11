# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:21:16 2020

@author: modak
"""

question=["what is capital of maharashtra","where did scientits  made covid-19","how many sides a heptagon has"]

anslist=["mumbai","wuhan","7"]

for i in range(3):
    print(question[i])
    ans=input("your ans")
    
    if ans==anslist[i]:
        print("correct")
    else:
        print("wrong")
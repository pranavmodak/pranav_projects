# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:45:31 2020
 
@author: modak
"""

math=int(input("enter your marks:"))
english=int(input("enter your marks:"))
science=int(input("enter your marks"))
total=math+english+science
if total>75:
    print("you are in grade A")
elif total>60 and total<75:
    print("you are in grade B")  
elif total>45 and total<60:
    print("you are in grade C")
elif total>35 and total<45:
    print ("you are in grade D")
else:
    print("you are fail")
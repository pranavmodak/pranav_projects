# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:30:36 2020

@author: pranav modak
"""

calnum=50
lolimit=0
uplimit=100
step=0
user_response = 0

print("Select a number in your mind, select greater than, lesser than or equal symbols for the questions asked")

while user_response!= "=":
    step=step+1
    
    calnum = int((uplimit+lolimit)/2)
    user_response = input("is your num :"+ str (calnum)+ " ")
    
    if user_response == '<' :
        uplimit = calnum
        
    if user_response == '>' :
        lolimit = calnum
        
print("your num is " + str(step) + " steps")
    
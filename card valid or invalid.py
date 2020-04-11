# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:08:49 2020

@author: modak
"""
import datetime

a=input("Enter your card number:")

if a=="20147":
    tday=datetime.date.today()
    exp=datetime.date(2019,3,31)
    val=exp-tday
    if val.total_seconds()<0 :
        print("Your card is valid")
        
    else :
        print("Your card is invalid")
        
if a=="54785":
    tday=datetime.date.today()
    exp=datetime.date(2020,3,30)
    val=exp-tday
    if val.total_seconds()<0 :
        print("Your card is valid")
      
    else :
        print("Your card is invalid")
        
        
if a=="85742" :
    now=datetime.datetime.now()
    exp=datetime.datetime(2020,4,1,17,0,0,00)
    val=exp-now
    if val.total_seconds()<0 :
        print("Your card is valid")
       
    else :
        print("Your card is invalid")
       

if a=="54654":
    tday=datetime.date.today()
    exp=datetime.date(2020,4,30)
    val=exp-tday
    if val.total_seconds()<0 :
        print("Your card is valid") 
    else :
        print("Your card is invalid")
        


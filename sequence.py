# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:20:04 2020

@author:pranav modak
"""
import datetime
import time
score=0

num1=6
num2=4
num3=7
num4=1
num5=5

print("memorize")
print(num1)
time.sleep(1)
print(num2)
time.sleep(1)
print(num3)
time.sleep(1)
print(num4)
time.sleep(1)
print(num5)
time.sleep(1)

for x in range(10):
    print("*"*x)

t1=datetime.datetime.now()

for x in range(1,6,1):
    ans=int(input("enter number in sequence: "))

    if x==1 and x==6:
        score=score+1
    elif x==2 and x==4:
        score=score+1
    elif x==3 and x ==7:
        score=score+1
    elif x==4 and x==1:
        score=score+1
    else:
        score=score-1
        
t2=datetime.datetime.now()   

delay=t2-t1
print("your score is"+str(score))
print("time you took is:"+str(delay.total_seconds()))


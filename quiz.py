# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:40:43 2020

@author: modak
"""
import datetime
import time

score=0

print("you have 4 seconds to ans the question")
time. sleep(2)

t1=datetime.datetime.now()
print("A. bhubaneswarB.mumbaiC.dehli.dubai")
time.sleep(2)
ans=input("what is the capital of odisha")

if ans=="a":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
t2= datetime.datetime.now()

delay=t2-t1

if delay.total_seconds()>5:
    print("sorry you took more time ,so 'bye'")
    print("time taken"+str(delay.total_seconds()))
else:
    print("you are quick")
    
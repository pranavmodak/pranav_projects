# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:21:56 2020

@author: pranav modak
"""

qnum=0
ans="a,b,c,d"
score = 0

while qnum<5:
    
    qnum=qnum+1
   
    if qnum ==1:
        print("question 1 ")
        print("what is the capital of new zealand")
        print("A:DUBAI B:christchurch C:wellington D:wanganui ")
        ans=input("whats your ans")
        
        if ans in ['c', 'C']:
            print("correct ans")
            print("good job")
            score = score + 1
        else:
             print("wrong ans")   
        
    if qnum ==2:
        print("question 2") 
        print("which plane india is going to purchase in2023")
        print("A:rafel B:rafal C:mig-21 D:L-39 albtros ")
        ans=input("whats your ans")
             
        if ans in ['b', 'B']:
             print("correct ans")
             print("good job")
             score = score + 1
        else:
             print("wrong ans")  
    
    if qnum ==3:
        print("question 3")
        print("which indian satalite is going to study sun") 
        print("A:aditya L-1 B:chandrayaan C:mangalyaan D:gaganyaan ")
        ans=input("whats your ans")
        
        if ans in ['a', 'A']:
             print("correct ans")
             print("good job")
             score = score + 1
        else:
             print("wrong ans")  
        
    if qnum ==4:
        print("question 4")
        print("which city does mumbai to dairet amarica flight goes")   
        print("A:ciatel B:athlanta C:new york D:washington dc ")
        ans=input("whats your ans")
        
        if ans in ['c', 'C']:
             print("correct ans")
             print("good job")
             score = score + 1
        else:
             print("wrong ans")  
        
    if qnum ==5:
        print("question 5")
        print("who was the first person to go to space")
        print("A:kalpana chawla B:neil armstrong C:rakesh sharma D:yuri gagrin ")
        ans=input("whats your ans")
        
        if ans in ['d', 'D']:                
            print("correct ans")
            print("good job")
            score = score + 1
        else:
             print("wrong ans")
             
print ("thank you for playing quiz,your score is ", str(score))
         
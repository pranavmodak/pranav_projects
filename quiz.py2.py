# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:52:02 2020

@author: modak
"""
import time
score=0
print("are you bored of sitting at home, take a quiz")
time.sleep(10)

print("question1")      
print("which is the largest bone in human body?")
print("A.scull: B.femur: C.sineal cod D.ribs")
ans=input("whats your answer:")
time.sleep(5)
if ans=="c" or "C":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 1 over
    
print("question2")      
print("in which city was jesus born?")
print("A.medina: B.mecca: C.bethlehem D.istanbul")
time.sleep(5)
if ans=="c" or "C":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 2 over
    
print("question3")      
print("in which country is cape town located?")
print("A.south africa: B.mongolia: C.chaina D.USA")
ans=input("whats your answer:")
time.sleep(5)
if ans=="a" or "A":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 3 over
    
print("question4")      
print("what food gets its name from the hugarian herdsmen who used to eat it??")
print("A.mussaka: B.souvalki: C.goulash D.tazatazaki")
ans=input("whats your answer:")
time.sleep(5)
if ans=="c" or "C":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 4 over
    
print("question 5")      
print("which holly wood flim director feld to france in 1978?")
print("A.steven pielberg: B.roman polanciki: C.martin scorese D.chirtopher nolan")
ans=input("whats your answer:")
time.sleep(5)
if ans=="B" or "b":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 5 over
    
print("question6")      
print("which north afroican city has a name which merans'white house'in spanish?")
print("A.mellia: B.casabalanca: C.ceuta D.ogoobu")
ans=input("whats your answer:")
time.sleep(5)
if ans=="b" or "B":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 6 over
    
print("question7")      
print("a geyser is what?")
print("A. hot spring: B.flight: C.water fall D.a helicopter")
ans=input("whats your answer:")
time.sleep(5)
if ans=="a" or "A":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 7 over
    
print("question8")      
print("glaglow is a city in which european country")
print("A.england: B.ireland: C.iceland D.sctchland")
ans=input("whats your answer:")
time.sleep(5)
if ans=="d" or "D":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 8 over
    
print("question9")      
print("into which lifeless sea does the river jordon flow?")
print("A.dead sea: B.red sea: C.black sea D.caspian sea")
ans=input("whats your answer:")
time.sleep(5)
if ans=="a" or "A":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 9 over
    
print("question10")      
print("ameerica is song about which of these?")
print("A.a death: B.a marriage: C.an alcohlic D.a road trip")
ans=input("whats your answer:")
time.sleep(5)
if ans=="d" or "D":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 10 over
    
print("question11")      
print("who did the monkeys tell to cheer to cheer up in'daydream bealiver'?")
print("A.sleepy jenny: B.SLEEPY janet C.SLEEPY JON D.sleepy jean")
ans=input("whats your answer:")
time.sleep(5)
if ans=="d" or "D":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 11 over
    
print("question12")      
print("first indian bowler to take hatrick in odi match?")
print("A.kapil dev: B.harbhan singh: C.mohmad shami D.chetan sharma")
ans=input("whats your answer:")
time.sleep(5)
if ans=="D" or "d":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 12 over
    

print("question13")      
print("which state is the highest time winner of santosh trophy in football?")
print("A.goa: B.kerala: C.west bengal D.uttar pradesh")
ans=input("whats your answer:")
time.sleep(5)
if ans=="C" or "c":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 13 over
    
print("question14")      
print("who was the player to be first ODI captain for india ?")
print("A.kapil dev: B.ravi shastri: C.ajit wadekar D.sunil gavaskar")
ans=input("whats your answer:")
time.sleep(5)
if ans=="D" or "d":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 14 over

print("question15")      
print("first indian cricketer to score 75 tests and centuries?")
print("A.kapil dev: B.sachin tendulkar: C.sourav ganguly D.sunil gavaskar")
ans=input("whats your answer:")
time.sleep(5)
if ans=="A" or "a":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    score=score-1
# question 15 over
    
print("your score is"+str(score))
if score>10:
    print("you are inteligent")
elif score>5:
    print("you are but litle studys will work")
elif score<3:
    print("you need lots of studys")
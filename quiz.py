import pyttsx3
import time

score2=0

engine=pyttsx3.init()
engine.setProperty('RATE', 175)

print("are you bored of sitting at home, take a quiz")
engine.say("are you bored of sitting at home, take a quiz")
engine.runAndWait()
time.sleep(1)

print("question1")      
engine.say()
engine.runAndWait()
print("which is the largest bone in human body?")
engine.say()
engine.runAndWait()
print("A.scull: B.femur: C.sineal cod D.ribs")
engine.say()
engine.runAndWait()
ans=input("whats your answer:")
engine.say()
engine.runAndWait()
time.sleep(5)
if ans=="c" or "C":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    engine.say()
    engine.runAndWait()
    score2=score2-1
# question 1 over
    
print("question2")  
engine.say()
engine.runAndWait()    
print("in which city was jesus born?")
engine.say()
engine.runAndWait()
print("A.medina: B.mecca: C.bethlehem D.istanbul")
engine.say()
engine.runAndWait()
ans = input("whats your answer: ").lower()
time.sleep(5)
if ans=="c" or "C":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    engine.say()
    engine.runAndWait()
    score2=score2-1
# question 2 over
    
print("question3")  
engine.say()
engine.runAndWait()    
print("in which country is cape town located?")
engine.say()
engine.runAndWait()
print("A.south africa: B.mongolia: C.chaina D.USA")
engine.say()
engine.runAndWait()
ans=input("whats your answer:")
engine.say()
engine.runAndWait()
time.sleep(5)
if ans=="a" or "A":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    engine.say()
    engine.runAndWait()
    score2=score2-1
# question 3 over
    
print("question4")     
engine.say()
engine.runAndWait() 
print("what food gets its name from the hugarian herdsmen who used to eat it??")
engine.say()
engine.runAndWait()
print("A.mussaka: B.souvalki: C.goulash D.tazatazaki")
engine.say()
engine.runAndWait()
ans=input("whats your answer:")
engine.say()
engine.runAndWait()
time.sleep(5)
if ans=="c" or "C":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    score2=score2-1
# question 4 over
    
print("question 5")      
engine.say()
engine.runAndWait()
print("which holly wood flim director feld to france in 1978?")
engine.say()
engine.runAndWait()
print("A.steven pielberg: B.roman polanciki: C.martin scorese D.chirtopher nolan")
engine.say()
engine.runAndWait()
ans=input("whats your answer:")
engine.say()
engine.runAndWait()
time.sleep(5)
if ans=="B" or "b":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    engine.say()
    engine.runAndWait()
    score2=score2-1
# question 5 over
    
print("question6") 
engine.say()
engine.runAndWait()     
print("which north afroican city has a name which merans'white house'in spanish?")
engine.say()
engine.runAndWait()
print("A.mellia: B.casabalanca: C.ceuta D.ogoobu")
engine.say()
engine.runAndWait()
ans=input("whats your answer:")
engine.say()
engine.runAndWait()
time.sleep(5)
if ans=="b" or "B":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    engine.say()
    engine.runAndWait()
    score2=score2-1
# question 6 over
    
print("question7")  
engine.say()
engine.runAndWait()    
print("a geyser is what?")
engine.say()
engine.runAndWait()
print("A. hot spring: B.flight: C.water fall D.a helicopter")
engine.say()
engine.runAndWait()
ans=input("whats your answer:")
engine.say()
engine.runAndWait()
time.sleep(5)
if ans=="a" or "A":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    engine.say()
    engine.runAndWait()
    score2=score2-1
# question 7 over
    
print("question8")    
engine.say()
engine.runAndWait()  
print("glaglow is a city in which european country")
engine.say()
engine.runAndWait()
print("A.england: B.ireland: C.iceland D.sctchland")
engine.say()
engine.runAndWait()
ans=input("whats your answer:")
engine.say()
engine.runAndWait()
time.sleep(5)
if ans=="d" or "D":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    engine.say()
    engine.runAndWait()
    score2=score2-1
# question 8 over
    
print("question9")      
engine.say()
engine.runAndWait()
print("into which lifeless sea does the river jordon flow?")
engine.say()
engine.runAndWait()
print("A.dead sea: B.red sea: C.black sea D.caspian sea")
engine.say()
engine.runAndWait()
ans=input("whats your answer:")
engine.say()
engine.runAndWait()
time.sleep(5)
if ans=="a" or "A":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    engine.say()
    engine.runAndWait()
    score2=score2-1
# question 9 over
    
print("question10") 
engine.say()
engine.runAndWait()     
print("ameerica is song about which of these?")
engine.say()
engine.runAndWait()
print("A.a death: B.a marriage: C.an alcohlic D.a road trip")
engine.say()
engine.runAndWait()
ans=input("whats your answer:")
engine.say()
engine.runAndWait()
time.sleep(5)
if ans=="d" or "D":
    print("correct ans")
    engine.say()
    engine.runAndWait()
    score2=score2+1
else:
    print("wrong ans")
    engine.say()
    engine.runAndWait()
    score2=score2-1
# question 10 over
    

    
print("your score is"+str(score2))
if score2==10:
    print("you are inteligent")
    engine.say()
    engine.runAndWait()
elif score2>5:
    print("you are but litle studys will work")
    engine.say()
    engine.runAndWait()
elif score2<3:
    print("you need lots of studys")
    engine.say()
    engine.runAndWait()
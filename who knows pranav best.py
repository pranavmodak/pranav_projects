"""who knows pranav best"""
import time
score=0
print("Lets see who knows pranav best!")
time.sleep(1)
print("you will get 10 questions")
time.sleep(1)
print("you will get 5 sec to ans each question")
time.sleep(1)
print("lets see who wins")
time.sleep(1)
print("10")
time.sleep(1)
print("9")
time.sleep(1)
print("8")
time.sleep(1)
print("7")
time.sleep(1)
print("6")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0")
time.sleep(1)

#main program
time.sleep(2)

print("question 1")
print("what does pranav likes in TV promgram")
print("A:pokemon B:ramayan C:Paw petrol D:rusty rivets")
time.sleep(5)
ans=input("whats your answer")

if ans=='d' or ans=='D' :
    print("correct ans")
    score=score+1
else:
    print("wrong answer")
time.sleep(2)

print("question 2")
print("which sweet dish does pranav likes")
print("A:gulabgamoon B:hot choclate sizling brownie C:RASSGULA D:honey noodles with caramel sauce")
time.sleep(5)
ans=input("whats your answer")
if ans=='b' or ans=='B' :
    print("correct ans")
    score=score+1   
else:
    print("wrong answer")
    score=score-1
time.sleep(2)
    
print("question 3")
print("what pranav wants to become in future ")
print("A:cricketer B:footboler C:superhero D:both A andB")
time.sleep(5)
ans=input("whats your answer")
if ans=='D' or ans=='d' :
    print("correct ans")
    score=score+1   
else:
    print("wrong answer")
    score=score-1
time.sleep(2)
    
print("question 4")
print("who was pranav loving in 2013")
print("A:MUMMA B:baba C:aparna aji D:ajoba")
time.sleep(5)
ans=input("whats your answer")
if ans=='C' or ans=='c' :
    print("correct ans")
    score=score+1   
else:
    print("wrong answer")
    score=score-1
time.sleep(2)
    
print("question 5")
print("which fruit pranav loves")
print("A:BOTH B ANDC B:watermelon C:MANGO D:ALL OF THESE")
time.sleep(5)
ans=input("whats your answer")
if ans=='d' or ans=='D' :
    print("correct ans")
    score=score+1   
else:
    print("wrong answer")
    score=score-1
time.sleep(2)
    
print("question 6")
print("if pranav wins a lottery")
print("A:plane B:vila C:diamonds D:banglow")
time.sleep(5)
ans=input("whats your answer")
if ans=='b' or ans=='B' : 
    score=score+1   
else:
    print("wrong answer")
    score=score-1
time.sleep(2)
    
print("question 7")
print("which saeson pranav willl prefer")
print("A:summer B:winter C:spring D:rainy")
time.sleep(5)
ans=input("whats your answer")
if ans=='d' or ans=='D' :
    print("correct ans")
    score=score+1   
else: 
    print("wrong answer")
    score=score-1
time.sleep(2)

    
print("question 8")
print("where would pranav will go if he can")
print("A:dubai B:usa C:taj mahal D:london")
time.sleep(5)
ans=input("whats your answer")
if ans=='B' or ans=='b':
    score= score+1
else:
    print("wrong answer")
time.sleep(2)

print("question 9")
print("what does pranav thinks")
print("A:positive B:negitive C:none of these D:both a and b")
time.sleep(5)
ans=input("whats your answer")
if ans=='D' or ans=='d':
    print("correct answer")
    score= score+1
else:
    print("wrong answer")
time.sleep(2)

print("question 10")
print("what will pranav choose")
print("A:read minds B:be a super hero C:do not be a super hero D:be invisible")
time.sleep(5)
ans=input("whats your answer")
if ans=='b' or ans=='B':
    print("correct answer")
    score= score+1
else:
    print("wrong answer")

print ("your score is"+str(score))
if score>3:
    print("not good")
elif score>5:
    print("i think you know pranav well")
elif score>7:
    print("wow ! nice work")
else:
    print("you know realy well")
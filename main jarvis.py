"""
By Team J.A.R.V.I.S
"""



# greets
facts=["More human twins are being born now than ever before.",
       "A narwhal's tusk reveals its past living conditions.",
       "The first person convicted of speeding was going eight mph.",
       " is the scent of dozens of chemicals."]

greets={"Bonjour its hello in French",
       "Hola its hello in Spanish",
       "Zdravstvuyte its hello in Russian",
       "Nǐn hǎo its hello in Chineese",
       "Salve its hello in Italian",
       "Konnichiwa its hello in Japeneese",
       "Guten Tag its hello in German",
       "Namaste its hello in Hindi"}


byes={"au revoir its bye in French",
      "do svidaniya its bye in Russian",
      "adiós its bye in Spanish",
      "Zàijiàn its bye in Chineese"
      "Zàijiàn its bye in Chineese",
      "addio its bye in Italian",
      "Sayōnara its bye in Japeneese",
      "Tschüss its bye in German",
      "alavida its bye in hindi"}


import pyttsx3
import speech_recognition as sr
import datetime
now = datetime.datetime.now()
import pyjokes
import pywhatkit as kit
import wikipedia
import webbrowser
import random
from playsound import playsound
# import subprocess as sub
import time
import tkinter as tk
# import tkinter.messagebox
# from tkinter import Label
import pickle
# from time import strftime
score2 = 0

def Hereitis():
    print('here it is')
    E.say("Here it is: !")
    E.runAndWait()






    
E=pyttsx3.init()

M = ["What can you see in darkness","what starts with 1 and ends with none","which was the tallest mountain before mount Everest was discovered","what is green but when fallen turns yellow ?","I am a part of your home niether inside nor outside. Who am I ","which month has 28 days ? "]

voices = E.getProperty('voices')
E.setProperty('voice', voices[0].id)


E.setProperty("RATE",175)





print("Allow me to introduce myself!")
E.say("Allow me to introduce myself!")
E.runAndWait()
time.sleep(1)

print("I am JARVIS the virtual artificial intelligence assistant")
E.say("I am JARVIS the virtual artificial intelligence assistant")
E.runAndWait()
time.sleep(1) 

print("And I am here to assist you with tasks as best as I can.")
E.say("And I am here to assist you with tasks as best as I can.")
E.runAndWait()

print("Twenty four hours a day and seven days a week.")
E.say("Twenty four hours a and day seven days a week.")
E.runAndWait()

E.say("I can do a lot of things such as tell you the time, play songs, crack jokes, toss the coin, do mathemathics, do webbrowser searching, wikipeideia, tell ifo about covid and vaccines,   and even tell you information of anything or anyone!")
E.runAndWait()
print("I can do a lot of things such as tell you the time, play songs, crack jokes, toss the coin, do mathemathics, do webbrowser searching, wikipeideia and even tell you information of anything or anyone!")
time.sleep(1)



print("Initializing startup sequence")
E.say("Initializing startup sequence")
E.runAndWait()
playsound('jarvis start sound.mp3')
time.sleep(1)

E.say("You can say, JARVIS at the first to activate me,and then it will start the code")
print("You can say, JARVIS at the first to activate me,and then it will start the code")
E.runAndWait()









try:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak:")
        E.say("Speak")
        E.runAndWait()
        audio=r.listen(source)
    j=r.recognize_google(audio)
    print("You said: "+j)
    
    if "Jarvis" in j:
        
        while True:
            try:
                #Take the user input to activate reception of Voice Commands
                E.say("Press v to start and q to quit: ")
                E.runAndWait()
                userInput=input("Press v to start and q to quit: ").lower()
                
                
                if userInput=='v':
                    
                    #Take Voice commands from mic
                    r=sr.Recognizer()
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        print("Speak: ")
                        E.say("Speak: ")
                        print("Listening. . . . ")
                        E.say(("Listening. . . . "))
                        E.runAndWait()
                        audio=r.listen(source)
                    #Convert Voice Commands to Text
                    command=r.recognize_google(audio)
                    command = command.lower()
                    print("You said : " + command)
                    E.say("You said : " + command)
                    E.runAndWait()
                    
                    
            
            # feature "time"
                    if 'time' in command :
                        print("The current time is: ")
                        E.say("The current time is: ")
                        E.runAndWait()
                        E.say(now.strftime("%H:%M:%S"))
                        print(now.strftime("%H:%M:%S"))
                        E.runAndWait()
                    
                # feature "playing anything"
                    elif 'play' and 'song' in command:
                        play = command.replace('play', '')
                        print("Playing " + play)
                        E.say("playing . ." + play)
                        E.runAndWait()
                        kit.playonyt(play)
                # feature "opening google" 
                    elif 'google' in command :
                        print("opening Google")
                        E.say("opening Google")
                        E.runAndWait()
                        webbrowser.open("www.google.com/")
                    
            # feature "opening youtube"
                    elif 'youtube' in command :
                       print("Opening Youtube")
                       E.say("Opening Youtube")
                       E.runAndWait()
                       webbrowser.open("www.youtube.com/")
               
            # feature "opening team website"
                    elif 'team website' in command:
                         E.say("Opening the team website for you!")
                         E.runAndWait()
                         print("Opening the team website for you!")
                         E.say("Looks like its going well!")
                         print("Looks like its going well!")
                         E.runAndWait()
                         webbrowser.open('https://sites.google.com/view/jarvis-tech-home/home')
        
            
            # feature "To-do list"
                    
                        
                    
            
            # feature "alarm"
                    elif 'alarm' in command:
                            E.say("Type the time! ")
                            E.runAndWait()
                            Alarm =input("Enter the time:- ")
                            print("Alarm has been set for", Alarm)
                            E.say(Alarm)
                            E.runAndWait()
                    
                            while True:
                                try:
                                    Time_Ac = datetime.datetime.now()
                                    now = Time_Ac.strftime("%H:%M")
                                
                                    if now == Alarm:
                                        print()
                                        E.say("come on go to your work! ")
                                        E.runAndWait()
                                        playsound("Alarm.mp3")
                                        time.sleep(5)
                                        pass
                                    
                            #Statement to Handle errors while playing Alarm beep.
                                except sr.UnknownValueError:
                                    print("Sorry, Could not understand.")
                                    E.say("Sorry, Could not understand.")
                                    E.runAndWait()
                                    
                                except sr.RequestError as e:
                                    print("Could not request results; {0}".format(e))
                                    E.say("Could not request results; {0}".format(e))
                                    E.runAndWait()
                                    
                                except KeyboardInterrupt:
                                    print()
                                    
                # feature "maths ChatBot"
                    elif 'mathematics' in command:
                        
                        print("Hello Everyone")
                        E.say("Hello Everyone")
                        E.runAndWait()
                        print("welcome to the mathematical chatbot")
                        E.say("welcome to the mathematical chatbot")
                        E.runAndWait()
                        print("you can do the following functions")
                        E.say("you can do the following functions")
                        E.runAndWait()
                        print("1. Addition, 2. subtraction, 3. multiplication, 4. division, 5. perimeter and 6.area")
                        E.say("1. Addition, 2. subtraction, 3. multiplication, 4. division, 5. perimeter and 6.area")
                        E.runAndWait()
                        
                        ask = input ("what opreation do you want to do: ")
                        E.say("what opreation do you want to do: ")
                        E.runAndWait()
                        
                        E.say("enter option number: ")
                        E.runAndWait()
                        num1 = int(input("Enter Your First Number: "))
                        E.say("Enter Your First Number: ")
                        E.runAndWait()
                        num2 = int(input("Enter Your Second Number: "))
                        E.say("Enter Your Second Number: ")
                        E.runAndWait()
                        
                        if ask =='addition':
                            print("Here is your sum to the question")
                            E.say("Here is your sum to the question")
                            E.runAndWait()
                            print("The answer is: "+ str (num1+num2))
                            E.say("The answer is: "+ str (num1+num2))
                            E.runAndWait()
                            
                        elif ask =='subtraction':
                            print("Here is your sum to the question")
                            E.say("Here is your sum to the question")
                            E.runAndWait()
                            print("The answer is: "+str(num1-num2))
                            E.say("The answer is: "+str(num1-num2))
                            E.runAndWait()
                            
                        elif ask =='multiplication':
                            print("Here is your product to the question")
                            E.say("Here is your product to the question")
                            E.runAndWait()
                            print("The answer is: "+str(num1*num2))
                            E.say("The answer is: "+str(num1*num2))
                            E.runAndWait()
                        
                        elif ask == 'division':
                            print("Here is the quoteint to you answer")
                            E.say("Here is the quoteint to you answer")
                            E.runAndWait()
                            print("The answer is: "+ str(num1/num2))
                            E.say("The answer is: "+ str(num1/num2))
                            E.runAndWait()
                            
                        elif ask =='perimeter': 
                            E.say("select square or rectange: ")
                            E.runAndWait()
                            sorr=input("select square or rectange: ").lower()                         
                            if sorr == "square":
                                
                                a=(num1+num1)
                                b=(num2+num2)
                                print("the perimeter is"+str(a+b))
                                E.say("the perimeter is"+str(a+b))
                                E.runAndWait()
                                
                        elif ask == "rectangle":
                            a=(num1+num1)
                            b=(num2+num2)
                            print("the perimeter is"+str(a+b))
                            E.say("the perimeter is"+str(a+b))
                            E.runAndWait()
                            
                            
                 
                
                        elif ask=="area":
                            print("the area is"+str(num1*num2))
                            E.say("the area is"+str(num1*num2))
                            E.runAndWait()
                    
            
                    # feature "unwell"
                    elif 'unwell' or 'doctor' in command :
                        print("Here are some clinics nearby:-")
                        E.say("Here are some clinics nearby:-")
                        E.runAndWait()
                        webbrowser.open("https://www.google.com/search?q=doctors+near+me&source=hp&ei=zSCeYM7LNt6H4-EPrpWv6Ak&iflsig=AINFCbYAAAAAYJ4u3b1m6yl5YZglXzNhCoeK2dJqyuZT&oq=doctors+&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQsQMQyQMyBQgAEJIDMgUIABCxAzIFCC4QsQMyBQgAELEDMggIABCxAxCDATIFCAAQsQMyCAguEMcBEK8BMggIABCxAxCDATICCAA6CwguELEDEMcBEKMCOggILhCxAxCDAToCCC5QrgZYjh1gvC1oAHAAeACAAcQBiAGJC5IBAzAuOJgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz")
            
                    
                    # feature "physician"
                    elif 'physician' in command:
                        print("Finding physicians nearby!")
                        E.say("Finding physicians nearby!")
                        E.runAndWait()
                        webbrowser.open("https://www.google.com/search?q=physician+near+me&source=hp&ei=zSWeYLnbMOvez7sPzquDoAU&iflsig=AINFCbYAAAAAYJ4z3UFbnwhwH1S2PB7uUkji0QVngyS6&oq=physicians+&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQsQMQyQMQCjIFCAAQkgMyBQgAEJIDMgIIADIHCAAQsQMQCjIECAAQCjICCAAyAggAMgIIADIHCAAQsQMQCjoICAAQsQMQgwE6CAguELEDEIMBOgUIABCxAzoICAAQsQMQyQM6BQguELEDUOIEWJMWYOsnaABwAHgAgAGvAYgBhg6SAQQwLjExmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz")
            
                    # feature "joke"
                    elif 'joke' in command:
                        Hereitis()
                        E.runAndWait()
                        print(pyjokes.get_joke())
                        E.say(pyjokes.get_joke())
                        E.runAndWait()
                    
                    # feature "who is"
                      
                    elif 'who is' in command :
                            person = command.replace('who is', '')
                            info = wikipedia.summary(person, 1)
                            print(info)
                            E.say(info)
                            E.runAndWait()
                    # feature "byes"
                    
                    elif 'bye' in command:
                        bye = random.choice(byes)
                        E.say(bye)
                        print("Bye!")
                        E.runAndWait()
                        break 
                    
                    # feature "what is"
                    elif 'what is' in command :
                        person = command.replace('what is', '')
                        info = wikipedia.summary(person, 1)
                        print(info)
                        E.say(info)
                        E.runAndWait()
                    
                    # feature "fact"
                    elif 'fact' in command:
                        Hereitis()
                        a=random.randint(0,7)
                        mesg=facts[a]
                        E.say(mesg)
                        E.runAndWait()
                        print(mesg)
                      
                        
                      
                    # feature "weather"
                    elif 'weather' in command:
                        print("Here is the weather sir")
                        E.say("Here is the weather sir")
                        E.runAndWait()                        
                        webbrowser.open("https://www.google.com/search?q=temperature&rlz=1C1CHZL_enIN903IN903&oq=tem&aqs=chrome.1.69i57j69i59l2j0i131i433j0i433j69i60l2j69i61.1845j0j7&sourceid=chrome&ie=UTF-8")
            
                    # feature "temp"
                    elif 'temprature' in command:
                        print("Here is temperature sir")
                        E.say("Here is temperature sir")
                        E.runAndWait()
                        webbrowser.open("https://www.google.com/search?q=temperature&rlz=1C1CHZL_enIN903IN903&oq=tem&aqs=chrome.1.69i57j69i59l2j0i131i433j0i433j69i60l2j69i61.1845j0j7&sourceid=chrome&ie=UTF-8")
            
            
                
                    # feature "news"
                    elif 'news' in command:
                        print("Opening times of India for latest news :")
                        E.say("Opening times of India for latest news :")
                        E.runAndWait()
                        webbrowser.open("timesofindia.indiatimes.com")
                    
                    
                    # feature "toss"
                    elif 'toss' in command:
                        
                        t=["heads",'tails']
                        toss=random.choice(t)
                        print("its "+toss)
                        E.say("its " +toss)
                        E.runAndWait()
                        
                    # feature "wake"
                    elif 'wake' in command:
                        print("always ready for you sir! ")
                        E.say("always ready for you sir! ")
                        E.runAndWait()
                    
                    # feature "greeet"
                    
                    
                    
                    # feature "date"
                    elif 'date' in command :
                        print("The current date is: ")
                        E.say("The current date is: ")
                        E.runAndWait()
                        E.say(now.strftime("%D:%M:%Y"))
                        print(now.strftime("%D:%M:%Y"))
                        E.runAndWait()
                        
                    # feature "covid-19"
                    elif 'covid' in command:
                        Hereitis()
                        print("option 1. covid-19 cases")
                        E.say("option 1. covid-19 cases")
                        E.runAndWait()
                        print("option 2. covid-19 precautions")
                        E.say("option 2. covid-19 precautions")
                        E.runAndWait()
                        print("option 3. covid-19 information ")
                        E.say("option 3. covid-19 information ")
                        E.runAndWait()
                        print("option 4. covid-19 vaccines")
                        E.say("option 4. covid-19 vaccines")
                        E.runAndWait()
                        print("option 5 . covid-19 vaccines in pune")
                        E.say("option 5 . covid-19 vaccines in pune")
                        E.runAndWait()
                        
                        covid=input("enter option number: ")
                        if covid == '1':
                            print("Here are covid-19 cases in the world")
                            E.say("Here are covid-19 cases in the world")
                            E.runAndWait()
                            webbrowser.open("https://www.worldometers.info/coronavirus/#countries")
                            
                        elif covid =='2':
                            print("here are the saftey pecaurtions sir")
                            E.say("here are the saftey pecautions sir")
                            E.runAndWait()
                            
                            print("Wear a mask.")
                            E.say("Wear a mask.")
                            E.runAndWait()
                            
                            print("Clean your hands.")
                            E.say("Clean your hands.")
                            E.runAndWait()
                            
                            print("Maintain safe distance.")
                            E.say("Maintain safe distance.")
                            E.runAndWait()
                            
                            print("Get vaccinated.")
                            E.say("Get vaccinated.")
                            E.runAndWait()
                            
                        elif covid=='3':
                            print("Here is some info about covid")
                            E.say("Here is some info about covid")
                            E.runAndWait()
                            
                            print("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.")
                            E.say("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.")
                            E.runAndWait()
                            
                        elif covid == '4':
                            print("here are the vaccines of covid till 20-5-2021")
                            E.say("here are the vaccines of covid till 20-5-2021")
                            E.runAndWait()
                            print("the vaccines are: Sputnik, Pfizer, covaxin and covisheild ")
                            E.say("the vaccines are: Sputnik, Pfizer, covaxin and covisheild ")
                            
                            
                    # feature "Quiz"
                        elif 'quiz' in command:
                            
                            print("aranging a Quiz for you")
                            E.say("aranging a Quiz for you")
                            E.runAndWait()
                            time.sleep(1)
                            
                            print("question1")      
                            E.say()
                            E.runAndWait()
                            print("which is the largest bone in human body?")
                            E.say()
                            E.runAndWait()
                            print("A.scull: B.femur: C.sineal cod D.ribs")
                            E.say()
                            E.runAndWait()
                            ans=input("whats your answer:")
                            E.say()
                            E.runAndWait()
                            time.sleep(5)
                            if ans=="c" or "C":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                E.say()
                                E.runAndWait()
                                score2=score2-1
                            # question 1 over
                                
                            print("question2")  
                            E.say()
                            E.runAndWait()    
                            print("in which city was jesus born?")
                            E.say()
                            E.runAndWait()
                            print("A.medina: B.mecca: C.bethlehem D.istanbul")
                            E.say()
                            E.runAndWait()
                            ans = input("whats your answer: ").lower()
                            time.sleep(5)
                            if ans=="c" or "C":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                E.say()
                                E.runAndWait()
                                score2=score2-1
                            # question 2 over
                                
                            print("question3")  
                            E.say()
                            E.runAndWait()    
                            print("in which country is cape town located?")
                            E.say()
                            E.runAndWait()
                            print("A.south africa: B.mongolia: C.chaina D.USA")
                            E.say()
                            E.runAndWait()
                            ans=input("whats your answer:")
                            E.say()
                            E.runAndWait()
                            time.sleep(5)
                            if ans=="a" or "A":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                E.say()
                                E.runAndWait()
                                score2=score2-1
                            # question 3 over
                                
                            print("question4")     
                            E.say()
                            E.runAndWait() 
                            print("what food gets its name from the hugarian herdsmen who used to eat it??")
                            E.say()
                            E.runAndWait()
                            print("A.mussaka: B.souvalki: C.goulash D.tazatazaki")
                            E.say()
                            E.runAndWait()
                            ans=input("whats your answer:")
                            E.say()
                            E.runAndWait()
                            time.sleep(5)
                            if ans=="c" or "C":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                score2=score2-1
                            # question 4 over
                                
                            print("question 5")      
                            E.say()
                            E.runAndWait()
                            print("which holly wood flim director feld to france in 1978?")
                            E.say()
                            E.runAndWait()
                            print("A.steven pielberg: B.roman polanciki: C.martin scorese D.chirtopher nolan")
                            E.say()
                            E.runAndWait()
                            ans=input("whats your answer:")
                            E.say()
                            E.runAndWait()
                            time.sleep(5)
                            if ans=="B" or "b":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                E.say()
                                E.runAndWait()
                                score2=score2-1
                            # question 5 over
                                
                            print("question6") 
                            E.say()
                            E.runAndWait()     
                            print("which north afroican city has a name which merans'white house'in spanish?")
                            E.say()
                            E.runAndWait()
                            print("A.mellia: B.casabalanca: C.ceuta D.ogoobu")
                            E.say()
                            E.runAndWait()
                            ans=input("whats your answer:")
                            E.say()
                            E.runAndWait()
                            time.sleep(5)
                            if ans=="b" or "B":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                E.say()
                                E.runAndWait()
                                score2=score2-1
                            # question 6 over
                                
                            print("question7")  
                            E.say()
                            E.runAndWait()    
                            print("a geyser is what?")
                            E.say()
                            E.runAndWait()
                            print("A. hot spring: B.flight: C.water fall D.a helicopter")
                            E.say()
                            E.runAndWait()
                            ans=input("whats your answer:")
                            E.say()
                            E.runAndWait()
                            time.sleep(5)
                            if ans=="a" or "A":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                E.say()
                                E.runAndWait()
                                score2=score2-1
                            # question 7 over
                                
                            print("question8")    
                            E.say()
                            E.runAndWait()  
                            print("glaglow is a city in which european country")
                            E.say()
                            E.runAndWait()
                            print("A.england: B.ireland: C.iceland D.sctchland")
                            E.say()
                            E.runAndWait()
                            ans=input("whats your answer:")
                            E.say()
                            E.runAndWait()
                            time.sleep(5)
                            if ans=="d" or "D":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                E.say()
                                E.runAndWait()
                                score2=score2-1
                            # question 8 over
                                
                            print("question9")      
                            E.say()
                            E.runAndWait()
                            print("into which lifeless sea does the river jordon flow?")
                            E.say()
                            E.runAndWait()
                            print("A.dead sea: B.red sea: C.black sea D.caspian sea")
                            E.say()
                            E.runAndWait()
                            ans=input("whats your answer:")
                            E.say()
                            E.runAndWait()
                            time.sleep(5)
                            if ans=="a" or "A":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                E.say()
                                E.runAndWait()
                                score2=score2-1
                            # question 9 over
                                
                            print("question10") 
                            E.say()
                            E.runAndWait()     
                            print("ameerica is song about which of these?")
                            E.say()
                            E.runAndWait()
                            print("A.a death: B.a marriage: C.an alcohlic D.a road trip")
                            E.say()
                            E.runAndWait()
                            ans=input("whats your answer:")
                            E.say()
                            E.runAndWait()
                            time.sleep(5)
                            if ans=="d" or "D":
                                print("correct ans")
                                E.say()
                                E.runAndWait()
                                score2=score2+1
                            else:
                                print("wrong ans")
                                E.say()
                                E.runAndWait()
                                score2=score2-1
                            # question 10 over
                                
                            
                                
                            print("your score is"+str(score2))
                            if score2==10:
                                print("you are inteligent")
                                E.say()
                                E.runAndWait()
                            elif score2>5:
                                print("you are but litle studys will work")
                                E.say()
                                E.runAndWait()
                            elif score2<3:
                                print("you need lots of studys")
                                E.say()
                                E.runAndWait()
                                
                        elif 'vaccines' in command:
                            print("Showing vaccines for age 1 - 18")
                            E.say("Showing vaccines for age 1 - 18")
                            E.runAndWait()
                            
                            print("BCG, OPV 0, Hepatitis B -1 at birth")
                            E.say("BCG, OPV 0, Hepatitis B -1 at birth")
                            E.runAndWait()
                            
                            print("IPV-1, DTwP-1, Hepatitis B -2, Hib -1, Rotavirus 1, PCV 1 at the age of 6 weeks")
                            E.say("IPV-1, DTwP-1, Hepatitis B -2, Hib -1, Rotavirus 1, PCV 1 ata the age of 6 weeks")
                            E.runAndWait()
                            
                            print("DTwP-2, IPV 2, Hib -2, Rotavirus 2, PCV 2 at the age of 10 weeks")
                            E.say("DTwP-2, IPV 2, Hib -2, Rotavirus 2, PCV 2 at the age of 10 weeks")
                            E.runAndWait()
                            
                            print("DTwP-3 , IPV-3 , Hib -3, Rotavirus 3, PCV 3 at the age of 14 weeks")
                            E.say("DTwP-3 , IPV-3 , Hib -3, Rotavirus 3, PCV 3 at the age of 14 weeks")
                            E.runAndWait()
                            
                            print("OPV 1, Hep B 3 at the age of 6 months")
                            E.say("OPV 1, Hep B 3 at the age of 6 months")
                            E.runAndWait()
                            
                            print("OPV 2, MMR-1 at the age of 9 months")
                            E.say("OPV 2, MMR-1 at the age of 9 months")
                            E.runAndWait()
                            
                            print("Typhoid Conjugate Vaccine we can give it between 9 - 12 months")
                            E.say("Typhoid Conjugate Vaccine we can give it between 9 to 12 months")
                            E.runAndWait()
                            
                            print("Hep-A 1 at thhe age of 12 months")
                            E.say("Hep-A 1 at the age of 12 months")
                            E.runAndWait()
                            
                            print("MMR 2, Varicella 1, PCV Booster at the age of 15 months")
                            E.say("MMR 2, Varicella 1, PCV Booster at the age of 15 months")
                            E.runAndWait()
                            
                            print("DTwP  B 1 / DTaP booster -1, IPV B 1, Hib booster 1 can be given in the age between 16 - 18")
                            E.say("DTwP  B 1 / DTaP booster -1, IPV B 1, Hib booster 1 can be given in the age between 16 to 18")
                            E.runAndWait()
                            
                            print("Hep-A 2 at the age of 18 months")
                            E.say("Hep-A 2 at the age of 18 months")
                            E.runAndWait()
                            
                            print("	Booster of Typhoid Conjugate Vaccine at the age of 2 years")
                            E.say("Booster of Typhoid Conjugate Vaccine at the age of 2 years")
                            E.runAndWait()
                            
                            print("	DTwP  B 2 / DTaP booster -2, OPV 3, MMR 3, Varicella 2 it acn be given in between the age of 4 - 6")
                            E.say("DTwP  B 2 / DTaP booster -2, OPV 3, MMR 3, Varicella 2 it acn be given in between the age of 4 - 6")
                            E.runAndWait()
                            
                            print("	Tdap / Td, HPV (Only for females, three doses at 0, 1-2 and 6 months at the age between 10 to 12 years")
                            E.say("Tdap / Td, HPV (Only for females, three doses at 0, 1-2 and 6 months at the age between 10 to 12 years")
                            E.runAndWait()
                
                        elif 'center' in command:
                            print("here are some vaccine centers in pune sir")
                            E.say("here are some vaccine centers in pune sir")
                            E.runAndWait()
                            webbrowser.open("https://www.google.com/search?q=some+vaccine+centres+for+babies+in+pune&safe=active&rlz=1C1CHZL_enIN903IN903&biw=1366&bih=625&ei=Az6mYPrQEoaz9QOoorjYDQ&oq=some+vaccine+centres+for+babies+in+pune&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BQgAEM0CUJFsWJhyYId2aAFwAngAgAHHAYgB9AeSAQMwLjaYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwi63ve9itjwAhWGWX0KHSgRDtsQ4dUDCA4&uact=5")
                        
                        elif 'twitter' in command:
                            print("opening twitter for you sir")
                            E.say('opening twitter for you sir')
                            E.runAndWait()
                            webbrowser.open('twitter.com')
                            
                        else:
                            print("command not found")
                            E.say('command not found')
                            E.runAndWait()
                            
                            
                #Statements to Handle errors while receiving voice commands
                    

            except sr.UnknownValueError:
                print("Sorry, Could not understand.")
                E.say("Sorry, Could not understand.")
                E.runAndWait()
                
            except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
                    E.say("Could not request results; {0}".format(e))
                    E.runAndWait()
                        
                        
            except KeyboardInterrupt:
                break

except sr.UnknownValueError:
    print("Sorry, Could not understand.")
    E.say("Sorry, Could not understand.")
    E.runAndWait()
    
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
    E.say("Could not request results; {0}".format(e))
    E.runAndWait()
    
except KeyboardInterrupt:
    print()   

E.say("Nice interacting with you .")
E.runAndWait()
print("Nice interacting with you!!")
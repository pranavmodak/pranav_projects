# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:04:39 2021

@author: modak_ng8awn0
"""



"""
JARVIS
"""

#lists
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


score2=0    

#importing libaries

import speech_recognition as speech
import pyttsx3
import datetime
import pyjokes
import time
import pywhatkit
import random
from playsound import playsound
import webbrowser
import winsound
import smtplib
#import keysDict as keys
import pygame,sys
import tkinter
import tkinter.messagebox
import pickle
"""inisilizing lib"""

pygame.init()


#defining libraries
#def MyAlarm(timing):
#    import MyAlarm
#    altime=str(datetime.datetime.now().strptime(timing("%I: %M %p ")))
#    print(altime)
    
#    altime=altime[11:-3]
    
#    Horeal=altime[:2]
#    Horeal=int(Horeal)
#    Mireal=altime[3:5]
#    Mireal=int(Mireal)
#    print("Done alarm is set for "+{timing})
#    while True:

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    
    
    server.starttls()
    server.login('modak.pranav10@gmail.com')
    server.sendmail('reciever email' ,EmailTo,content)
    server.close() 
    
def takecommand():
    print()
    

    

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
"""making height of window"""
h=500
w=500

"""setting screen"""
screen=pygame.display.set_mode((h,w))


#initilizing libs
now = datetime.datetime.now()

engine=pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.setProperty("RATE",175)

#starting code
 
#l=random.choice(greets)
#engine.say(l)
#engine.runAndWait()
#print(l)


print("you need to fix alarm greets and byes pygame")
engine.say("you need to fix alarm greets and byes pygame")
engine.runAndWait()

print("Allow me to introduce myself!")
engine.say("Allow me to introduce myself!")
engine.runAndWait()
time.sleep(1)

print("I am JARVIS the virtual artificial intelligence assistant")
engine.say("I am JARVIS the virtual artificial intelligence assistant")
engine.runAndWait()
time.sleep(1) 

print("And I am here to assist you with tasks as best as I can.")
engine.say("And I am here to assist you with tasks as best as I can.")
engine.runAndWait()

print("Twenty four hours a day and seven days a week.")
engine.say("Twenty four hours a and day seven days a week.")
engine.runAndWait()

engine.say("I can do a lot of things such as tell you the time, play songs, crack jokes, toss the coin, do mathemathics, do webbrowser searching, wikipeideia, tell ifo about covid and vaccines,   and even tell you information of anything or anyone!")
engine.runAndWait()
print("I can do a lot of things such as tell you the time, play songs, crack jokes, toss the coin, do mathemathics, do webbrowser searching, wikipeideia and even tell you information of anything or anyone!")
time.sleep(1)



print("Initializing startup sequence")
engine.say("Initializing startup sequence")
engine.runAndWait()
playsound('jarvis start sound.mp3')
time.sleep(1)

engine.say("You can say, JARVIS at the first to activate me,and then it will start the code")
print("You can say, JARVIS at the first to activate me,and then it will start the code")
engine.runAndWait()







    
#starting voice staterup
try:
    r=speech.Recognizer()
    with speech.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak:")
        engine.say("Speak")
        engine.runAndWait()
        audio=r.listen(source)
    j=r.recognize_google(audio)
    print("You said: "+j)
    engine.say("you said: "+j)
    engine.runAndWait()
    if "Jarvis" in j:
        while True:
            
            
             
                
                
                 
             #   for event in pygame.event.get():
              #      if event.type == pygame.QUIT:
              #          pygame.quit()
              #          EventStatus="Quit"
              #          break
       
        
               #     if EventStatus == "Quit":
                #        break
            #background music
            #playsound('background sound1.mp3',False)
            
            try:
                #Take the user input to activate reception of Voice Commands
                
                engine.say("Press v to start voice commands and q to quit: ")
                engine.runAndWait()
                userInput=input("Press v to start voice commands and q to quit: ").lower()
                
                
                if userInput=='v':
                    
                    #Take Voice commands from mic
                    r=speech.Recognizer()
                    with speech.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        print("Speak:")
                        engine.say("Speak")
                        engine.runAndWait()
                        audio=r.listen(source)
                    #Convert Voice Commands to Text
                    command=r.recognize_google(audio)
                    print("You said: "+command)
                    engine.say("you said: "+command)
                    engine.runAndWait()
                    
                    if "wake" in command :
                        engine.say("Up and ready for you sir!")
                        engine.runAndWait()
                        print ("Up and ready for you sir!")   
                    
                    if "time" in command:
                        engine.say("The time is:")
                        engine.say(now.strftime("%H:%M:%S"))
                        engine.runAndWait()
                        
                            
                    if "joke" in command :
                        engine.say("Here it is!")
                        print("Here it is")
                        print(pyjokes.get_joke())
                        engine.say(pyjokes.get_joke())
                        engine.say("ha ha ha")
                        engine.runAndWait()
                        print("Here it is")
                        print(pyjokes.get_joke())
                        
                    if 'play' and 'song' in command:
                            song = command.replace('play', '')
                            engine.say('playing ' + song)
                            print('Playing ' + song)
                            engine.runAndWait()
                            pywhatkit.playonyt(song)
                        
                    if 'who is' in command :
                            person = command.replace('who is', '')
                            webbrowser.open(person)
                            
                            
                        
                    if 'what is' in command :
                            person = command.replace('what is', '')
                            webbrowser.open(person)
                            
                    
                    if 'fact' in command :
                        l=random.choice(facts)
                        engine.say(l)
                        engine.runAndWait()
                        print(l)
                            
                    if 'ready' in command :
                        print("For you sir? Always!")
                        engine.say("For you sir? Always!")
                        engine.runAndWait()
                        
                    if 'toss' in command:
                        toss=random.randint ("Heads", "Tails")
                        print("its "+toss)
                        engine.say("its "+toss)
                        engine.runAndWait()
                        
                    if 'mathematics' in command:
                        engine.say('type the opretion to be done, addition, subtraction, multiplication, perimeter, area or division')
                        engine.runAndWait()
                        try:
                            r=speech.Recognizer()
                            with speech.Microphone() as source:
                                r.adjust_for_ambient_noise(source)
                                print("Speak:")
                                engine.say("Speak")
                                engine.runAndWait()
                                audio=r.listen(source)
                            opreation=r.recognize_google(audio)
                            print("You said: "+opreation)
                            engine.say("you said: "+opreation)
                            engine.runAndWait()
                        
                            num1=int(input("enter your first number or lenght: "))
                            engine.say("enter your first numberor lenght: ")
                            engine.runAndWait()
                            num2=int(input("enter your second number or breath: "))
                            engine.say("enter your second number or breath: ")
                            engine.runAndWait()
                            
                            if opreation=='addition':
                                print("The sum is: "+str(num1+num2))
                                engine.say("The sum is: "+str(num1+num2))
                                engine.runAndWait()
                            
                            if opreation=='subtraction':
                                print("The sum is: "+str(num1-num2))
                                engine.say("The sum is: "+str(num1-num2))
                                engine.runAndWait()
                            
                            if opreation=='multiplication' or 'multiply':
                                print("The product is: "+str(num1*num2))
                                engine.say("The product is: "+str(num1*num2))
                                engine.runAndWait()
                                
                            if opreation=='division':
                                print("The quotient is  is: "+str(num1/num2))
                                engine.say("The quoteint is: "+str(num1/num2))
                                engine.runAndWait()
                                
                            if opreation=='perimeter':
                                engine.say("select square or rectange: ")
                                engine.runAndWait()
                                sorr=input("select square or rectange: ").lower()
                                
                                if sorr == "square":
                                    a=(num1+num1)
                                    b=(num2+num2)
                                    print("the perimeter is"+str(a+b))
                                    engine.say("the perimeter is"+str(a+b))
                                    engine.runAndWait()
                                    
                                if sorr == "rectangle":
                                    a=(num1+num1)
                                    b=(num2+num2)
                                    print("the perimeter is"+str(a+b))
                                    engine.say("the perimeter is"+str(a+b))
                                    engine.runAndWait()
                                    
                                 
                                
                            if opreation=="area":
                                print("the area is"+str(a*b))
                                engine.say("the area is"+str(a*b))
                                engine.runAndWait()
                                
                            else:
                                print("Opreation not found")
                                engine.say("Opreation not found")
                                engine.runAndWait()
                            
                        except speech.UnknownValueError:
                            print("Could not understand audio")
                            engine.say("Could not understand audio")
                            engine.runAndWait()
                            
                        except speech.RequestError as e:
                            print("Could not request results; {0}".format(e))
                            engine.sayprint("Could not request results; {0}".format(e))
                            engine.runAndWait()
                            
                        except KeyboardInterrupt:
                            break
                            
                    if 'unwell' or 'doctor' in command :
                        print("Here are some clinics nearby:-")
                        engine.say("Here are some clinics nearby:-")
                        engine.runAndWait()
                        webbrowser.open("https://www.google.com/search?q=doctors+near+me&source=hp&ei=zSCeYM7LNt6H4-EPrpWv6Ak&iflsig=AINFCbYAAAAAYJ4u3b1m6yl5YZglXzNhCoeK2dJqyuZT&oq=doctors+&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQsQMQyQMyBQgAEJIDMgUIABCxAzIFCC4QsQMyBQgAELEDMggIABCxAxCDATIFCAAQsQMyCAguEMcBEK8BMggIABCxAxCDATICCAA6CwguELEDEMcBEKMCOggILhCxAxCDAToCCC5QrgZYjh1gvC1oAHAAeACAAcQBiAGJC5IBAzAuOJgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz")
                        engine.runAndWait()
                        
                    if 'music' in command:
                        engine.say("I have this music so Not really professional at it sir but I'll still try!")
                        print("I have this music so ot really professional at it sir but I'll still try!")
                        engine.runAndWait()
                        playsound('b.mp3')
                        engine.say("How do you think it was?")
                        print("How do you think it was?")
                        engine.runAndWait()
                        
                    if 'physician' in command:
                        print("Finding physicians nearby!")
                        engine.say("Finding physicians nearby!")
                        engine.runAndWait()
                        webbrowser.open("https://www.google.com/search?q=physician+near+me&source=hp&ei=zSWeYLnbMOvez7sPzquDoAU&iflsig=AINFCbYAAAAAYJ4z3UFbnwhwH1S2PB7uUkji0QVngyS6&oq=physicians+&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQsQMQyQMQCjIFCAAQkgMyBQgAEJIDMgIIADIHCAAQsQMQCjIECAAQCjICCAAyAggAMgIIADIHCAAQsQMQCjoICAAQsQMQgwE6CAguELEDEIMBOgUIABCxAzoICAAQsQMQyQM6BQguELEDUOIEWJMWYOsnaABwAHgAgAGvAYgBhg6SAQQwLjExmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz")
                    
                    if 'nice' in command:
                        print("Thank you for your compliment sir. It matters a lot!")
                        engine.say("Thank you for your compliment sir. It matters a lot!")
                        engine.runAndWait()
                    
                    if 'Google' in command:
                        engine.say('opening google for you')
                        print('opening google for you')
                        engine.runAndWait()
                        webbrowser.open('google.com')
                     
                    if 'news' in command:
                        engine.say('opening news site for you')
                        engine.runAndWait()
                        print('opening news site for you')
                        webbrowser.open('timesofindia.indiatimes.com')
                        
                        news = command.replace('play', '')
                        engine.say('playing ' + news)
                        print('Playing ' + news)
                        engine.runAndWait()
                        pywhatkit.playonyt(news)
                        
                    if 'temperature' in command:
                        print("Here is temperature sir")
                        engine.say("Here is temperature sir")
                        engine.runAndWait()
                        webbrowser.open("https://www.google.com/search?q=temperature&rlz=1C1CHZL_enIN903IN903&oq=tem&aqs=chrome.1.69i57j69i59l2j0i131i433j0i433j69i60l2j69i61.1845j0j7&sourceid=chrome&ie=UTF-8")
                        
                    if 'weather' in command:
                        print("Here is the weather sir")
                        engine.say("Here is the weather sir")
                        engine.runAndWait()                        
                        webbrowser.open("https://www.google.com/search?q=temperature&rlz=1C1CHZL_enIN903IN903&oq=tem&aqs=chrome.1.69i57j69i59l2j0i131i433j0i433j69i60l2j69i61.1845j0j7&sourceid=chrome&ie=UTF-8")
                        
                    if 'alarm' in command:
                        engine.setProperty("RATE",30)
                        engine.say("Type here for what do you want Alarm? ")
                        engine.runAndWait()
                        act = str(input("for what do you want Alarm? :- "))
                        engine.say("Type the time! ")
                        engine.runAndWait()
                        alarmH =input("Enter the time:- ")
                        print("Alarm has been set for ", alarmH)
                        engine.say(alarmH)
                        engine.runAndWait()

                        while True:
                            Time_Ac = datetime.datetime.now()
                            now = Time_Ac.strftime("%H:%M")
                        
                            if now == alarmH:
                                print("time to ", act)
                                engine.say(act)
                                engine.runAndWait()
                                playsound("Alarm.mp3")
                        
                        
                            elif now>alarmH:
                                break
                    
                    if 'youtube' in command:
                        print("opening youtube for you")
                        engine.say("opening youtube for you")
                        engine.runAndWait()
                        webbrowser.open("https://www.youtube.com/")
                    
                    if 'vaccines' in command:
                        print("Showing vaccines for age 1 - 18")
                        engine.say("Showing vaccines for age 1 - 18")
                        engine.runAndWait()
                        
                        print("BCG, OPV 0, Hepatitis B -1 at birth")
                        engine.say("BCG, OPV 0, Hepatitis B -1 at birth")
                        engine.runAndWait()
                        
                        print("IPV-1, DTwP-1, Hepatitis B -2, Hib -1, Rotavirus 1, PCV 1 at the age of 6 weeks")
                        engine.say("IPV-1, DTwP-1, Hepatitis B -2, Hib -1, Rotavirus 1, PCV 1 ata the age of 6 weeks")
                        engine.runAndWait()
                        
                        print("DTwP-2, IPV 2, Hib -2, Rotavirus 2, PCV 2 at the age of 10 weeks")
                        engine.say("DTwP-2, IPV 2, Hib -2, Rotavirus 2, PCV 2 at the age of 10 weeks")
                        engine.runAndWait()
                        
                        print("DTwP-3 , IPV-3 , Hib -3, Rotavirus 3, PCV 3 at the age of 14 weeks")
                        engine.say("DTwP-3 , IPV-3 , Hib -3, Rotavirus 3, PCV 3 at the age of 14 weeks")
                        engine.runAndWait()
                        
                        print("OPV 1, Hep B 3 at the age of 6 months")
                        engine.say("OPV 1, Hep B 3 at the age of 6 months")
                        engine.runAndWait()
                        
                        print("OPV 2, MMR-1 at the age of 9 months")
                        engine.say("OPV 2, MMR-1 at the age of 9 months")
                        engine.runAndWait()
                        
                        print("Typhoid Conjugate Vaccine we can give it between 9 - 12 months")
                        engine.say("Typhoid Conjugate Vaccine we can give it between 9 to 12 months")
                        engine.runAndWait()
                        
                        print("Hep-A 1 at thhe age of 12 months")
                        engine.say("Hep-A 1 at the age of 12 months")
                        engine.runAndWait()
                        
                        print("MMR 2, Varicella 1, PCV Booster at the age of 15 months")
                        engine.say("MMR 2, Varicella 1, PCV Booster at the age of 15 months")
                        engine.runAndWait()
                        
                        print("DTwP  B 1 / DTaP booster -1, IPV B 1, Hib booster 1 can be given in the age between 16 - 18")
                        engine.say("DTwP  B 1 / DTaP booster -1, IPV B 1, Hib booster 1 can be given in the age between 16 to 18")
                        engine.runAndWait()
                        
                        print("Hep-A 2 at the age of 18 months")
                        engine.say("Hep-A 2 at the age of 18 months")
                        engine.runAndWait()
                        
                        print("	Booster of Typhoid Conjugate Vaccine at the age of 2 years")
                        engine.say("Booster of Typhoid Conjugate Vaccine at the age of 2 years")
                        engine.runAndWait()
                        
                        print("	DTwP  B 2 / DTaP booster -2, OPV 3, MMR 3, Varicella 2 it acn be given in between the age of 4 - 6")
                        engine.say("DTwP  B 2 / DTaP booster -2, OPV 3, MMR 3, Varicella 2 it acn be given in between the age of 4 - 6")
                        engine.runAndWait()
                        
                        print("	Tdap / Td, HPV (Only for females, three doses at 0, 1-2 and 6 months at the age between 10 to 12 years")
                        engine.say("Tdap / Td, HPV (Only for females, three doses at 0, 1-2 and 6 months at the age between 10 to 12 years")
                        engine.runAndWait()
                        
                    if 'vaccine center' or 'vaccine centers' in command:
                        print("here are some vaccine centers in pune sir")
                        engine.say("here are some vaccine centers in pune sir")
                        engine.runAndWait()
                        webbrowser.open("https://www.google.com/search?q=some+vaccine+centres+for+babies+in+pune&safe=active&rlz=1C1CHZL_enIN903IN903&biw=1366&bih=625&ei=Az6mYPrQEoaz9QOoorjYDQ&oq=some+vaccine+centres+for+babies+in+pune&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BQgAEM0CUJFsWJhyYId2aAFwAngAgAHHAYgB9AeSAQMwLjaYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwi63ve9itjwAhWGWX0KHSgRDtsQ4dUDCA4&uact=5")
                        
                    if 'covid' or 'covid 19' or 'corona virus' in command:
                        
                        try:
                            r=speech.Recognizer()
                            with speech.Microphone() as source:
                                r.adjust_for_ambient_noise(source)
                                print("Speak:")
                                engine.say("Speak")
                                engine.runAndWait()
                                audio=r.listen(source)
                            opreation=r.recognize_google(audio)
                            print("You said: "+opreation)
                            engine.say("you said: "+opreation)
                            engine.runAndWait()
                            
                            print("option 1. covid-19 cases")
                            engine.say("option 1. covid-19 cases")
                            engine.runAndWait()
                            print("option 2. covid-19 precautions")
                            engine.say("option 2. covid-19 precautions")
                            engine.runAndWait()
                            print("option 3. covid-19 information ")
                            engine.say("option 3. covid-19 information ")
                            engine.runAndWait()
                            print("option 4. covid-19 vaccines")
                            engine.say("option 4. covid-19 vaccines")
                            engine.runAndWait()
                            print("option 5 . covid-19 vaccines in pune")
                            engine.say("option 5 . covid-19 vaccines in pune")
                            engine.runAndWait()
                            
                            covid=input("enter option number: ")
                            if covid == '1':
                                print("Here are covid-19 cases in the world")
                                engine.say("Here are covid-19 cases in the world")
                                engine.runAndWait()
                                webbrowser.open("https://www.worldometers.info/coronavirus/#countries")
                                
                            if covid =='2':
                                print("here are the saftey pecaurions sir")
                                engine.say("here are the saftey pecaurions sir")
                                engine.runAndWait()
                                
                                print("Wear a mask.")
                                engine.say("Wear a mask.")
                                engine.runAndWait()
                                
                                print("Clean your hands.")
                                engine.say("Clean your hands.")
                                engine.runAndWait()
                                
                                print("Maintain safe distance.")
                                engine.say("Maintain safe distance.")
                                engine.runAndWait()
                                
                                print("Get vaccinated.")
                                engine.say("Get vaccinated.")
                                engine.runAndWait()
                                
                            if covid=='3':
                                print("Here is some info about covid")
                                engine.say("Here is some info about covid")
                                engine.runAndWait()
                                
                                print("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.")
                                engine.say("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.")
                                engine.runAndWait()
                                
                            if covid == '4':
                                print("here are the vaccines of covid till 20-5-2021")
                                engine.say("here are the vaccines of covid till 20-5-2021")
                                engine.runAndWait()
                            
                            if covid == '5':
                                print("Here are the centers for covid 19 vaccine")
                                engine.say("Here are the centers for covid 19 vaccine")
                                engine.runAndWait()
                                
                            else:
                                print("Command not found")
                                engine.say("Command not found")
                                engine.runAndWait()
                            
                        except speech.UnknownValueError:
                            print("Could not understand audio")
                            engine.say("Could not understand audio")
                            engine.runAndWait()
                            
                        except speech.RequestError as e:
                            print("Could not request results; {0}".format(e))
                            engine.sayprint("Could not request results; {0}".format(e))
                            engine.runAndWait()
                            
                        except KeyboardInterrupt:
                            break
                        
                    if 'quiz' in command:
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
                        
                    if 'twitter ' in command:
                        print("opening twitter for you sir")
                        engine.say(("opening twitter for you sir"))
                        engine.runAndWait()
                        webbrowser.open("https://twitter.com/?lang=en")
                    
                    if 'stupid' in command :
                        engine.say("Sorry sir, but I am not.")
                        engine.runAndWait()
                   
                    if 'email' in command :
                        try:
                            EmailTo=input("Enter The email id to the person you want to send email: ")
                            content=input("what sould i say sir?: ")
                            content=takecommand()
                            to=EmailTo
                            sendEmail(to, content)
                            engine.say("The email has been sent")
                            engine.runAndWait()
                    
                        except speech.UnknownValueError:
                            print("Could not understand audio")
                        except speech.RequestError as e:
                            print("Could not request results; {0}".format(e))
                        except KeyboardInterrupt:
                            break
                        
                    if 'you eat' in command:
                        engine.say("Thank you for showing a concern for me sir!")
                        engine.runAndWait()
                        engine.say("I love feasting on information! I start with an appetiser of facts , a main course of trivia, followed by a desert of jokes and poems!")
                        engine.runAndWait()
                        
                    if 'awesome' in command:
                        engine.say("My pleasure sir!")
                        engine.runAndWait()
                    
                    if 'created' in command:
                            engine.say("Its you sir!")
                            engine.runAndWait()
                    
                    if 'how are you' in command :
                            engine.say("I am awesome, and ready to take down your targets sir.")
                            engine.runAndWait()
                            
                    if 'be back' in command:
                            engine.say('Ok sir! Here for you everytime!')
                            engine.runAndWait()
                            
                    if 'here' in command:
                            engine.say("Welcome back sir!")
                            engine.runAndWait()
                            
                    if 'website' in command:
                            engine.say("Opening the team website for you sir!")
                            engine.say("Looks like its going well!")
                            engine.runAndWait()
                            webbrowser.open('https://sites.google.com/view/jarvis-tech-home/home')
                            
                    if 'respond' in command :
                            engine.say("At your service sir!")
                            engine.runAndWait()
                            
                    if 'serious' in command :
                        engine.say("Yes sir of course I am serious I am not made for humor")
                        engine.runAndWait()
                     
                    if "todo"  in command:
                        root = tkinter.Tk()
                        root.title("Your To do List. ")
                        
                        
                        
                        # Create GUI
                        frame_tasks = tkinter.Frame(root)
                        frame_tasks.pack()
                        
                        listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
                        listbox_tasks.pack(side=tkinter.LEFT)
                        
                        scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
                        scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
                        
                        listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
                        scrollbar_tasks.config(command=listbox_tasks.yview)
                        
                        entry_task = tkinter.Entry(root, width=50)
                        entry_task.pack()
                        
                        button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
                        button_add_task.pack()
                        
                        button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
                        button_delete_task.pack()
                        
                        button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
                        button_load_tasks.pack()
                        
                        button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
                        button_save_tasks.pack()
                        
                        root.mainloop()
                    else:
                        print("Command not found")
                        engine.say("Command not found")
                        engine.runAndWait()
                        
                    
                else:
                    
                    break
            
        #Statements to Handle errors while receiving voice commands
        
            except speech.UnknownValueError:
                print("Could not understand audio")
                engine.say("Could not understand audio")
                engine.runAndWait()
                
            except speech.RequestError as e:
                print("Could not request results; {0}".format(e))
                engine.say("Could not request results; {0}".format(e))
                engine.runAndWait()
                
            except KeyboardInterrupt:
                break
            
except speech.UnknownValueError:
    print("Could not understand audio")
    engine.say("Could not understand audio")
    engine.runAndWait()
    
except speech.RequestError as e:
    print("Could not request results; {0}".format(e))
    engine.say("Could not request results; {0}".format(e))
    engine.runAndWait()
    
except KeyboardInterrupt:
    print()
    
#ending statment

playsound('jarvis end sound.mp3',False)

c=random.choice[byes]
print(c)
engine.say(c)
engine.runAndWait()

engine.say("Nice interacting with you sir.")
engine.runAndWait()
print("Nice interacting with you!!")
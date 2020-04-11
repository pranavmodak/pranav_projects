# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:29:45 2020

@author: modak
"""
import pyttsx3
import speech_recognition as Covexa

engine = pyttsx3.init() # object creation

speak=("Covexa")

listening=0 #On or Off


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
                       #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
                     #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female (italian acccent)


while listening == 0:
    AudioIn=Covexa.Recognizer()
    with Covexa.Microphone() as source :
      print("I am switched on")
      engine.say("I am switched on")
      engine.runAndWait()
      audio=AudioIn.listen(source)
    command=AudioIn.recognize_google(audio)

if "covexa" in command :
    listening=listening+1
    print("What do you want to know about Covid-19")
    engine.say("What do you want to know about Covid nineteen")
    engine.runAndWait()
    print("I am with you, you can ask")
    engine.say("I am with you, you can ask")
    engine.runAndWait()

while listening == 1 :

    AudioIn=Covexa.Recognizer()
    with Covexa.Microphone() as source:

         print( "Go ahead.")
         engine.say("go ahead")
         engine.runAndWait()
         audio=AudioIn.listen(source)
    command=AudioIn.recognize_google(audio)


    if "sanitizer" in command :
        print ( "You should use an alcoholic hand sanitizer to kill germs")
        engine.say("You should use an alcoholic hand sanitizer to kill germs")
        engine.runAndWait()


    if "what" and "corona virus" in command :
        print("It is a new virus that has a mortality rate of 1.38%")
        engine.say("It is a new virus that has a mortality rate of 1.38%")
        engine.runAndWait()

    if "what" and "symptoms" and "corona virus" in command :
        print ("The symptoms of COVID-19 include dry cough, fever, fatigue,Severe Acute Respiratory Sindrome ,etc")
        engine.say("The symptoms of Covid nineteen include dry cough, fever, fatigue, Severe Acute Respiratory Sindrome, etc")
        engine.runAndWait()


    if "cure" and "corona virus" in command :
        print ("A cure to Corona Virus is not found yet")
        engine.say ("A cure to Corona Virus is not found yet")
        engine.runAndWait()

    if "prevent" and "corona virus" in command :
        print ("You should always wash your hands with soap and water, you should not restrain from touching things and quarantine yourself if you are ill and if you are in a Corona Virus Affrected area")
        engine.say("You should always wash your hands with soap and water, you should not restrain from touching things and quarantine yourself if you are ill and if you are in a Corona Virus Affrected area")
        engine.runAndWait()

    if "cases"   and "worldwide"  in command  :
        print ("There are 803547 cases of corona virus worldwide as of 7:20 IST, 31st March,2020")
        engine.say ("There are 803547 cases of corona virus worldwide as of 7:20 IST, 31st March,2020")
        engine.runAndWait()

    if "cases" and "india" in command :
        print ("There are 1117 cases of Corona Virus in India as of 7:34 IST, 31st March,2020")
        engine.say("There are 1117 cases of Corona Virus in India as of 7:34 IST, 31st March,2020")
        engine.runAndWait()

    if "test " in command :
        # Variables 
        # Variables 

        Q=0

        Yes=0


        # Questions

        while Q<=4 :
            Q=Q+1

            if Q==1:
                ans=input("Do you have cough:")
                if ans=='yes' or ans=="Yes" or ans=="YES" or ans=="YEs" :
                    Yes=Yes+1




            if Q==2 :
                ans=input("Do you have fever:")
                if ans=='yes' or ans=="Yes"  or ans=="YES" or ans=="YEs" :
                    Yes=Yes+1


            if Q==3:
                ans=input("Do you have breathing problems:")
                if ans=='yes' or ans=="Yes"  or ans=="YES" or ans=="YEs":
                    Yes=Yes+1

            if Q==4:
                ans=input("Do you have Fatigue and body Aches:")
                if ans=='yes' or ans=="Yes"  or ans=="YES" or ans=="YEs":
                    Yes=Yes+1





        if Yes>=3 :
            print ("You should have a CoronaVirus Test Done Now!")
        if Yes ==1 or Yes==2 :
            print ("You should visit a doctor as soon as possible.")
        if Yes==0 :
            print ("You are healthy and well")


    if "bye" in command :
        print("Bye, hope you are well buddy!")
        engine.say("Bye, hope you are well buddy!")
        engine.runAndWait()
        engine.stop()




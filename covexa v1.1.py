# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:23:01 2020

@author: modak
"""
import pyttsx3
import speech_recognition as speech

engine = pyttsx3.init("sapi5")

def start_listening():
            
    r = speech.Recognizer() 
    with speech.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            print("Speak:")
            audio = r.listen(source)
    command=r.recognize_google(audio)
    print("You said" + command)
    return command         


words = start_listening().lower()

if 'hello' in words:    
    engine.say('Hi I am Covexa, your Alexa for the Corona Virus Help  ')
    engine.runAndWait() 


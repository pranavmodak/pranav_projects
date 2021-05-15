"""
JARVIS
"""

#lists
facts=["More human twins are being born now than ever before.",
       "A narwhal's tusk reveals its past living conditions.",
       "The first person convicted of speeding was going eight mph.",
       " is the scent of dozens of chemicals."]


#importing libaries

import speech_recognition as speech
import pyttsx3
import datetime
import pyjokes
import time
import pywhatkit
import wikipedia
import random
from playsound import playsound


#initilizing libs
now = datetime.datetime.now()
engine=pyttsx3.init()
engine.setProperty("RATE",175)

#starting program

print("Hello sir!")
engine.say("Hello sir!")
time.sleep(1)
print("am Just a rather intelligent system or, in short, JARVIS")
engine.say("am Just a rather intelligent system or, in short, JARVIS")
time.sleep(1) 
engine.say("I can do a lot of things such as tell you the time, play songs, crack jokes, toss the coin and even tell you information of anything or anyone!")
print("I can do a lot of things such as tell you the time, play songs, crack jokes, toss coin and even tell you information of anything or anyone!")
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
    if j=='Jarvis':
        while True:
            #background music
            playsound('background sound1.mp3',False)
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
                        engine.say(pyjokes.get_joke())
                        engine.say("ha ha ha")
                        engine.runAndWait()
                        print("Here it is")
                        print(pyjokes.get_joke())
                        
                    if 'play' or 'song' in command:
                            song = command.replace('play', '')
                            engine.say('playing ' + song)
                            print('Playing ' + song)
                            engine.runAndWait()
                            pywhatkit.playonyt(song)
                        
                    if 'who is' in command :
                            person = command.replace('who is', '')
                            info = wikipedia.summary(person, 1)
                            print(info)
                            engine.say(info)
                            engine.runAndWait()
                        
                    if 'what is' in command :
                            person = command.replace('what is', '')
                            info = wikipedia.summary(person, 1)
                            print(info)
                            engine.say(info)
                            engine.runAndWait()
                    
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
                        toss=random.randint("Heads", "Tails")
                        print("its "+str(toss))
                        #engine.say("its "+str(toss)
                else:
                    break
            
        #Statements to Handle errors while receiving voice commands
            except speech.UnknownValueError:
                print("Could not understand audio")
            except speech.RequestError as e:
                print("Could not request results; {0}".format(e))
            except KeyboardInterrupt:
                break
            
except speech.UnknownValueError:
    print("Could not understand audio")
except speech.RequestError as e:
    print("Could not request results; {0}".format(e))
except KeyboardInterrupt:
    print()
#ending statment
engine.say("Nice interacting with you sir.")
engine.runAndWait()
print("Nice interacting with you!!")
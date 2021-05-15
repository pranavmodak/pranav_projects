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
engine.say("I can do a lot of things such as tell you the time, play songs, crack jokes and even tell you information of anything or anyone!")
print("I can do a lot of things such as tell you the time, play songs, crack jokes and even tell you information of anything or anyone!")
time.sleep(1)
engine.say("You can say, JARVIS wake up to activate me, If I am inactive, which I rather won't be!")
print("You can say, JARVIS wake up to activate me, If I am inactive, which I rather won't be!")


engine.runAndWait()


while True:
    playsound('background sound1.mp3',False)
    try:
        #Take the user input to activate reception of Voice Commands
        userInput=input("Press v to start voice commands and q to quit: ").lower()
        #winsound.PlaySound('background sound1.mp3', winsound.SND_ASYNC)
        
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
            print("you said: "+command)
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
                    print('playing ' + song)
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
                
        else:
            break
            
    #Statements to Handle errors while receiving voice commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break

#ending statment
engine.say("Nice interacting with you sir.")
engine.runAndWait()
print("Nice interacting with you!!")
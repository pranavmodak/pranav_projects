

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
import webbrowser


"""inisilizing lib"""
import pygame
pygame.init()

"""making height of window"""
h=512
w=512

"""setting screen"""
screen=pygame.display.set_mode((h,w))


#initilizing libs
now = datetime.datetime.now()
engine=pyttsx3.init()
engine.setProperty("RATE",175)

#starting code
 
pygame.display.set_caption("J.A.R.V.I.S")
dispimg=pygame.image.load("Images/i.png")
screen.blit(dispimg,(0,0))
eventstatus="None"
 
print("Allow me to introduce myself!")
engine.say("Allow me to introduce myself!")
engine.runAndWait()
time.sleep(1)

print("I am JARVIS the virtual artificial intelligence assistant")
engine.say("I am JARVIS the virtual artificial intelligence assistant")
engine.runAndWait()
time.sleep(1) 

engine.say("I can do a lot of things such as tell you the time, play songs, crack jokes, toss the coin, do mathemathics, do webbrowser searching, wikipeideia and even tell you information of anything or anyone!")
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



while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            eventstatus="QUIT"
            break
        
    if eventstatus =="QUIT":
        break




    
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
                    
                    if 'mathemathics' in command:
                        engine.say('type the opretion to be done, addition, subtraction, multiplication, perimeter, area or division')
                        engine.runAndWait()
                        opreation=input('type the opreation to be done, addition, subtraction, multiplication, perimeter, area or division: ').lower()
                        
                        num1=int(input("enter your first number or lenght: "))
                        engine.say("enter your first numberor lenght: ")
                        num2=int(input("enter your second number or breath: "))
                        engine.say("enter your second number or breath: ")
                        engine.runAndWait()
                        
                        if opreation=='adiition':
                            print("The sum is: "+str(num1+num2))
                            engine.say("The sum is: "+str(num1+num2))
                            engine.runAndWait()
                        
                        if opreation=='subtraction':
                            print("The sum is: "+str(num1-num2))
                            engine.say("The sum is: "+str(num1-num2))
                            engine.runAndWait()
                        
                        if opreation=='multiplication':
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
                                
                            else:
                                print("The sum is: "+str(num1/num2))
                                engine.say("The sum is: "+str(num1/num2))
                                engine.runAndWait() 
                            
                        if opreation=="area":
                            print("the area is"+str(a*b))
                            engine.say("the area is"+str(a*b))
                            engine.runAndWait()
                            
                        else:
                            print("Opreation not found")
                            engine.say("Opreation not found")
                            engine.runAndWait()
                            
                    if 'unwell' in command :
                        print("Here are some clinics nearby:-")
                        engine.say("Here are some clinics nearby:-")
                        engine.runAndWait()
                        webbrowser.open("https://www.google.com/search?q=doctors+near+me&source=hp&ei=zSCeYM7LNt6H4-EPrpWv6Ak&iflsig=AINFCbYAAAAAYJ4u3b1m6yl5YZglXzNhCoeK2dJqyuZT&oq=doctors+&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQsQMQyQMyBQgAEJIDMgUIABCxAzIFCC4QsQMyBQgAELEDMggIABCxAxCDATIFCAAQsQMyCAguEMcBEK8BMggIABCxAxCDATICCAA6CwguELEDEMcBEKMCOggILhCxAxCDAToCCC5QrgZYjh1gvC1oAHAAeACAAcQBiAGJC5IBAzAuOJgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz")
                        engine.runAndWait()
                        
                    if 'make music' in command:
                        engine.say("Not really professional at it sir but I'll still try!")
                        print("Not really professional at it sir but I'll still try!")
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
                        webbrowser.open('https://timesofindia.indiatimes.com/')
                        
                        news = command.replace('play', '')
                        engine.say('playing ' + news)
                        print('Playing ' + news)
                        engine.runAndWait()
                        pywhatkit.playonyt(news)
                        
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

playsound('jarvis end sound.mp3',False)
engine.say("Nice interacting with you sir.")
engine.runAndWait()
print("Nice interacting with you!!")
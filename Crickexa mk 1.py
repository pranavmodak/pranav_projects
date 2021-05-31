

"importing libraries"
import pyttsx3
import time
from playsound import playsound
import speech_recognition as speech
import webbrowser

"""initlizing libraies"""
engine = pyttsx3.init()
engine.setProperty("RATE", 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


"""starting code"""

print("Hello")
engine.say("hello")
engine.runAndWait()
time.sleep(1)

print("I am Crickexa, the Alexa for cricket, you can ask anything about cricket such as show IPL scores")
engine.say("I am Crickexa, the Alexa for cricket, you can anything about cricket such as show IPL scores")
engine.runAndWait()
time.sleep(1)

print("initilizing startup sequence")
engine.say("initilizing startup sequence")
engine.runAndWait()
playsound("crickexa startup sound.mp3")
time.sleep(1)

print("you can say cricket to activate me")
engine.say("you can say cricket to activate me")
engine.runAndWait()
time.sleep(1)

"""starting voice input"""

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
    
    if "cricket" in j:
        while True:
            try:
                playsound("crickexa middle sound.mp3")
                engine.say("press V to start and say bye to quit: ")
                engine.runAndWait()
                
                userinput=input("press V to start and Q to quit: ").lower()
                
                if userinput == "v":
                    r=speech.Recognizer()
                    with speech.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        print("Speak: ")
                        engine.say("Speak: ")
                        print("Listening. . . . ")
                        engine.say(("Listening. . . . "))
                        engine.runAndWait()
                        audio=r.listen(source)
                    #Convert Voice Commands to Text
                    command=r.recognize_google(audio)
                    command = command.lower()
                    print("You said : " + command)
                    engine.say("You said : " + command)
                    engine.runAndWait()
                    """starting main code"""
                
    
                    if "ipl" in command:
                        print("here is the latest score of ipl")
                        engine.say("here is the latest score of ipl")
                        engine.runAndWait()
                        webbrowser.open("https://www.google.com/search?rlz=1C1CHZN_enIN955IN955&q=ipl+score&spell=1&sa=X&ved=2ahUKEwjg4ufhsfPwAhUp63MBHQgWD4AQBSgAegQIARAw&biw=1280&bih=600#sie=lg;/g/11fqtnjjg0;5;/m/03b_lm1;mt;fp;1;;")
                        
                    elif "world matches" in command:
                        print("here is the score for the going on matches")
                        engine.say("here is the score for the going on matches")
                        engine.runAndWait()
                        webbrowser.open("https://www.google.com/search?gs_ssp=eJzj4tTP1TcwMiw0MjZg9GLOTE4GACEjA_U&q=icc&rlz=1C1CHZN_enIN955IN955&oq=icc&aqs=chrome.1.69i57j46i433j0i433l2j0j0i433j46i433j0i433j46i433j46i175i199.5106j0j9&sourceid=chrome&ie=UTF-8#sie=lg;/g/11jnl8yvj1;5;/m/021q23;mt;fp;1;;")
                        
                    elif "last " and "ipl" in command:
                        print("this is the result for the last ipl")
                        engine.say("this is the result for the last ipl")
                        engine.runAndWait()
                        webbrowser.open("https://www.google.com/search?rlz=1C1CHZN_enIN955IN955&q=ipl+score&spell=1&sa=X&ved=2ahUKEwjg4ufhsfPwAhUp63MBHQgWD4AQBSgAegQIARAw&biw=1280&bih=600&safe=active#sie=lg;/g/11fqtnjjg0;5;/m/03b_lm1;st;fp;1;;https://www.google.com/search?rlz=1C1CHZN_enIN955IN955&q=ipl+score&spell=1&sa=X&ved=2ahUKEwjg4ufhsfPwAhUp63MBHQgWD4AQBSgAegQIARAw&biw=1280&bih=600&safe=active#sie=lg;/g/11fqtnjjg0;5;/m/03b_lm1;st;fp;1;;")
                        
                    elif "world cup" in command:
                        print("The cricket world cup is played 4 years after befores world cup")
                        engine.say("The cricket world cup is played 4 years after befores world cup")
                        engine.runAndWait()
                        print("here is a site for the world cup")
                        engine.say("here is a site for cricket world cup")
                        engine.runAndWait()
                        webbrowser.open("https://www.cricketworldcup.com/")
                        
                    
                    elif "show matches" in command:
                        print("here are the matches")
                        engine.say("here are the matches")
                        engine.runAndWait()
                        webbrowser.open("https://www.youtube.com/results?search_query=cricket")
                        
                    elif "bye" in command:
                        break
                    
                    elif "comparison" in command:
                        person1 = input("enter name of first person: ")
                        person2 = input("enter name of person 2: ")
                        
                        final=command.replace(person1, person2)
                        webbrowser.open(final)
                        
                    else:
                        print("command not found")
                        engine.say("command not found")
                        engine.runAndWait()
                        
                        break
        
                """end of the code"""
            except speech.UnknownValueError:
                print("Sorry, Could not understand.")
                engine.say("Sorry, Could not understand.")
                engine.runAndWait()
            
            except speech.RequestError as e:
                print("Could not request results; {0}".format(e))
                engine.say("Could not request results; {0}".format(e))
                engine.runAndWait()
                
            except KeyboardInterrupt:
                break  
        
except speech.UnknownValueError:
    print("Sorry, Could not understand.")
    engine.say("Sorry, Could not understand.")
    engine.runAndWait()
    
except speech.RequestError as e:
    print("Could not request results; {0}".format(e))
    engine.say("Could not request results; {0}".format(e))
    engine.runAndWait()
    
except KeyboardInterrupt:
    print()         
print("Nice Interacting With You")
engine.say(("Nice Interacting With You"))
engine.runAndWait()
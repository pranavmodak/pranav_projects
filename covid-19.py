import speech_recognition as speech
import pyttsx3
import webbrowser

engine=pyttsx3.init()
command=input("enter ")
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
            print("the vaccines are: Sputnik, Pfizer, covaxin and covisheild ")
            engine.say("the vaccines are: Sputnik, Pfizer, covaxin and covisheild ")
            
        else:
            print("Command not found")
            engine.say("Command not found")
            engine.runAndWait()
        
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        print()
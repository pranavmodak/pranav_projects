"""
Made By: Team Vanar Vede Warriors
Members: Gautam, Pranav And Ninad
solarex
"""
"""lists"""
solar_syestem={
               "sun":"The sun lies at the heart of the solar system, where it is by far the largest object. It holds 99.8 percent of the solar system's mass and is roughly 109 times the diameter of the Earth — about one million Earths could fit inside the sun. ... The sun is one of more than 100 billion stars in the Milky Way",
               "mercury":"Mercury is the smallest planet in our solar system. ... Along with Venus, Earth, and Mars, Mercury is one of the rocky planets. It has a solid surface that is covered with craters. It has no atmosphere, and it doesn't have any moons.",
               "venus":"Venus is the second planet from the Sun, and is Earth's closest neighbor in the solar system. Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky. The planet is a little smaller than Earth, and is similar to Earth inside",
               "earth":"Earth is the third planet from the Sun and the only astronomical object known to harbor and support life. About 29.2% of Earth's surface is land consisting of continents and islands",
               "mars":"Mars is sometimes called the Red Planet. It's red because of rusty iron in the ground. Like Earth, Mars has seasons, polar ice caps, volcanoes, canyons, and weather. It has a very thin atmosphere made of carbon dioxide, nitrogen, and argon",
               "astroid belt": "The asteroid belt is a torus-shaped region in the Solar System, located roughly between the orbits of the planets Jupiter and Mars. It contains a great many solid, irregularly shaped bodies, of many sizes but much smaller than planets, called asteroids or minor planets.",
               "jupiter":"Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass (more than) two and a half times that of all the other planets in the Solar System combined, but (a little) less than one-thousandth the mass of the Sun",
               "saturn":"Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth. It only has one-eighth the average density of Earth; however, with its larger volume, Saturn is over 95 times more massive.",
               "uranus":"Uranus is known as the “sideways planet” because it rotates on its side. Uranus was discovered in 1781 by William Herschel. Uranus was the first planet found using a telescope. Uranus is an Ice Giant planet and nearly four times larger than Earth.",
               "neptune":"Neptune is the eighth and farthest-known Solar planet from the Sun. In the Solar System, it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet. It is 17 times the mass of Earth, slightly more massive than its near-twin Uranus.",
               "pluto":"Pluto (minor planet designation: 134340 Pluto) is a dwarf planet in the Kuiper belt, a ring of bodies beyond the orbit of Neptune. It was the first and the largest Kuiper belt object to be discovered. After Pluto was discovered in 1930, it was declared to be the ninth planet from the Sun.",
               "solar syestem": "Our solar system consists of our star, the Sun, and everything bound to it by gravity — the planets Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune, dwarf planets such as Pluto, dozens of moons and millions of asteroids, comets and meteoroids."
               }


"""importing libraies"""
import pyttsx3 
import speech_recognition as speech
import time

"""initilizing libraies"""
engine=pyttsx3.init()
engine.setProperty("RATE",175)

"""starting stament"""
print("Hello Everyone")
engine.say("Hello Everyone")
engine.runAndWait()
time.sleep(1)

print("I am solarex, the guide for the solar syestem")
engine.say("I am solarex, the guide for the solar syestem")
engine.runAndWait()
time.sleep(1)

while True:
    try:         
        #Take the user input to activate reception of Voice Commands
        engine.say("Press v to start and q to quit: ")
        engine.runAndWait()
        userInput=input("Press v to start and q to quit: ").lower()
        
        """Starting voice command"""
        if userInput=="v":
            r=speech.Recognizer()
            with speech.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak:")
                engine.say("Speak")
                engine.runAndWait()
                audio=r.listen(source)
            j=r.recognize_google(audio)
            j=j.lower()
            print("You said: "+j)
            engine.say("you said: "+j)
            engine.runAndWait()
            if "sun" in j:
                print(solar_syestem.get("sun"))
                engine.say(solar_syestem.get("sun"))
                engine.runAndWait()
                
            elif "mercury" in j:
                print(solar_syestem.get("mercury"))
                engine.say(solar_syestem.get("mercury"))
                engine.runAndWait()
                
            elif "venus" in j:
                print(solar_syestem.get("venus"))
                engine.say(solar_syestem.get("venus"))
                engine.runAndWait()
                
            elif "earth" in j:
                print(solar_syestem.get("earth"))
                engine.say(solar_syestem.get("earth"))
                engine.runAndWait()
                
            elif "mars" in j:
                print(solar_syestem.get("mars"))
                engine.say(solar_syestem.get("mars"))
                engine.runAndWait()
                
            elif "asteroid belt" in j:
                print(solar_syestem.get("astroid belt"))
                engine.say(solar_syestem.get("astroid belt"))
                engine.runAndWait()
                
            elif "jupiter" in j:
                print(solar_syestem.get("jupiter"))
                engine.say(solar_syestem.get("jupiter"))
                engine.runAndWait()
                
            elif "saturn" in j:
                print(solar_syestem.get("saturn"))
                engine.say(solar_syestem.get("saturn"))
                engine.runAndWait()
                
            elif "uranus" in j:
                print(solar_syestem.get("uranus"))
                engine.say(solar_syestem.get("uranus"))
                engine.runAndWait()
                
            elif "neptune" in j:
                print(solar_syestem.get("neptune"))
                engine.say(solar_syestem.get("neptune"))
                engine.runAndWait()
                
            elif "solar system" in j:
                print(solar_syestem.get("solar syestem"))
                engine.say(solar_syestem.get("solar syestem"))
                engine.runAndWait()
                
            elif "pluto" in j:
                print(solar_syestem.get("pluto"))
                engine.say(solar_syestem.get("pluto"))
                engine.runAndWait()
            elif "bye" in j:
                break
            
            
            else:
                print("could not understand")
                engine.say("could not understand")
                engine.runAndWait()
        
        else:
            break
            """except statment"""
        
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


"""ending staement"""
print("nice interacting with you")
engine.say("nice interacting with you")
engine.runAndWait()
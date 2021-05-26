import pywhatkit
command = input("what do you want to do: ")
if 'play' or 'song' in command:
    song = command.replace('play', '')
    
    print('Playing ' + song)
    
    pywhatkit.playonyt(song)
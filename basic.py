import os
import pyttsx3 as py

py.speak("Welcome at your services... ")
while True:
    py.speak( "Tell me how can I help you ?")
    print("Tell me how can I help you ?")
    d= input()
  
    if   ("don't" in d or "no need " in d  or "do not" in d or "dont" in d):
            py.speak("Okay")
            print("Okay")
    elif  ("editor" in d or "notepad" in d ):
            py.speak("Launching notepad")
            print("Launching notepad")
            os.system("notepad")
    elif  ("chrome" in d or "browser" in d or "web browser" in d ):
            py.speak("launching chrome")
            print("Launching chrome") 
            os.system("chrome")
    elif  ("media player" in d or "wmplayer" in d ):
            py.speak("launching wmplayer")
            print("launching wmplayer")
            os.system("wmplayer")
    elif  ("firefox" in d  ):
            py.speak("launching firefox")
            print("launching firefox")
            os.system("firefox")
    elif  ("vscode" in d or "studio code" in d ):
            py.speak("launching vscode")
            print("launching vscode")
            os.system("code")
    elif  ("close" in d or "bye" in d  or "exit" in d or "stop" in d ):
            py.speak("BYE BYE...Happy to help you")
            print("Happy to help you...")
            break
            
    else:
            py.speak("Sorry about that!!! We don't support this..." )
            print(" We don't support this...") 
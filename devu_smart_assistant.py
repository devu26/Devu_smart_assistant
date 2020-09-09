import pyttsx3
import time
import speech_recognition as sr
import os

pyttsx3.speak("hey!Welcome to devanshi's smart assistant")
print("hey!welcome to devanshi's smart assistant")
print("enter exit to when u want to leave this smart assistant")
pyttsx3.speak("talk with this assistant for your requirement")


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("talk with my assistant")
        audio = r.listen(source)
        pyttsx3.speak("opening your app")
        print("opening your app")
        p = r.recognize_google(audio)
        print(p)
    
    if (("run" in p) or ("open" in p) or ("launch" in p) or ("execute" in p))  and (("Chrome" in p) or ("Google" in p)) :
        os.system("chrome")
        time.sleep(5)

    elif (("run" in p) or ("open" in p) or ("launch" in p) or ("execute" in p)) and ("camera" in p):
        os.system("start microsoft.windows.camera:")
        time.sleep(5)
        
    elif (("run" in p) or ("open" in p) or ("launch" in p) or  ("execute" in p )) and  (("Notepad" in p) or ("editor" in p) ) :
        os.system("notepad")
        time.sleep(5)
        
    elif (("run" in p) or ("play" in p) or ("launch" in p) or  ("execute" in p ))  and ( ("Media" in p) and ("Player" in p)):
        os.system("wmplayer")
        time.sleep(5)

    elif (("run" in p) or ("open" in p) or ("launch" in p) or  ("execute" in p )) and ("calendar" in p):  
        os.system("start outlookcal:")
        time.sleep(5)
        
    elif (("run" in p) or ("open" in p) or ("launch" in p) or  ("execute" in p )) and (("mail" in p) or ("Gmail" in p)):
        os.system("start outlookmail:")
        time.sleep(5)
        
    elif (("run" in p) or ("open" in p) or ("launch" in p) or  ("execute" in p )) and (("WhatsApp" in p) or ("messenger" in p)):
        os.system("whatsApp")
        time.sleep(5)

    elif (("run" in p) or ("open" in p) or ("launch" in p) or  ("execute" in p )) and ("calculator" in p):
        os.system("calc")
        time.sleep(5)

    elif (("run" in p) or ("open" in p) or ("launch" in p) or  ("execute" in p )) and ("edge" in p):
        os.system("start microsoft-edge:")
        time.sleep(5)

    elif (("run" in p) or ("open" in p) or ("launch" in p) or  ("execute" in p )) and ("Anaconda" in p):
        os.system("Anaconda -h")
        time.sleep(5)

    elif  ("exit" in p)  or ("quit" in p):
        print("hope u enjoyed it")
        print("Bye!Have a nice day")
        pyttsx3.speak("hope u have enjoy it")
        pyttsx3.speak("Bye!Have a nice day")
        break;
    else:
        print("dont support")
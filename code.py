import os, pyttsx3

import speech_recognition as sr

def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am ready Now for your Order !")
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Loading ...")
            query = r.recognize_google(audio)
            print("the command is :", query)
        
        except Exception as e:
            print(e)
            print("Could you please repeat again ?")
            return "None"

        import time
        time.sleep(2)
        return query

def machineSound(audio):
    machine = pyttsx3.init()
    machine.say(audio)
    machine.runAndWait()

machineSound("Should i turn off the PC ?")

while True:
    command = takeCommands()

    if "exit" in takeCommands:
        machineSound("sure bye")
        break
    
    elif "yes" in takeCommands:
        machineSound("It will be shutdown Now")
        os.system("shutdown /s /t 30")

    elif "no" in takeCommands:
        machineSound("Enjoy your rest time")
        break


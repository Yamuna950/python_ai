import pyttsx3 as pt
import os

def speak(output):
    e = pt.init()
    voices = e.getProperty('voices')
    e.setProperty('voice',voices[1].id)
    speed = e.getProperty("rate")
    e.setProperty("rate",165)
    # e.say(output)
    e.save_to_file(output,"kognitiv_speech.mp3")
    e.runAndWait()
# output=input("enter query: ")
# speak(output)
def readFile():
    with open("Welcome_kognitians.txt") as f:
        content = f.readlines()
        speak(content)
readFile()
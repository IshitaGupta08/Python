#Install an external module and se it to perform n operation of your interest
# install pyttx3 this is used to convert text into speech
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
import pyaudio
import speech_recognition as sr


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("Say something!")
	audio = r.listen(source)
	print("Okay, now checking.")

WIT_AI_KEY = "7BO32QHUGL7H4XU3HJTTA2EJH2KLHEMV"
try:
	print("You said: " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
	print("Wit.ai could not understand audio.")
except sr.RequestError as e:
	print("Could not request results from wit.ai; {0}".format(e))

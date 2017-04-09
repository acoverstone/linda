from command import Command
import threading
import speech
import sys


class TimerCmd(Command):             #command for starting a timer
    INSTRUCTIONS = ['timer'] #list of keywords
    
    def execute(self):
        speech.speak("How long do you wish to set the timer for?")
        # Input must be in the form of ____ hour, ___ minute, _____ seconds
        response = speech.takeInput()

        understood = False

        while not understood:
            if "hours" in response or "hour" in response or "minutes" in response or "minute" in response or "seconds" in response or "second" in response:
                speech.speak("Timer starting");
                understood = True
                totalTime = parseTime(response)
                t = threading.Timer(totalTime, beep)
                t.start() 
            else:
                 speech.speak("I'm sorry I did not understand that. Please answer by saying blank hours blank minutes or blank seconds.");
            

def beep():
    speech.speak("beep beep beep beep")

def parseTime(response):
    hourIndex = -10
    minuteIndex = -10
    secondIndex = -10
    totalztime = 0
    
    response = response.split(" ")
    if "hour" in response:
        hourIndex = response.index("hour")
    elif "hours" in response:
        hourIndex = response.index("hours")      
    if "minute" in response:
        minuteIndex = response.index("minute")
    elif "minutes" in response:
        minuteIndex = response.index("minutes")
    if "second" in response:
        secondIndex = response.index("second")
    elif "seconds" in response:
        secondIndex = response.index("seconds")


    if hourIndex != -10:
        mainNumber = text2int(response[hourIndex - 1])
        possibleSecondNumber = text2int(response[hourIndex - 2])
        totalTime = totalTime + 3600 * mainNumber + 3600 * possibleSecondNumber

    if minuteIndex != -10:
        mainNumber = text2int(response[minuteIndex - 1])
        possibleSecondNumber = text2int(response[minuteIndex - 2])
        totalTime = totalTime + 60 * mainNumber + 60 * possibleSecondNumber

    if secondIndex != -10:
        mainNumber = text2int(response[hourIndex - 1])
        possibleSecondNumber = text2int(response[hourIndex - 2])
        totalTime = totalTime + mainNumber + possibleSecondNumber


    return totalTime


def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

        

def twoWordNumber(word):
    if word == "twenty":
        return 20
    elif word == "thirty":
        return 30
    elif word == "forty":
        return 40
    elif word == "fifty":
        return 50
    elif word == "sixty":
        return 60
    elif word == "seventy":
        return 70
    elif word == "eighty":
        return 80
    elif word == "ninety":
        return 90
    else:
      return 0


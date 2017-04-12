import pyowm
from datetime import datetime
import speech
import string
from command import Command

class WeatherCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['weather']      #list of keywords
    def execute(self,Screens):              #filled in abstract execute method
        frame = Screens.getFrame()
        #dd22fb7a8f13a5c753721b8b9d2b447f
        #fdde6469a8c085d628b1d10d371a798c
        #a432359e1ee01e2160c85db69ec90ac9

        owm = pyowm.OWM('fdde6469a8c085d628b1d10d371a798c')
        obs = owm.weather_at_place("Gainesville,Fl")

        fd = owm.daily_forecast(name='Gainesville,Fl',limit=5)

        #day1
        day1 = fd._forecast._weathers[0]
        datetime_unix = day1._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        print('\nday 1')
        print((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4]))
        print(day_of_the_week)
        print(string.capwords(day1._status))

        weatherString = "Today is " + day1._status + " with a high of " + str(round(day1._temperature['max']*9/5-459.67,2)) + " degrees, and a low of " + str(round(day1._temperature['min']*9/5-459.67,2)) + " degrees."
        speech.speak(weatherString)
        frame.today(weatherString)
        day1tempmin = str(round(day1._temperature['min']*9/5-459.67,2))
        day1tempmax = str(round(day1._temperature['max']*9/5-459.67,2))
        day1tempmorn = str(round(day1._temperature['morn']*9/5-459.67,2))
        day1tempday = str(round(day1._temperature['day']*9/5-459.67,2))
        day1tempeve = str(round(day1._temperature['eve']*9/5-459.67,2))
        day1tempnight = str(round(day1._temperature['night']*9/5-459.67,2))
        print('min ' + day1tempmin)
        print('max ' + day1tempmax)
        print('morn ' + day1tempmorn)
        print('day ' + day1tempday)
        print('eve ' + day1tempeve)
        print('night ' + day1tempnight)

        #day2
        day2 = fd._forecast._weathers[1]
        datetime_unix = day2._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        day2 = ""
        day2 += ('\nday 2\n')
        day2 += ((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4] + '\n'))
        day2 += (day_of_the_week + '\n')
        day2 += (string.capwords(day1._status) + '\n')

        day2tempmin = str(round(day2._temperature['min']*9/5-459.67,2))
        day2tempmax = str(round(day2._temperature['max']*9/5-459.67,2))
        day2tempmorn = str(round(day2._temperature['morn']*9/5-459.67,2))
        day2tempday = str(round(day2._temperature['day']*9/5-459.67,2))
        day2tempeve = str(round(day2._temperature['eve']*9/5-459.67,2))
        day2tempnight = str(round(day2._temperature['night']*9/5-459.67,2))
        day2 += ('min ' + day2tempmin + '\n')
        day2 += ('max ' + day2tempmax + '\n')
        day2 += ('morn ' + day2tempmorn + '\n')
        day2 += ('day ' + day2tempday + '\n')
        day2 += ('eve ' + day2tempeve + '\n')
        day2 += ('night ' + day2tempnight + '\n')
        frame.day2(day2)

        #day3
        day3 = fd._forecast._weathers[2]
        datetime_unix = day3._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        day3 += ('\nday 3' + '\n')
        day3 += ((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4] + '\n'))
        day3 += (day_of_the_week + '\n')
        day3 += (string.capwords(day3._status) + '\n')

        day3tempmin = str(round(day3._temperature['min']*9/5-459.67,2))
        day3tempmax = str(round(day3._temperature['max']*9/5-459.67,2))
        day3tempmorn = str(round(day3._temperature['morn']*9/5-459.67,2))
        day3tempday = str(round(day3._temperature['day']*9/5-459.67,2))
        day3tempeve = str(round(day3._temperature['eve']*9/5-459.67,2))
        day3tempnight = str(round(day3._temperature['night']*9/5-459.67,2))
        day3 += ('min ' + day3tempmin + '\n')
        day3 += ('max ' + day3tempmax + '\n')
        day3 += ('morn ' + day3tempmorn + '\n')
        day3 += ('day ' + day3tempday + '\n')
        day3 += ('eve ' + day3tempeve + '\n')
        day3 += ('night ' + day3tempnight + '\n')
        frame.day3(day3)

        #day4
        day4 = fd._forecast._weathers[3]
        datetime_unix = day4._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        day4 += ('\nday 4' + '\n')
        day4 += ((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4] + '\n'))
        day4 += (day_of_the_week + '\n')
        day4 += (string.capwords(day4._status) + '\n')

        day4tempmin = str(round(day4._temperature['min']*9/5-459.67,2))
        day4tempmax = str(round(day4._temperature['max']*9/5-459.67,2))
        day4tempmorn = str(round(day4._temperature['morn']*9/5-459.67,2))
        day4tempday = str(round(day4._temperature['day']*9/5-459.67,2))
        day4tempeve = str(round(day4._temperature['eve']*9/5-459.67,2))
        day4tempnight = str(round(day4._temperature['night']*9/5-459.67,2))
        day4 += ('min ' + day4tempmin + '\n')
        day4 += ('max ' + day4tempmax + '\n')
        day4 += ('morn ' + day4tempmorn + '\n')
        day4 += ('day ' + day4tempday + '\n')
        day4 += ('eve ' + day4tempeve + '\n')
        day4 += ('night ' + day4tempnight + '\n')
        frame.day4(day4)

        #day5
        day5 = fd._forecast._weathers[4]
        datetime_unix = day5._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        day5 += ('\nday 5' + '\n')
        day5 += ((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4]) + '\n')
        day5 += (day_of_the_week + '\n')
        day5 += (string.capwords(day5._status) + '\n')

        day5tempmin = str(round(day5._temperature['min']*9/5-459.67,2))
        day5tempmax = str(round(day5._temperature['max']*9/5-459.67,2))
        day5tempmorn = str(round(day5._temperature['morn']*9/5-459.67,2))
        day5tempday = str(round(day5._temperature['day']*9/5-459.67,2))
        day5tempeve = str(round(day5._temperature['eve']*9/5-459.67,2))
        day5tempnight = str(round(day5._temperature['night']*9/5-459.67,2))
        day5 += ('min ' + day5tempmin + '\n')
        day5 += ('max ' + day5tempmax + '\n')
        day5 += ('morn ' + day5tempmorn + '\n')
        day5 += ('day ' + day5tempday + '\n')
        day5 += ('eve ' + day5tempeve + '\n')
        day5 += ('night ' + day5tempnight + '\n')
        frame.day5(day5)

##weatherCmd = WeatherCmd()
##weatherCmd.decode("weather")

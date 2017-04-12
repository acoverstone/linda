import pyowm
from datetime import datetime
import speech
import string
from command import Command

class WeatherCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['weather']      #list of keywords
    def execute(self,Screens):              #filled in abstract execute method
        Screens.show_frame("WeatherScreen")
        frame = Screens.getFrame()
        #dd22fb7a8f13a5c753721b8b9d2b447f
        #fdde6469a8c085d628b1d10d371a798c
        #a432359e1ee01e2160c85db69ec90ac9

        owm = pyowm.OWM('dd22fb7a8f13a5c753721b8b9d2b447f')
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
        day2String = ""
        day2String += ('\nday 2\n')
        day2String += ((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4] + '\n'))
        day2String += (day_of_the_week + '\n')
        day2String += (string.capwords(day1._status) + '\n')

        day2tempmin = str(round(day2._temperature['min']*9/5-459.67,2))
        day2tempmax = str(round(day2._temperature['max']*9/5-459.67,2))
        day2tempmorn = str(round(day2._temperature['morn']*9/5-459.67,2))
        day2tempday = str(round(day2._temperature['day']*9/5-459.67,2))
        day2tempeve = str(round(day2._temperature['eve']*9/5-459.67,2))
        day2tempnight = str(round(day2._temperature['night']*9/5-459.67,2))
        day2String += ('min ' + day2tempmin + '\n')
        day2String += ('max ' + day2tempmax + '\n')
        day2String += ('morn ' + day2tempmorn + '\n')
        day2String += ('day ' + day2tempday + '\n')
        day2String += ('eve ' + day2tempeve + '\n')
        day2String += ('night ' + day2tempnight + '\n')
        frame.day2(day2String)

        #day3
        day3 = fd._forecast._weathers[2]
        datetime_unix = day3._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        day3String = ""
        day3String += ('\nday 3' + '\n')
        day3String += ((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4] + '\n'))
        day3String += (day_of_the_week + '\n')
        day3String += (string.capwords(day3._status) + '\n')

        day3tempmin = str(round(day3._temperature['min']*9/5-459.67,2))
        day3tempmax = str(round(day3._temperature['max']*9/5-459.67,2))
        day3tempmorn = str(round(day3._temperature['morn']*9/5-459.67,2))
        day3tempday = str(round(day3._temperature['day']*9/5-459.67,2))
        day3tempeve = str(round(day3._temperature['eve']*9/5-459.67,2))
        day3tempnight = str(round(day3._temperature['night']*9/5-459.67,2))
        day3String += ('min ' + day3tempmin + '\n')
        day3String += ('max ' + day3tempmax + '\n')
        day3String += ('morn ' + day3tempmorn + '\n')
        day3String += ('day ' + day3tempday + '\n')
        day3String += ('eve ' + day3tempeve + '\n')
        day3String += ('night ' + day3tempnight + '\n')
        frame.day3(day3String)

        #day4
        day4 = fd._forecast._weathers[3]
        datetime_unix = day4._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        day4String = ""
        day4String += ('\nday 4' + '\n')
        day4String += ((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4] + '\n'))
        day4String += (day_of_the_week + '\n')
        day4String += (string.capwords(day4._status) + '\n')

        day4tempmin = str(round(day4._temperature['min']*9/5-459.67,2))
        day4tempmax = str(round(day4._temperature['max']*9/5-459.67,2))
        day4tempmorn = str(round(day4._temperature['morn']*9/5-459.67,2))
        day4tempday = str(round(day4._temperature['day']*9/5-459.67,2))
        day4tempeve = str(round(day4._temperature['eve']*9/5-459.67,2))
        day4tempnight = str(round(day4._temperature['night']*9/5-459.67,2))
        day4String += ('min ' + day4tempmin + '\n')
        day4String += ('max ' + day4tempmax + '\n')
        day4String += ('morn ' + day4tempmorn + '\n')
        day4String += ('day ' + day4tempday + '\n')
        day4String += ('eve ' + day4tempeve + '\n')
        day4String += ('night ' + day4tempnight + '\n')
        frame.day4(day4String)

        #day5
        day5 = fd._forecast._weathers[4]
        datetime_unix = day5._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        day5String = ""
        day5String += ('\nday 5' + '\n')
        day5String += ((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4]) + '\n')
        day5String += (day_of_the_week + '\n')
        day5String += (string.capwords(day5._status) + '\n')

        day5tempmin = str(round(day5._temperature['min']*9/5-459.67,2))
        day5tempmax = str(round(day5._temperature['max']*9/5-459.67,2))
        day5tempmorn = str(round(day5._temperature['morn']*9/5-459.67,2))
        day5tempday = str(round(day5._temperature['day']*9/5-459.67,2))
        day5tempeve = str(round(day5._temperature['eve']*9/5-459.67,2))
        day5tempnight = str(round(day5._temperature['night']*9/5-459.67,2))
        day5String += ('min ' + day5tempmin + '\n')
        day5String += ('max ' + day5tempmax + '\n')
        day5String += ('morn ' + day5tempmorn + '\n')
        day5String += ('day ' + day5tempday + '\n')
        day5String += ('eve ' + day5tempeve + '\n')
        day5String += ('night ' + day5tempnight + '\n')
        frame.day5(day5String)

##weatherCmd = WeatherCmd()
##weatherCmd.decode("weather")

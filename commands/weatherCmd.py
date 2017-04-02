import pyowm
from datetime import datetime
import string
from command import Command

class WeatherCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['weather']      #list of keywords
    def execute(self):              #filled in abstract execute method
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
        print('\nday 2')
        print((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4]))
        print(day_of_the_week)
        print(string.capwords(day1._status))

        day2tempmin = str(round(day2._temperature['min']*9/5-459.67,2))
        day2tempmax = str(round(day2._temperature['max']*9/5-459.67,2))
        day2tempmorn = str(round(day2._temperature['morn']*9/5-459.67,2))
        day2tempday = str(round(day2._temperature['day']*9/5-459.67,2))
        day2tempeve = str(round(day2._temperature['eve']*9/5-459.67,2))
        day2tempnight = str(round(day2._temperature['night']*9/5-459.67,2))
        print('min ' + day2tempmin)
        print('max ' + day2tempmax)
        print('morn ' + day2tempmorn)
        print('day ' + day2tempday)
        print('eve ' + day2tempeve)
        print('night ' + day2tempnight)

        #day3
        day3 = fd._forecast._weathers[2]
        datetime_unix = day3._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        print('\nday 3')
        print((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4]))
        print(day_of_the_week)
        print(string.capwords(day3._status))

        day3tempmin = str(round(day3._temperature['min']*9/5-459.67,2))
        day3tempmax = str(round(day3._temperature['max']*9/5-459.67,2))
        day3tempmorn = str(round(day3._temperature['morn']*9/5-459.67,2))
        day3tempday = str(round(day3._temperature['day']*9/5-459.67,2))
        day3tempeve = str(round(day3._temperature['eve']*9/5-459.67,2))
        day3tempnight = str(round(day3._temperature['night']*9/5-459.67,2))
        print('min ' + day3tempmin)
        print('max ' + day3tempmax)
        print('morn ' + day3tempmorn)
        print('day ' + day3tempday)
        print('eve ' + day3tempeve)
        print('night ' + day3tempnight)

        #day4
        day4 = fd._forecast._weathers[3]
        datetime_unix = day4._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        print('\nday 4')
        print((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4]))
        print(day_of_the_week)
        print(string.capwords(day4._status))

        day4tempmin = str(round(day4._temperature['min']*9/5-459.67,2))
        day4tempmax = str(round(day4._temperature['max']*9/5-459.67,2))
        day4tempmorn = str(round(day4._temperature['morn']*9/5-459.67,2))
        day4tempday = str(round(day4._temperature['day']*9/5-459.67,2))
        day4tempeve = str(round(day4._temperature['eve']*9/5-459.67,2))
        day4tempnight = str(round(day4._temperature['night']*9/5-459.67,2))
        print('min ' + day4tempmin)
        print('max ' + day4tempmax)
        print('morn ' + day4tempmorn)
        print('day ' + day4tempday)
        print('eve ' + day4tempeve)
        print('night ' + day4tempnight)

        #day5
        day5 = fd._forecast._weathers[4]
        datetime_unix = day5._reference_time
        dtu = datetime.fromtimestamp(datetime_unix)
        day_of_the_week = dtu.strftime("%A")

        dtu = str(dtu)
        print('\nday 5')
        print((dtu[5:7] + '/' + dtu[8:10] + '/' + dtu[0:4]))
        print(day_of_the_week)
        print(string.capwords(day5._status))

        day5tempmin = str(round(day5._temperature['min']*9/5-459.67,2))
        day5tempmax = str(round(day5._temperature['max']*9/5-459.67,2))
        day5tempmorn = str(round(day5._temperature['morn']*9/5-459.67,2))
        day5tempday = str(round(day5._temperature['day']*9/5-459.67,2))
        day5tempeve = str(round(day5._temperature['eve']*9/5-459.67,2))
        day5tempnight = str(round(day5._temperature['night']*9/5-459.67,2))
        print('min ' + day5tempmin)
        print('max ' + day5tempmax)
        print('morn ' + day5tempmorn)
        print('day ' + day5tempday)
        print('eve ' + day5tempeve)
        print('night ' + day5tempnight)

##weatherCmd = WeatherCmd()
##weatherCmd.decode("weather")

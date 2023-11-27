
# 3)
from datetime import datetime
from time import sleep
# import pyglet


class Clock:

    def print_now(self):
        now = datetime.now
        return now().strftime('%H:%M:%S')

class Alarm:

    def init(self):
        self.alarm_is_on = False


    def switch_on(self):
        self.alarm_is_on = True
        print("Alarm is on")


    def switch_off(self):
        self.alarm_is_on = False
        print("Alarm clock is off")



class AlarmClock(Clock, Alarm):
    def __init__(self, hour, minute) -> None:
        self.hour = str(hour)
        self.minute = str(minute)
        if len(self.hour) == 1:
            self.hour = '0' + str(self.hour)
        if len(self.minute) == 1:
            self.minute = '0' + str(self.minute)

    def alarm_clock(self):
        print('Будильник запущен!')
        while True:
            time_now = datetime.now
            if str(time_now().hour) == self.hour and str(time_now().minute) == self.minute:
                print(f'Время уже {self.hour}:{self.minute}')
                break
            sleep(1)


h, m = input(f'На какое время поставить будильник?\nЧасы: '), input('Минуты: ')
obj = AlarmClock(h, m)

obj.alarm_clock()

# #1)

# class Auto:
#     name = 'Car'
#     def ride(self):
#         print(self.name + ' is riding on a ground')

# class Boat:
#     name = 'Boat'
#     def swim(self):
#         print(self.name + ' is floating on water')

# class Amphibian(Auto, Boat):
#     name = 'Swimming-car'
#     def ride(self):
#         super().ride()
#     def swim(self):
#         super().swim()



# car = Auto()
# boat = Boat()
# amphibian = Amphibian()

# car.ride()
# boat.swim()
# print()
# amphibian.ride()
# amphibian.swim()






# #2)
# class RadioMixin:
#     def play_music(self, song_name):
#         print(f'Ceйчас играет песня "{song_name}"')

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian(Auto, Boat, RadioMixin):
#     pass



# car = Auto()
# boat = Boat()
# amphibian = Amphibian()

# car.play_music('The Weeknd - Save Your Tears')
# print()
# car.play_music('Marshmello ft. Bastille - Happier')
# print()
# amphibian.play_music("Ali Gatie - It's You")




# #3)
# import time

# class Clock:
#     def show_time(self):
#         print(f"Текущее время: {time.strftime('%X')}")



# class Alarm:
#     def init(self):
#         self.alarm_is_on = False


#     def switch_on(self):
#         self.alarm_is_on = True
#         print("Будильник включен")


#     def switch_off(self):
#         self.alarm_is_on = False
#         print("Будильник отключен")


# class Alarm_Clock(Clock, Alarm):
#     def set_alarm(self, alarm_time):
#         self.alarm_time = alarm_time
#         print(f"Установить будильник на {alarm_time}")
#         self.switch_on()


# clock = Clock()
# alarm = Alarm_Clock()
# clock.show_time()
# alarm.set_alarm("07:00")
# clock.show_time()
# alarm.switch_off()
# clock.show_time()
# print()



        


# #4)
# from abc import ABC, abstractmethod


# class Coder(ABC):
#     count_code_time = 0

#     def __init__(self, experience) -> None:
#         self.experience = experience

#     @abstractmethod
#     def get_info(self):
#         pass
    
#     @abstractmethod
#     def coding(self):
#         pass

# class Backend(Coder,):
#     def __init__(self, experience, languages_backend) -> None:
#         super().__init__(experience)
#         self.languages_backend = languages_backend

#     @property
#     def get_info(self):
#         print(f'Опыт работы: {self.experience} лет. Общее время кодинга: {self.count_code_time}')

#     def coding(self, coding_time):
#         self.count_code_time += coding_time


# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend) -> None:
#         super().__init__(experience)
#         self.languages_frontend = languages_frontend

#     @property
#     def get_info(self):
#         print(f'Опыт работы: {self.experience} лет. Общее время кодинга: {self.count_code_time}')

#     def coding(self, coding_time):
#         self.count_code_time += coding_time

# class FullStack(Backend, Frontend):
#     def __init__(self, experience, languages_fullstack) -> None:
#         self.experience = experience
#         self.languages_fullstack = languages_fullstack

#     @property
#     def get_info(self):
#         return super().get_info
    
#     def coding(self, coding_time):
#         return super().coding(coding_time)



# bnd = Backend(1, 'Python')
# fnd = Frontend(7, 'Dart')
# fs = FullStack(9, 'Python, HTML, CSS, JavaScript')
# fnd.coding(4)
# fnd.coding(1)
# fnd.coding(8)
# bnd.coding(3)
# bnd.coding(2)
# bnd.coding(5)
# bnd.coding(8)
# fs.coding(7)
# fs.coding(2)
# fs.coding(9)
# fs.coding(2)
# for i in (fnd, bnd, fs):
#     i.get_info
from colorama import Fore, Style
from datetime import date





class Student:
    # Поля класса
    name = 'Vasya'
    birthday = ''
    group = 108
    GPA = 10
    color = Fore.LIGHTWHITE_EX

     # Конструктор
    def __init__(self, name='', birthday=1999, group=19464, GPA=10, color=Fore.LIGHTWHITE_EX):
        self.datetime = date
        self.name = name
        self.datatime = date
        self.group = group
        self.GPA = GPA

    def get_age(self):
        today = self.datetime.date.today().year #2023
        birthday = int(self.birthday)
        return \
            f'{today - birthday}\n' \


    def get_stats(self):
        return \
             f'{self.color}' \
             f'Имя: {self.name}\n' \
             f'Год рождения: {self.birthday}\n' \
             f'Группа: {self.group}\n' \
             f'Средний балл: {self.GPA}\n' \
             f'{Style.RESET_ALL}'
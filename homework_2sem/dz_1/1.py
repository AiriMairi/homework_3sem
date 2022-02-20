from abc import ABC
from random import randint


class Human(ABC):
    def people(self, age, disabled_person, participant_in_the_war, name):

        self.age = age
        print('Вам больше 65 лет?: 1-да, 2-нет')
        age = int(input())

        self.disabled_person = disabled_person
        print('У вас есть инвалидность?: 1-да, 2-нет')
        disabled_person = int(input())

        self.participant_in_the_war = participant_in_the_war
        print('Вы участвовали в войне?: 1-да, 2-нет')
        participant_in_the_war = int(input())

        self.name = name
        print('Вас зовут Нияз?: 1-да, я красавчик, 2-нет, я дэбил')
        name = int(input())

        if age == 1 or disabled_person == 1 or participant_in_the_war == 1 or name == 1:
            print('Вы проходите без очереди!')
        elif age == 2 and disabled_person == 2 and participant_in_the_war == 2 and name == 2:
            num = randint(1, 20)
            print(f'Ваш номер {num}.')


class Queue(ABC):
    def service_selection(self):
        print('Выберите услугу: 1-Карта, 2-Кредит/Ипотека, 3-Снять/положить наличные, 4-Открать вклад')
        service_selection = int(input())
        if service_selection == 1:
            print('Ваше окно: 1')
        elif service_selection == 2:
            print('Ваше окно: 2')
        elif service_selection == 3:
            print('Ваше окно: 3')
        elif service_selection == 4:
            print('Ваше окно: 4')
        else:
            print('Введите номер существующей услуги.')


human = Human()
human.people(age=2, disabled_person=2, participant_in_the_war=2, name=1)
queue = Queue()
queue.service_selection()

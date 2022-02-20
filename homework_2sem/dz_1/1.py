from abc import ABC

class Human(ABC):
    def age(self):
        print('Вам больше 65 лет?: 1-да, 2-нет')
        age = int(input())
    def disabled_person(self):
        print('У вас есть инвалидность?: 1-да, 2-нет')
        disabled_person = int(input())
    def participant_in_the_war(self):
        print('Вы участвовали в войне?: 1-да, 2-нет')
        participant_in_the_war = int(input())
    def name(self):
        print('Вас зовут Нияз?: 1-да, я красавчик, 2-нет, я дэбил')
        name = int(input())

    def number(self):
        if Human.age(1) or Human.disabled_person(1) or Human.participant_in_the_war(1) or Human.name(1):
            print('Вы проходите без очереди!')
        elif Human.age(2) and Human.disabled_person(2) and Human.participant_in_the_war(2) and Human.name(2):
            print('Вы не можете пройти без очереди')



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


Human.age(2)
Human.disabled_person(2)
Human.participant_in_the_war(2)
Human.name(1)
Queue.service_selection(4)








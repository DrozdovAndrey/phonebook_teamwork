#Анна
from datetime import datetime as dt
from typing import List

def get_choice_logger(choise):
    time = dt.now().strftime('%D:%M:%H:%M')
    with open('log.log', 'a',encoding='utf-8') as file : 
            file.write('{};- user нажал цифру ; {}\n'
                .format(time, choise))

def add_contact_logger(contact):
    time = dt.now().strftime('%D:%M:%H:%M')
    with open('log.log', 'a',encoding='utf-8') as file : 
        file.write('{}; added_new_contact; {}\n'
                .format(time, contact))

#def get_choice_logger(choise):
#    time = dt.now().strftime('%D:%M:%H:%M')
#    while True:
#        if choise == 1:
#            with open('log.csv', 'a',encoding='utf-8') as file : 
#                file.write('{} выбор меню ; {}\n'
#                    .format(time, choise))
#        if choise == 2:
#            with open('log.csv', 'a',encoding='utf-8') as file :
#                file.write('{}; выбор меню; {}\n'
#                    .format(time, choise))
#            while True:
#                if choise == 1:
#                    with open('log.csv', 'a',encoding='utf-8') as file : 
#                        file.write('{}; редактирование контакта ; {}\n'
#                            .format(time, choise))
#                elif choise == 2:
#                    with open('log.csv', 'a',encoding='utf-8') as file : 
#                        file.write('{}; WARNING! контакт удален ; {}\n'
#                            .format(time, choise))
#                else :
#                    break
#        if choise == 3:
#            with open('log.csv', 'a',encoding='utf-8') as file :
#                file.write('{}; просмотр тел книги; {}\n'
#                    .format(time, choise))
#        if choise == 4:
#            with open('log.csv', 'a',encoding='utf-8') as file :
#                file.write('{}; произвели запись в json; {}\n'
#                    .format(time, choise))
#        if choise == 5:
#            with open('log.csv', 'a',encoding='utf-8') as file :
#                file.write('{}; выход; {}\n'
#                    .format(time, choise))
#        else:
#            break

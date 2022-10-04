from ast import Dict
import json
import csv
import datetime

from typing import List
'''
глобальный список для записи контактов. 
'''
global contact_list
contact_list = []


def add_task(contact: List) -> None:
    '''
    добавить в список контакт
    '''
    contact = [[datetime.datetime.now()], ]
    contact_list.append(contact)


def search_contact(searchstring: str, contacts:str) -> List:
    '''
    Поиск в телефонной книге
    '''
    for contact in contacts:
        if searchstring in contact:
            return contact


def select_contact(choice: str, searched_contacts: Dict) -> Dict:
    '''
    Выбрать элемент в найденных
    '''
    for key, value in searched_contacts.items():
        if choice == key:
            return key, value


def delete_contact(contact: str) -> None:
    '''
    Удалить контакт из списка 
    '''
    contact_list.remove(contact_list[contact])


def edit_contact(index, value) -> None:
    '''
    Редактирование контакта. 
    '''
    contact_list[index] = value


def read_csv() -> None:
    '''
    Чтение из файла csv
    '''
    
    with open('data.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        contact =''
        for line in reader:
            contact += ' '.join(line)+'\n'
            #contact_list.append(line)
    return contact
# read_csv()
# print(contact_list)

def write_csv() -> None:
    '''
    Запись в csv фаил. 
    '''
    with open('data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\r')
        for contact in contact_list:
            writer.writerow(contact)


def write_json() -> None:
    '''
    Вызвать метод для первой записи в файле
    '''

    with open('data.json', 'w', encoding='utf-8', newline='') as rf:
        json.dump(contact_list, rf, ensure_ascii=False, indent=2)


print(contact_list)

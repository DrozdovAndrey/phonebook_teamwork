import csv
from ctypes.wintypes import BOOL
from re import template
import string
from typing import List

from sqlalchemy import true

from to_do_list_bot import retask


'''
глобальный список для записи контактов. 
'''
global tasks
global searched_tasks
global temp
tasks = []
searched_tasks = []

 


def add_task(key:str, value:str) -> None:
    '''
    добавить в список контакт
    '''
    tasks[key] = value


def search_task(searchstring: str, tasks:List):
    '''
    Поиск в телефонной книге
    '''
    for task in tasks:
        for value in task.values():
            if searchstring in value:
                   searched_tasks.append(task)
    return searched_tasks        

# def filter_task(searchstring_1: str, tasks:List):
#     '''
#     Поиск в телефонной книге
#     '''
#     for task in tasks:
#         for value in task.values():
#             if searchstring_1 in value:
#                    filter_tasks.append(task)
#     return filter_tasks

def delete_task(searchstring, tasks: List) -> None:
    '''
    Удалить контакт из списка 
    '''
    
    for task in tasks:
        if searchstring in task.get('Задача'):
            tasks.remove(task)
            return True
        else:
            False                

def edit_task(searchstring, tasks, re_task: List) -> None:
    '''
    Редактирование контакта. 
    '''
    for task in tasks: 
        if searchstring in task['Задача']:
            task['Задача'] = re_task

def find_tasks(tasks, searchstring):
    for task in tasks:
        if searchstring in task['Задача']:
            searched_tasks.append(task)          
    return searched_tasks


def check_have_task(searchstring, tasks): 
    '''
    Проверка на совпадение
    '''
    for task in tasks: 
        if searchstring in task['Задача']:
            return True
        else:
            False

def view_tasks(tasks: List) -> string:
    '''
    Запись в строку для Telegram
    '''
    strings =[]
    for task in tasks:
        for key, value in task.items():
            strings.append('{}: {}'.format(key.capitalize(), value))
        strings.append(' ')        
    result ='\n'.join(strings)        
    return result


def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('todo.csv','r', encoding='utf-8') as f:
        tasks = [{key: value  for key, value in task.items()}
                for task in csv.DictReader(f, skipinitialspace=True)]
    return tasks
 
#print(read_csv())

def write_csv(tasks: List) -> None:
    '''
    Запись в csv фаил. 
    '''
    fieldnames = tasks[0].keys()
    with open('todo.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames,lineterminator='\n')
        writer.writeheader()
        writer.writerows(tasks)
        




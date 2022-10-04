#Саша
from typing import List
import check as ch
from colorama import Fore, Back, Style 
import logger as log

def greetings_user():
    '''
    Приветсвует пользователя
    
    '''
    print(f'{Fore.YELLOW + Style.BRIGHT}Добро пожаловать в телефонную записную книжку 📙 {Style.RESET_ALL}')
    
def farewell_user():
    '''
    Прощание с пользователем
    
    '''
    print(f'{Fore.YELLOW + Style.BRIGHT}До новых встреч 👋{Style.RESET_ALL}')


def view_data(lst_input: list) -> str: #показать телефонную книгу
    '''
    Вывод информации пользователю
    
    '''
    print(f'\n{Fore.YELLOW + Style.BRIGHT}      <Ваши контакты> ↓ ')
    for line in lst_input:
        print(line)
    
def view_dict(lst_input: list) -> str: #показать телефонную книгу
    '''
    Вывод информации пользователю(словарь)
    '''
    print(f'\n{Fore.YELLOW + Style.BRIGHT}      <Ваши контакты> ↓ ')
    for key, value in lst_input.items():
        print(key, value)      

def view_contact(contact:str):
    '''
    Вывод информации пользователю(словарь)
    '''
    print(f'\n{Fore.YELLOW + Style.BRIGHT}      <Ваши контакты> ↓ ')
    print(contact)



def add_contact() -> list:
    '''
    Добоваляет контакт в спсисок
    
    '''
    print(f'{Fore.YELLOW + Style.BRIGHT}Введите данные о контакте ↓ {Style.RESET_ALL}')
    contact = []
    print(Fore.CYAN + Style.BRIGHT)
    text =ch.get_name(f'-> Имя: {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    text = text.capitalize()
    contact.append(text)
    text = ch.get_surname(f'{Fore.CYAN + Style.BRIGHT}-> Фамилия: {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    text = text.capitalize()
    contact.append(text)
    text = ch.get_phone_number(f'{Fore.CYAN + Style.BRIGHT}-> Номер телефона: {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    contact.append(text)
    text = ch.get_comment(f'{Fore.CYAN + Style.BRIGHT}-> Комментарий: {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    text = text.capitalize()
    contact.append(text)
    print(f'\n{Fore.GREEN}✅ Контакт успешно добавлен {Style.RESET_ALL}')
    print(Style.RESET_ALL)
    log.add_contact_logger(contact)
    return contact


def get_choice(input_string: str) -> str:
    '''
    Ввод выбора пользователя

    '''
    choise = ch.get_selection(input_string)
    log.get_choice_logger(choise)
    return choise

def get_choice_contact(input_string: str, searched_list:List) -> str:
    '''
    Ввод выбора действия пользователя

    '''
    choiсe = ch.get_selection_contact(input_string, searched_list)
    return choiсe    

def get_action(input_string: str) -> str:
    '''
    Ввод выбора действия пользователя

    '''
    return input(input_string)   

def get_number(input_string: str) -> str:
    '''
    Ввод выбора действия пользователя

    '''
    choise = ch.get_number_int(input_string)
    return choise   


def show_menu()-> None:
    '''
    Выводит основное меню
    
    '''
    return ('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Выберите нужное действие: ↓{Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}' 
      ' 1 -📲 <добавление записи в телефонную книгу> \n'
      ' 2 -🔎 <поиск записи в телефонной книге> \n'
      ' 3 -👀 <просмотр телефонной книги> \n'
      ' 4 -✍  <загрузить из CSV>\n'
      ' 5 -✍  <сохранить в CSV> \n'
      ' 6 -✍  <сохранить в json> \n'
      ' 7 -👋 <выход> \n'
      f' ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    
      
def search_contact_user():
    '''
    Выводит сообщение о поиске
    
    '''
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Введите значение для поиска ->: {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
    print(Style.RESET_ALL) 

def select_contact():
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Введите номер контакта для действия ->: {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
    print(Style.RESET_ALL)

def menu_search()-> None:
    '''
    Меню функции поиска
   
    '''
    return ('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Выберите нужное действие: ↓{Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}' 
      ' 1 -✍  <Редактировать контакт> \n'
      ' 2 -❌ <Удалить контакт> \n'
      ' 3 -🔙  <Выйти в главное меню> \n'
      f' ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    
def edit_user_contact(searchstring: str) -> None:

    '''
    Выводит сообщение об изменении контакта
    
    '''
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Введите обновлённые данные о контакте ↓ {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))

    print(Style.RESET_ALL)

def change_user_contact(searchstring: str) -> None:
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Контакт изменен на {searchstring}{Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
    print(Style.RESET_ALL)    

    
def delete_user_contact(searchstring: str) -> None:
    '''
    Выводит сообщение об удалении контакта
    
    '''
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Контакт {searchstring} удалён{Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
    print(Style.RESET_ALL)

def message_read_csv() -> None:
    '''
     Инфо сообщение о прочтении даннных
    
    '''
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Данные прочитаны. Просмотрите вашу записную книгу.{Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
    print(Style.RESET_ALL)    

def message_write_csv() -> None:
    '''
     Инфо сообщение о записи данных
    
    '''
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Данные записаны{Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
    print(Style.RESET_ALL)
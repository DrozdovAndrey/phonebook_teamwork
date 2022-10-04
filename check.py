# Андрей
import csv

def get_number_int(input_string: str) -> int:
    '''
    Проверка целого числа
    '''
    while True:
        try:
            num = input(input_string)
            num = int(num)
            return num
        except ValueError:
            print('Это не то ...')


def get_symbol(input_string: str) -> str:
    '''
    Проверка символа для действий
    '''
    while True:
        try:
            char = input(input_string)
            if char not in '+-/*':
                print('Не правильно!')
                continue
            return char

        except ValueError:
            print('Это не то ...')


def get_selection(input_string: str) -> int:
    '''
    Проверка числа для выбора результата
    '''
    while True:
        try:
            char = input(input_string)
            if char in '1234567':
                return int(char)
            print('Не правильно!')
            continue
        except ValueError:
            print('Это не то ...')

def get_selection_contact(input_string:str, searched_list) ->str:
    '''
    Проверка пользовательского ввода для выбора контакта из поиска
    '''            
    while True:
        try:
            choice = int(input(input_string))
            for key in searched_list:
                if choice == key:
                    return choice
            print('Не правильно!')
            continue
        except ValueError:
            print('Это не то ...')


def get_name(input_string: str) -> str:
    '''
    Проверка строки с именем, она не должна быть пустой и ограничена по колличеству символов,
    проверка выведет первую букву имени в верхнем регистре,
    остальные будут в нижнем
    '''
    while True:
        string = input(input_string)
        if len(string) < 17:
            if len(string) != 0:
                if string[0].isalpha():
                    return string.title()
                else:
                    print('Имя должно начинаться с буквы!')
            elif len(string) == 0:
                print('Это поле должно быть заполнено')  
        else: 
            print('вы ввели слишком много символов')
          

def get_surname(input_string: str) -> str:
    '''
    Проверка строки с именем, может быть пустой и ограничена по колличеству символов,
    проверка выведет первую букву имени в верхнем регистре,
    остальные будут в нижнем
    '''
    while True:
        string = input(input_string)
        if len(string) < 17:
            if len(string) != 0:
                if string[0].isalpha():
                    return string.title()
                else:
                    print('Имя должно начинаться с буквы!')
            elif len(string) == 0:
                return string    
        else: 
            print('вы ввели слишком много символов')

        
def get_phone_number(input_string: str) -> str:
    '''
    Проверка строки с номером телефона на числа и длинну номера
    '''

    while True:
        try:
            num = input(input_string)
            if len(num) < 12:
                if len(num) != 0:
                    num = int(num)
                    return str(num)
                elif len(num) == 0:
                    print('Это поле должно быть заполнено')  
            else: 
                print('вы ввели слишком много символов')
        except ValueError:
            print('Это не то ...')


def get_comment(input_string: str) -> str:
    '''
    Проверка строки с комментарием на колличество символов
    '''
    while True:
            string = input(input_string)
            if len(string) < 17:
                return string 
            else: 
                print('вы ввели слишком много символов')
        

def check_phone_number(num: str) -> bool:
    '''
    Проверка номера телефона на совпадение в базе
    '''
    path = 'data.csv'
    with open(path, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=' ')
        for line in reader:
            for i in line:    
                if num in line:
                    print('Контакт с таким номером уже существует!')
                    return True
                else:
                    return False


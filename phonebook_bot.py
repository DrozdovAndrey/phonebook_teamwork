
import logging
import csv
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CHOICE, WRITE_CVS, SEARCH, FIO, TEL = range(5)
    

# функция обратного вызова точки входа в разговор


def start(update, _):
    update.message.reply_text(
        'Добро пожаловать в телефонную книгу.\n Выберите нужное действие:')
    update.message.reply_text(
        '1 - добавление записи в телефонную книгу \n'
        '2 - поиск записи в телефонной книге \n'
        '3 - просмотр телефонной книги \n'
        '4 - выход')
    return CHOICE


def choice(update, context):
    user_choice = update.message.text
    if user_choice == '1':
        update.message.reply_text(
            'Фамилия Имя:')
        return FIO
    if user_choice == '2':
        context.bot.send_message(
            update.effective_chat.id, 'Введите значение для поиска: ')
        return SEARCH
    if user_choice == '3':
        text = read_csv()
        context.bot.send_message(
            update.effective_chat.id, text)
        return start(update, context)
    if user_choice == '4':
        return cancel(update, context)
    
def fio(update, context):
    lst = []
    text = update.message.text
    lst.append(text)
    update.message.reply_text(
            'Номер телефона: ')
    with open ('phone_book_bot.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator=',')
        file_writer.writerow(lst)
    return TEL

def tel(update, context):
    lst = []
    text = update.message.text
    lst.append(text)
    update.message.reply_text(
            'Комментарий: ')
    with open ('phone_book_bot.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator=',')
        file_writer.writerow(lst)
    return WRITE_CVS

def write_cvs(update, context):
    '''
    Запись в csv фаил
    '''
    lst = []
    text = update.message.text
    lst.append(text)
    # update.message.reply_text(
    #         'Номер телефона: ')
    # text_1 = update.message.text
    # lst.append(text_1)
    # update.message.reply_text(
    #         'Комментарий: ')
    # text_2 = update.message.text
    # lst.append(text_2)
    with open ('phone_book_bot.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
        file_writer.writerow(lst)
    return start(update, context)

def search(update, context):
    '''
    Поиск в телефонной книге
    '''
    text = update.message.text
    lst_input = read_csv()
    line_output = ''
    for line in lst_input:
        if text in line:
            line_output += line + '\n'
    update.message.reply_text(line_output)
    return start(update, context)

def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('phone_book_bot.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        contact =''
        for line in reader:
            contact += ' '.join(line)+'\n'
            #contact_list.append(line)
    return contact


    # with open('phone_book_bot.csv', encoding='utf-8') as r_file:
    #     file_reader_1 = csv.reader(r_file, delimiter=' ')
    #     file_reader = []
    #     for line in file_reader_1:
    #         line = ' '.join(line)
    #         file_reader.append(line)
    #     return file_reader

def cancel(update, _):
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - заходи.',
    )
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями CHOICE, RATIONAL_ONE, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO
    conversation_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            WRITE_CVS: [MessageHandler(Filters.text, write_cvs)],
            SEARCH: [MessageHandler(Filters.text, search)],
            FIO: [MessageHandler(Filters.text, fio)],
            TEL: [MessageHandler(Filters.text, tel)],
            # COMPLEX_ONE: [MessageHandler(Filters.text, complex_one)],
            # COMPLEX_TWO: [MessageHandler(Filters.text, complex_two)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
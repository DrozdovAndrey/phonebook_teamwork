import telebot
from datetime import datetime as dt
import logging
import operations as o
from operations import read_csv, tasks
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import stickers as st
import config
from phonebook_bot import choice
bot = telebot.TeleBot(config.TOKEN)
# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора

START, SHOW_MENU, MENU, EDIT, ADD, DELETE, VIEW, SEARCH, SEARCH_MENU, GET_TASK, GET_DATE, DATA, TIME = range(13)


TIME_NOW = dt.now().strftime('%D_%H:%M')

# функция обратного вызова точки входа в разговор

def start(update, _):
    reply_keyboard = [['GO ➡']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    bot.send_sticker(update.message.chat.id, st.welcome)
    bot.send_message(update.effective_chat.id,
                     f'Здраствуйте мастер {update.effective_user.first_name}, я Альфред, ваш персональный помощник')
    update.message.reply_text(
        'Добро пожаловать в ToDoList.', reply_markup=markup_key)
    return SHOW_MENU

def main_menu():
    return MENU

def show_menu(update, _):
    reply_keyboard = [['👀 VIEW', '📝 ADD','🔎 SEARCH', '❌ DELETE', '✍ EDIT', '🚪 EXIT']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    bot.send_sticker(update.message.chat.id, st.hello)
    update.message.reply_text('Чем займёмся, сэр? 🧐', reply_markup=markup_key)
    return MENU

def menu(update, _):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    choice = update.message.text
    if choice == '👀 VIEW':
        return view(update, _)
    if choice == '📝 ADD':
        update.message.reply_text('Введите задачу сэр: ')
        return ADD
    if choice == '🔎 SEARCH':
        bot.send_sticker(update.message.chat.id, st.listen)
        bot.send_message(update.effective_chat.id,
                     f'Что бы вы хотели найти, Мастер {update.effective_user.first_name}: ')
        return SEARCH
    if choice == '❌ DELETE':
        update.message.reply_text("Найти задачу для удаления: ")
        return DELETE
    if choice == '✍ EDIT':
        update.message.reply_text("Найти задачу для редактирования: ")
        return EDIT    
    if choice == '🚪 EXIT':
        return cancel(update, _)


def view(update, _):
    user = update.message.from_user
    logger.info("Контакт %s: %s", user.first_name, update.message.text)
    bot.send_sticker(update.message.chat.id, st.view_sticker)
    bot.send_message(update.effective_chat.id,
                     f'Давайте-ка взглянем на список задач мастер {update.effective_user.first_name} ⬇⬇⬇')
    tasks = read_csv()
    user = update.message.from_user
    tasks_filter = o.filter_task(user.first_name, tasks)
    tasks_string = o.view_tasks(tasks_filter)
    update.message.reply_text(tasks_string)
    return show_menu(update, _)

def add(update, context):
    user = update.message.from_user
    logger.info("Task %s: %s", user.first_name, update.message.text)
    name = update.message.text
    context.user_data['name'] = name
    update.message.reply_text("Сэр, Введите дату в формате ДД/ММ/ГГ: ")
    return DATA

def data(update, context):
    user = update.message.from_user
    logger.info("Task %s: %s", user.first_name, update.message.text)
    data = update.message.text

    if len(data) == 8 and data[2] == '/' and data[5] == '/':
        temp = data.replace('/', '')
        if temp.isdigit():
            data += '_'
            context.user_data['data'] = data
            update.message.reply_text("Введите время в формате ЧЧ:ММ ")
            return TIME
        else:
            update.message.reply_text("Введите дату в формате ДД/ММ/ГГ: ")
    else:
        update.message.reply_text("Введите дату в формате ДД/ММ/ГГ: ")

    data += '_'
    context.user_data['data'] = data
    update.message.reply_text("Сэр, Введите время в формате ЧЧ:ММ ")
    return TIME


def time(update, context):
    tasks = read_csv()
    task = {}
    user = update.message.from_user
    logger.info("Task %s: %s", user.first_name, update.message.text)
    time = update.message.text
    if len(time) == 5 and time[2] == ':':
        temp = time.replace(':', '')
        if temp.isdigit():
            data = context.user_data.get('data') + time
            name = context.user_data.get('name')
            task['Имя'] = user.first_name
            task['Фамилия'] = user.last_name
            task['Текущая дата'] = TIME_NOW
            task['Дата выполнения'] = data
            task['Задача'] = name
            tasks.append(task)
            o.write_csv(tasks)
            return start(update, context)
        else:
            update.message.reply_text("Введите время в формате ЧЧ:ММ ")
    else:
        update.message.reply_text("Введите время в формате ЧЧ:ММ ")


def search(update, _):
    user = update.message.from_user
    logger.info("Выбор поиска: %s: %s", user.first_name, update.message.text)
    searchstring = update.message.text
    tasks = read_csv()
    tasks_filter = o.filter_task(user.first_name, tasks)
    searched_tasks = o.search_task(searchstring, tasks_filter)
    bot.send_message(update.effective_chat.id,
                    f'Мастер {update.effective_user.first_name}, по вашему запросу <{searchstring}> найдено:')
    update.message.reply_text('🧐')
    tasks_string = o.view_tasks(searched_tasks)
    update.message.reply_text(tasks_string)

    return show_menu(update, _)

    


def delete(update, _):
    tasks = read_csv()
    user = update.message.from_user
    logger.info("Выбор удаления: %s: %s", user.first_name, update.message.text)
    searchstring = update.message.text
    o.delete_task(searchstring, tasks)
    bot.send_sticker(update.message.chat.id, st.complete)
    update.message.reply_text('Задача удалена, сэр.')
    o.write_csv(tasks)
    return show_menu(update, _)

    
def edit(update, _):
    tasks = read_csv()
    user = update.message.from_user
    logger.info("Выбор редактирования: %s: %s", user.first_name, update.message.text)
    searchstring = update.message.text
    o.edit_task(searchstring, tasks)
    bot.send_sticker(update.message.chat.id, st.complete)
    update.message.reply_text('Задача отредактирована, сэр.')
    o.write_csv(tasks)
    return show_menu(update, _)



def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    bot.send_sticker(update.message.chat.id, st.goodbye)
    bot.send_message(update.effective_chat.id,
                     f'До новых встреч, мастер {update.effective_user.first_name}. 👋')
    update.message.reply_text(
        'Вы знаете где меня найти.',)
    bot.send_sticker(update.message.chat.id, st.relax)
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    game_conversation_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            VIEW: [MessageHandler(Filters.text, view)],
            START: [CommandHandler('start', start)],
            SHOW_MENU: [MessageHandler(Filters.text, show_menu)],
            ADD: [MessageHandler(Filters.text, add)],
            DELETE: [MessageHandler(Filters.text, delete)],
            SEARCH: [MessageHandler(Filters.text, search)],
            MENU: [MessageHandler(Filters.text, menu)],
            EDIT: [MessageHandler(Filters.text, edit)],
            DATA: [MessageHandler(Filters.text, data)],
            TIME: [MessageHandler(Filters.text, time)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(game_conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

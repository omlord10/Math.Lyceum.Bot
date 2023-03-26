from typing import *
import mems
import telebot
from telebot import types
import openpyxl
import datetime
from random import randint
import sqlite3
import os
conn = sqlite3.connect('users.db',check_same_thread=False)
cursor = conn.cursor()

bot = telebot.TeleBot('TOKEN')

import xlrd
import os

os.system('old_bot.py')
@bot.message_handler(commands=['start', 'Start', 'старт', 'Старт'])
def start(message):
    if message.from_user.last_name !='None' or message.from_user.last_name != None:
        mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. Я бот Математического лицея. Создан помочь всем в школе. ' \
               f'Нажми /help, чтобы узнать, что я могу.' + '\n' + 'Для получения новостей необходимо указать себя.'\
               + '\n' + 'Например: <pre>/add_user Иванов Иван 5А</pre> \n Можно нажать и команда скопируется в буфер'
        bot.reply_to(message, mess, parse_mode='html')
    else:
        mess = f'Привет, <b>{message.from_user.first_name}</b>. Я бот Математического лицея. Создан помочь всем в школе. ' \
               f'Нажми /help, чтобы узнать, что я могу.' + '\n' + 'Для получения новостей необходимо указать себя.' \
               + '\n' + 'Например: <pre>/add_user Иванов Иван 5А</pre> \n Можно нажать и команда скопируется в буфер'
        bot.send_message(message.chat.id,'')


@bot.message_handler(commands=['change_mem'])
def change_mem(message):
    if message.chat.id == 5048652373:
        bot.send_message(message.chat.id, 'Successfully! Thank You!')
        change_text = message.text[12:]
        file = open('mems.txt', 'w', encoding='windows-1251')
        file.close
        file.write(change_text)
    else:
        bot.send_message(message.chat.id, "You aren't the developer! Only developers can make changes")

# @bot.message_handler(commands=['sendletter'])
# def letter(message):
#     if message.chat.id == 5048652373:
#         bot.send_message(message.chat.id, 'You are developer!')
#         user_id = message.text[12:21]
#         user_text = message.text[23:]
#         # print (user_id)
#         bot.send_message(user_id,user_text)
#     else:
#         bot.send_message(message.chat.id, "You can't do this")

@bot.message_handler(commands=['add_user'])
def add_user(message):
    params = message.text.split()
    user_id = message.chat.id
    user_name = params[1] +' '+ params [2]
    user_class = params[3]
    sql_query = "INSERT INTO students (name, tg_id, user_class) VALUES (?, ?, ?)"
    values = (user_name, user_id, user_class)
    cursor.execute(sql_query, values)
    conn.commit()
    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, text=f"Ученик {user_name} добавлен в базу данных.")



@bot.message_handler(commands=['logs'])
def all_print(message):
    if message.chat.id == 5048652373:
        sqlite_select_query = """SELECT * from students"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            mess = str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3])
            bot.send_message(message.chat.id,mess)
    else:
        bot.send_message(message.chat.id,'Yor are not developer!')

@bot.message_handler(commands=['Site', 'site', 'website', 'сайт', 'Сайт'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Сайт", url='матлицей.рф'))
    markup.add(types.InlineKeyboardButton("VK-группа", url='https://vk.com/matliceum'))
    markup.add(types.InlineKeyboardButton("Однаклассники", url='https://ok.ru/group/70000001007910'))
    markup.add(types.InlineKeyboardButton("Telegram-группа", url='https://t.me/wxGCj7i8HfE3MDky'))
    bot.send_message(message.chat.id, 'Наши Соц.Сети', reply_markup=markup)


@bot.message_handler(commands=['help', 'Help','back','Назад'])
def help(message):
    markup_reply = types.ReplyKeyboardMarkup()
    # izmenenie = types.KeyboardButton('/Изменение в расписании')
    website = types.KeyboardButton('/Сайт')
    start = types.KeyboardButton('/Старт')
    classes = types.KeyboardButton('/Классы')
    meme = types.KeyboardButton('/Мем')
    # markup_reply.row(izmenenie)
    markup_reply.row(website, start)
    markup_reply.row(classes, meme)
    bot.send_message(message.chat.id, 'Чем могу помочь?', reply_markup=markup_reply)
    # markup_reply.add(website, start, time)


@bot.message_handler(commands=['Класс_10А'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 10А')
    Tuesday = types.KeyboardButton('/Вторник 10А')
    Wednesday = types.KeyboardButton('/Среда 10А')
    Thirsday = types.KeyboardButton('/Четверг 10А')
    Friday = types.KeyboardButton('/Пятница 10А')
    Saturday = types.KeyboardButton('/Суббота 10А')
    Sunday = types.KeyboardButton('/Воскресенье 10А')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_11А'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 11А')
    Tuesday = types.KeyboardButton('/Вторник 11А')
    Wednesday = types.KeyboardButton('/Среда 11А')
    Thirsday = types.KeyboardButton('/Четверг 11А')
    Friday = types.KeyboardButton('/Пятница 11А')
    Saturday = types.KeyboardButton('/Суббота 11А')
    Sunday = types.KeyboardButton('/Воскресенье 11А')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_11Б'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 11Б')
    Tuesday = types.KeyboardButton('/Вторник 11Б')
    Wednesday = types.KeyboardButton('/Среда 11Б')
    Thirsday = types.KeyboardButton('/Четверг 11Б')
    Friday = types.KeyboardButton('/Пятница 11Б')
    Saturday = types.KeyboardButton('/Суббота 11Б')
    Sunday = types.KeyboardButton('/Воскресенье 11Б')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_9В'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 9В')
    Tuesday = types.KeyboardButton('/Вторник 9В')
    Wednesday = types.KeyboardButton('/Среда 9В')
    Thirsday = types.KeyboardButton('/Четверг 9В')
    Friday = types.KeyboardButton('/Пятница 9В')
    Saturday = types.KeyboardButton('/Суббота 9В')
    Sunday = types.KeyboardButton('/Воскресенье 9В')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_9Б'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 9Б')
    Tuesday = types.KeyboardButton('/Вторник 9Б')
    Wednesday = types.KeyboardButton('/Среда 9Б')
    Thirsday = types.KeyboardButton('/Четверг 9Б')
    Friday = types.KeyboardButton('/Пятница 9Б')
    Saturday = types.KeyboardButton('/Суббота 9Б')
    Sunday = types.KeyboardButton('/Воскресенье 9Б')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_9А'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 9А')
    Tuesday = types.KeyboardButton('/Вторник 9А')
    Wednesday = types.KeyboardButton('/Среда 9А')
    Thirsday = types.KeyboardButton('/Четверг 9А')
    Friday = types.KeyboardButton('/Пятница 9А')
    Saturday = types.KeyboardButton('/Суббота 9А')
    Sunday = types.KeyboardButton('/Воскресенье 9А')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_8В'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 8В')
    Tuesday = types.KeyboardButton('/Вторник 8В')
    Wednesday = types.KeyboardButton('/Среда 8В')
    Thirsday = types.KeyboardButton('/Четверг 8В')
    Friday = types.KeyboardButton('/Пятница 8В')
    Saturday = types.KeyboardButton('/Суббота 8В')
    Sunday = types.KeyboardButton('/Воскресенье 8В')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_8Б'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 8Б')
    Tuesday = types.KeyboardButton('/Вторник 8Б')
    Wednesday = types.KeyboardButton('/Среда 8Б')
    Thirsday = types.KeyboardButton('/Четверг 8Б')
    Friday = types.KeyboardButton('/Пятница 8Б')
    Saturday = types.KeyboardButton('/Суббота 8Б')
    Sunday = types.KeyboardButton('/Воскресенье 8Б')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_8А'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 8А')
    Tuesday = types.KeyboardButton('/Вторник 8А')
    Wednesday = types.KeyboardButton('/Среда 8А')
    Thirsday = types.KeyboardButton('/Четверг 8А')
    Friday = types.KeyboardButton('/Пятница 8А')
    Saturday = types.KeyboardButton('/Суббота 8А')
    Sunday = types.KeyboardButton('/Воскресенье 8А')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_7В'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 7В')
    Tuesday = types.KeyboardButton('/Вторник 7В')
    Wednesday = types.KeyboardButton('/Среда 7В')
    Thirsday = types.KeyboardButton('/Четверг 7В')
    Friday = types.KeyboardButton('/Пятница 7В')
    Saturday = types.KeyboardButton('/Суббота 7В')
    Sunday = types.KeyboardButton('/Воскресенье 7В')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_7Б'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 7Б')
    Tuesday = types.KeyboardButton('/Вторник 7Б')
    Wednesday = types.KeyboardButton('/Среда 7Б')
    Thirsday = types.KeyboardButton('/Четверг 7Б')
    Friday = types.KeyboardButton('/Пятница 7Б')
    Saturday = types.KeyboardButton('/Суббота 7Б')
    Sunday = types.KeyboardButton('/Воскресенье 7Б')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_7А'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 7А')
    Tuesday = types.KeyboardButton('/Вторник 7А')
    Wednesday = types.KeyboardButton('/Среда 7А')
    Thirsday = types.KeyboardButton('/Четверг 7А')
    Friday = types.KeyboardButton('/Пятница 7А')
    Saturday = types.KeyboardButton('/Суббота 7А')
    Sunday = types.KeyboardButton('/Воскресенье 7А')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_6Б'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 6Б')
    Tuesday = types.KeyboardButton('/Вторник 6Б')
    Wednesday = types.KeyboardButton('/Среда 6Б')
    Thirsday = types.KeyboardButton('/Четверг 6Б')
    Friday = types.KeyboardButton('/Пятница 6Б')
    Saturday = types.KeyboardButton('/Суббота 6Б')
    Sunday = types.KeyboardButton('/Воскресенье 6Б')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_6А'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 6А')
    Tuesday = types.KeyboardButton('/Вторник 6А')
    Wednesday = types.KeyboardButton('/Среда 6А')
    Thirsday = types.KeyboardButton('/Четверг 6А')
    Friday = types.KeyboardButton('/Пятница 6А')
    Saturday = types.KeyboardButton('/Суббота 6А')
    Sunday = types.KeyboardButton('/Воскресенье 6А')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_5В'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 5В')
    Tuesday = types.KeyboardButton('/Вторник 5В')
    Wednesday = types.KeyboardButton('/Среда 5В')
    Thirsday = types.KeyboardButton('/Четверг 5В')
    Friday = types.KeyboardButton('/Пятница 5В')
    Saturday = types.KeyboardButton('/Суббота 5В')
    Sunday = types.KeyboardButton('/Воскресенье 5В')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_5Б'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 5Б')
    Tuesday = types.KeyboardButton('/Вторник 5Б')
    Wednesday = types.KeyboardButton('/Среда 5Б')
    Thirsday = types.KeyboardButton('/Четверг 5Б')
    Friday = types.KeyboardButton('/Пятница 5Б')
    Saturday = types.KeyboardButton('/Суббота 5Б')
    Sunday = types.KeyboardButton('/Воскресенье 5Б')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)


@bot.message_handler(commands=['Класс_5А'])
def cl11A(message):
    params = message.text.split()
    markup_classes = types.ReplyKeyboardMarkup()
    Monday = types.KeyboardButton('/Понедельник 5А')
    Tuesday = types.KeyboardButton('/Вторник 5А')
    Wednesday = types.KeyboardButton('/Среда 5А')
    Thirsday = types.KeyboardButton('/Четверг 5А')
    Friday = types.KeyboardButton('/Пятница 5А')
    Saturday = types.KeyboardButton('/Суббота 5А')
    Sunday = types.KeyboardButton('/Воскресенье 5А')
    markup_classes.row(Monday, Tuesday, Wednesday)
    markup_classes.row(Thirsday, Friday, Saturday)
    markup_classes.row(Sunday)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой день недели нужен?', reply_markup=markup_classes)



@bot.message_handler(commands=['Понедельник'])
def pon(message):
    Day=1
    params=message.text.split()
    school_class = params[1]
    # bot.send_message(message.chat.id,params)
    # bot.send_message(message.chat.id,school_class)
    if school_class == '10А':
        filename = '10а.xls'
    elif school_class == '11А':
        filename = '11а.xls'
    elif school_class == '11Б':
        filename = '11б.xls'
    elif school_class == '9А':
        filename = '9а.xls'
    elif school_class == '9Б':
        filename = '9б.xls'
    elif school_class == '9В':
        filename = '9в.xls'
    elif school_class == '8А':
        filename = '8а.xls'
    elif school_class == '8Б':
        filename = '8б.xls'
    elif school_class == '8В':
        filename = '8в.xls'
    elif school_class == '7А':
        filename = '7а.xls'
    elif school_class == '7Б':
        filename = '7б.xls'
    elif school_class == '7В':
        filename = '7в.xls'
    elif school_class == '6А':
        filename = '6а.xls'
    elif school_class == '6Б':
        filename = '6б.xls'
    elif school_class == '5А':
        filename = '5а.xls'
    elif school_class == '5Б':
        filename = '5б.xls'
    elif school_class == '5В':
        filename = '5в.xls'
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        for i in range(Day - 1, Day):
            result = []
            for j in range(0, 6):
                string=''
                if sheet.cell_value(i, j) !='None':
                    string = f'{j+1}) {sheet.cell_value(i,j)}\n\n'
                    # result.append(j + 1)
                    # result.append(sheet.cell_value(i, j))
                    # result.append('\n\n')
                    result.append(string)
            for i in result:
                bot.send_message(message.chat.id,i)
                # print(*result)


@bot.message_handler(commands=['Вторник'])
def pon(message):
    Day=2
    params=message.text.split()
    school_class = params[1]
    # bot.send_message(message.chat.id,params)
    # bot.send_message(message.chat.id,school_class)
    if school_class == '10А':
        filename = '10а.xls'
    elif school_class == '11А':
        filename = '11а.xls'
    elif school_class == '11Б':
        filename = '11б.xls'
    elif school_class == '9А':
        filename = '9а.xls'
    elif school_class == '9Б':
        filename = '9б.xls'
    elif school_class == '9В':
        filename = '9в.xls'
    elif school_class == '8А':
        filename = '8а.xls'
    elif school_class == '8Б':
        filename = '8б.xls'
    elif school_class == '8В':
        filename = '8в.xls'
    elif school_class == '7А':
        filename = '7а.xls'
    elif school_class == '7Б':
        filename = '7б.xls'
    elif school_class == '7В':
        filename = '7в.xls'
    elif school_class == '6А':
        filename = '6а.xls'
    elif school_class == '6Б':
        filename = '6б.xls'
    elif school_class == '5А':
        filename = '5а.xls'
    elif school_class == '5Б':
        filename = '5б.xls'
    elif school_class == '5В':
        filename = '5в.xls'
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        for i in range(Day - 1, Day):
            result = []
            for j in range(0, 6):
                string=''
                if sheet.cell_value(i, j) !='None':
                    string = f'{j+1}) {sheet.cell_value(i,j)}\n\n'
                    # result.append(j + 1)
                    # result.append(sheet.cell_value(i, j))
                    # result.append('\n\n')
                    result.append(string)
            for i in result:
                bot.send_message(message.chat.id,i)
                # print(*result)


@bot.message_handler(commands=['Среда'])
def pon(message):
    Day=3
    params=message.text.split()
    school_class = params[1]
    # bot.send_message(message.chat.id,params)
    # bot.send_message(message.chat.id,school_class)
    if school_class == '10А':
        filename = '10а.xls'
    elif school_class == '11А':
        filename = '11а.xls'
    elif school_class == '11Б':
        filename = '11б.xls'
    elif school_class == '9А':
        filename = '9а.xls'
    elif school_class == '9Б':
        filename = '9б.xls'
    elif school_class == '9В':
        filename = '9в.xls'
    elif school_class == '8А':
        filename = '8а.xls'
    elif school_class == '8Б':
        filename = '8б.xls'
    elif school_class == '8В':
        filename = '8в.xls'
    elif school_class == '7А':
        filename = '7а.xls'
    elif school_class == '7Б':
        filename = '7б.xls'
    elif school_class == '7В':
        filename = '7в.xls'
    elif school_class == '6А':
        filename = '6а.xls'
    elif school_class == '6Б':
        filename = '6б.xls'
    elif school_class == '5А':
        filename = '5а.xls'
    elif school_class == '5Б':
        filename = '5б.xls'
    elif school_class == '5В':
        filename = '5в.xls'
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        for i in range(Day - 1, Day):
            result = []
            for j in range(0, 6):
                string=''
                if sheet.cell_value(i, j) !='None':
                    string = f'{j+1}) {sheet.cell_value(i,j)}\n\n'
                    # result.append(j + 1)
                    # result.append(sheet.cell_value(i, j))
                    # result.append('\n\n')
                    result.append(string)
            for i in result:
                bot.send_message(message.chat.id,i)
                # print(*result)


@bot.message_handler(commands=['Четверг'])
def pon(message):
    Day=4
    params=message.text.split()
    school_class = params[1]
    # bot.send_message(message.chat.id,params)
    # bot.send_message(message.chat.id,school_class)
    if school_class == '10А':
        filename = '10а.xls'
    elif school_class == '11А':
        filename = '11а.xls'
    elif school_class == '11Б':
        filename = '11б.xls'
    elif school_class == '9А':
        filename = '9а.xls'
    elif school_class == '9Б':
        filename = '9б.xls'
    elif school_class == '9В':
        filename = '9в.xls'
    elif school_class == '8А':
        filename = '8а.xls'
    elif school_class == '8Б':
        filename = '8б.xls'
    elif school_class == '8В':
        filename = '8в.xls'
    elif school_class == '7А':
        filename = '7а.xls'
    elif school_class == '7Б':
        filename = '7б.xls'
    elif school_class == '7В':
        filename = '7в.xls'
    elif school_class == '6А':
        filename = '6а.xls'
    elif school_class == '6Б':
        filename = '6б.xls'
    elif school_class == '5А':
        filename = '5а.xls'
    elif school_class == '5Б':
        filename = '5б.xls'
    elif school_class == '5В':
        filename = '5в.xls'
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        for i in range(Day - 1, Day):
            result = []
            for j in range(0, 6):
                string=''
                if sheet.cell_value(i, j) !='None':
                    string = f'{j+1}) {sheet.cell_value(i,j)}\n\n'
                    # result.append(j + 1)
                    # result.append(sheet.cell_value(i, j))
                    # result.append('\n\n')
                    result.append(string)
            for i in result:
                bot.send_message(message.chat.id,i)
                # print(*result)


@bot.message_handler(commands=['Пятница'])
def pon(message):
    Day=5
    params=message.text.split()
    school_class = params[1]
    # bot.send_message(message.chat.id,params)
    # bot.send_message(message.chat.id,school_class)
    if school_class == '10А':
        filename = '10а.xls'
    elif school_class == '11А':
        filename = '11а.xls'
    elif school_class == '11Б':
        filename = '11б.xls'
    elif school_class == '9А':
        filename = '9а.xls'
    elif school_class == '9Б':
        filename = '9б.xls'
    elif school_class == '9В':
        filename = '9в.xls'
    elif school_class == '8А':
        filename = '8а.xls'
    elif school_class == '8Б':
        filename = '8б.xls'
    elif school_class == '8В':
        filename = '8в.xls'
    elif school_class == '7А':
        filename = '7а.xls'
    elif school_class == '7Б':
        filename = '7б.xls'
    elif school_class == '7В':
        filename = '7в.xls'
    elif school_class == '6А':
        filename = '6а.xls'
    elif school_class == '6Б':
        filename = '6б.xls'
    elif school_class == '5А':
        filename = '5а.xls'
    elif school_class == '5Б':
        filename = '5б.xls'
    elif school_class == '5В':
        filename = '5в.xls'
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        for i in range(Day - 1, Day):
            result = []
            for j in range(0, 6):
                string=''
                if sheet.cell_value(i, j) !='None':
                    string = f'{j+1}) {sheet.cell_value(i,j)}\n\n'
                    # result.append(j + 1)
                    # result.append(sheet.cell_value(i, j))
                    # result.append('\n\n')
                    result.append(string)
            for i in result:
                bot.send_message(message.chat.id,i)
                # print(*result)


@bot.message_handler(commands=['Суббота'])
def pon(message):
    Day=6
    params=message.text.split()
    school_class = params[1]
    # bot.send_message(message.chat.id,params)
    # bot.send_message(message.chat.id,school_class)
    if school_class == '10А':
        filename = '10а.xls'
    elif school_class == '11А':
        filename = '11а.xls'
    elif school_class == '11Б':
        filename = '11б.xls'
    elif school_class == '9А':
        filename = '9а.xls'
    elif school_class == '9Б':
        filename = '9б.xls'
    elif school_class == '9В':
        filename = '9в.xls'
    elif school_class == '8А':
        filename = '8а.xls'
    elif school_class == '8Б':
        filename = '8б.xls'
    elif school_class == '8В':
        filename = '8в.xls'
    elif school_class == '7А':
        filename = '7а.xls'
    elif school_class == '7Б':
        filename = '7б.xls'
    elif school_class == '7В':
        filename = '7в.xls'
    elif school_class == '6А':
        filename = '6а.xls'
    elif school_class == '6Б':
        filename = '6б.xls'
    elif school_class == '5А':
        filename = '5а.xls'
    elif school_class == '5Б':
        filename = '5б.xls'
    elif school_class == '5В':
        filename = '5в.xls'
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        for i in range(Day - 1, Day):
            result = []
            for j in range(0, 6):
                string=''
                if sheet.cell_value(i, j) !='None':
                    string = f'{j+1}) {sheet.cell_value(i,j)}\n\n'
                    # result.append(j + 1)
                    # result.append(sheet.cell_value(i, j))
                    # result.append('\n\n')
                    result.append(string)
            for i in result:
                bot.send_message(message.chat.id,i)
                # print(*result)


@bot.message_handler(commands=['Классы'])
def raspisanie_knopki(message):
    markup_classes = types.ReplyKeyboardMarkup()
    class_10A = types.KeyboardButton('/Класс_10А')
    class_11A = types.KeyboardButton('/Класс_11А')
    class_11B = types.KeyboardButton('/Класс_11Б')
    class_9B = types.KeyboardButton('/Класс_9Б')
    class_9A = types.KeyboardButton('/Класс_9А')
    class_9C = types.KeyboardButton('/Класс_9В')
    class_8A = types.KeyboardButton('/Класс_8А')
    class_8B = types.KeyboardButton('/Класс_8Б')
    class_8C = types.KeyboardButton('/Класс_8В')
    class_7A = types.KeyboardButton('/Класс_7А')
    class_7B = types.KeyboardButton('/Класс_7Б')
    class_7C = types.KeyboardButton('/Класс_7В')
    class_5A = types.KeyboardButton('/Класс_5А')
    class_5B = types.KeyboardButton('/Класс_5Б')
    class_5C = types.KeyboardButton('/Класс_5В')
    class_6A = types.KeyboardButton('/Класс_6А')
    class_6B = types.KeyboardButton('/Класс_6Б')
    markup_classes.row(class_11B, class_11A, class_10A)
    markup_classes.row(class_9A, class_9B, class_9C)
    markup_classes.row(class_8A, class_8B, class_8C)
    markup_classes.row(class_7A, class_7B, class_7C)
    markup_classes.row(class_6A, class_6B)
    markup_classes.row(class_5A, class_5B, class_5C)
    Back = types.KeyboardButton('/Назад')
    markup_classes.row(Back)
    bot.send_message(message.chat.id, 'Какой тебе нужный класс?', reply_markup=markup_classes)

@bot.message_handler(commands=['Воскресенье'])
def vosk(message):
    b = randint(1, 3)
    if b == 1:
        mem1 = open("1.jpg", "rb")
        bot.send_photo(message.chat.id, mem1)
    if b == 2:
        mem2 = open("2.jpg", "rb")
        bot.send_photo(message.chat.id, mem2)
    if b == 3:
        mem3 = open("3.jpg", "rb")
        bot.send_photo(message.chat.id, mem3)
    bot.send_message(message.chat.id, 'Выспись в воскресенье!', parse_mode='html')

@bot.message_handler(commands=['Мем'])
def mem(message):
    bot.send_message(message.chat.id, mems.MEM)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == ["Привет","привет","Hi", 'HI', "Hello"]:
        bot.send_message(message.chat.id, 'Привет', parse_mode='html')
    elif message.text == "Id":
        bot.send_message(message.chat.id, f"Твой ID: {message.chat.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, f"Я тебя не понимаю")


bot.infinity_polling()

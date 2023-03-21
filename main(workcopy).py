from typing import Any
import class_10A,class_11A,class_11Б,class_9Б,class_9А,class_9C,class_7A,class_7B,class_7C,class_8A,class_8B,class_8C
import mems
import telebot
from telebot import types
import openpyxl
import datetime
from random import randint
import sqlite3
conn = sqlite3.connect('users.db',check_same_thread=False)
cursor = conn.cursor()

bot = telebot.TeleBot('5977947434:AAF_I0F6NjS-US_lXaXkKBljX2GsnLb7pGs')
a = datetime.datetime.today().weekday()
a=a+1

@bot.message_handler(commands=['start', 'Start', 'старт', 'Старт'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. Я бот Математического лицея. Создан помочь всем в школе. Нажми /help, чтобы узнать, что я могу.' + '\n' + 'Для дальнейшей работы необходимо указать себя.' + '\n' + 'Например: <pre>/add_user Иванов Иван 5А</pre>'
    # mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>! Я бот Математического лицея. Для дальнейшей работы необходимо указать свой класс.' + '\n' + f'Например: ' + '\n' + '/setusername Ivan' + '\n' + f'/setusersurname Ivanov' + '\n' + f'/setuserclass 11A'
    bot.reply_to(message, mess, parse_mode='html')

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

@bot.message_handler(commands=['printusers'])
def all_print(message):
    sqlite_select_query = """SELECT * from students"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        mess = str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3])
        bot.send_message(message.chat.id,mess)

@bot.message_handler(commands=['logs'])
def logs(message):
    wb = openpyxl.open('аккаунты.xlsx')
    sheet = wb.active
    for row in sheet.rows:
        string = ''
        for cell in row:
            string = string + str(cell.value) + ' '
        bot.send_message(message.chat.id, string)
    wb.save('аккаунты.xlsx')


@bot.message_handler(commands=['Site', 'site', 'website', 'сайт', 'Сайт'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Сайт", url='матлицей.рф'))
    bot.send_message(message.chat.id, 'Перейти на сайт Математического лицея', reply_markup=markup)


@bot.message_handler(commands=['help', 'Help'])
def help(message):
    markup_reply = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('/Сайт')
    start = types.KeyboardButton('/Старт')
    classes = types.KeyboardButton('/Классы')
    meme = types.KeyboardButton('/MEM')
    markup_reply.row(website, start)
    markup_reply.row(classes, meme)
    bot.send_message(message.chat.id, 'Чем могу помочь?', reply_markup=markup_reply)
    # markup_reply.add(website, start, time)


@bot.message_handler(commands=['Классы'])
def raspisanie_knopki(message):
    markup_classes = types.ReplyKeyboardMarkup()
    class_10A = types.KeyboardButton('10А')
    class_11A = types.KeyboardButton('11А')
    class_11B = types.KeyboardButton('11Б')
    class_9A = types.KeyboardButton('9А')
    class_9B = types.KeyboardButton('9Б')
    class_9C = types.KeyboardButton('9В')
    class_8A = types.KeyboardButton('8А')
    class_8B = types.KeyboardButton('8Б')
    class_8C = types.KeyboardButton('8В')
    class_7A = types.KeyboardButton('7А')
    class_7B = types.KeyboardButton('7Б')
    class_7C = types.KeyboardButton('7В')
    # class_6A = types.KeyboardButton('6А')
    # class_6B = types.KeyboardButton('6Б')
    # class_6C = types.KeyboardButton('6В')
    markup_classes.row(class_11B, class_11A, class_10A)
    markup_classes.row(class_9A, class_9B, class_9C)
    markup_classes.row(class_8A, class_8B, class_8C)
    markup_classes.row(class_7A, class_7B, class_7C)
    # markup_classes.row(class_6A, class_6B, class_6C)
    bot.send_message(message.chat.id, 'Какие тебе нужный классы?', reply_markup=markup_classes)


@bot.message_handler(commands=['MEM'])
def mem(message):
    bot.send_message(message.chat.id, mems.MEM)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == ["Привет", 'привет', 'Hi', 'HI', 'Hello']:
        bot.send_message(message.chat.id, 'Привет', parse_mode='html')
    elif message.text == "10А":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_10A.string)
        if a==7:
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
    elif message.text == "11А":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_11A.string)
        if a == 7:
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
    elif message.text == "11Б":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_11Б.string)
        if a == 7:
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
    elif message.text == "9А":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_9А.string)
        if a == 7:
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
    elif message.text == "9Б":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_9Б.string)
        if a == 7:
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
    elif message.text == "9В":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_9C.string)
        if a == 7:
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
    elif message.text == "8А":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_8A.string)
        if a == 7:
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
    elif message.text == "8Б":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_8B.string)
        if a == 7:
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
    elif message.text == "8В":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_8C.string)
        if a == 7:
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
    elif message.text == "7А":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_7A.string)
        if a == 7:
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
    elif message.text == "7Б":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_7B.string)
        if a == 7:
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
    elif message.text == "7В":
        if a == 1 or 2 or 3 or 4 or 5 or 6:
            bot.send_message(message.chat.id, class_7C.string)
        if a == 7:
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
    elif message.text == "MEM":
        bot.send_message(message.chat.id, mems.MEM)
    elif message.text == "Id":
        bot.send_message(message.chat.id, f"Твой ID: {message.chat.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, f"Я тебя не понимаю")


bot.infinity_polling()

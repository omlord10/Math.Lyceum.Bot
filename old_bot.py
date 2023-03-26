# -*- coding: utf8 -*-
import telebot
bot = telebot.TeleBot('TOKEN')
@bot.message_handler(commands=['start','Start','Старт','help', 'Help','back','Назад','Классы','Мем','Site', 'site', 'website', 'сайт', 'Сайт'])
def start(message):
    bot.send_message(message.chat.id,'Привет дорогой друг, мы перешли на нового бота.\nhttps://t.me/Math_Lyceum_bot')

bot.infinity_polling()

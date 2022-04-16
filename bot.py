import os
import telebot
from telebot import types
from dotenv import load_dotenv

import services

load_dotenv ()

bot = telebot.TeleBot(os.getenv('BOT'))


@bot.message_handler(commands=['start'])
def start(message):
    pass

@bot.message_handler(commands=['keyboard'])
def keyboard(message):
    kb = types.ReplyKeyboardMarkup(row_width=1)
    btn_calories = types.KeyboardButton(text='Калории')
    kb.add(btn_calories)
    bot.send_message(message.chat.id, 'Выберите', reply_markup=kb)


@bot.message_handler(content_types='text')
def button_calories(message):
    if message.text == 'Калории':
        data = services.read_json('calories.json')
        user_id = str(message.from_user.id)
        user = data.get(user_id, False)
        kb = types.ReplyKeyboardMarkup(row_width=2)
        btn_limit = types.KeyboardButton(text='Установить лимит')
        message_text = 'Добавьте лимит калорий'
        if user:
            message_text = 'Добавьте или измените лимит калорий'
            btn_calories_save = types.KeyboardButton(text='Записать калории')
            kb.add(btn_calories_save)
        kb.add(btn_limit,)
        bot.send_message(message.chat.id, message_text, reply_markup=kb)
    elif message.text == 'Установить лимит':
        send_limit = bot.reply_to(message, 'Введите лимит')
        bot.register_next_step_handler(send_limit, limit)
    elif message.text == 'Записать калории':
        send_calories = bot.reply_to(message, 'Введите кол-во калорий')
        bot.register_next_step_handler(send_calories, total)


def limit(message):
    data = services.read_json('calories.json')
    user_id = str(message.from_user.id)
    user = data.get(user_id, False)
    if user:
        try:
            data[user_id]['calories_limit'] = int(message.text)
            services.write_json(data)
            bot.send_message(message.chat.id, 'Лимит записан!')
        except ValueError:
            bot.send_message(message.chat.id, 'Введите число')
    else:
        try:
            data[user_id] = {
                'calories_limit': int(message.text),
                'calories_total': 0
            }
            services.write_json(data)
            bot.send_message(message.chat.id, 'Лимит записан!')
        except ValueError:
            bot.send_message(message.chat.id, 'Введите число')


def total(message):
    data = services.read_json('calories.json')
    user_id = str(message.from_user.id)
    user = data.get(user_id, False)
    if user:
        try:
            data[user_id]['calories_total'] += int(message.text)
            services.write_json(data)
            limit = data[user_id]['calories_limit']
            total = data[user_id]['calories_total']
            bot.send_message(message.chat.id, f'Лимит: {limit} \nСъедено: {total}')
        except ValueError:
            bot.send_message(message.chat.id, 'Введите число')


bot.polling()
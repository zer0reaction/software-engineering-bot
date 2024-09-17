import telebot
import creds
from telebot import types


bot = telebot.TeleBot(creds.bot_token)


# Initial message
def hello(message):
    markup = types.InlineKeyboardMarkup()  # Создаем разметку для inline-кнопок
    button1 = types.InlineKeyboardButton("День 1", callback_data='day_1')
    button2 = types.InlineKeyboardButton("День 2", callback_data='day_2')
    button3 = types.InlineKeyboardButton("День 3", callback_data='day_3')

    markup.add(button1, button2, button3)  # Добавляем кнопки в разметку

    bot.send_message(message.chat.id, "Привет! Выберите день:", reply_markup=markup)


def day_1_display(call):
    markup = types.InlineKeyboardMarkup()  # Создаем разметку для inline-кнопок
    button1 = types.InlineKeyboardButton("Назад", callback_data='hello')
    markup.add(button1)  # Добавляем кнопки в разметку

    bot.send_photo(call.message.chat.id, photo=open("img/test.jpg", "rb"), caption="kek", reply_markup=markup)


def day_2_display(call):
    markup = types.InlineKeyboardMarkup()  # Создаем разметку для inline-кнопок
    button1 = types.InlineKeyboardButton("Назад", callback_data='hello')
    markup.add(button1)  # Добавляем кнопки в разметку

    bot.send_message(call.message.chat.id, "Template day 2")


def day_3_display(call):
    markup = types.InlineKeyboardMarkup()  # Создаем разметку для inline-кнопок
    button1 = types.InlineKeyboardButton("Назад", callback_data='hello')
    markup.add(button1)  # Добавляем кнопки в разметку

    bot.send_message(call.message.chat.id, "Template day 3")


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    hello(message)


# Обработчик нажатий на inline-кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'hello':
        hello(call.message)
    elif call.data == 'day_1':
        day_1_display(call)
    elif call.data == 'day_2':
        day_2_display(call)
    elif call.data == 'day_3':
        day_3_display(call)


# Запуск бота
bot.polling(none_stop=True)

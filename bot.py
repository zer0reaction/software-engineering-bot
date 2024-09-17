import telebot
import creds
import msg
from telebot import types


bot = telebot.TeleBot(creds.bot_token)


# Initial message
def hello(message):
    markup = types.InlineKeyboardMarkup()
    day_1_button = types.InlineKeyboardButton("День 1", callback_data='day_1')
    day_2_button = types.InlineKeyboardButton("День 2", callback_data='day_2')
    day_3_button = types.InlineKeyboardButton("День 3", callback_data='day_3')
    facts_button = types.InlineKeyboardButton("Интересные факты", callback_data='facts')

    markup.add(day_1_button, day_2_button, day_3_button, facts_button)

    bot.send_message(message.chat.id, msg.greeting, reply_markup=markup)


def facts(call):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Назад", callback_data='hello')

    markup.add(back_button)

    bot.send_message(call.message.chat.id, msg.facts, reply_markup=markup)


# ----- DAY 1 -----
def day_1_display(call):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Назад", callback_data='hello')
    event_1_button = types.InlineKeyboardButton(msg.day_1_event_1_label, callback_data='day_1_event_1')

    markup.add(event_1_button, back_button)

    bot.send_photo(call.message.chat.id, photo=open(msg.day_1_image, "rb"), caption=msg.day_1_text, reply_markup=markup)

def day_1_event_1_display(call):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Назад", callback_data='day_1')

    markup.add(back_button)

    bot.send_photo(call.message.chat.id, photo=open(msg.day_1_event_1_image, "rb"), caption=msg.day_1_event_1_text, reply_markup=markup)
# -----------------


# ----- DAY 2 -----
def day_2_display(call):
    markup = types.InlineKeyboardMarkup()
    event_1_button = types.InlineKeyboardButton(msg.day_2_event_1_label, callback_data='day_2_event_1')
    back_button = types.InlineKeyboardButton("Назад", callback_data='hello')

    markup.add(event_1_button, back_button)

    bot.send_photo(call.message.chat.id, photo=open(msg.day_2_image, "rb"), caption=msg.day_2_text, reply_markup=markup)

def day_2_event_1_display(call):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Назад", callback_data='day_2')

    markup.add(back_button)

    bot.send_photo(call.message.chat.id, photo=open(msg.day_2_event_1_image, "rb"), caption=msg.day_2_event_1_text, reply_markup=markup)
# -----------------


# ----- DAY 3 -----
def day_3_display(call):
    markup = types.InlineKeyboardMarkup()  # Создаем разметку для inline-кнопок
    event_1_button = types.InlineKeyboardButton(msg.day_3_event_1_label, callback_data='day_3_event_1')
    back_button = types.InlineKeyboardButton("Назад", callback_data='hello')

    markup.add(event_1_button, back_button)

    bot.send_photo(call.message.chat.id, photo=open(msg.day_3_image, "rb"), caption=msg.day_3_text, reply_markup=markup)

def day_3_event_1_display(call):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Назад", callback_data='day_3')

    markup.add(back_button)

    bot.send_photo(call.message.chat.id, photo=open(msg.day_3_event_1_image, "rb"), caption=msg.day_3_event_1_text, reply_markup=markup)
# -----------------


@bot.message_handler(commands=['start'])
def send_welcome(message):
    hello(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'hello':
        hello(call.message)
    elif call.data == 'facts':
        facts(call)

    elif call.data == 'day_1':
        day_1_display(call)
    elif call.data == 'day_2':
        day_2_display(call)
    elif call.data == 'day_3':
        day_3_display(call)

    elif call.data == 'day_1_event_1':
        day_1_event_1_display(call)
    elif call.data == 'day_2_event_1':
        day_2_event_1_display(call)
    elif call.data == 'day_3_event_1':
        day_3_event_1_display(call)

    bot.answer_callback_query(call.id)


bot.polling(none_stop=True)

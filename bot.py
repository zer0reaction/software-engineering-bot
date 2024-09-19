import telebot
import creds
import dicts
from telebot import types


bot = telebot.TeleBot(creds.bot_token)


def hello(message):
    markup = types.InlineKeyboardMarkup()

    for day_key in dicts.days.keys():
        label = dicts.days[day_key]["label"]
        day_button = types.InlineKeyboardButton(label, callback_data=day_key)
        markup.add(day_button)

    facts_button = types.InlineKeyboardButton("Интересные факты", callback_data='facts')
    markup.add(facts_button)

    try:
        bot.send_message(message.chat.id, "Выберите день:", reply_markup=markup)
    except:
        print("Error sending hello")


def facts(call):
    markup = types.InlineKeyboardMarkup()

    for fact_key in dicts.facts.keys():
        label = dicts.facts[fact_key]["label"]
        fact_button = types.InlineKeyboardButton(label, callback_data=fact_key)
        markup.add(fact_button)

    back_button = types.InlineKeyboardButton("Назад", callback_data='hello')
    markup.add(back_button)

    try:
        bot.send_message(call.message.chat.id, "Список фактов:", reply_markup=markup)
    except:
        print("Error sending facts")


def day_display(call, day_key):
    markup = types.InlineKeyboardMarkup()

    for event_key in dicts.days[day_key]["events"].keys():
        label = dicts.days[day_key]["events"][event_key]["label"]
        event_button = types.InlineKeyboardButton(label, callback_data=event_key)
        markup.add(event_button)

    back_button = types.InlineKeyboardButton("Назад", callback_data='hello')
    markup.add(back_button)

    image = open(dicts.days[day_key]["image"], "rb")
    text = dicts.days[day_key]["text"]

    try:
        bot.send_photo(call.message.chat.id, photo=image, caption=text, reply_markup=markup)
    except:
        print("Error sending day")


def event_display(call, day_key, event_key):
    markup = types.InlineKeyboardMarkup()

    back_button = types.InlineKeyboardButton("Назад", callback_data=day_key)
    markup.add(back_button)

    image = open(dicts.days[day_key]["events"][event_key]["image"], "rb")
    text = dicts.days[day_key]["events"][event_key]["text"]

    try:
        bot.send_photo(call.message.chat.id, photo=image, caption=text, reply_markup=markup)
    except:
        print("Error sending event")


def fact_display(call, fact_key):
    markup = types.InlineKeyboardMarkup()

    back_button = types.InlineKeyboardButton("Назад", callback_data='facts')
    markup.add(back_button)

    text = dicts.facts[fact_key]["text"]
    image = open(dicts.facts[fact_key]["image"], "rb")

    try:
        bot.send_photo(call.message.chat.id, photo=image, caption=text, reply_markup=markup)
    except:
        print("Error sending facts")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    hello(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'hello':
        hello(call.message)
    elif call.data == 'facts':
        facts(call)
    elif call.data in dicts.days.keys():
        day_display(call, call.data)
    elif call.data in dicts.facts.keys():
        fact_display(call, call.data)
    elif "event" in call.data:
        for day_key in dicts.days.keys():
            if call.data in dicts.days[day_key]["events"]:
                event_display(call, day_key, call.data)


    print("User " + str(call.from_user.username) + " opened " + call.data)
    try:
        bot.answer_callback_query(call.id)
    except:
        print("Error answering callback")


bot.polling(none_stop=True)

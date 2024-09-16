import telebot
import creds
from telebot import types

bot = telebot.TeleBot(creds.bot_token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()  # Создаем разметку для inline-кнопок
    button1 = types.InlineKeyboardButton("Понедельник", callback_data='monday')
    button2 = types.InlineKeyboardButton("Среда", callback_data='wednesday')
    button3 = types.InlineKeyboardButton("Пятница", callback_data='friday')
    
    markup.add(button1, button2, button3)  # Добавляем кнопки в разметку
    
    bot.send_message(message.chat.id, "Привет! Выберите день:", reply_markup=markup)


# Обработчик нажатий на inline-кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'monday':
        bot.send_message(call.message.chat.id, "Тест для Понедельника")
    elif call.data == 'wednesday':
        bot.send_message(call.message.chat.id, "Тест для Среды")
    elif call.data == 'friday':
        bot.send_message(call.message.chat.id, "Тест для Пятницы")


# Запуск бота
bot.polling(none_stop=True)

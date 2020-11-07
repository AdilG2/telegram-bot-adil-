import telebot
from telebot import types

name = ''
surname = ''
age = 0

bot = telebot.TeleBot("1410891661:AAGr2l8Wctd7JXYoiPBLBhzfN9s9DDJ4oqc")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    s = 'Welcome to my bot, my lord! My creator and father is Adil Mukanbetov'
    bot.reply_to(message, s)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'hello':
        bot.reply_to(message, 'hello, my lord')
    elif message.text == 'привет':
        bot.reply_to(message, 'salam aleikum')
    elif message.text == 'Hello there':
        bot.reply_to(message, 'General Kenobi')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, 'My lord, what is your name?')
        bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Can you write your surname?')
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'What is your age?')
    bot.register_next_step_handler(message, reg_age)


def reg_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'WRITE YOR AGE!!!')

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='yeah boyyy',
                                         callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Nooo', callback_data='no')
    keyboard.add(key_no)
    v = 'As I understand your age is ' + str(age) + \
        '? And yor name and surname is '+name+' '+surname+'?'
    bot.send_message(message.from_user.id, text=v, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Okay, nice to meet you. I will'
                                               ' not forgive you.')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Okay,lets remake it')
        bot.send_message(call.message.chat.id, 'My lord, what is your name?')
        bot.register_next_step_handler(call.message, reg_name)
bot.polling()

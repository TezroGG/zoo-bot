import telebot
from telebot import types

bot = telebot.TeleBot('token')

bd = []

@bot.message_handler(commands=['start', 'Start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    income = types.KeyboardButton('Выбрать доход')
    markup.add(income)

    userfname = message.from_user.first_name
    bot.send_message(message.chat.id, f'Привет, <b>{userfname}</b>! Этот бот поможет выбрать тебе питомца',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler()
def income(message):
    if message.text == ('Выбрать доход'):
        sent = bot.send_message(message.chat.id, 'Напиши свой доход в рублях')
        bot.register_next_step_handler(sent, user_income_f)

def user_income_f(message):
    bd.append(message.text)  #bd[0]




bot.polling(none_stop=True)

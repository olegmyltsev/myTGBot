import telebot
from telebot import types

token: str = '7896898992:AAHeeBulSBtvseJIkdJ3mU3-vpHvT0k6isE'
bot = telebot.TeleBot(token)
isWelcomeSends: bool = False


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn = types.KeyboardButton('Press me!')
    markup.add(itembtn)

    msg = bot.send_message(message.chat.id, "Hello, press the button!", reply_markup=markup)

    bot.register_next_step_handler(msg, test)

def test(message):
    print(message.text)
    bot.send_message(message.chat.id,'You send me message', reply_markup=types.ReplyKeyboardRemove())


bot.infinity_polling()

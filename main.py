from pydoc import text
from string import digits
from urllib import response
import telebot
from config import bot_token
import random

bot=telebot.TeleBot(bot_token)
DIGITS=[str (x) for (x) in range (10)]

my_number=''


@bot.message_handler(comands=['start','game'])
def start_game(message):
    digits=DIGITS.copy()
    my_number=''
    for pos in  range(4):
        if pos:
            digit=random.choice(digits)
        else:
            digits=random.choice(digits[1:])
        my_number+=digit
        digits.remove(digit)
    bot.reply_to(message,f'Я загадал четырехзначное число, попробуй  отгадать{message.from_user.first_name}!')
@bot.message_handler(content_types=['text'])
def bot_answer(message):
    text=message.text
    if len(text)==4 and text.isnumeric:
        response=text
    else:
        response='Пришлт мне 4-ех значное число'
    bot.send_message(message.from_user.id,response)

if __name__=='__main__':
    bot.polling(non_stop=True)
   

     





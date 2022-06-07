from string import digits
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
    bot.reply_to(message,my_number)
if __name__=='__main__':
    bot.polling(non_stop=True)
     





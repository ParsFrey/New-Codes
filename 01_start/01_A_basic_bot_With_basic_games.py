"""
name of the bot: SomebotForSomthing bot(yes the 'somthing' really doesn`t have an 'e'.
username: Parsaff30_bot
"""
import random
import telebot

bot = telebot.TeleBot('6740329565:AAEKcCLqETaRS6AuiTZPatnZ_K_1KCB6JjI')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """Hello Human! I`M A BOT that wants to play basic games with you!\nwhat game do you prefer to play?\nfor fliping a coin, please type 'coin flip'\n for rock paper scissors, please type 'rock paper scissors'""")


@bot.message_handler(func=lambda message: 'coin flip' in message.text.lower())
def coinflip(message):
    try:
        r = random.randint(0,1)
        if r == 1:
            response = "IT IS TAILS!"
        else:
            response = "IT IS HEADS!"

    except ValueError:
        responce = "you should Enter 'coin flip' to play Coinflip or 'rock paper scissors' to play RockPaperScissors" 


    bot.reply_to(message, response)

bot.polling()

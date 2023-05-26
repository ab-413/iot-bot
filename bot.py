
import telebot
import requests
from settings import log
import settings
from methods import getData, getUserState, getUserID

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    log.info(f"cmd: '{message.text}' from: {message.chat.id}")
    bot.send_message(message.chat.id, "Type /getdata")


@bot.message_handler(commands=['myid'])
def send_id(message):
    bot.send_message(message.chat.id, f"You chat ID: {message.chat.id}")
    log.info(f"cmd: '{message.text}' from: {message.chat.id}")


@bot.message_handler(commands=['getdata'])
def send_temperature(message):
    try:
        log.info(f"cmd: '{message.text}' from: {message.chat.id}")
        if getUserState(message.chat.id):
            bot.send_message(message.chat.id, getData(
                getUserID(message.chat.id)))
        else:
            bot.send_message(message.chat.id, "You account diactivated.")
    except requests.exceptions.ConnectionError:
        bot.send_message(
            message.chat.id, "Oops. Problem with connection. Try later.")
        raise


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    log.info(f"msg: '{message.text}' from: {message.chat.id}")


bot.infinity_polling()

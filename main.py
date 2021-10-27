import telebot

bot = telebot.TeleBot("1919018669:AAEuwx3xFcEHiYURzi6x94aiCMNeOvSIqLo")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Hii")


bot.polling(True)
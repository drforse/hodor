import telebot
import os
bot = telebot.TeleBot(os.environ['token'])

@bot.message_handler(content_types = ['text'])
def reply_unic_fucking_func(message):
    list = ['hodor','ходор']
    for keyword in list:
        if keyword in message.text.lower():
            bot.reply_to(message, 'Hodor')
    if message.reply_to_message and message.reply_to_message.from_user.id == 875106649:
        bot.reply_to(message, 'Hodor')
        

bot.polling()

import telebot
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')
greetings = ["Hello","hi","welcome"]
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start","help"])
def welcome(message):
    bot.send_message(message.chat.id,"مرحبا بك في هذا البوت الله يستر ما نبعرها")

def isMSg(message):
    return True

@bot.message_handler(func=isMSg)
def reply(message):
    words = message.text.split().lower()

    if words[0].lower() in greetings :
        return bot.reply_to(message, "ع راسي يا طيب")
    else:
        return bot.reply_to(message,"ماشي الحال انت كيفك")
    

bot.polling()
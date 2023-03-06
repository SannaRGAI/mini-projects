import telebot 
from decouple import config
token = config('TOKEN')

bot =telebot. TeleBot(token)

# @bot.message_handler(commands =['start'])
# def start_message(message):
#     bot.send_message(892891195, 'godmorgon')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id,'CAACAgMAAxkBAAEIBTZkBXYjKZsQQHTzqrN8P0p08kskjQACKwQAAr-MkAQUljpk_Jhu6C4E')
    bot.send_photo(message.chat.id,'https://images.app.goo.gl/DmzwQGqk6qzPuaE1A')

#bot.polling()

@bot.message_handler(content_types = ['text'])
def aaaa(message):
    if message.text == 'hi there':
        bot.send_message(message.chat.id,'hi there')
    else:        
        bot.send_message(message.chat.id,'message is not recognised')



bot.polling()
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import random

bot = telebot.TeleBot('5940847478:AAF-cwf8wCPnZIKl8K3sTSBq6hOdta8pJPc')


@bot.message_handler(content_types=['text'])
def get_capibara(message):
    if message.text == "/get_capibara":
        number = random.randint(1, 4)
        if number == 1:
            bot.send_message(message.from_user.id, "Поздравляю, вам выпала умиротворённая капибара!")
            bot.send_photo(message.from_user.id,
                           'https://natworld.info/wp-content/uploads/2018/02/vodosvinka-ili-kapibara.jpg')
        elif number == 2:
            bot.send_message(message.from_user.id, "Поздравляю, вам выпала  капибара, отдыхающая в водичке!")
            bot.send_photo(message.from_user.id,
                           'https://s9.travelask.ru/uploads/post/000/025/923/main_image/full-2af6fc8c8210d9ac04b6f99f426b45bd.jpg')
        elif number == 3:
            bot.send_message(message.from_user.id, "Поздравляю, вам выпала  крутая капибара!!")
            bot.send_photo(message.from_user.id,
                           'https://i.etsystatic.com/36264433/r/il/6f8250/4000983595/il_fullxfull.4000983595_49pk.jpg')
        elif number == 4:
            bot.send_message(message.from_user.id, "Поздравляю, вам выпала  зевающая капибара!")
            bot.send_photo(message.from_user.id,
                           'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS3DIQZKgysknak2J5kDXnxluZPCdFJEIX1J6ZI1ByLXh7Wn9N3')
    elif message.text == "/help":
        bot.send_message(message.from_user.id,
                         "Напиши /get_capibara или тыкни на кнопку, чтобы получить свою собственную капибаринку!")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)

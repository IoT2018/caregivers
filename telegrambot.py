import telegram
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, utils

def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome to the Smart Caregiver assistant \n"
                                                          "please write your caregiver ID followed by \ID")

def registry(bot, update, args):
    reply_message = ' '.join(args)

    # button_list = [KeyboardButton("Hello", callback_data=location),
    #                KeyboardButton("Report", callback_data=report)]

    # reply_markup = ReplyKeyboardMarkup(button_list)
    bot.send_message(chat_id=update.message.chat_id, text="echo")

def location(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="The old man is not here")

def report(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="The old man is alive")


if __name__== '__main__':
    token = '556229447:AAH4bIzvmk-HXYLl3X9bzHqIC61hGH29Hfo'
    updater = Updater(token=token) #config the bot token
    dispatcher= updater.dispatcher #create the updater
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO) #basic configuration of the logging for event or errors

    #reply to start command
    start_handler = CommandHandler('start',start) #execute the function start when the method /start is done in telegram
    dispatcher.add_handler(start_handler)

    registry_handler = CommandHandler('id', registry, pass_args=True)
    dispatcher.add_handler(registry_handler)

    location_handler = MessageHandler('Location',location)

    updater.start_polling()





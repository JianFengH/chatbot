from pydoc import text

from telegram import Update, message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
from config import config
import configparser
import os

#Use the function from MaclehoseTrail
from MaclehoseTrail import checkroute
from LantauTrail import checkroute2
from WilsonTrail import checkroute3

global redis1

def main():

    #////connect the bot
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['telegram']['access_token']),use_context = True)
    dispatcher = updater.dispatcher
    

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    #access_token = config('telegram')['access_token']
    #logging.info('telegramParams access_token: %s', access_token)



    #////FIVE SUB MACLEHOSE TRAIL
    dispatcher.add_handler(CommandHandler("MACLEHOSE1",Trail1))
    dispatcher.add_handler(CommandHandler("MACLEHOSE2",Trail1))
    dispatcher.add_handler(CommandHandler("MACLEHOSE3",Trail1))
    dispatcher.add_handler(CommandHandler("MACLEHOSE4",Trail1))
    dispatcher.add_handler(CommandHandler("MACLEHOSE5",Trail1))

    #////FIVE SUB LANTAU TRAIL
    dispatcher.add_handler(CommandHandler("LANTAU1",Trail2))
    dispatcher.add_handler(CommandHandler("LANTAU2",Trail2))
    dispatcher.add_handler(CommandHandler("LANTAU3",Trail2))
    dispatcher.add_handler(CommandHandler("LANTAU4",Trail2))
    dispatcher.add_handler(CommandHandler("LANTAU5",Trail2))    

    #////FIVE SUB WILSON TRAIL
    dispatcher.add_handler(CommandHandler("WILSON1",Trail3))
    dispatcher.add_handler(CommandHandler("WILSON2",Trail3))
    dispatcher.add_handler(CommandHandler("WILSON3",Trail3))
    dispatcher.add_handler(CommandHandler("WILSON4",Trail3))
    dispatcher.add_handler(CommandHandler("WILSON5",Trail3))    


    updater.start_polling()
    updater.idle()
    


    #////MACLEHOSE TRAIL
def Trail1(update: Update, context: CallbackContext) -> None:
    logging.info(str(update.message.text))
    result =checkroute(update.message.text)
    Result = result[0]
    update.message.reply_text('Here is the route:')
    context.bot.send_message(chat_id=update.effective_chat.id,text = Result)


    #////LANTAU TRAIL
def Trail2(update: Update, context: CallbackContext) -> None:
    logging.info(str(update.message.text))
    result =checkroute2(update.message.text)
    Result = result[0]
    update.message.reply_text('Here is the route:')
    context.bot.send_message(chat_id=update.effective_chat.id,text = Result)


    #/////WILSON TRAIL
def Trail3(update: Update, context: CallbackContext) -> None:
    logging.info(str(update.message.text))
    result =checkroute3(update.message.text)
    Result = result[0]
    update.message.reply_text('Here is the route:')
    context.bot.send_message(chat_id=update.effective_chat.id,text = Result)
   
    

if __name__ == '__main__':
    main()
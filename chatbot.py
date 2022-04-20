from cgi import test
from pydoc import text

from telegram import Update, message, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import logging
from config import config
import configparser
import os

# Use the function from MaclehoseTrail
from MaclehoseTrail import checkroute
from LantauTrail import checkroute2
from WilsonTrail import checkroute3

global redis1


def main():

    # ////connect the bot
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(
        token=(config['telegram']['access_token']), use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    #access_token = config('telegram')['access_token']
    #logging.info('telegramParams access_token: %s', access_token)

    # ////Setting start Menu
    dispatcher.add_handler(CommandHandler("start", Startmenu))
    dispatcher.add_handler(CallbackQueryHandler(Checkmenu))

    # ////FIVE SUB MACLEHOSE TRAIL
    dispatcher.add_handler(CommandHandler("MACLEHOSE1", Trail1))
    dispatcher.add_handler(CommandHandler("MACLEHOSE2", Trail1))
    dispatcher.add_handler(CommandHandler("MACLEHOSE3", Trail1))
    dispatcher.add_handler(CommandHandler("MACLEHOSE4", Trail1))
    dispatcher.add_handler(CommandHandler("MACLEHOSE5", Trail1))

    # ////FIVE SUB LANTAU TRAIL
    dispatcher.add_handler(CommandHandler("LANTAU1", Trail2))
    dispatcher.add_handler(CommandHandler("LANTAU2", Trail2))
    dispatcher.add_handler(CommandHandler("LANTAU3", Trail2))
    dispatcher.add_handler(CommandHandler("LANTAU4", Trail2))
    dispatcher.add_handler(CommandHandler("LANTAU5", Trail2))

    # ////FIVE SUB WILSON TRAIL
    dispatcher.add_handler(CommandHandler("WILSON1", Trail3))
    dispatcher.add_handler(CommandHandler("WILSON2", Trail3))
    dispatcher.add_handler(CommandHandler("WILSON3", Trail3))
    dispatcher.add_handler(CommandHandler("WILSON4", Trail3))
    dispatcher.add_handler(CommandHandler("WILSON5", Trail3))


    updater.start_polling()
    updater.idle()

    # ////MACLEHOSE TRAIL


def Trail1(update: Update, context: CallbackContext) -> None:
    logging.info(str(update.message.text))
    result = checkroute(update.message.text)
    Result = result[0]
    update.message.reply_text('Here is the route:')
    context.bot.send_message(chat_id=update.effective_chat.id, text=Result)

    # ////LANTAU TRAIL


def Trail2(update: Update, context: CallbackContext) -> None:
    logging.info(str(update.message.text))
    result = checkroute2(update.message.text)
    Result = result[0]
    update.message.reply_text('Here is the route:')
    context.bot.send_message(chat_id=update.effective_chat.id, text=Result)

    # /////WILSON TRAIL


def Trail3(update: Update, context: CallbackContext) -> None:
    logging.info(str(update.message.text))
    result = checkroute3(update.message.text)
    Result = result[0]
    update.message.reply_text('Here is the route:')
    context.bot.send_message(chat_id=update.effective_chat.id, text=Result)

#startMenu
def Startmenu(update: Update, context: CallbackContext) -> None:
    Text = "Welcome to this hiking trail finder robot!\
         The robot currently offers three Long Distance Hiking Trails for those hikers,\
              please select the button for the route you want to search."
    update.message.reply_text(text=Text, reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton('MACLEHOSE TRAIL', callback_data='1')],
            [InlineKeyboardButton('LANTAU TRAIL', callback_data='2')],
            [InlineKeyboardButton('WILSON TRAIL', callback_data='3')]]))


#get the callback data from startmenu and respond
def Checkmenu(update: Update, context: CallbackContext) -> None:
    querydata = update.callback_query
    logging.info(str(querydata))

    text1 = ("Here are the five routes for Maclehose Trail.You can click on them directly to get the route.\n\n"
    " /MACLEHOSE1 \n\n /MACLEHOSE2 \n\n /MACLEHOSE3 \n\n /MACLEHOSE4 \n\n /MACLEHOSE5")

    text2 = ("Here are the five routes for Lantau Trail.You can click on them directly to get the route.\n\n"
    "/LANTAU1 \n\n /LANTAU2 \n\n /LANTAU3 \n\n /LANTAU4 \n\n /LANTAU5")

    text3 = "Here are the five routes for Wilson Trail.You can click on them directly to get the route.\n\n"
    "/WILSON1 \n\n /WILSON2 \n\n /LANTAU3 \n\n /LANTAU4 \n\n /LANTAU5"

    if querydata.data == "1":
        update.callback_query.edit_message_text(text =text1 )
    elif querydata.data == "2":
        update.callback_query.edit_message_text(text =text2 )
    elif querydata.data == "3":
         update.callback_query.edit_message_text(text =text3 )
         

if __name__ == '__main__':
    main()

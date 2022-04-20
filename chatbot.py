from cgi import test
from pydoc import text
from random import randint
from telegram import Update, Video, message, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import logging
from config import config
import configparser
import os

# Use the function from MaclehoseTrail
from MaclehoseTrail import Photo, checkroute
from LantauTrail import checkroute2
from WilsonTrail import checkroute3
from CookingVideo import watch

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

    # ////Sharing cooking videos
    dispatcher.add_handler(CommandHandler("cookingvideo", Watch))

    updater.start_polling()
    updater.idle()

    # ////MACLEHOSE TRAIL
def Trail1(update: Update, context: CallbackContext) -> None:
    logging.info(str(update.message.text))
    result,Photo = checkroute(update.message.text)
    update.message.reply_text('Here are the route and landscape photo:')
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=Photo)

    # ////LANTAU TRAIL
def Trail2(update: Update, context: CallbackContext) -> None:
    logging.info(str(update.message.text))
    result,Photo = checkroute2(update.message.text)
    update.message.reply_text('Here are the route and landscape photo:')
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=Photo)
    

    # /////WILSON TRAIL
def Trail3(update: Update, context: CallbackContext) -> None:
    logging.info(str(update.message.text))
    result,Photo = checkroute3(update.message.text)
    update.message.reply_text('Here are the route and landscape photo:')
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=Photo)

#startMenu
def Startmenu(update: Update, context: CallbackContext) -> None:
    Text = ("Welcome to the windbot! This bot includes three famous hiking trails in Hong Kong and some cooking videos."
    " Now it can not only share hiking trails with you, but also cooking videos! \n"
    "You can click the button to get the service~")
    update.message.reply_text(text=Text, reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton('MACLEHOSE TRAIL', callback_data='1')],
            [InlineKeyboardButton('LANTAU TRAIL', callback_data='2')],
            [InlineKeyboardButton('WILSON TRAIL', callback_data='3')],
            [InlineKeyboardButton('COOKING VIDEOS', callback_data='4')]]))


#get the callback data from startmenu and respond
def Checkmenu(update: Update, context: CallbackContext) -> None:
    querydata = update.callback_query
    logging.info(str(querydata))

    text1 = ("Here are the five routes for Maclehose Trail.You can click on them directly to get the route.\n\n"
    " The numbers after the command represent the order of the Maclehose Trail\n\n"
    " /MACLEHOSE1 \n\n /MACLEHOSE2 \n\n /MACLEHOSE3 \n\n /MACLEHOSE4 \n\n /MACLEHOSE5")

    text2 = ("Here are the five routes for Lantau Trail.You can click on them directly to get the route.\n\n"
    " The numbers after the command represent the order of the Lantau Trail\n\n"
    " /LANTAU1 \n\n /LANTAU2 \n\n /LANTAU3 \n\n /LANTAU4 \n\n /LANTAU5")

    text3 = ("Here are the five routes for Wilson Trail.You can click on them directly to get the route."
    " The numbers after the command represent the order of the Wilson Trail\n\n"
    " /WILSON1 \n\n /WILSON2 \n\n /WILSON3 \n\n /WILSON4 \n\n /WILSON5")

    text4 = ("If you want to enjoy wonderful cooking videos, then I recommend Gordon Ramsay,"
    " a Top chef from the UK, whose videos I am sure you will enjoy!\n\n"
    "Click on the commands below to access the video\n\n""/cookingvideo")

    if querydata.data == "1":
        update.callback_query.edit_message_text(text =text1 )
    elif querydata.data == "2":
        update.callback_query.edit_message_text(text =text2 )
    elif querydata.data == "3":
         update.callback_query.edit_message_text(text =text3 )
    elif querydata.data == "4":
         update.callback_query.edit_message_text(text =text4 )


def Watch(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('The cooking video is coming~')
    Cvideo = watch()
    context.bot.send_message(chat_id=update.effective_chat.id,text=Cvideo, disable_web_page_preview = "False")



if __name__ == '__main__':
    main()

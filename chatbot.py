from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
from config import config

global redis1

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    access_token = config('telegram')['access_token']

    logging.info('telegramParams access_token: %s', access_token)


if __name__ == '__main__':
    main()
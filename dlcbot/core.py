import re

import telegram
from telegram.ext import Updater, CommandHandler

from dlcbot.providers import DLC

class DlcBot:

    COMMAND_DEFINITION = 'def'

    def __init__(self, token):
        self.updater = Updater(token=token)

    def configure_callbacks(self):
        dispatcher = self.updater.dispatcher

        dispatcher.add_handler(CommandHandler(
            self.COMMAND_DEFINITION,
            self.__definition_handler
        ))

    def __definition_handler(self, bot, update):
        chat_id = update.message.chat_id
        message = update.message.text

        word = self.__strip_command(self.COMMAND_DEFINITION, message)

        provider = DLC()
        definition = provider.find(word)

        bot.send_message(chat_id, definition)

    def __strip_command(self, command, message):
        return message.replace(f'/{command} ', '')

    def start(self):
        self.configure_callbacks()
        self.updater.start_polling()
        self.updater.idle()

    def stop(self):
        self.updater.stop()

import re

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

from dlcbot import messages, commands

class DlcBot:

    AVAILABLE_COMMANDS = [
        commands.DLC,
        commands.DCVB
    ]

    AVAILABLE_MESSAGES = [
        messages.DLC,
        messages.DCVB
    ]

    def __init__(self, token):
        self.updater = Updater(token=token)

    def start(self):
        self._configure_callbacks()
        self.updater.start_polling()
        self.updater.idle()

    def stop(self):
        self.updater.stop()

    def _configure_callbacks(self):
        self._configure_commands()
        self._configure_handlers()

    def _configure_commands(self):
        dispatcher = self.updater.dispatcher
        for command in self.AVAILABLE_COMMANDS:
            dispatcher.add_handler(CommandHandler(
               command.NAME,
               command.handler
            ))

    def _configure_handlers(self):
        dispatcher = self.updater.dispatcher
        for message in self.AVAILABLE_MESSAGES:
            dispatcher.add_handler(MessageHandler(
               message.filter,
               message.handler
            ))
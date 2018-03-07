import re

import telegram
from telegram.ext import Updater, CommandHandler

from dlcbot import commands

class DlcBot:

    AVAILABLE_COMMANDS = [
        commands.DLC,
        commands.DCVB,
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
        dispatcher = self.updater.dispatcher

        for command in self.AVAILABLE_COMMANDS:
            dispatcher.add_handler(CommandHandler(
               command.NAME,
               command.handler
            ))

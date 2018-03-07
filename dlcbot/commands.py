from dlcbot.dictionary import Factory

class Command:
    NAME = None
    DICTIONARY = None

    @property
    def dictionary(self):
        raise NotImplementedError()

    @classmethod
    def handler(cls, bot, update):
        chat_id = update.message.chat_id
        message = update.message.text
        word = cls._parse_message(message)

        definition =  cls.DICTIONARY.find(word)

        bot.send_message(chat_id, definition)

    @classmethod
    def _parse_message(cls, message):
        return message.replace(f'/{cls.NAME} ', '')


class DLC(Command):
    NAME = 'dlc'
    DICTIONARY = Factory.dlc()


class DCVB(Command):
    NAME = 'dcvb'
    DICTIONARY = Factory.dcvb()


from dlcbot.dictionary import Factory


class Message:
    TEXT = None
    NAME = None
    DICTIONARY = None

    @classmethod
    def filter(cls, message):
        return message.text and message.text.lower().startswith(cls.TEXT)

    @classmethod
    def handler(cls, bot, update):
        chat_id = update.message.chat_id
        message = update.message.text
        word = cls._parse_message(message)

        definition =  cls.DICTIONARY.find(word)

        bot.send_message(chat_id, definition)

    @classmethod
    def _parse_message(cls, message):
        return message.replace(f'{cls.TEXT} ', '')


class DLC(Message):
    TEXT = '!dlc'
    NAME = 'dlc'
    DICTIONARY = Factory.dlc()


class DCVB(Message):
    TEXT = '!dcvb'
    NAME = 'dcvb'
    DICTIONARY = Factory.dcvb()
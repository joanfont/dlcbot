
class Command:
    NAME = None

    @classmethod
    def handler(cls, bot, update):
        raise NotImplementedError()

    @classmethod
    def _parse_message(cls, message):
        return message.replace(f'/{cls.NAME} ', '')


class DictionaryCommandDeprecated(Command):

    @classmethod
    def handler(cls, bot, update):
        chat_id = update.message.chat_id
        message = update.message.text
        word = cls._parse_message(message)
        bot.send_message(
            chat_id,
            f'Usa `!{cls.NAME} {word}` per a obtenir la definició de la paraula',
            parse_mode='Markdown'
        )


class DLC(DictionaryCommandDeprecated):
    NAME = 'dlc'


class DCVB(DictionaryCommandDeprecated):
    NAME = 'dcvb'
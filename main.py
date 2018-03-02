import logging
from dlcbot.config import config
from dlcbot.core import DlcBot

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

bot = DlcBot(config.TELEGRAM_TOKEN)

if __name__ == '__main__':
    try:
        bot.start()
    except KeyboardInterrupt:
        exit(1)

import decouple


class Config:

    @property
    def TELEGRAM_TOKEN(self):
        return decouple.config('TELEGRAM_TOKEN')


config = Config()

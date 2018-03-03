import decouple


class Config:

    @property
    def TELEGRAM_TOKEN(self):
        return decouple.config('TELEGRAM_TOKEN')

    @property
    def REDIS_HOST(self):
        return decouple.config('REDIS_HOST')

    @property
    def REDIS_PORT(self):
        return decouple.config('REDIS_PORT')

config = Config()

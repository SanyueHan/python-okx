from enum import Enum


class Side(Enum):
    BUY = 'buy'
    SELL = 'sell'
    NULL = ''

    def __bool__(self):
        return bool(self.value)

from enum import Enum


class Currency(Enum):
    # 稳定币
    USDT = 'USDT'
    USDC = 'USDC'
    TUSD = 'TUSD'
    USDK = 'USDK'

    # 平台币
    OKB = 'OKB'

    # 比特币
    BTC = 'BTC'
    BCH = 'BCH'
    BSV = 'BSV'

    NULL = ''

    def __bool__(self):
        return bool(self.value)

from enum import Enum

from .currency import Currency
from .instance_type import InstanceType


class Instance(Enum):
    # SPOT
    TUSD_USDT = 'TUSD-USDT', Currency.TUSD, Currency.USDT, InstanceType.SPOT, 5, 6, 5

    BTC_USDT = 'BTC-USDT', Currency.BTC, Currency.USDT, InstanceType.SPOT, 1, 8, 1
    BCH_USDT = 'BCH-USDT', Currency.BCH, Currency.USDT, InstanceType.SPOT, 2, 6, 2
    BSV_USDT = 'BSV-USDT', Currency.BSV, Currency.USDT, InstanceType.SPOT, 2, 6, 2

    BTC_USDC = 'BTC-USDC', Currency.BTC, Currency.USDC, InstanceType.SPOT, 1, 8, 1
    BCH_USDC = 'BCH-USDC', Currency.BCH, Currency.USDC, InstanceType.SPOT, 2, 4, 2
    BSV_USDC = 'BSV-USDC', Currency.BSV, Currency.USDC, InstanceType.SPOT, 2, 4, 2

    # SWAP

    NULL = '', Currency.NULL, Currency.NULL, InstanceType.NULL, 0, 0, 0

    def __init__(self, id_: str, base: Currency, quote: Currency, instance_type: InstanceType, price_precision, size_precision, amount_precision):
        self.__id = id_
        self.__base = base    # 交易货币
        self.__quote = quote  # 计价货币
        self.__type = instance_type
        self.__price_precision = price_precision
        self.__size_precision = size_precision
        self.__amount_precision = amount_precision

    def __bool__(self):
        return bool(self.value)

    @property
    def id(self) -> str:
        return self.__id

    @property
    def base(self) -> Currency:
        return self.__base

    @property
    def quote(self) -> Currency:
        return self.__quote

    @property
    def type(self) -> InstanceType:
        return self.__type

    @property
    def price_precision(self) -> int:
        return self.__price_precision

    @property
    def size_precision(self) -> int:
        return self.__size_precision

    @property
    def amount_precision(self) -> int:
        return self.__amount_precision

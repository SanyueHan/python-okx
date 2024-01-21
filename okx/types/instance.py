from enum import Enum

from .currency import Currency
from .instance_type import InstanceType


class Instance(Enum):
    # SPOT
    TUSD_USDT = 'TUSD-USDT', Currency.TUSD, Currency.USDT, InstanceType.SPOT, 5, 6, 5, None

    BTC_USDT = 'BTC-USDT', Currency.BTC, Currency.USDT, InstanceType.SPOT, 1, 8, 1, 0.00001
    BCH_USDT = 'BCH-USDT', Currency.BCH, Currency.USDT, InstanceType.SPOT, 2, 6, 2, 0.01
    BSV_USDT = 'BSV-USDT', Currency.BSV, Currency.USDT, InstanceType.SPOT, 2, 6, 2, 0.1

    BTC_USDC = 'BTC-USDC', Currency.BTC, Currency.USDC, InstanceType.SPOT, 1, 8, 1, None
    BCH_USDC = 'BCH-USDC', Currency.BCH, Currency.USDC, InstanceType.SPOT, 2, 4, 2, None
    BSV_USDC = 'BSV-USDC', Currency.BSV, Currency.USDC, InstanceType.SPOT, 2, 4, 2, None

    # SWAP

    NULL = '', Currency.NULL, Currency.NULL, InstanceType.NULL, 0, 0, 0, 0.0

    def __init__(self, id_: str, base: Currency, quote: Currency, instance_type: InstanceType,
                 price_precision: int, size_precision: int, amount_precision: int, min_size: float):
        self.__id = id_
        self.__base = base    # 交易货币
        self.__quote = quote  # 计价货币
        self.__type = instance_type
        self.__price_precision = price_precision
        self.__size_precision = size_precision
        self.__amount_precision = amount_precision
        self.__min_size = min_size

    def __bool__(self):
        return bool(self.value)

    @property
    def id(self) -> str:
        if self.__id is None:
            raise NotImplementedError
        return self.__id

    @property
    def base(self) -> Currency:
        if self.__base is None:
            raise NotImplementedError
        return self.__base

    @property
    def quote(self) -> Currency:
        if self.__quote is None:
            raise NotImplementedError
        return self.__quote

    @property
    def type(self) -> InstanceType:
        if self.__type is None:
            raise NotImplementedError
        return self.__type

    @property
    def price_precision(self) -> int:
        if self.__price_precision is None:
            raise NotImplementedError
        return self.__price_precision

    @property
    def size_precision(self) -> int:
        if self.__size_precision is None:
            raise NotImplementedError
        return self.__size_precision

    @property
    def amount_precision(self) -> int:
        if self.__amount_precision is None:
            raise NotImplementedError
        return self.__amount_precision

    @property
    def min_size(self) -> float:
        if self.__min_size is None:
            raise NotImplementedError
        return self.__min_size

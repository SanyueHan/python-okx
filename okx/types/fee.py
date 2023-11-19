from enum import Enum


class Fee(Enum):
    """
    https://www.okx.com/cn/fees
    """

    Lv1 = 0.080, 0.100
    Lv2 = 0.075, 0.095
    Lv3 = 0.070, 0.090
    Lv4 = 0.065, 0.085
    Lv5 = 0.060, 0.080

    def __init__(self, entry_order_rate, market_order_rate):
        """
        :param entry_order_rate: 挂单成交手续费
        :param market_order_rate: 吃单成交手续费
        """
        self.__entry_order_rate = entry_order_rate * 0.01
        self.__market_order_rate = market_order_rate * 0.01

    @property
    def entry_order_rate(self):
        return self.__entry_order_rate

    @property
    def market_order_rate(self):
        return self.__market_order_rate

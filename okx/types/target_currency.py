from enum import Enum


class TargetCurrency(Enum):
    """
    In forex, currencies are traded in pairs.
    The first currency is called the base currency and the second currency is called the quote currency.
    So for example, EUR/USD, means that the base currency is the Euro and the quote currency is the USD.
    """
    BASE_CCY = 'base_ccy'    # 交易货币
    QUOTE_CCY = 'quote_ccy'  # 计价货币
    NULL = ''

    def __bool__(self):
        return bool(self.value)

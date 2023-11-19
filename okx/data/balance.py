from ..types import Currency


class Balance:
    def __init__(self, currency: Currency, available=0, frozen=0, cash=0):
        """
        :available: 当前可用的
        :frozen: 订单中冻结的
        :cash: 总共的
        """
        self._ccy = currency
        self._available_balance = available
        self._frozen_balance = frozen
        self._cash_balance = cash

    def __repr__(self):
        return f"Balance(ccy={self._ccy.name}, availBal={self._available_balance}, frozenBal={self._frozen_balance}, cashBal={self._cash_balance})"

    @classmethod
    def from_json(cls, data):
        balance = cls(Currency[data['ccy']])
        balance._available_balance = float(data['availBal'])
        balance._frozen_balance = float(data['frozenBal'])
        balance._cash_balance = float(data['cashBal'])
        return balance

    @property
    def available_balance(self):
        return self._available_balance

    @property
    def frozen_balance(self):
        return self._frozen_balance

    @property
    def cash_balance(self):
        return self._cash_balance

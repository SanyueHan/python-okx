import datetime

from ..types import Instance, OrderState, OrderType, Side, TargetCurrency, Currency


class Order:
    """
    暂时仅支持：
        LIMIT
        MARKET
    """

    TYPE = OrderType.NULL

    def __init__(self,
                 create_time: datetime.datetime = None,
                 instance: Instance = Instance.NULL,
                 _id: str = "",
                 price: float = None,
                 side: Side = Side.NULL,
                 size: float = None,
                 state: OrderState = OrderState.NULL,
                 target_currency: Currency = Currency.NULL,
                 avg_price: float = None,
                 fee: float = None,
                 update_time: datetime.datetime = None):
        """
        @param create_time: 订单创建时间，Unix时间戳的毫秒数格式，如1597026383085
        @param instance: 产品ID
        @param _id: 订单ID
        @param price: 委托价格
        @param side: 订单方向
        @param size: 委托数量
        @param state: 订单状态
        @param target_currency:
            币币市价单委托数量sz的单位
            base_ccy: 交易货币；quote_ccy：计价货币
            仅适用于币币市价订单
            默认买单为quote_ccy，卖单为base_ccy
        @param avg_price: 成交均价，如果成交数量为0，该字段也为""
        @param fee:
            手续费与返佣
            对于币币和杠杆，为订单交易累计的手续费，平台向用户收取的交易手续费，为负数。如： -0.01
            对于交割、永续和期权，为订单交易累计的手续费和返佣
        @param update_time: 订单状态更新时间，Unix时间戳的毫秒数格式，如 1597026383085
        """
        self._create_time = create_time
        self._instance = instance
        self._id = _id
        self._price = price
        self._side = side
        self._size = size
        self._state = state
        self._target_currency = target_currency
        self.__size_unit = Currency.NULL
        self._avg_price = avg_price
        self._fee = fee
        self.__fee_currency = Currency.NULL
        self._update_time = update_time

    def __str__(self):
        if self._state is OrderState.FILLED:
            return f'<{self._str_base()}: {self._str_core()}, {self._repr_result()}>'
        else:
            return f'<{self._str_base()}: {self._str_core()}>'

    def __repr__(self):
        """
        暂不考虑另外两种：
        1. 已取消订单不会长期保存，会被自动清理
        2. 部分成交订单未达到最终状态，当作未成交处理
        """
        return (f"{self.__class__.__name__}("
                f"ID={self._id}, instance={self._instance.name}, createTime={self._create_time}, updateTime={self._update_time}, "
                f"side={self._side.name}, size={self._size}, unit={self.size_unit.name}, price={self._price}, "
                f"avgPrice={self._avg_price}, fee={self._fee}, feeCurrency={self.fee_currency.name}"
                f")")

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return self._id == other.id

    @classmethod
    def from_json(cls, data) -> 'Order':
        order = cls()
        order._create_time = datetime.datetime.fromtimestamp(int(data['cTime']) * 0.001)
        order._instance = Instance[data['instId'].replace('-', '_')]
        order._id = data['ordId']
        order._side = Side[data['side'].upper()]
        order._size = float(data['sz'])
        order._state = OrderState[data['state'].upper()]
        if order._state is OrderState.FILLED:
            order._avg_price = float(data['avgPx'])
            order._fee = float(data['fee'].lstrip('-'))
            order._update_time = datetime.datetime.fromtimestamp(int(data['uTime']) * 0.001)
        return order

    @property
    def create_time(self) -> datetime.datetime:
        return self._create_time

    @property
    def instance(self) -> Instance:
        return self._instance

    @property
    def id(self) -> str:
        return self._id

    @property
    def price(self) -> float:
        return self._price

    @property
    def type(self) -> OrderType:
        return self.TYPE

    @property
    def side(self) -> Side:
        return self._side

    @property
    def size(self) -> float:
        return self._size

    @property
    def state(self) -> OrderState:
        return self._state

    @property
    def update_time(self) -> datetime.datetime:
        return self._update_time

    @property
    def fee(self) -> float:
        return self._fee

    @property
    def avg_price(self) -> float:
        return self._avg_price

    @property
    def size_unit(self) -> Currency:
        if not self.__size_unit:
            if self._target_currency is TargetCurrency.BASE_CCY:
                self.__size_unit = self._instance.base
            if self._target_currency is TargetCurrency.QUOTE_CCY:
                self.__size_unit = self._instance.quote
        return self.__size_unit

    @property
    def fee_currency(self) -> Currency:
        if not self.__fee_currency:
            if self._side is Side.BUY:
                self.__fee_currency = self._instance.base
            if self._side is Side.SELL:
                self.__fee_currency = self._instance.quote
        return self.__fee_currency

    def _str_sell(self, sell_quantity, sell_amount, delegate_price):
        return f'SELL {sell_quantity} {self._instance.base.name} for {sell_amount} {self._instance.quote.name} at {delegate_price}'

    def _str_buy(self, buy_quantity, buy_amount, delegate_price):
        return f'BUY {buy_quantity} {self._instance.base.name} with {buy_amount} {self._instance.quote.name} at {delegate_price}'

    def _str_base(self):
        return f'{self.__class__.__name__} for {self._instance.name}'

    def _str_core(self):
        pass

    def _repr_result(self):
        return f'filled at {self._avg_price}, paid {self._fee} {self.fee_currency.name} as fee'


class LimitOrder(Order):
    TYPE = OrderType.LIMIT

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._target_currency = TargetCurrency.BASE_CCY

    @classmethod
    def from_json(cls, data):
        order = super().from_json(data)
        order._price = float(data['px'])
        return order

    def _str_core(self):
        quantity = self._size
        amount = self._price * quantity

        if self._side is Side.BUY:
            return self._str_buy(quantity, amount, self._price)
        elif self._side is Side.SELL:
            return self._str_sell(quantity, amount, self._price)
        else:
            raise ValueError


class MarketOrder(Order):
    TYPE = OrderType.MARKET

    @classmethod
    def from_json(cls, data):
        order = super().from_json(data)
        if target_currency := data.get('tgtCcy'):
            order._target_currency = TargetCurrency[target_currency.upper()]
        else:
            # 默认买单为quote_ccy，卖单为base_ccy
            if order._side == Side.BUY:
                order._target_currency = TargetCurrency.QUOTE_CCY
            elif order._side == Side.SELL:
                order._target_currency = TargetCurrency.BASE_CCY
            else:
                raise ValueError
        return order

    def _str_core(self):
        if self._target_currency is TargetCurrency.BASE_CCY:
            quantity = self._size
            amount = 'some'
        elif self._target_currency is TargetCurrency.QUOTE_CCY:
            amount = self._size
            quantity = 'some'
        else:
            raise ValueError

        if self._side is Side.BUY:
            return self._str_buy(quantity, amount, 'market price')
        elif self._side is Side.SELL:
            return self._str_sell(quantity, amount, 'market price')
        else:
            raise ValueError


SUPPORTED_TYPES = {
    OrderType.LIMIT: LimitOrder,
    OrderType.MARKET: MarketOrder,
}


def to_order(data: dict) -> Order:
    return SUPPORTED_TYPES[OrderType[data['ordType'].upper()]].from_json(data)

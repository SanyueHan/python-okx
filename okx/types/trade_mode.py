from enum import Enum


class TradeMode(Enum):
    CASH = 'cash'          # 非保证金
    ISOLATED = 'isolated'  # 逐仓保证金模式
    CROSS = 'cross'        # 全仓保证金模式
    NULL = ''

    def __bool__(self):
        return bool(self.value)

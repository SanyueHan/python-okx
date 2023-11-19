from enum import Enum


class OrderState(Enum):
    CANCELED = 'canceled'                  # 撤单成功
    LIVE = 'live'                          # 等待成交
    PARTIALLY_FILLED = 'partially_filled'  # 部分成交
    FILLED = 'filled'                      # 完全成交
    NULL = ''

    def __bool__(self):
        return bool(self.value)

from enum import Enum


class OrderType(Enum):
    MARKET = 'market'                        # 市价单
    LIMIT = 'limit'                          # 限价单
    POST_ONLY = 'post_only'                  # 只做maker单
    FOK = 'fok'                              # 全部成交或立即取消
    IOC = 'ioc'                              # 立即成交并取消剩余
    OPTIMAL_LIMIT_IOC = 'optimal_limit_ioc'  # 市价委托立即成交并取消剩余（仅适用交割、永续）
    MMP = 'mmp'                              # 做市商保护(仅适用于组合保证金账户模式下的期权订单)
    MMP_AND_POST_ONLY = 'mmp_and_post_only'  # 做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)
    NULL = ''

    def __bool__(self):
        return bool(self.value)

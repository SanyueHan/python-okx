from enum import Enum


class InstanceType(Enum):
    SPOT = 'SPOT'        # 币币
    MARGIN = 'MARGIN'    # 币币杠杆
    SWAP = 'SWAP'        # 永续合约
    FUTURES = 'FUTURES'  # 交割合约
    OPTION = 'OPTION'    # 期权
    NULL = ''

    def __bool__(self):
        return bool(self.value)

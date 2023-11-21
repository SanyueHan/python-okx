from .client import Client
from .consts import *


class TradingDataAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    def get_support_coin(self):
        return self._request(GET, SUPPORT_COIN)

    def get_taker_volume(self, ccy, inst_type, begin='', end='', period=''):
        params = {'ccy': ccy, 'instType': inst_type, 'begin': begin, 'end': end, 'period': period}
        return self._request(GET, TAKER_VOLUME, params)

    def get_margin_lending_ratio(self, ccy, begin='', end='', period=''):
        params = {'ccy': ccy, 'begin': begin, 'end': end, 'period': period}
        return self._request(GET, MARGIN_LENDING_RATIO, params)

    def get_long_short_ratio(self, ccy, begin='', end='', period=''):
        params = {'ccy': ccy, 'begin': begin, 'end': end, 'period': period}
        return self._request(GET, LONG_SHORT_RATIO, params)

    def get_contracts_interest_volume(self, ccy, begin='', end='', period=''):
        params = {'ccy': ccy, 'begin': begin, 'end': end, 'period': period}
        return self._request(GET, CONTRACTS_INTEREST_VOLUME, params)

    def get_options_interest_volume(self, ccy, period=''):
        params = {'ccy': ccy, 'period': period}
        return self._request(GET, OPTIONS_INTEREST_VOLUME, params)

    def get_put_call_ratio(self, ccy, period=''):
        params = {'ccy': ccy, 'period': period}
        return self._request(GET, PUT_CALL_RATIO, params)

    def get_interest_volume_expiry(self, ccy, period=''):
        params = {'ccy': ccy, 'period': period}
        return self._request(GET, OPEN_INTEREST_VOLUME_EXPIRY, params)

    def get_interest_volume_strike(self, ccy, exp_time, period=''):
        params = {'ccy': ccy, 'expTime': exp_time, 'period': period}
        return self._request(GET, INTEREST_VOLUME_STRIKE, params)

    def get_taker_block_volume(self, ccy, period=''):
        params = {'ccy': ccy, 'period': period}
        return self._request(GET, TAKER_FLOW, params)

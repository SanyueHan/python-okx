from .client import Client
from .consts import *


class FDBrokerAPI(Client):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    def generate_rebate_details_download_link(self, begin='', end=''):
        params = {'begin': begin, 'end': end}
        return self._post(FD_REBATE_PER_ORDERS, params)

    def get_rebate_details_download_link(self, type_='', begin='', end=''):
        params = {'type': type_, 'begin': begin, 'end': end}
        return self._get(FD_GET_REBATE_PER_ORDERS, params)

from .client import Client
from .consts import *


class StatusAPI(Client):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    def status(self, state=''):
        params = {'state': state}
        return self._get(STATUS, params)

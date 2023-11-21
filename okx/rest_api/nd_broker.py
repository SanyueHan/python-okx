from .client import Client
from .consts import *


class NDBrokerAPI(Client):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    # GET /api/v5/broker/nd/info
    def get_broker_info(self):
        return self._request(GET, BROKER_INFO)

    # POST /api/v5/broker/nd/create-subaccount
    def create_subaccount(self, sub_acct='', label=''):
        params = {
            'subAcct': sub_acct,
            'label': label
        }
        return self._request(POST, CREATE_SUBACCOUNT, params)

    def delete_subaccount(self, sub_acct=''):
        params = {
            'subAcct': sub_acct
        }
        return self._request(POST, DELETE_SUBACCOUNT, params)

    def get_subaccount_info(self, sub_acct='', page='', limit=''):
        params = {
            'subAcct': sub_acct,
            'page': page,
            'limit': limit
        }
        return self._request(GET, SUBACCOUNT_INFO, params)

    def create_subaccount_apikey(self, sub_acct='', label='', passphrase='', ip='', perm=''):
        params = {
            'subAcct': sub_acct,
            'label': label,
            'passphrase': passphrase,
            'ip': ip,
            'perm': perm
        }
        return self._request(POST, ND_CREATE_APIKEY, params)

    def get_subaccount_apikey(self, sub_acct='', api_key=''):
        params = {
            'subAcct': sub_acct,
            'apiKey': api_key
        }
        return self._request(GET, ND_SELECT_APIKEY, params)

    def reset_subaccount_apikey(self, sub_acct='', api_key='', label='', perm='', ip=''):
        params = {
            'subAcct': sub_acct,
            'apiKey': api_key,
            'label': label,
            'perm': perm,
            'ip': ip
        }
        return self._request(POST, ND_MODIFY_APIKEY, params)

    def delete_subaccount_apikey(self, sub_acct='', api_key=''):
        params = {
            'subAcct': sub_acct,
            'apiKey': api_key
        }
        return self._request(POST, ND_DELETE_APIKEY, params)

    def set_subaccount_level(self, sub_acct='', acct_lv=''):
        params = {
            'subAcct': sub_acct,
            'acctLv': acct_lv
        }
        return self._request(POST, SET_SUBACCOUNT_LEVEL, params)

    def set_subaccount_fee_rate(self, sub_acct='', inst_type='', chg_type='', chg_taker='', chg_maker='', eff_date=''):
        params = {
            'subAcct': sub_acct,
            'instType': inst_type,
            'chgType': chg_type,
            'chgTaker': chg_taker,
            'chgMaker': chg_maker,
            'effDate': eff_date
        }
        return self._request(POST, SET_SUBACCOUNT_FEE_RATE, params)

    def create_subaccount_deposit_address(self, sub_acct='', ccy='', chain='', addr_type='', to=''):
        params = {
            'subAcct': sub_acct,
            'ccy': ccy,
            'chain': chain,
            'addrType': addr_type,
            'to': to
        }
        return self._request(POST, SUBACCOUNT_DEPOSIT_ADDRESS, params)

    def reset_subaccount_deposit_address(self, sub_acct='', ccy='', chain='', addr='', to=''):
        params = {
            'subAcct': sub_acct,
            'ccy': ccy,
            'chain': chain,
            'addr': addr,
            'to': to
        }
        return self._request(POST, MODIFY_SUBACCOUNT_DEPOSIT_ADDRESS, params)

    def get_subaccount_deposit_address(self, sub_acct='', ccy=''):
        params = {
            'subAcct': sub_acct,
            'ccy': ccy
        }
        return self._request(GET, GET_SUBACCOUNT_DEPOSIT, params)

    def get_subaccount_deposit_history(self, sub_acct='', ccy='', tx_id='', state='', after='', before='', limit=''):
        params = {
            'subAcct': sub_acct,
            'ccy': ccy,
            'txId': tx_id,
            'state': state,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, SUBACCOUNT_DEPOSIT_HISTORY, params)

    def get_rebate_daily(self, sub_acct='', begin='', end='', page='', limit=''):
        params = {
            'subAcct': sub_acct,
            'begin': begin,
            'end': end,
            'page': page,
            'limit': limit
        }
        return self._request(GET, REBATE_DAILY, params)

    def get_rebate_details_download_link(self, type_='', begin='', end=''):
        params = {
            'type': type_,
            'begin': begin,
            'end': end
        }
        return self._request(GET, GET_REBATE_PER_ORDERS, params)

    def generate_rebate_details_download_link(self, begin='', end=''):
        params = {
            'begin': begin,
            'end': end
        }
        return self._request(POST, REBATE_PER_ORDERS, params)

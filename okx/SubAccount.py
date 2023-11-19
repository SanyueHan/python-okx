from .client import Client
from .consts import *


class SubAccountAPI(Client):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    def get_account_balance(self, sub_acct):
        params = {"subAcct": sub_acct}
        return self._request_with_params(GET, BALANCE, params)

    def bills(self, ccy='', type_='', sub_acct='', after='', before='', limit=''):
        params = {"ccy": ccy, 'type': type_, 'subAcct': sub_acct, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, BILLs, params)

    def reset_subaccount_apikey(self, sub_acct, api_key, label='', perm='', ip='-1'):
        params = {'subAcct': sub_acct, 'apiKey': api_key}

        if ip != '-1':
            params['ip'] = ip
        if label != '':
            params['label'] = label
        if perm != '':
            params['perm'] = perm
        return self._request_with_params(POST, RESET, params)

    def get_subaccount_list(self, enable='', sub_acct='', after='', before='', limit=''):
        params = {'enable': enable, 'subAcct': sub_acct, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, VIEW_LIST, params)

    def sub_account_transfer(self, ccy, amt, from_, to, from_sub_account, to_sub_account, loan_trans='false', omit_pos_risk='false'):
        params = {'ccy': ccy, 'amt': amt, 'from': from_, 'to': to, 'fromSubAccount': from_sub_account, 'toSubAccount': to_sub_account, 'loanTrans': loan_trans,
                  'omitPosRisk': omit_pos_risk}
        return self._request_with_params(POST, SUBACCOUNT_TRANSFER, params)

    # GET /api/v5/users/entrust-subaccount-list
    def get_entrust_subaccount_list(self, sub_acct=''):
        params = {
            'subAcct': sub_acct
        }
        return self._request_with_params(GET, ENTRUST_SUBACCOUNT_LIST, params)

    # POST /api/v5/users/subaccount/set-transfer-out
    def set_permission_transfer_out(self, sub_acct='', can_trans_out=''):
        params = {
            'subAcct': sub_acct,
            'canTransOut': can_trans_out
        }
        return self._request_with_params(POST, SET_TRSNSFER_OUT, params)

    # GET /api/v5/asset/subaccount/balances
    def get_funding_balance(self, sub_acct='', ccy=''):
        params = {
            'subAcct': sub_acct,
            'ccy': ccy
        }
        return self._request_with_params(GET, GET_ASSET_SUBACCOUNT_BALANCE, params)

    # - Get the user's affiliate rebate information
    def get_the_user_affiliate_rebate_information(self, api_key=''):
        params = {
            'apiKey': api_key
        }
        return self._request_with_params(GET, GET_THE_USER_AFFILIATE_REBATE, params)

    # - Set sub_accounts VIP loan%
    def set_sub_accounts_vip_loan(self, enable='', alloc=None):
        params = {
            'enable': enable,
            'alloc': alloc
        }
        return self._request_with_params(POST, SET_SUB_ACCOUNTS_VIP_LOAN, params)

    # - Get sub_account borrow interest and limit
    def get_sub_account_borrow_interest_and_limit(self, sub_acct='', ccy=''):
        params = {
            'subAcct': sub_acct,
            'ccy': ccy
        }
        return self._request_with_params(GET, GET_SUB_ACCOUNT_BORROW_INTEREST_AND_LIMIT, params)

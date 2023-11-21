from .client import Client
from .consts import *


class FundingAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    # Get Deposit Address
    def get_deposit_address(self, ccy):
        params = {'ccy': ccy}
        return self._request(GET, DEPOSIT_ADDRESS, params)

    # Get Transfer State
    def transfer_state(self, trans_id, type_=''):
        params = {'transId': trans_id, 'type': type_}
        return self._request(GET, TRANSFER_STATE, params)

    # Get Balance
    def get_balances(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, GET_BALANCES, params)

    # Get Account Configuration
    def funds_transfer(self, ccy, amt, from_, to, type_='0', sub_acct='', inst_id='', to_inst_id='', loan_trans=''):
        params = {'ccy': ccy, 'amt': amt, 'from': from_, 'to': to, 'type': type_, 'subAcct': sub_acct, 'instId': inst_id,
                  'toInstId': to_inst_id, 'loanTrans': loan_trans}
        return self._request(POST, FUNDS_TRANSFER, params)

    # Withdrawal
    def withdrawal(self, ccy, amt, dest, to_addr, fee, chain='', area_code='', client_id=''):
        params = {'ccy': ccy, 'amt': amt, 'dest': dest, 'toAddr': to_addr, 'fee': fee, 'chain': chain,
                  'areaCode': area_code, 'clientId': client_id}
        return self._request(POST, WITHDRAWAL_COIN, params)

    # Get Deposit History
    def get_deposit_history(self, ccy='', state='', after='', before='', limit='', tx_id='', dep_id='', from_wd_id=''):
        params = {'ccy': ccy, 'state': state, 'after': after, 'before': before, 'limit': limit, 'txId': tx_id,
                  'depId': dep_id, 'fromWdId': from_wd_id}
        return self._request(GET, DEPOSIT_HISTORY, params)

    # Get Currencies
    def get_currencies(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, CURRENCY_INFO, params)

    # PiggyBank Purchase/Redemption
    def purchase_redempt(self, ccy, amt, side, rate):
        params = {'ccy': ccy, 'amt': amt, 'side': side, 'rate': rate}
        return self._request(POST, PURCHASE_REDEMPT, params)

    # Get Withdrawal History
    def get_bills(self, ccy='', type_='', after='', before='', limit=''):
        params = {'ccy': ccy, 'type': type_, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, BILLS_INFO, params)

    # Get Deposit Lightning
    def get_deposit_lightning(self, ccy, amt, to=""):
        params = {'ccy': ccy, 'amt': amt}
        if to:
            params = {'to': to}
        return self._request(GET, DEPOSIT_LIGHTNING, params)

    # Withdrawal Lightning
    def withdrawal_lightning(self, ccy, invoice, memo=''):
        params = {'ccy': ccy, 'invoice': invoice, 'memo': memo}
        return self._request(POST, WITHDRAWAL_LIGHTNING, params)

    # POST SET LENDING RATE
    def set_lending_rate(self, ccy, rate):
        params = {'ccy': ccy, 'rate': rate}
        return self._request(POST, SET_LENDING_RATE, params)

    # GET LENDING HISTORY
    def get_lending_history(self, ccy='', before='', after='', limit=''):
        params = {'ccy': ccy, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, LENDING_HISTORY, params)

    # GET LENDING RATE HISTORY
    def get_lending_rate_history(self, ccy='', after='', before='', limit=''):
        params = {'ccy': ccy, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, LENDING_RATE_HISTORY, params)

    # GET LENDING RATE SUMMARY
    def get_lending_rate_summary(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, LENDING_RATE_SUMMARY, params)

    # POST /api/v5/asset/cancel-withdrawal
    def cancel_withdrawal(self, wd_id=''):
        params = {
            'wdId': wd_id
        }
        return self._request(POST, CANCEL_WITHDRAWAL, params)

    # POST /api/v5/asset/convert-dust-assets
    def convert_dust_assets(self, ccy=None):
        params = {
            'ccy': ccy
        }
        return self._request(POST, CONVERT_DUST_ASSETS, params)

    # GET /api/v5/asset/asset-valuation
    def get_asset_valuation(self, ccy=''):
        params = {
            'ccy': ccy
        }
        return self._request(GET, ASSET_VALUATION, params)

    # GET / api / v5 / asset / saving - balance
    def get_saving_balance(self, ccy=''):
        params = {
            'ccy': ccy
        }
        return self._request(GET, GET_SAVING_BALANCE, params)

    # Get non-tradable assets
    def get_non_tradable_assets(self, ccy=''):
        params = {
            'ccy': ccy
        }
        return self._request(GET, GET_NON_TRADABLE_ASSETS, params)

    # Get deposit withdraw status
    def get_deposit_withdraw_status(self, wd_id='', tx_id='', ccy='', to='', chain=''):
        params = {'wdId': wd_id, 'txId': tx_id, 'ccy': ccy, 'to': to, 'chain': chain}
        return self._request(GET, GET_DEPOSIT_WITHDrAW_STATUS, params)

    # Get withdrawal history
    def get_withdrawal_history(self, ccy='', wd_id='', client_id='', tx_id='', type_='', state='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'wdId': wd_id,
            'clientId': client_id,
            'txId': tx_id,
            'type': type_,
            'state': state,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, GET_WITHDRAWAL_HISTORY, params)

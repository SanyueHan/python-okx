from .client import Client
from .consts import *


class AccountAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    # Get Positions
    def get_position_risk(self, inst_type=''):
        params = {}
        if inst_type:
            params['instType'] = inst_type
        return self._request(GET, POSITION_RISK, params)

    # Get Balance
    def get_account_balance(self, ccy=''):
        params = {}
        if ccy:
            params['ccy'] = ccy
        return self._request(GET, ACCOUNT_INFO, params)

    # Get Positions
    def get_positions(self, inst_type='', inst_id=''):
        params = {'instType': inst_type, 'instId': inst_id}
        return self._request(GET, POSITION_INFO, params)

    # Get Bills Details (recent 7 days)
    def get_account_bills(self, inst_type='', ccy='', mgn_mode='', ct_type='', type_='', sub_type='', after='', before='', limit=''):
        params = {'instType': inst_type, 'ccy': ccy, 'mgnMode': mgn_mode, 'ctType': ct_type, 'type': type_,
                  'subType': sub_type, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, BILLS_DETAIL, params)

    # Get Bills Details (recent 3 months)
    def get_account_bills_archive(self, inst_type='', ccy='', mgn_mode='', ct_type='', type_='', sub_type='', after='', before='', limit=''):
        params = {'instType': inst_type, 'ccy': ccy, 'mgnMode': mgn_mode, 'ctType': ct_type, 'type': type_,
                  'subType': sub_type, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, BILLS_ARCHIVE, params)

    # Get Account Configuration
    def get_account_config(self):
        return self._request(GET, ACCOUNT_CONFIG)

    # Get Account Configuration
    def set_position_mode(self, pos_mode):
        params = {'posMode': pos_mode}
        return self._request(POST, POSITION_MODE, params)

    # Get Account Configuration
    def set_leverage(self, lever, mgn_mode, inst_id='', ccy='', pos_side=''):
        params = {'lever': lever, 'mgnMode': mgn_mode, 'instId': inst_id, 'ccy': ccy, 'posSide': pos_side}
        return self._request(POST, SET_LEVERAGE, params)

    # Get Maximum Tradable Size For Instrument
    def get_max_order_size(self, inst_id, td_mode, ccy='', px=''):
        params = {'instId': inst_id, 'tdMode': td_mode, 'ccy': ccy, 'px': px}
        return self._request(GET, MAX_TRADE_SIZE, params)

    # Get Maximum Available Tradable Amount
    def get_max_avail_size(self, inst_id, td_mode, ccy='', reduce_only='', un_spot_offset='', quick_mgn_type=''):
        params = {'instId': inst_id, 'tdMode': td_mode, 'ccy': ccy, 'reduceOnly': reduce_only,
                  'unSpotOffset': un_spot_offset, 'quickMgnType': quick_mgn_type}
        return self._request(GET, MAX_AVAIL_SIZE, params)

    # Increase / Decrease margin
    def adjustment_margin(self, inst_id, pos_side, type_, amt, loan_trans=''):
        params = {'instId': inst_id, 'posSide': pos_side, 'type': type_, 'amt': amt, 'loanTrans': loan_trans}
        return self._request(POST, ADJUSTMENT_MARGIN, params)

    # Get Leverage
    def get_leverage(self, inst_id, mgn_mode):
        params = {'instId': inst_id, 'mgnMode': mgn_mode}
        return self._request(GET, GET_LEVERAGE, params)

    # Get the maximum loan of isolated MARGIN
    def get_max_loan(self, inst_id, mgn_mode, mgn_ccy):
        params = {'instId': inst_id, 'mgnMode': mgn_mode, 'mgnCcy': mgn_ccy}
        return self._request(GET, MAX_LOAN, params)

    # Get Fee Rates
    def get_fee_rates(self, inst_type, inst_id='', uly='', category='', inst_family=''):
        params = {'instType': inst_type, 'instId': inst_id, 'uly': uly, 'category': category, 'instFamily': inst_family}
        return self._request(GET, FEE_RATES, params)

    # Get interest-accrued
    def get_interest_accrued(self, inst_id='', ccy='', mgn_mode='', after='', before='', limit=''):
        params = {'instId': inst_id, 'ccy': ccy, 'mgnMode': mgn_mode, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, INTEREST_ACCRUED, params)

    # Get interest-accrued
    def get_interest_rate(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, INTEREST_RATE, params)

    # Set Greeks (PA/BS)
    def set_greeks(self, greeks_type):
        params = {'greeksType': greeks_type}
        return self._request(POST, SET_GREEKS, params)

    # Set Isolated Mode
    def set_isolated_mode(self, iso_mode, type_):
        params = {'isoMode': iso_mode, 'type': type_}
        return self._request(POST, ISOLATED_MODE, params)

    # Get Maximum Withdrawals
    def get_max_withdrawal(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, MAX_WITHDRAWAL, params)

    # Get borrow repay
    def borrow_repay(self, ccy='', side='', amt='', ord_id=''):
        params = {'ccy': ccy, 'side': side, 'amt': amt, 'ordId': ord_id}
        return self._request(POST, BORROW_REPAY, params)

    # Get borrow repay history
    def get_borrow_repay_history(self, ccy='', after='', before='', limit=''):
        params = {'ccy': ccy, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, BORROW_REPAY_HISTORY, params)

    # Get Obtain borrowing rate and limit
    def get_interest_limits(self, type_='', ccy=''):
        params = {'type': type_, 'ccy': ccy}
        return self._request(GET, INTEREST_LIMITS, params)

    # Get Simulated Margin
    def get_simulated_margin(self, inst_type='', incl_real_pos=True, spot_offset_type='', sim_pos=None):
        params = {'instType': inst_type, 'inclRealPos': incl_real_pos, 'spotOffsetType': spot_offset_type, 'simPos': sim_pos}
        return self._request(POST, SIMULATED_MARGIN, params)

    # Get  Greeks
    def get_greeks(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, GREEKS, params)

    # GET /api/v5/account/risk-state
    def get_account_position_risk(self):
        return self._request(GET, ACCOUNT_RISK)

    # GET /api/v5/account/positions-history
    def get_positions_history(self, inst_type='', inst_id='', mgn_mode='', type_='', pos_id='', after='', before='', limit=''):
        params = {
            'instType': inst_type,
            'instId': inst_id,
            'mgnMode': mgn_mode,
            'type': type_,
            'posId': pos_id,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, POSITIONS_HISTORY, params)

    # GET /api/v5/account/position-tiers
    def get_account_position_tiers(self, inst_type='', uly='', inst_family=''):
        params = {
            'instType': inst_type,
            'uly': uly,
            'instFamily': inst_family
        }
        return self._request(GET, GET_PM_LIMIT, params)

    # - Get VIP interest accrued data
    def get_vip_interest_accrued_data(self, ccy='', ord_id='', after='', before='', limit=''):
        params = {'ccy': ccy, 'ordId': ord_id, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, GET_VIP_INTEREST_ACCRUED_DATA, params)

    # - Get VIP interest deducted data
    def get_vip_interest_deducted_data(self, ccy='', ord_id='', after='', before='', limit=''):
        params = {'ccy': ccy, 'ordId': ord_id, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, GET_VIP_INTEREST_DEDUCTED_DATA, params)

    # - Get VIP loan order list
    def get_vip_loan_order_list(self, ord_id='', state='', ccy='', after='', before='', limit=''):
        params = {'ordId': ord_id, 'state': state, 'ccy': ccy, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, GET_VIP_LOAN_ORDER_LIST, params)

    # - Get VIP loan order detail
    def get_vip_loan_order_detail(self, ccy='', ord_id='', after='', before='', limit=''):
        params = {'ccy': ccy, 'ordId': ord_id, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, GET_VIP_LOAN_ORDER_DETAIL, params)

    # - Set risk offset type
    def set_risk_offset_type(self, type_=''):
        params = {'type': type_}
        return self._request(POST, SET_RISK_OFFSET_TYPE, params)

    # - Set auto loan
    def set_auto_loan(self, auto_loan=''):
        params = {
            'autoLoan': auto_loan
        }
        return self._request(POST, SET_AUTO_LOAN, params)

    # - Activate option
    def activate_option(self):
        return self._request(POST, ACTIVATE_OPTION)

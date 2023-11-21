from .client import Client
from .consts import *


class PublicAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    # Get Instruments
    def get_instruments(self, inst_type, uly='', inst_id='', inst_family=''):
        params = {'instType': inst_type, 'uly': uly, 'instId': inst_id, 'instFamily': inst_family}
        return self._request(GET, INSTRUMENT_INFO, params)

    # Get Delivery/Exercise History
    def get_delivery_exercise_history(self, inst_type, uly='', after='', before='', limit='', inst_family=''):
        params = {'instType': inst_type, 'uly': uly, 'after': after, 'before': before, 'limit': limit, 'instFamily': inst_family}
        return self._request(GET, DELIVERY_EXERCISE, params)

    # Get Open Interest
    def get_open_interest(self, inst_type, uly='', inst_id='', inst_family=''):
        params = {'instType': inst_type, 'uly': uly, 'instId': inst_id, 'instFamily': inst_family}
        return self._request(GET, OPEN_INTEREST, params)

    # Get Funding Rate
    def get_funding_rate(self, inst_id):
        params = {'instId': inst_id}
        return self._request(GET, FUNDING_RATE, params)

    # Get Funding Rate History
    def funding_rate_history(self, inst_id, after='', before='', limit=''):
        params = {'instId': inst_id, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, FUNDING_RATE_HISTORY, params)

    # Get Limit Price
    def get_price_limit(self, inst_id):
        params = {'instId': inst_id}
        return self._request(GET, PRICE_LIMIT, params)

    # Get Option Market Data
    def get_opt_summary(self, uly='', exp_time='', inst_family=''):
        params = {'uly': uly, 'expTime': exp_time, 'instFamily': inst_family}
        return self._request(GET, OPT_SUMMARY, params)

    # Get Estimated Delivery/Excercise Price
    def get_estimated_price(self, inst_id):
        params = {'instId': inst_id}
        return self._request(GET, ESTIMATED_PRICE, params)

    # Get Discount Rate And Interest-Free Quota
    def discount_interest_free_quota(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, DISCOUNT_INTEREST_INFO, params)

    # Get System Time
    def get_system_time(self):
        return self._request(GET, SYSTEM_TIME)

    # Get Mark Price
    def get_mark_price(self, inst_type, uly='', inst_id='', inst_family=''):
        params = {'instType': inst_type, 'uly': uly, 'instId': inst_id, 'instFamily': inst_family}
        return self._request(GET, MARK_PRICE, params)

    # Get Tier
    def get_position_tiers(self, inst_type, td_mode, uly='', inst_id='', ccy='', tier='', inst_family=''):
        params = {'instType': inst_type, 'tdMode': td_mode, 'uly': uly, 'instId': inst_id, 'ccy': ccy, 'tier': tier, 'instFamily': inst_family}
        return self._request(GET, TIER, params)

    # GET /api/v5/public/interest-rate-loan-quota
    def get_interest_rate_loan_quota(self):
        return self._request(GET, INTEREST_LOAN)

    # GET /api/v5/public/vip-interest-rate-loan-quota
    def get_vip_interest_rate_loan_quota(self):
        return self._request(GET, VIP_INTEREST_RATE_LOAN_QUOTA)

    # GET /api/v5/public/underlying
    def get_underlying(self, inst_type=''):
        params = {
            'instType': inst_type
        }
        return self._request(GET, UNDERLYING, params)

    # GET /api/v5/public/insurance-fund
    def get_insurance_fund(self, inst_type='', type_='', uly='', ccy='', before='', after='', limit='', inst_family=''):
        params = {
            'instType': inst_type,
            'type': type_,
            'uly': uly,
            'ccy': ccy,
            'before': before,
            'after': after,
            'limit': limit,
            'instFamily': inst_family
        }
        return self._request(GET, INSURANCE_FUND, params)

    # GET /api/v5/public/convert-contract-coin
    def get_convert_contract_coin(self, type_='', inst_id='', sz='', px='', unit=''):
        params = {
            'type': type_,
            'instId': inst_id,
            'sz': sz,
            'px': px,
            'unit': unit
        }
        return self._request(GET, CONVERT_CONTRACT_COIN, params)

    # Get option tickBands
    def get_option_tick_bands(self, inst_type='', inst_family=''):
        params = {
            'instType': inst_type,
            'instFamily': inst_family
        }
        return self._request(GET, GET_OPTION_TICKBANDS, params)

    # Get option trades
    def get_option_trades(self, inst_id='', inst_family='', opt_type=''):
        params = {
            'instId': inst_id,
            'instFamily': inst_family,
            'optType': opt_type
        }
        return self._request(GET, GET_OPTION_TRADES, params)

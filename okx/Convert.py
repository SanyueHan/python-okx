from .client import Client
from .consts import *


class ConvertAPI(Client):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com', debug=True):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    def get_currencies(self):
        params = {}
        return self._request_with_params(GET, GET_CURRENCIES, params)

    def get_currency_pair(self, from_ccy='', to_ccy=''):
        params = {"fromCcy": from_ccy, 'toCcy': to_ccy}
        return self._request_with_params(GET, GET_CURRENCY_PAIR, params)

    def estimate_quote(self, base_ccy='', quote_ccy='', side='', rfq_sz='', rfq_sz_ccy='', cl_q_req_id='', tag=''):
        params = {'baseCcy': base_ccy, 'quoteCcy': quote_ccy, 'side': side, 'rfqSz': rfq_sz, 'rfqSzCcy': rfq_sz_ccy, 'clQReqId': cl_q_req_id, 'tag': tag}
        return self._request_with_params(POST, ESTIMATE_QUOTE, params)

    def convert_trade(self, quote_id='', base_ccy='', quote_ccy='', side='', sz='', sz_ccy='', cl_t_req_id='', tag=''):
        params = {'quoteId': quote_id, 'baseCcy': base_ccy, 'quoteCcy': quote_ccy, 'side': side, 'sz': sz, 'szCcy': sz_ccy, 'clTReqId': cl_t_req_id, 'tag': tag}
        return self._request_with_params(POST, CONVERT_TRADE, params)

    def get_convert_history(self, after='', before='', limit='', tag=''):
        params = {'after': after, 'before': before, 'limit': limit, 'tag': tag}
        return self._request_with_params(GET, CONVERT_HISTORY, params)

from .client import Client
from .consts import *


class BlockTradingAPI(Client):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com', debug=True):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    def counterparties(self):
        params = {}
        return self._request_with_params(GET, COUNTERPARTIES, params)

    def create_rfq(self, counterparties=None, anonymous='false', cl_rfq_id='', tag='', allow_partial_execution='false', legs=None):
        params = {'counterparties': counterparties, 'anonymous': anonymous, 'clRfqId': cl_rfq_id, 'tag': tag,
                  'allowPartialExecution': allow_partial_execution, 'legs': legs}
        return self._request_with_params(POST, CREATE_RFQ, params)

    def cancel_rfq(self, rfq_id='', cl_rfq_id=''):
        params = {'rfqId': rfq_id, 'clRfqId': cl_rfq_id}
        return self._request_with_params(POST, CANCEL_RFQ, params)

    def cancel_batch_rfqs(self, rfq_ids=None, cl_rfq_ids=None):
        params = {'rfqIds': rfq_ids, 'clRfqIds': cl_rfq_ids}
        return self._request_with_params(POST, CANCEL_BATCH_RFQS, params)

    def cancel_all_rfqs(self):
        params = {}
        return self._request_with_params(POST, CANCEL_ALL_RSQS, params)

    def execute_quote(self, rfq_id='', quote_id='', legs=None):
        params = {'rfqId': rfq_id, 'quoteId': quote_id, 'legs': legs}
        return self._request_with_params(POST, EXECUTE_QUOTE, params)

    def create_quote(self, rfq_id='', cl_quote_id='', tag='', quote_side='', legs=None, anonymous=False, expires_in=''):
        params = {'rfqId': rfq_id, 'clQuoteId': cl_quote_id, 'tag': tag, 'quoteSide': quote_side, 'legs': legs,
                  'anonymous': anonymous, 'expiresIn': expires_in}
        return self._request_with_params(POST, CREATE_QUOTE, params)

    def cancel_quote(self, quote_id='', cl_quote_id=''):
        params = {'quoteId': quote_id, 'clQuoteId': cl_quote_id}
        return self._request_with_params(POST, CANCEL_QUOTE, params)

    def cancel_batch_quotes(self, quote_ids='', cl_quote_ids=''):
        params = {'quoteIds': quote_ids, 'clQuoteIds': cl_quote_ids}
        return self._request_with_params(POST, CANCEL_BATCH_QUOTES, params)

    def cancel_all_quotes(self):
        params = {}
        return self._request_with_params(POST, CANCEL_ALL_QUOTES, params)

    def get_rfqs(self, rfq_id='', cl_rfq_id='', state='', begin_id='', end_id='', limit=''):
        params = {'rfqId': rfq_id, 'clRfqId': cl_rfq_id, 'state': state, 'beginId': begin_id, 'endId': end_id, 'limit': limit}
        return self._request_with_params(GET, GET_RFQS, params)

    def get_quotes(self, rfq_id='', cl_rfq_id='', quote_id='', cl_quote_id='', state='', begin_id='', end_id='', limit=''):
        params = {'rfqId': rfq_id, 'clRfqId': cl_rfq_id, 'quoteId': quote_id, 'clQuoteId': cl_quote_id, 'state': state, 'beginId': begin_id, 'endId': end_id,
                  'limit': limit}
        return self._request_with_params(GET, GET_QUOTES, params)

    def get_trades(self, rfq_id='', cl_rfq_id='', quote_id='', cl_quote_id='', state='', begin_id='', end_id='', begin_ts='',
                   end_ts='', limit=''):
        params = {'rfqId': rfq_id, 'clRfqId': cl_rfq_id, 'quoteId': quote_id, 'clQuoteId': cl_quote_id, 'state': state,
                  'beginId': begin_id, 'endId': end_id, 'beginTs': begin_ts, 'endTs': end_ts, 'limit': limit}
        return self._request_with_params(GET, GET_RFQ_TRADES, params)

    def get_public_trades(self, begin_id='', end_id='', limit=''):
        params = {'beginId': begin_id, 'endId': end_id, 'limit': limit}
        return self._request_with_params(GET, GET_PUBLIC_TRADES, params)

    def reset_mmp(self):
        return self._request_without_params(POST, MMP_RESET)

    def set_marker_instrument(self, params=None):
        return self._request_with_params(POST, MARKER_INSTRUMENT_SETTING, params)

    # Get Quote products
    def get_quote_products(self):
        return self._request_without_params(GET, MARKER_INSTRUMENT_SETTING)

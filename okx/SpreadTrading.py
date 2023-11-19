from .client import Client
from .consts import *


class SpreadTradingAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    # Place Order
    def place_order(self, sprd_id='', cl_ord_id='', tag='', side='', ord_type='', sz='', px=''):
        params = {'sprdId': sprd_id, 'clOrdId': cl_ord_id, 'tag': tag, 'side': side, 'ordType': ord_type, 'sz': sz,
                  'px': px}
        return self._request_with_params(POST, SPREAD_PLACE_ORDER, params)

    # Cancel Order
    def cancel_order(self, ord_id='', cl_ord_id=''):
        params = {'ordId': ord_id, 'clOrdId': cl_ord_id}
        return self._request_with_params(POST, SPREAD_CANAEL_ORDER, params)

    # Cancel All orders
    def cancel_all_orders(self, sprd_id=''):
        params = {'sprdId': sprd_id}
        return self._request_with_params(POST, SPREAD_CANAEL_ALL_ORDERS, params)

    # Get order details
    def get_order_details(self, ord_id='', cl_ord_id=''):
        params = {'ordId': ord_id, 'clOrdId': cl_ord_id}
        return self._request_with_params(GET, SPREAD_GET_ORDER_DETAILS, params)

    # Get active orders
    def get_active_orders(self, sprd_id='', ord_type='', state='', begin_id='', end_id='', limit=''):
        params = {'sprdId': sprd_id, 'ordType': ord_type, 'state': state, 'beginId': begin_id, 'endId': end_id, 'limit': limit}
        return self._request_with_params(GET, SPREAD_GET_ACTIVE_ORDERS, params)

    # Get orders (last 7 days)
    def get_orders(self, sprd_id='', ord_type='', state='', begin_id='', end_id='', begin='', end='', limit=''):
        params = {'sprdId': sprd_id, 'ordType': ord_type, 'state': state, 'beginId': begin_id, 'endId': end_id,
                  'begin': begin, 'end': end, 'limit': limit}
        return self._request_with_params(GET, SPREAD_GET_ORDERS, params)

    # Get trades (last 7 days)
    def get_trades(self, sprd_id='', trade_id='', ord_id='', begin_id='', end_id='', begin='', end='', limit=''):
        params = {'sprdId': sprd_id, 'tradeId': trade_id, 'ordId': ord_id, 'beginId': begin_id, 'endId': end_id,
                  'begin': begin, 'end': end, 'limit': limit}
        return self._request_with_params(GET, SPREAD_GET_TRADES, params)

    # Get Spreads (Public)
    def get_spreads(self, base_ccy='', inst_id='', sprd_id='', state=''):
        params = {'baseCcy': base_ccy, 'instId': inst_id, 'sprdId': sprd_id, 'state': state}
        return self._request_with_params(GET, SPREAD_GET_SPREADS, params)

    # Get order book (Public)
    def get_order_book(self, sprd_id='', sz=''):
        params = {'sprdId': sprd_id, 'sz': sz}
        return self._request_with_params(GET, SPREAD_GET_ORDER_BOOK, params)

    # Get ticker (Public)
    def get_ticker(self, sprd_id=''):
        params = {'sprdId': sprd_id}
        return self._request_with_params(GET, SPREAD_GET_TICKER, params)

    # Get public trades (Public)
    def get_public_trades(self, sprd_id=''):
        params = {'sprdId': sprd_id}
        return self._request_with_params(GET, SPREAD_GET_PUBLIC_TRADES, params)

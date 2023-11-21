from .client import Client
from .consts import *


class MarketAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    # Get Tickers
    def get_tickers(self, inst_type, uly='', inst_family=''):
        if uly:
            params = {'instType': inst_type, 'uly': uly, 'instFamily': inst_family}
        else:
            params = {'instType': inst_type, 'instFamily': inst_family}
        return self._request(GET, TICKERS_INFO, params)

    # Get Ticker
    def get_ticker(self, inst_id):
        params = {'instId': inst_id}
        return self._request(GET, TICKER_INFO, params)

    # Get Index Tickers
    def get_index_tickers(self, quote_ccy='', inst_id=''):
        params = {'quoteCcy': quote_ccy, 'instId': inst_id}
        return self._request(GET, INDEX_TICKERS, params)

    # Get Order Book
    def get_orderbook(self, inst_id, sz=''):
        params = {'instId': inst_id, 'sz': sz}
        return self._request(GET, ORDER_BOOKS, params)

    # Get Candlesticks
    def get_candlesticks(self, inst_id, after='', before='', bar='', limit=''):
        params = {'instId': inst_id, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_CANDLES, params)

    # GGet Candlesticks History（top currencies only）
    def get_history_candlesticks(self, inst_id, after='', before='', bar='', limit=''):
        params = {'instId': inst_id, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, HISTORY_CANDLES, params)

    # Get Index Candlesticks
    def get_index_candlesticks(self, inst_id, after='', before='', bar='', limit=''):
        params = {'instId': inst_id, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, INDEX_CANDLES, params)

    # Get Mark Price Candlesticks
    def get_mark_price_candlesticks(self, inst_id, after='', before='', bar='', limit=''):
        params = {'instId': inst_id, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARK_PRICE_CANDLES, params)

    # Get Index Candlesticks
    def get_trades(self, inst_id, limit=''):
        params = {'instId': inst_id, 'limit': limit}
        return self._request(GET, MARKET_TRADES, params)

    # Get Volume
    def get_volume(self):
        return self._request(GET, VOLUME)

    # Get Oracle
    def get_oracle(self):
        return self._request(GET, ORACLE)

    # Get Tier
    def get_tier(self, inst_type='', td_mode='', uly='', inst_id='', ccy='', tier=''):
        params = {'instType': inst_type, 'tdMode': td_mode, 'uly': uly, 'instId': inst_id, 'ccy': ccy, 'tier': tier}
        return self._request(GET, TIER, params)

    # GET /api/v5/market/index-components
    def get_index_components(self, index=''):
        param = {
            'index': index
        }
        return self._request(GET, INDEX_COMPONENTS, param)

    # GET /api/v5/market/exchange-rate
    def get_exchange_rate(self):
        return self._request(GET, EXCHANGE_RATE)

    # GET /api/v5/market/history-trades
    def get_history_trades(self, inst_id='', type_='', after='', before='', limit=''):
        params = {
            'instId': inst_id,
            'type': type_,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, HISTORY_TRADES, params)

    # GET /api/v5/market/block-ticker
    def get_block_ticker(self, inst_id=''):
        params = {
            'instId': inst_id
        }
        return self._request(GET, BLOCK_TICKER, params)

    # GET /api/v5/market/block-tickers
    def get_block_tickers(self, inst_type='', uly='', inst_family=''):
        params = {
            'instType': inst_type,
            'uly': uly,
            'instFamily': inst_family
        }
        return self._request(GET, BLOCK_TICKERS, params)

    # GET /api/v5/market/block-trades
    def get_block_trades(self, inst_id=''):
        params = {
            'instId': inst_id
        }
        return self._request(GET, BLOCK_TRADES, params)

    # - Get order lite book
    def get_order_lite_book(self, inst_id=''):
        params = {
            'instId': inst_id
        }
        return self._request(GET, GET_ORDER_LITE_BOOK, params)

    # - Get option trades
    def get_option_trades(self, inst_family=''):
        params = {
            'instFamily': inst_family
        }
        return self._request(GET, GET_OPTION_TRADES, params)

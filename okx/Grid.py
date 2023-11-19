from .client import Client
from .consts import *


class GridAPI(Client):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    def grid_order_algo(self, inst_id='', algo_ord_type='', max_px='', min_px='', grid_num='', run_type='', tp_trigger_px='',
                        sl_trigger_px='', tag='', quote_sz='', base_sz='', sz='', direction='', lever='', base_pos=''):
        params = {'instId': inst_id, 'algoOrdType': algo_ord_type, 'maxPx': max_px, 'minPx': min_px, 'gridNum': grid_num,
                  'runType': run_type, 'tpTriggerPx': tp_trigger_px, 'slTriggerPx': sl_trigger_px, 'tag': tag,
                  'quoteSz': quote_sz, 'baseSz': base_sz, 'sz': sz, 'direction': direction, 'lever': lever,
                  'basePos': base_pos}
        return self._request_with_params(POST, GRID_ORDER_ALGO, params)

    def grid_amend_order_algo(self, algo_id='', inst_id='', sl_trigger_px='', tp_trigger_px=''):
        params = {'algoId': algo_id, 'instId': inst_id, 'slTriggerPx': sl_trigger_px, 'tpTriggerPx': tp_trigger_px}
        return self._request_with_params(POST, GRID_AMEND_ORDER_ALGO, params)

    def grid_stop_order_algo(self, algo_id='', inst_id='', algo_ord_type='', stop_type=''):
        params = [{'algoId': algo_id, 'instId': inst_id, 'algoOrdType': algo_ord_type, 'stopType': stop_type}]
        return self._request_with_params(POST, GRID_STOP_ORDER_ALGO, params)

    def grid_orders_algo_pending(self, algo_ord_type='', algo_id='', inst_id='', inst_type='', after='', before='',
                                 limit='', inst_family=''):
        params = {'algoOrdType': algo_ord_type, 'algoId': algo_id, 'instId': inst_id, 'instType': inst_type, 'after': after,
                  'before': before, 'limit': limit, 'instFamily': inst_family}
        return self._request_with_params(GET, GRID_ORDERS_ALGO_PENDING, params)

    def grid_orders_algo_history(self, algo_ord_type='', algo_id='', inst_id='', inst_type='', after='', before='',
                                 limit='', inst_family=''):
        params = {'algoOrdType': algo_ord_type, 'algoId': algo_id, 'instId': inst_id, 'instType': inst_type, 'after': after,
                  'before': before, 'limit': limit, 'instFamily': inst_family}
        return self._request_with_params(GET, GRID_ORDERS_ALGO_HISTORY, params)

    def grid_orders_algo_details(self, algo_ord_type='', algo_id=''):
        params = {'algoOrdType': algo_ord_type, 'algoId': algo_id}
        return self._request_with_params(GET, GRID_ORDERS_ALGO_DETAILS, params)

    def grid_sub_orders(self, algo_id='', algo_ord_type='', type_='', group_id='', after='', before='', limit=''):
        params = {'algoId': algo_id, 'algoOrdType': algo_ord_type, 'type': type_, 'groupId': group_id, 'after': after,
                  'before': before, 'limit': limit}
        return self._request_with_params(GET, GRID_SUB_ORDERS, params)

    def grid_positions(self, algo_ord_type='', algo_id=''):
        params = {'algoOrdType': algo_ord_type, 'algoId': algo_id}
        return self._request_with_params(GET, GRID_POSITIONS, params)

    def grid_withdraw_income(self, algo_id=''):
        params = {'algoId': algo_id}
        return self._request_with_params(POST, GRID_WITHDRAW_INCOME, params)

    def grid_compute_margin_balance(self, algo_id='', type_='', amt=''):
        params = {
            'algoId': algo_id,
            'type': type_,
            'amt': amt
        }
        return self._request_with_params(POST, GRID_COMPUTE_MARIGIN_BALANCE, params)

    def grid_adjust_margin_balance(self, algo_id='', type_='', amt='', percent=''):
        params = {
            'algoId': algo_id,
            'type': type_,
            'amt': amt,
            'percent': percent
        }
        return self._request_with_params(POST, GRID_MARGIN_BALANCE, params)

    def grid_ai_param(self, algo_ord_type='', inst_id='', direction='', duration=''):
        params = {
            'algoOrdType': algo_ord_type,
            'instId': inst_id,
            'direction': direction,
            'duration': duration
        }
        return self._request_with_params(GET, GRID_AI_PARAM, params)

    # - Place recurring buy order
    def place_recurring_buy_order(self, stgy_name='', recurring_list=None, period='', recurring_day='', recurring_time='',
                                  time_zone='', amt='', investment_ccy='', td_mode='', algo_cl_ord_id='', tag=''):
        params = {'stgyName': stgy_name, 'recurringList': recurring_list, 'period': period, 'recurringDay': recurring_day,
                  'recurringTime': recurring_time,
                  'timeZone': time_zone, 'amt': amt, 'investmentCcy': investment_ccy, 'tdMode': td_mode,
                  'algoClOrdId': algo_cl_ord_id, 'tag': tag}
        return self._request_with_params(POST, PLACE_RECURRING_BUY_ORDER, params)

    # - Amend recurring buy order
    def amend_recurring_buy_order(self, algo_id='', stgy_name=''):
        params = {'algoId': algo_id, 'stgyName': stgy_name}
        return self._request_with_params(POST, AMEND_RECURRING_BUY_ORDER, params)

    # - Stop recurring buy order
    def stop_recurring_buy_order(self, orders_data):
        return self._request_with_params(POST, STOP_RECURRING_BUY_ORDER, orders_data)

    # - Get recurring buy order list
    def get_recurring_buy_order_list(self, algo_id='', after='', before='', limit=''):
        params = {
            'algoId': algo_id,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request_with_params(GET, GET_RECURRING_BUY_ORDER_LIST, params)

    # - Get recurring buy order history
    def get_recurring_buy_order_history(self, algo_id='', after='', before='', limit=''):
        params = {
            'algoId': algo_id,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request_with_params(GET, GET_RECURRING_BUY_ORDER_HISTORY, params)

    # - Get recurring buy order details
    def get_recurring_buy_order_details(self, algo_id=''):
        params = {'algoId': algo_id}
        return self._request_with_params(GET, GET_RECURRING_BUY_ORDER_DETAILS, params)

    # - Get recurring buy sub orders
    def get_recurring_buy_sub_orders(self, algo_id='', ord_id='', after='', before='', limit=''):
        params = {
            'algoId': algo_id,
            'ordId': ord_id,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request_with_params(GET, GET_RECURRING_BUY_SUB_ORDERS, params)

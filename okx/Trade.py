from .client import Client
from .consts import *


class TradeAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    # Place Order
    def place_order(self, inst_id, td_mode, side, ord_type, sz, ccy='', cl_ord_id='', tag='', pos_side='', px='',
                    reduce_only='', tgt_ccy='', tp_trigger_px='', tp_ord_px='', sl_trigger_px='', sl_ord_px='',
                    tp_trigger_px_type='', sl_trigger_px_type='', quick_mgn_type='', stp_id='', stp_mode=''):
        params = {'instId': inst_id, 'tdMode': td_mode, 'side': side, 'ordType': ord_type, 'sz': sz, 'ccy': ccy,
                  'clOrdId': cl_ord_id, 'tag': tag, 'posSide': pos_side, 'px': px, 'reduceOnly': reduce_only,
                  'tgtCcy': tgt_ccy, 'tpTriggerPx': tp_trigger_px, 'tpOrdPx': tp_ord_px, 'slTriggerPx': sl_trigger_px,
                  'slOrdPx': sl_ord_px, 'tpTriggerPxType': tp_trigger_px_type, 'slTriggerPxType': sl_trigger_px_type,
                  'quickMgnType': quick_mgn_type, 'stpId': stp_id, 'stpMode': stp_mode}
        return self._request_with_params(POST, PLACR_ORDER, params)

    # Place Multiple Orders
    def place_multiple_orders(self, orders_data):
        return self._request_with_params(POST, BATCH_ORDERS, orders_data)

    # Cancel Order
    def cancel_order(self, inst_id, ord_id='', cl_ord_id=''):
        params = {'instId': inst_id, 'ordId': ord_id, 'clOrdId': cl_ord_id}
        return self._request_with_params(POST, CANAEL_ORDER, params)

    # Cancel Multiple Orders
    def cancel_multiple_orders(self, orders_data):
        return self._request_with_params(POST, CANAEL_BATCH_ORDERS, orders_data)

    # Amend Order
    def amend_order(self, inst_id, cxl_on_fail='', ord_id='', cl_ord_id='', req_id='', new_sz='', new_px='', new_tp_trigger_px='',
                    new_tp_ord_px='', new_sl_trigger_px='', new_sl_ord_px='', new_tp_trigger_px_type='', new_sl_trigger_px_type=''):
        params = {'instId': inst_id, 'cxlOnFail': cxl_on_fail, 'ordId': ord_id, 'clOrdId': cl_ord_id, 'reqId': req_id,
                  'newSz': new_sz, 'newPx': new_px, 'newTpTriggerPx': new_tp_trigger_px, 'newTpOrdPx': new_tp_ord_px,
                  'newSlTriggerPx': new_sl_trigger_px, 'newSlOrdPx': new_sl_ord_px, 'newTpTriggerPxType': new_tp_trigger_px_type,
                  'newSlTriggerPxType': new_sl_trigger_px_type}
        return self._request_with_params(POST, AMEND_ORDER, params)

    # Amend Multiple Orders
    def amend_multiple_orders(self, orders_data):
        return self._request_with_params(POST, AMEND_BATCH_ORDER, orders_data)

    # Close Positions
    def close_positions(self, inst_id, mgn_mode, pos_side='', ccy='', auto_cxl='', cl_ord_id='', tag=''):
        params = {'instId': inst_id, 'mgnMode': mgn_mode, 'posSide': pos_side, 'ccy': ccy, 'autoCxl': auto_cxl,
                  'clOrdId': cl_ord_id, 'tag': tag}
        return self._request_with_params(POST, CLOSE_POSITION, params)

    # Get Order Details
    def get_order(self, inst_id, ord_id='', cl_ord_id=''):
        params = {'instId': inst_id, 'ordId': ord_id, 'clOrdId': cl_ord_id}
        return self._request_with_params(GET, ORDER_INFO, params)

    # Get Order List
    def get_order_list(self, inst_type='', uly='', inst_id='', ord_type='', state='', after='', before='', limit='', inst_family=''):
        params = {'instType': inst_type, 'uly': uly, 'instId': inst_id, 'ordType': ord_type, 'state': state,
                  'after': after, 'before': before, 'limit': limit, 'instFamily': inst_family}
        return self._request_with_params(GET, ORDERS_PENDING, params)

    # Get Order History (last 7 days）
    def get_orders_history(self, inst_type, uly='', inst_id='', ord_type='', state='', after='', before='', begin='',
                           end='', limit='', inst_family=''):
        params = {'instType': inst_type, 'uly': uly, 'instId': inst_id, 'ordType': ord_type, 'state': state,
                  'after': after, 'before': before, 'begin': begin, 'end': end, 'limit': limit,
                  'instFamily': inst_family}
        return self._request_with_params(GET, ORDERS_HISTORY, params)

    # Get Order History (last 3 months)
    def get_orders_history_archive(self, inst_type, uly='', inst_id='', ord_type='', state='', after='', before='',
                                   begin='', end='', limit='', inst_family=''):
        params = {'instType': inst_type, 'uly': uly, 'instId': inst_id, 'ordType': ord_type, 'state': state,
                  'after': after, 'before': before, 'begin': begin, 'end': end, 'limit': limit,
                  'instFamily': inst_family}
        return self._request_with_params(GET, ORDERS_HISTORY_ARCHIVE, params)

    # Get Transaction Details
    def get_fills(self, inst_type='', uly='', inst_id='', ord_id='', after='', before='', limit='', inst_family=''):
        params = {'instType': inst_type, 'uly': uly, 'instId': inst_id, 'ordId': ord_id, 'after': after, 'before': before,
                  'limit': limit, 'instFamily': inst_family}
        return self._request_with_params(GET, ORDER_FILLS, params)

    # Place Algo Order
    def place_algo_order(self, inst_id='', td_mode='', side='', ord_type='', sz='', ccy='',
                         pos_side='', reduce_only='', tp_trigger_px='',
                         tp_ord_px='', sl_trigger_px='', sl_ord_px='',
                         trigger_px='', order_px='', tgt_ccy='', px_var='',
                         px_spread='',
                         sz_limit='', px_limit='', time_interval='', tp_trigger_px_type='', sl_trigger_px_type='',
                         callback_ratio='', callback_spread='', active_px='', tag='', trigger_px_type='', close_fraction='',
                         quick_mgn_type='', algo_cl_ord_id=''):
        params = {'instId': inst_id, 'tdMode': td_mode, 'side': side, 'ordType': ord_type, 'sz': sz, 'ccy': ccy,
                  'posSide': pos_side, 'reduceOnly': reduce_only, 'tpTriggerPx': tp_trigger_px, 'tpOrdPx': tp_ord_px,
                  'slTriggerPx': sl_trigger_px, 'slOrdPx': sl_ord_px, 'triggerPx': trigger_px, 'orderPx': order_px,
                  'tgtCcy': tgt_ccy, 'pxVar': px_var, 'szLimit': sz_limit, 'pxLimit': px_limit,
                  'timeInterval': time_interval,
                  'pxSpread': px_spread, 'tpTriggerPxType': tp_trigger_px_type, 'slTriggerPxType': sl_trigger_px_type,
                  'callbackRatio': callback_ratio, 'callbackSpread': callback_spread, 'activePx': active_px,
                  'tag': tag, 'triggerPxType': trigger_px_type, 'closeFraction': close_fraction, 'quickMgnType': quick_mgn_type, 'algoClOrdId': algo_cl_ord_id}
        return self._request_with_params(POST, PLACE_ALGO_ORDER, params)

    # Cancel Algo Order
    def cancel_algo_order(self, params):
        return self._request_with_params(POST, CANCEL_ALGOS, params)

    # Cancel Advance Algos
    def cancel_advance_algos(self, params):
        return self._request_with_params(POST, Cancel_Advance_Algos, params)

    # Get Algo Order List
    def order_algos_list(self, ord_type='', algo_id='', inst_type='', inst_id='', after='', before='', limit='', algo_cl_ord_id=''):
        params = {'ordType': ord_type, 'algoId': algo_id, 'instType': inst_type, 'instId': inst_id, 'after': after,
                  'before': before, 'limit': limit, 'algoClOrdId': algo_cl_ord_id}
        return self._request_with_params(GET, ORDERS_ALGO_OENDING, params)

    # Get Algo Order History
    def order_algos_history(self, ord_type, state='', algo_id='', inst_type='', inst_id='', after='', before='', limit=''):
        params = {'ordType': ord_type, 'state': state, 'algoId': algo_id, 'instType': inst_type, 'instId': inst_id,
                  'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, ORDERS_ALGO_HISTORY, params)

    # Get Transaction Details History
    def get_fills_history(self, inst_type, uly='', inst_id='', ord_id='', after='', before='', limit='', inst_family=''):
        params = {'instType': inst_type, 'uly': uly, 'instId': inst_id, 'ordId': ord_id, 'after': after, 'before': before,
                  'limit': limit, 'instFamily': inst_family}
        return self._request_with_params(GET, ORDERS_FILLS_HISTORY, params)

    def get_easy_convert_currency_list(self):
        return self._request_without_params(GET, EASY_CONVERT_CURRENCY_LIST)

    def easy_convert(self, from_ccy=None, to_ccy=''):
        params = {
            'fromCcy': from_ccy,
            'toCcy': to_ccy
        }
        return self._request_with_params(POST, EASY_CONVERT, params)

    def get_easy_convert_history(self, before='', after='', limit=''):
        params = {
            'before': before,
            'after': after,
            'limit': limit
        }
        return self._request_with_params(GET, CONVERT_EASY_HISTORY, params)

    def get_oneclick_repay_list(self, debt_type=''):
        params = {
            'debtType': debt_type
        }
        return self._request_with_params(GET, ONE_CLICK_REPAY_SUPPORT, params)

    def oneclick_repay(self, debt_ccy=None, repay_ccy=''):
        params = {
            'debtCcy': debt_ccy,
            'repayCcy': repay_ccy
        }
        return self._request_with_params(POST, ONE_CLICK_REPAY, params)

    def oneclick_repay_history(self, after='', before='', limit=''):
        params = {
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request_with_params(GET, ONE_CLICK_REPAY_HISTORY, params)

    # Get algo order details
    def get_algo_order_details(self, algo_id='', algo_cl_ord_id=''):
        params = {'algoId': algo_id, 'algoClOrdId': algo_cl_ord_id}
        return self._request_with_params(GET, GET_ALGO_ORDER_DETAILS, params)

    # Amend algo order
    def amend_algo_order(self, inst_id='', algo_id='', algo_cl_ord_id='', cxl_on_fail='', req_id='', new_sz='',
                         new_tp_trigger_px='', new_tp_ord_px='', new_sl_trigger_px='', new_sl_ord_px='', new_tp_trigger_px_type='',
                         new_sl_trigger_px_type=''):
        params = {'instId': inst_id, 'algoId': algo_id, 'algoClOrdId': algo_cl_ord_id, 'cxlOnFail': cxl_on_fail,
                  'reqId': req_id, 'newSz': new_sz, 'newTpTriggerPx': new_tp_trigger_px, 'newTpOrdPx': new_tp_ord_px,
                  'newSlTriggerPx': new_sl_trigger_px, 'newSlOrdPx': new_sl_ord_px,
                  'newTpTriggerPxType': new_tp_trigger_px_type, 'newSlTriggerPxType': new_sl_trigger_px_type}
        return self._request_with_params(POST, AMEND_ALGO_ORDER, params)

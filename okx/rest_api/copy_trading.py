from .client import Client
from .consts import *


class CopyTradingAPI(Client):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain)

    # Get existing leading positions
    def get_existing_leading_positions(self, inst_id=''):
        params = {
            'instId': inst_id
        }
        return self._get(GET_EXISTING_LEADING_POSITIONS, params)

    # Get leading position history
    def get_leading_position_history(self, inst_id='', after='', before='', limit=''):
        params = {
            'instId': inst_id,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._get(GET_LEADING_POSITIONS_HISTORY, params)

    # Place leading stop order
    def place_leading_stop_order(self, sub_pos_id='', tp_trigger_px='', sl_trigger_px='', tp_trigger_px_type='', sl_trigger_px_type=''):
        params = {
            'subPosId': sub_pos_id,
            'tpTriggerPx': tp_trigger_px,
            'slTriggerPx': sl_trigger_px,
            'tpTriggerPxType': tp_trigger_px_type,
            'slTriggerPxType': sl_trigger_px_type
        }
        return self._post(PLACE_LEADING_STOP_ORDER, params)

    # Close leading position
    def close_leading_position(self, sub_pos_id=''):
        params = {
            'subPosId': sub_pos_id
        }
        return self._post(CLOSE_LEADING_POSITIONS, params)

    # Get leading instruments
    def get_leading_instruments(self):
        return self._get(GET_LEADING_POSITIONS)

    # Amend leading instruments
    def amend_leading_instruments(self, inst_id=''):
        params = {
            'instId': inst_id
        }
        return self._post(AMEND_EXISTING_LEADING_POSITIONS, params)

    # Get profit sharing details
    def get_profit_sharing_details(self, after='', before='', limit=''):
        params = {
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._get(GET_PROFIT_SHARING_DETAILS, params)

    # Get total profit sharing
    def get_total_profit_sharing(self):
        return self._get(GET_TOTAL_PROFIT_SHARING)

    # Get unrealized profit sharing details
    def get_unrealized_profit_sharing_details(self):
        return self._get(GET_UNREALIZED_PROFIT_SHARING_DETAILS)

import json

import httpx

from okx.rest_api import utils, consts


class Client:

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', base_api=consts.API_URL):
        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.PASSPHRASE = passphrase
        self.use_server_time = use_server_time
        self.flag = flag
        self.client = httpx.Client(base_url=base_api, http2=True)

    @utils.unify_error
    def _get(self, request_path, params: dict = None):
        request_path += utils.parse_params_to_str(params)
        return self.client.get(request_path, headers=self._get_header("GET", request_path, "")).json()

    @utils.unify_error
    def _post(self, request_path, params: dict = None):
        return self.client.post(request_path,
                                json=params,
                                headers=self._get_header("POST", request_path, json.dumps(params))).json()

    def _get_header(self, method, request_path, body):
        if self.API_KEY != '-1':
            timestamp = self._get_timestamp()
            sign = utils.sign(utils.pre_hash(timestamp, method, request_path, body), self.API_SECRET_KEY)
            return utils.get_header(self.API_KEY, sign, timestamp, self.PASSPHRASE, self.flag)
        else:
            return utils.get_header_no_sign(self.flag)

    def _get_timestamp(self):
        if self.use_server_time:
            return self._request_timestamp()
        else:
            return utils.get_timestamp()

    def _request_timestamp(self):
        request_path = consts.API_URL + consts.SERVER_TIMESTAMP_URL
        response = self.client.get(request_path)
        if response.status_code == 200:
            return response.json()['ts']
        else:
            return ""

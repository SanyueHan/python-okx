import hmac
import base64
import datetime
import functools
import httpx

from okx.rest_api import consts as c
from okx.rest_api.errors import *


def sign(message, secret_key):
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + request_path + body


def get_header(api_key, sign, timestamp, passphrase, flag):
    header = dict()
    header[c.CONTENT_TYPE] = c.APPLICATION_JSON
    header[c.OK_ACCESS_KEY] = api_key
    header[c.OK_ACCESS_SIGN] = sign
    header[c.OK_ACCESS_TIMESTAMP] = str(timestamp)
    header[c.OK_ACCESS_PASSPHRASE] = passphrase
    header['x-simulated-trading'] = flag
    return header


def get_header_no_sign(flag):
    header = dict()
    header[c.CONTENT_TYPE] = c.APPLICATION_JSON
    header['x-simulated-trading'] = flag
    return header


def parse_params_to_str(params):
    if params:
        return '?' + '&'.join(f"{key}={value}" for key, value in params.items())
    else:
        return ''


def get_timestamp():
    now = datetime.datetime.utcnow()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


def unify_error(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
        except httpx.HTTPError as e:
            raise OkxRequestException(f"HTTPError: {e}") from e
        if response['code'] != '0':
            raise OkxResponseException(f"code={response.get('code')}, 'msg={response.get('msg')}")
        return response
    return decorator

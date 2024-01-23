import hmac
import base64
import datetime
import functools
import httpx
import json

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
            response: httpx.Response = func(*args, **kwargs)
        except httpx.HTTPError as e:
            raise OkxRequestException(f"HTTPError: {e}") from e

        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            raise OkxResponseException(response.text)

        code = result.get("code")
        msg = result.get("msg")
        if code == "0":
            return result
        if code == "1":
            # bulk operation all failed
            raise OkxResponseException(f"code={code}, msg={msg}, details={get_details_from_bulk_operation_response(result)}")
        if code == "2":
            # bulk operation partially successful
            raise BulkOperationPartiallySuccessful(f"code={code}, msg={msg}, details={get_details_from_bulk_operation_response(result)}")
        raise OkxResponseException(f"code={code}, msg={msg}")
    return decorator


def get_details_from_bulk_operation_response(response):
    details = {}
    for res in response.get("data", []):
        if scode := res.get("sCode", "0") != "0":
            details[scode] = res.get("sMsg")
    return details

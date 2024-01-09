

class OkxApiException(Exception):
    pass


class OkxRequestException(OkxApiException):
    pass


class OkxResponseException(OkxApiException):
    pass


class BulkOperationPartiallySuccessful(OkxResponseException):
    """
    code = 2
    """
    pass

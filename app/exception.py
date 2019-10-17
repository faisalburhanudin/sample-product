class RequestError(Exception):
    message = "request error"
    status_code = 400

    def __init__(self, message=None):
        if message is not None:
            self.message = message


class UserNotFound(RequestError):
    message = "user not found"


class ProductNotFound(RequestError):
    message = "product not found"

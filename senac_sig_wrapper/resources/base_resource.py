from senac_sig_wrapper.request import Request


class BaseResource:
    def __init__(self, request: Request = None):
        if not request:
            raise ValueError("You need to configure the request")
        self.request = request

class AuthenticationFailureException(Exception):
    """Raise when authentication didn't succeed
    """

    def __init__(self, message: str = None, **kwargs):
        self.auth_type = kwargs.get("auth_type", "access_token")
        self.message = f"{message} with {self.auth_type} auth type"


class BadAPIRequest(Exception):
    """Raise when submitting an invalid request parameter
    """

    def __init__(self, message: str = None, **kwargs):
        self.message = f"{message}"

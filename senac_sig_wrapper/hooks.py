"""Collection of request hooks useful for supplement responses behavior
"""
from senac_sig_wrapper.settings import Config
from senac_sig_wrapper.enum import ErrorCodesEnum

CONFIG = Config()


def check_response_errors(response, *args, **kwargs):
    """Hook to raise the expected exception in failure cases
    """
    auth_type = (
        "Oauth 2.0"
        if "Authorization" in response.request.headers
        else "access_token"
    )

    if response.status_code in [400, 401, 429]:
        msg, exception = ErrorCodesEnum.message_and_exception_for_code(
            code=response.status_code
        )

        raise exception(message=msg, **{"auth_type": auth_type})
    return response.raise_for_status()

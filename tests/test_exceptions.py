import pytest
from senac_sig_wrapper import exceptions


class TestExceptions:
    
    def test_authentication_failure_can_be_raised(self):
        with pytest.raises(exceptions.AuthenticationFailureException):
            raise exceptions.AuthenticationFailureException(
                message="Authentication Failed"
            )

    def test_bad_request_can_be_raised(self):
        with pytest.raises(exceptions.BadAPIRequest):
            raise exceptions.BadAPIRequest(message="Bad Request")

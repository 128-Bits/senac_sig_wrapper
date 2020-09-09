import enum
import senac_sig_wrapper
from senac_sig_wrapper import enum as error_enum


class TestErrorCodesEnum:
    def test_is_subclass(self):
        assert issubclass(error_enum.ErrorCodesEnum, enum.Enum)

    def test_representation(self):
        assert (
            error_enum.ErrorCodesEnum.API_AUTH_ISSUE.error
            == "401 - API Authentication Issue"
        )

    def test_get_message_and_exception(self):
        assert error_enum.ErrorCodesEnum.message_and_exception_for_code(
            code=400
        ) == ("Bad Request", senac_sig_wrapper.exceptions.BadAPIRequest)
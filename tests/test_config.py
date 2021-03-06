"""
"""
import os
import logging
from pathlib import Path
import inspect
import pytest
import decouple
from senac_sig_wrapper.settings import Config


class TestConfig:
    def setup(self):
        self.configobj = Config()

    def test_is_class(self):
        assert inspect.isclass(Config), "Config is anything but a class"

    def test_is_instantiable(self):
        assert self.configobj is not None, "Config cannot be instantiated"

    def test_raise_invalid_base_url(self):
        os.environ["BASE_URL"] = "something"
        config = Config()
        with pytest.raises(ValueError):
            config.base_url
        del os.environ["BASE_URL"]

    def test_raise_no_base_url(self):
        BASE_URL = os.environ.pop(
            "BASE_URL",
            "https://localhost"
        )
        path = Path(__file__).parent
        config = Config(path)
        with pytest.raises(decouple.UndefinedValueError):
            config.base_url
        os.environ["BASE_URL"] = BASE_URL

    def test_raise_no_token(self):

        path = Path(__file__).parent
        config = Config(path)
        del config.access_token
        with pytest.raises(ValueError):
            config.access_token

    def test_debug(self):
        assert self.configobj.debug is False

    def test_setup_logging(self):
        os.environ["DEBUG_REQUESTS"] = "true"
        config = Config()
        config.setup_logging()
        assert (
            logging.getLevelName(
                logging.getLogger("senac_sig_wrapper").level
            )
            == "DEBUG"
        )

    def test_set_new_token(self):
        config = Config()
        config.access_token = 'new_token'
        assert config.access_token == 'new_token'
        
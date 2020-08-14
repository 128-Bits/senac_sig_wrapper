"""
"""
from typing import Any, Dict, Union
from pathlib import Path
import logging
import decouple
import http.client as http_client
from senac_sig_wrapper.validators import Validator


class Config:
    def __init__(
        self,
        config_path: Union[Any, Path] = None,
        supported: Dict[Union[Any, bytes], Any] = None,
    ):
        self._config = decouple.AutoConfig(search_path=config_path)
        self._config.SUPPORTED = supported or {".env": decouple.RepositoryEnv}

    @property
    def base_url(self):
        base_url = self._config("BASE_URL")
        if Validator.validate_url(base_url):
            return base_url
        raise ValueError("Invalid address provided.")

    @property
    def access_token(self):
        access_token = self._config("ACCESS_TOKEN")
        return access_token

    @property
    def debug(self):
        return self._config("DEBUG_REQUESTS", default=False, cast=bool)

    def setup_logging(self):
        if self.debug:
            http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger("senac_sig_wrapper").setLevel(logging.DEBUG)

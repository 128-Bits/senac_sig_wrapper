"""
"""
from typing import Any, Dict, Union
from pathlib import Path
import logging
import decouple
import http.client as http_client
from senac_sig_wrapper.validators import Validator


class Config:

    _access_token: Union[str, None] = None

    def __init__(
        self,
        config_path: Union[Any, Path] = None,
        supported: Dict[Union[Any, bytes], Any] = None,
        token: Union[str, None] = None
    ):
        self._config = decouple.AutoConfig(search_path=config_path)
        self._config.SUPPORTED = supported or {".env": decouple.RepositoryEnv}
        self._access_token = token

    @property
    def base_url(self):
        base_url = self._config("BASE_URL")
        if Validator.validate_url(base_url):
            return base_url
        raise ValueError("Endereço da api parece inválido.")

    @property
    def access_token(self):
        if self._access_token is None:
            raise ValueError("Token de acesso não foi informado")
        return self._access_token

    @access_token.setter
    def access_token(self, value: str):
        self._access_token = value
    
    @access_token.deleter
    def access_token(self):
        self._access_token = None


    @property
    def debug(self):
        return self._config("DEBUG_REQUESTS", default=False, cast=bool)


    def setup_logging(self):
        if self.debug:
            http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger("senac_sig_wrapper").setLevel(logging.DEBUG)

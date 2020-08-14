"""Senac SIG client module
"""
from senac_sig_wrapper.settings import Config
from senac_sig_wrapper.request import Request
from senac_sig_wrapper.resources.administration import Administration
from senac_sig_wrapper.resources.finance import Finance


class SigClient:
    """SigClient
    """

    def __init__(self, config: Config = Config()):
        self._config = config
        self.request = Request(self._config)

    @property
    def administration(self):
        return Administration(self.request)
    
    @property
    def finance(self):
        return Finance(self.request)

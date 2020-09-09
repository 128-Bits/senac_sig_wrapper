"""Senac SIG client module
"""
from senac_sig_wrapper.settings import Config
from senac_sig_wrapper.request import Request
from senac_sig_wrapper.resources.administration import Administration
from senac_sig_wrapper.resources.finance import Finance
from senac_sig_wrapper.resources.registration import Registration
from senac_sig_wrapper.resources.course import Course
from senac_sig_wrapper.resources.classes import Classes


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
    
    @property
    def registration(self):
        return Registration(self.request)
    
    @property
    def course(self):
        return Course(self.request)
    
    @property
    def classes(self):
        return Classes(self.request)
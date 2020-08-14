import inspect
import pytest
from tests.helper import not_raises
from senac_sig_wrapper.client import SigClient


class TestSigClient:
    def setup(self):
        self.client = SigClient()

    def test_is_class(self):
        assert inspect.isclass(SigClient)

    def test_can_instantiate(self):
        client = SigClient()
        assert client is not None

    def test_need_config(self):
        client_init = inspect.getfullargspec(SigClient.__init__)
        assert "config" in client_init.args

    def test_has_administration(self):
        assert hasattr(self.client, "administration")
    
    def test_has_finance(self):
        assert hasattr(self.client, "finance")

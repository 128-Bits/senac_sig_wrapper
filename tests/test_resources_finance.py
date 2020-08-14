from unittest import mock

from _pytest.monkeypatch import MonkeyPatch
from senac_sig_wrapper.settings import Config
from senac_sig_wrapper.request import Request
from senac_sig_wrapper.resources import BaseResource
from senac_sig_wrapper.resources import finance


class TestFinance:

    monkeypatch = MonkeyPatch()

    def setup(self):
        self.config = Config()
        self.request = Request(self.config)
        self.finance = finance.Finance(self.request)
        self.mock_get = mock.MagicMock()
        self.mock_post = mock.MagicMock()
        self.mock_delete = mock.MagicMock()
        self.monkeypatch.setattr("requests.Session.get", self.mock_get)
        self.monkeypatch.setattr("requests.Session.post", self.mock_post)
        self.monkeypatch.setattr("requests.Session.delete", self.mock_delete)

    @classmethod
    def teardown_class(cls):
        cls.monkeypatch.undo()

    def test_class_tree(self):
        assert issubclass(finance.Finance, BaseResource)

    def test_has_get_voucher(self):
        assert hasattr(self.finance, "get_voucher")
    
    def test_get_voucher(self):
        self.finance.get_voucher()
        self.mock_get.assert_called()
    

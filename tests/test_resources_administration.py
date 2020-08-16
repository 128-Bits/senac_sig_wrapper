import json
from unittest import mock
import inspect
import pytest
import requests
from _pytest.monkeypatch import MonkeyPatch
from senac_sig_wrapper.settings import Config
from senac_sig_wrapper.request import Request
from senac_sig_wrapper.resources import BaseResource
from senac_sig_wrapper.resources import administration


class TestAdministration:

    monkeypatch = MonkeyPatch()

    def setup(self):
        self.config = Config(token='teste')
        self.request = Request(self.config)
        self.administration = administration.Administration(self.request)
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
        assert issubclass(administration.Administration, BaseResource)

    def test_has_get_cities(self):
        assert hasattr(self.administration, "get_cities")

    def test_has_get_person(self):
        assert hasattr(self.administration, "get_person")

    def test_has_get_business(self):
        assert hasattr(self.administration, "get_business")

    def test_has_get_op_unit(self):
        assert hasattr(self.administration, "get_op_unit")

    def test_get_cities(self):
        self.administration.get_cities()
        assert self.mock_get.is_called()

    def test_get_person(self):
        self.administration.get_person("a")
        assert self.mock_get.is_called()

    def test_get_business(self):
        self.administration.get_business("a")
        assert self.mock_get.is_called()

    def test_get_op_unit(self):
        self.administration.get_op_unit()
        assert self.mock_get.is_called_with("/api/unidade-operativa")

    def test_get_full_op_unit_list(self):
        self.administration.get_op_unit(complete=True)
        assert self.mock_get.is_called_with(
            "/api/unidade-operativa/lista-completa"
        )

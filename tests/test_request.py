"""Tests for request.Request class
"""
import inspect
from unittest import mock
import pytest
from _pytest.monkeypatch import MonkeyPatch
from senac_sig_wrapper.settings import Config
from senac_sig_wrapper.request import Request


class TestRequest:

    monkeypatch = MonkeyPatch()

    def setup(self):
        config = Config(token='test')
        self.requestobj = Request(config)

    def test_is_class(self):
        assert inspect.isclass(Request)

    def test_raises_without_config(self):
        with pytest.raises(ValueError):
            Request()

    def test_has_docstring(self):
        assert len(inspect.getdoc(Request)) > 1

    def test_has_member_get(self):
        assert hasattr(self.requestobj, "get")

    def test_get_is_callable(self):
        assert hasattr(self.requestobj.get, "__call__")

    def test_get_call_requests_get(self):
        mock_get = mock.MagicMock()
        self.monkeypatch.setattr("requests.Session.get", mock_get)

        self.requestobj.get("/")
        mock_get.assert_called_once()
        self.monkeypatch.undo()

    def test_get_call_requests_get_with(self):
        mock_get = mock.MagicMock()
        self.monkeypatch.setattr("requests.Session.get", mock_get)

        self.requestobj.get("/")
        mock_get.assert_called_once_with(url="https://localhost/")
        self.monkeypatch.undo()

    def test_has_member_post(self):
        assert hasattr(self.requestobj, "post")

    def test_post_is_callable(self):
        assert hasattr(self.requestobj.post, "__call__")

    def test_post_call_requests_post(self):
        mock_post = mock.MagicMock()
        self.monkeypatch.setattr("requests.Session.post", mock_post)

        self.requestobj.post("/", data={})
        mock_post.assert_called_once()
        self.monkeypatch.undo()

    def test_post_calls_requests_post_with(self):
        data = {"test": "Test"}
        mock_post = mock.MagicMock()
        self.monkeypatch.setattr("requests.Session.post", mock_post)

        self.requestobj.post("/", data=data)
        mock_post.assert_called_once_with("/", data=data)
        self.monkeypatch.undo()

    def test_has_member_delete(self):
        assert hasattr(self.requestobj, "delete")

    def test_delete_is_callable(self):
        assert hasattr(self.requestobj.delete, "__call__")

    def test_delete_call_requests_delete(self):
        mock_delete = mock.MagicMock()
        self.monkeypatch.setattr("requests.Session.delete", mock_delete)

        self.requestobj.delete("/")
        mock_delete.assert_called_once()
        self.monkeypatch.undo()

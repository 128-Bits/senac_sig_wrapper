import pytest
from unittest import mock
from _pytest.monkeypatch import MonkeyPatch
from senac_sig_wrapper.settings import Config
from senac_sig_wrapper.request import Request
from senac_sig_wrapper.resources import BaseResource
from senac_sig_wrapper.resources import course


class TestCourse:

    monkeypatch = MonkeyPatch()

    def setup(self):
        self.config = Config()
        self.request = Request(self.config)
        self.course = course.Course(self.request)
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
        assert issubclass(course.Course, BaseResource)
    
    def test_has_get_segments(self):
        assert hasattr(self.course, "get_segments")
    
    def test_get_segments(self):
        self.course.get_segments()
        self.mock_get.assert_called_once()
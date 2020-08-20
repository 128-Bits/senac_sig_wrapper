import pytest
from unittest import mock
from _pytest.monkeypatch import MonkeyPatch
from senac_sig_wrapper.settings import Config
from senac_sig_wrapper.request import Request
from senac_sig_wrapper.resources import BaseResource
from senac_sig_wrapper.resources import classes


class TestCourse:

    monkeypatch = MonkeyPatch()

    def setup(self):
        self.config = Config(token='teste')
        self.request = Request(self.config)
        self.classes = classes.Classes(self.request)
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
        assert issubclass(classes.Classes, BaseResource)
    
    def test_has_get_single_class(self):
        assert hasattr(self.classes, "get_single_class")
    
    def test_has_get_open_spaces(self):
        assert hasattr(self.classes, "get_open_spaces")
    
    def test_get_single_class_raises(self):
        with pytest.raises(ValueError):
            self.classes.get_single_class() 
        
    def test_get_open_spaces(self):
        with pytest.raises(ValueError):
            self.classes.get_open_spaces()
        
    def test_get_single_class(self):
        self.classes.get_single_class(1)
        self.mock_get.assert_called_once()
        self.mock_get.assert_called_with(url="https://localhost/api/turma/1")
        
    def test_get_open_spaces(self):
        self.classes.get_open_spaces(1)
        self.mock_get.assert_called_once()
        self.mock_get.assert_called_with(url="https://localhost/api/turma/vagas-disponiveis/1")
    
import pytest
from unittest import mock
from _pytest.monkeypatch import MonkeyPatch
from senac_sig_wrapper.settings import Config
from senac_sig_wrapper.request import Request
from senac_sig_wrapper.resources import BaseResource
from senac_sig_wrapper.resources import registration


class TestRegistration:

    monkeypatch = MonkeyPatch()

    def setup(self):
        self.config = Config()
        self.request = Request(self.config)
        self.registration = registration.Registration(self.request)
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
        assert issubclass(registration.Registration, BaseResource)
    
    def test_has_get_demand_type(self):
        assert hasattr(self.registration, "get_demand_type")
    
    def test_has_get_communication_channels(self):
        assert hasattr(self.registration, "get_communication_channels")
    
    def test_has_demand(self):
        assert hasattr(self.registration, "send_demand")
    
    def test_has_students_with_class(self):
        assert hasattr(self.registration, "get_students_with_class")
    
    def test_has_students_to_integrate(self):
        assert hasattr(self.registration, "get_students_to_integrate")
    
    def test_get_demand_type(self):
        self.registration.get_demand_type()
        self.mock_get.assert_called_once()

    def test_get_communication_channels(self):
        self.registration.get_communication_channels()
        self.mock_get.assert_called_once()

    def test_get_students_with_class(self):
        self.registration.get_students_with_class()
        self.mock_get.assert_called_once()
    
    def test_get_students_to_integrate(self):
        self.registration.get_students_to_integrate()
        self.mock_get.assert_called_once()
    
    def test_send_demand_without_data(self):
        with(pytest.raises(ValueError)):
            self.registration.send_demand()
    
    def test_send_invalid_demand(self, invalid_demand):
        with(pytest.raises(ValueError)):
            self.registration.send_demand(invalid_demand)
        
    def test_with_valid_demand(self, valid_demand):
        self.registration.send_demand(valid_demand)
        self.mock_post.assert_called_once()

        


# GET
# /api/demanda/tipos-de-demanda

# GET
# /api/demanda/canais-de-comunicacao


# POST
# /api/demanda


# GET
# /api/matricula/alunos-com-turma


# GET
# /api/matricula/alunos-para-integracao-office-365
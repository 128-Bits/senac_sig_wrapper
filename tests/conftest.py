"""Conftest plugin module for pytest
"""
import pytest
from senac_sig_wrapper.enum import (
    TipoRecursoFinanceiroEnum,
    TipoPessoaDemandaEnum,
)


@pytest.fixture(scope="session")
def fields():
    return [
        "VigenciaInicial",
        "VigenciaFinal",
        "Estado",
        "Situacao",
    ]


@pytest.fixture(scope="session")
def data_fields():
    return [
        "VigenciaInicial",
        "VigenciaFinal",
        "Estado",
        "Situacao",
        "AnyField",
    ]


@pytest.fixture(scope="session")
def invalid_demand():
    return {
        "tipoDeRecursoId": TipoRecursoFinanceiroEnum.GRATUITO.value,
        "tipoDePessoaDaDemanda": TipoPessoaDemandaEnum.PESSOA_FISICA.value,
        "canalId": 25,
        "numeroDoDocumento": 3234235,
        "nome": "teste",
        "numeroDoTelefone": "00990099090",
    }

@pytest.fixture(scope="session")
def valid_demand():
    return {
        "tipoDeRecursoId": TipoRecursoFinanceiroEnum.GRATUITO.value,
        "tipoDePessoaDaDemanda": TipoPessoaDemandaEnum.PESSOA_FISICA.value,
        "canalId": 25,
        "numeroDoDocumento": 3234235,
        "nome": "teste",
        "codigoDeArea": 86,
        "numeroDoTelefone": "00990099090",
    }
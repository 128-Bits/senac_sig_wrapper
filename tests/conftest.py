"""Conftest plugin module for pytest
"""
import pytest


@pytest.fixture()
def fields():
    return [
        "VigenciaInicial",
        "VigenciaFinal",
        "Estado",
        "Situacao",
    ]


@pytest.fixture()
def data_fields():
    return [
        "VigenciaInicial",
        "VigenciaFinal",
        "Estado",
        "Situacao",
        "AnyField"
    ]

import pytest
from senac_sig_wrapper import helper


def test_intersect_fields(fields, data_fields):
    assert helper.dict_has_invalid_fields(fields, data_fields)


def test_without_dict_fields(fields):
    with(pytest.raises(ValueError)):
        helper.dict_has_invalid_fields(fields, None)

from senac_sig_wrapper.enum import (
    TipoRecursoFinanceiroEnum,
    TipoPessoaDemandaEnum,
)


def test_tipo_recurso_financeiro_choices():
    expected_tuple = (
        ("Gratuito", 1),
        ("Comercial", 2)
    )

    assert TipoRecursoFinanceiroEnum.choices() == expected_tuple


def test_tipo_pessoa_demanda_choices():
    expected_tuple = (
        ("Pessoa Física", 1),
        ("Pessoa Jurídica", 2)
    )

    assert TipoPessoaDemandaEnum.choices() == expected_tuple

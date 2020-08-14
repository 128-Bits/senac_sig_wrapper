from typing import Iterable, Union


def dict_has_invalid_fields(
    schema_fields: Union[Iterable[str], None] = None,
    dict_fields: Union[Iterable[str], None] = None,
) -> set:
    if not schema_fields or not dict_fields:
        raise ValueError("Precisamos das duas listas para fazer esta checagem")

    return set(dict_fields).difference(schema_fields)

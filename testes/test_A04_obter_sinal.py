import pytest
from artefatos.A04_obter_sinal import obter_sinal


@pytest.mark.parametrize(
    "n, esperado",
    [
        (10, 1),
        (1, 1),
        (0.5, 1),
        (-10, -1),
        (-1, -1),
        (-0.5, -1),
        (0, 0),
        (0.0, 0),
    ],
)
def test_obter_sinal_valores_numericos(n, esperado):
    assert obter_sinal(n) == esperado


@pytest.mark.parametrize(
    "n",
    [
        None,
        "10",
        "abc",
        [],
        {},
    ],
)
def test_obter_sinal_entradas_invalidas(n):
    with pytest.raises(TypeError):
        obter_sinal(n)

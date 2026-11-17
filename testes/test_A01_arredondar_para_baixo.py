import pytest

from artefatos.A01_arredondar_para_baixo import arredondar_para_baixo


@pytest.mark.parametrize(
    "valor, esperado",
    [
        (0, 0),
        (1, 1),
        (-1, -1),
        (42, 42),
        (-42, -42),
        (0.0, 0),
        (-0.0, 0),
        (3.0, 3),
        (-3.0, -3),
        (3.7, 3),
        (-3.7, -4),
        (0.9, 0),
        (-0.9, -1),
        (1.999999999, 1),
        (-1.000000001, -2),
        (1e-300, 0),
        (-1e-300, -1),
        (10**100, 10**100),
        (-(10**100), -(10**100)),
        (True, 1),
        (False, 0),
    ],
)
def test_arredondar_para_baixo_resultados(valor, esperado):
    resultado = arredondar_para_baixo(valor)

    assert resultado == esperado
    assert type(resultado) is int
    assert resultado <= valor < resultado + 1


@pytest.mark.parametrize("valor", [None, [], {}, (), object(), 1 + 2j])
def test_arredondar_para_baixo_tipos_invalidos(valor):
    with pytest.raises(TypeError):
        arredondar_para_baixo(valor)


@pytest.mark.parametrize("valor", ["", "abc", "3.7", float("nan")])
def test_arredondar_para_baixo_valores_invalidos(valor):
    with pytest.raises(ValueError):
        arredondar_para_baixo(valor)


@pytest.mark.parametrize("valor", ["3", "-3", "0"])
def test_arredondar_para_baixo_strings_inteiras(valor):
    with pytest.raises(TypeError):
        arredondar_para_baixo(valor)


@pytest.mark.parametrize("valor", [float("inf"), float("-inf")])
def test_arredondar_para_baixo_infinitos(valor):
    with pytest.raises(OverflowError):
        arredondar_para_baixo(valor)

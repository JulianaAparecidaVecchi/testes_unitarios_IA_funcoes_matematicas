import pytest

from artefatos.A10_euclides_estendido import euclides_estendido


def test_dois_numeros_positivos():
    mdc, x, y = euclides_estendido(48, 18)

    assert mdc == 6
    assert 48 * x + 18 * y == mdc


def test_numeros_coprimos():
    mdc, x, y = euclides_estendido(17, 5)

    assert mdc == 1
    assert 17 * x + 5 * y == mdc


def test_primeiro_argumento_zero():
    mdc, x, y = euclides_estendido(0, 15)

    assert mdc == 15
    assert 0 * x + 15 * y == mdc


def test_segundo_argumento_zero():
    mdc, x, y = euclides_estendido(15, 0)

    assert mdc == 15
    assert 15 * x + 0 * y == mdc


def test_dois_numeros_negativos():
    mdc, x, y = euclides_estendido(-48, -18)

    assert mdc == 6
    assert -48 * x + (-18) * y == mdc


def test_primeiro_argumento_negativo():
    mdc, x, y = euclides_estendido(-48, 18)

    assert mdc == 6
    assert -48 * x + 18 * y == mdc


def test_segundo_argumento_negativo():
    mdc, x, y = euclides_estendido(48, -18)

    assert mdc == 6
    assert 48 * x + (-18) * y == mdc


def test_numeros_iguais():
    mdc, x, y = euclides_estendido(25, 25)

    assert mdc == 25
    assert 25 * x + 25 * y == mdc


def test_numeros_muito_grandes():
    a = 10**100
    b = 10**50

    mdc, x, y = euclides_estendido(a, b)

    assert mdc == b
    assert a * x + b * y == mdc


def test_argumentos_zero_gera_value_error():
    with pytest.raises(ValueError, match="a e b não podem ser ambos zero"):
        euclides_estendido(0, 0)


def test_retorno_e_uma_tupla():
    resultado = euclides_estendido(48, 18)

    assert isinstance(resultado, tuple)
    assert len(resultado) == 3


def test_retorno_contem_inteiros():
    resultado = euclides_estendido(48, 18)

    assert all(isinstance(valor, int) for valor in resultado)


@pytest.mark.parametrize(
    "a, b",
    [
        (1, 1),
        (2, 3),
        (7, 13),
        (100, 25),
        (81, 27),
        (-7, 13),
        (7, -13),
        (-7, -13),
        (0, 1),
        (1, 0),
        (123456, 7890),
        (10**20, 10**15),
    ],
)
def test_identidade_de_bezout(a, b):
    mdc, x, y = euclides_estendido(a, b)

    assert a * x + b * y == mdc
    assert mdc >= 0


@pytest.mark.parametrize(
    "a, b",
    [
        (0, 0),
        (0, 0),
    ],
)
def test_casos_invalidos(a, b):
    with pytest.raises(ValueError):
        euclides_estendido(a, b)


@pytest.mark.parametrize(
    "a, b, mdc_esperado",
    [
        (48, 18, 6),
        (100, 10, 10),
        (17, 5, 1),
        (0, 12, 12),
        (12, 0, 12),
        (-48, 18, 6),
        (48, -18, 6),
        (-48, -18, 6),
        (7, 7, 7),
        (1, 1, 1),
        (-1, 1, 1),
    ],
)
def test_mdc_esperado(a, b, mdc_esperado):
    mdc, x, y = euclides_estendido(a, b)

    assert mdc == mdc_esperado
    assert a * x + b * y == mdc_esperado

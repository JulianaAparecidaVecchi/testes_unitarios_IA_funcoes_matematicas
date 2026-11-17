import pytest

from A02_avaliar_polinomio import avaliar_polinomio


@pytest.mark.parametrize(
    "coeficientes, x, esperado",
    [
        ([2, 3, 1], 2, 15),
        ([1, 0, -4], 3, 5),
        ([3, -2, 5], 0, 5),
        ([5], 10, 5),
        ([0], 7, 0),
        ([], 3, 0),
        ([0, 0, 0], 5, 0),
        ([1, 2, 3], -2, 3),
        ([2, -3, 1], -1, 6),
        ([1, 1, 1, 1], 2, 15),
        ([0, 2, 3], 4, 11),
        ([2, 0, 0], 3, 18),
        ([-1, -2, -3], 2, -11),
        ([1.5, 2.5], 2, 5.5),
        ([0.1, 0.2, 0.3], 2, 0.9),
        ([1, 0, 0, 0, 0], 10, 10000),
        ([1, -1], 1, 0),
        ([10], -100, 10),
        ([1, 2, 3], 1, 6),
        ([1, 2, 3], 0, 3),
    ],
)
def test_avaliar_polinomio_valores_validos(
    coeficientes, x, esperado
):
    resultado = avaliar_polinomio(coeficientes, x)
    assert resultado == pytest.approx(esperado)


def test_avaliar_polinomio_grau_alto():
    coeficientes = [1] + [0] * 20
    resultado = avaliar_polinomio(coeficientes, 2)
    assert resultado == 2**20


def test_avaliar_polinomio_coeficientes_grandes():
    coeficientes = [1000000, 2000000, 3000000]
    resultado = avaliar_polinomio(coeficientes, 10)
    assert resultado == 123000000


def test_avaliar_polinomio_com_tupla():
    resultado = avaliar_polinomio((1, 2, 3), 2)
    assert resultado == 11


def test_avaliar_polinomio_com_gerador():
    coeficientes = (c for c in [1, 2, 3])
    resultado = avaliar_polinomio(coeficientes, 2)
    assert resultado == 11


def test_avaliar_polinomio_nao_modifica_coeficientes():
    coeficientes = [2, 3, 4]
    original = coeficientes.copy()

    avaliar_polinomio(coeficientes, 5)

    assert coeficientes == original


@pytest.mark.parametrize(
    "coeficientes, x",
    [
        (None, 2),
        (5, 2),
        (3.5, 2),
    ],
)
def test_avaliar_polinomio_coeficientes_nao_iteraveis(
    coeficientes, x
):
    with pytest.raises(TypeError):
        avaliar_polinomio(coeficientes, x)


@pytest.mark.parametrize(
    "coeficientes, x",
    [
        ([1, 2, 3], None),
        ([1, 2, 3], "abc"),
        ([1, 2, 3], [2]),
        ([1, 2, 3], {}),
    ],
)
def test_avaliar_polinomio_x_invalido(coeficientes, x):
    with pytest.raises(TypeError):
        avaliar_polinomio(coeficientes, x)


@pytest.mark.parametrize(
    "coeficientes, x",
    [
        ([1, None, 3], 2),
        ([1, "abc", 3], 2),
        ([1, [2], 3], 2),
        ([1, {}, 3], 2),
    ],
)
def test_avaliar_polinomio_coeficientes_invalidos(
    coeficientes, x
):
    with pytest.raises(TypeError):
        avaliar_polinomio(coeficientes, x)


def test_avaliar_polinomio_lista_vazia_com_x_invalido():
    resultado = avaliar_polinomio([], None)
    assert resultado == 0


def test_avaliar_polinomio_coeficientes_booleanos():
    resultado = avaliar_polinomio([True, False, True], 2)
    assert resultado == 5


def test_avaliar_polinomio_x_booleano():
    resultado = avaliar_polinomio([1, 2, 3], True)
    assert resultado == 6
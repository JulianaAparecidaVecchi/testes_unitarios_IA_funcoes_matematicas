import pytest
from artefatos.A14_coeficiente_binomial import coeficiente_binomial


@pytest.mark.parametrize(
    "n, k, esperado",
    [
        (5, 2, 10),
        (6, 3, 20),
        (10, 4, 210),
        (5, 0, 1),
        (0, 0, 1),
        (1, 1, 1),
        (10, 1, 10),
        (10, 9, 10),
        (10, 10, 1),
        (5, 6, 0),
        (5, -1, 0),
        (0, 1, 0),
        (20, 2, 190),
        (100, 50, 100891344545564193334812497256),
        (50, 25, 126410606437752),
    ],
)
def test_coeficiente_binomial_casos_validos(n, k, esperado):
    assert coeficiente_binomial(n, k) == esperado


@pytest.mark.parametrize(
    "n, k",
    [
        (5.0, 2),
        (5, 2.0),
        (3.5, 1),
        (5, 1.5),
        ("5", 2),
        (5, "2"),
        (None, 2),
        (5, None),
        ([], 2),
        (5, []),
    ],
)
def test_coeficiente_binomial_entradas_invalidas(n, k):
    with pytest.raises(TypeError, match="n e k devem ser inteiros"):
        coeficiente_binomial(n, k)


def test_coeficiente_binomial_valores_negativos():
    assert coeficiente_binomial(-5, 0) == 1
    assert coeficiente_binomial(-5, 1) == 0
    assert coeficiente_binomial(-5, -1) == 0


def test_coeficiente_binomial_resultado_simetrico():
    assert coeficiente_binomial(10, 3) == coeficiente_binomial(10, 7)


def test_coeficiente_binomial_k_maior_que_n():
    assert coeficiente_binomial(4, 10) == 0

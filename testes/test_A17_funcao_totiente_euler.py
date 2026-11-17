import pytest
from artefatos.A17_funcao_totiente_euler import funcao_totiente_euler


@pytest.mark.parametrize(
    "n, esperado",
    [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 4),
        (6, 2),
        (7, 6),
        (8, 4),
        (9, 6),
        (10, 4),
        (12, 4),
        (15, 8),
        (20, 8),
        (30, 8),
        (36, 12),
        (49, 42),
        (100, 40),
        (97, 96),
        (121, 110),
        (1000, 400),
    ],
)
def test_funcao_totiente_euler_casos_validos(n, esperado):
    assert funcao_totiente_euler(n) == esperado


@pytest.mark.parametrize(
    "n",
    [
        0,
        -1,
        -10,
        -100,
        1.5,
        2.5,
        "10",
        "abc",
        None,
        [],
        {},
    ],
)
def test_funcao_totiente_euler_entradas_invalidas(n):
    with pytest.raises(ValueError, match="n deve ser inteiro positivo"):
        funcao_totiente_euler(n)


def test_funcao_totiente_euler_numero_primo():
    assert funcao_totiente_euler(13) == 12
    assert funcao_totiente_euler(101) == 100


def test_funcao_totiente_euler_potencia_de_primo():
    assert funcao_totiente_euler(16) == 8
    assert funcao_totiente_euler(27) == 18
    assert funcao_totiente_euler(125) == 100


def test_funcao_totiente_euler_produto_de_primos_distintos():
    assert funcao_totiente_euler(30) == 8
    assert funcao_totiente_euler(210) == 48


def test_funcao_totiente_euler_numero_grande():
    assert funcao_totiente_euler(10000) == 4000

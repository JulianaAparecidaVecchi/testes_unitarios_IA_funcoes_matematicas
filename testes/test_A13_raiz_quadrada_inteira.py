import pytest
from artefatos.A13_raiz_quadrada_inteira import raiz_quadrada_inteira


# Cenários de execução normal
def test_raiz_quadrada_de_zero():
    assert raiz_quadrada_inteira(0) == 0


def test_raiz_quadrada_de_um():
    assert raiz_quadrada_inteira(1) == 1


def test_raiz_quadrada_de_quatro():
    assert raiz_quadrada_inteira(4) == 2


def test_raiz_quadrada_de_nove():
    assert raiz_quadrada_inteira(9) == 3


def test_raiz_quadrada_de_vinte_e_cinco():
    assert raiz_quadrada_inteira(25) == 5


def test_raiz_quadrada_de_cem():
    assert raiz_quadrada_inteira(100) == 10


# Números que não possuem raiz quadrada exata
@pytest.mark.parametrize(
    "n, esperado",
    [
        (2, 1),
        (3, 1),
        (5, 2),
        (8, 2),
        (10, 3),
        (15, 3),
        (24, 4),
        (26, 5),
        (99, 9),
        (101, 10),
    ],
)
def test_raiz_quadrada_inteira_sem_raiz_exata(n, esperado):
    assert raiz_quadrada_inteira(n) == esperado


# Casos extremos
def test_raiz_quadrada_de_numero_grande():
    assert raiz_quadrada_inteira(1000000) == 1000


def test_raiz_quadrada_de_numero_grande_sem_raiz_exata():
    assert raiz_quadrada_inteira(1000001) == 1000


def test_raiz_quadrada_de_numero_muito_grande():
    assert raiz_quadrada_inteira(10**18) == 10**9


def test_raiz_quadrada_de_numero_muito_grande_sem_raiz_exata():
    assert raiz_quadrada_inteira(10**18 + 1) == 10**9


def test_raiz_quadrada_de_numero_extremamente_grande():
    assert raiz_quadrada_inteira(10**100) == 10**50


# Entradas inválidas: números negativos
@pytest.mark.parametrize(
    "n",
    [-1, -2, -10, -100, -1000000],
)
def test_raiz_quadrada_de_numero_negativo(n):
    with pytest.raises(ValueError, match="n deve ser não negativo"):
        raiz_quadrada_inteira(n)


# Entradas inválidas: tipos diferentes de inteiro
@pytest.mark.parametrize(
    "n",
    [
        2.5,
        3.0,
        0.5,
        "10",
        "abc",
        None,
        [4],
        (9,),
        {16},
        {"valor": 25},
    ],
)
def test_entrada_com_tipo_invalido(n):
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        raiz_quadrada_inteira(n)


# Verificação de valores próximos aos quadrados perfeitos
@pytest.mark.parametrize(
    "n, esperado",
    [
        (8, 2),
        (10, 3),
        (15, 3),
        (17, 4),
        (24, 4),
        (26, 5),
        (35, 5),
        (37, 6),
        (48, 6),
        (50, 7),
        (63, 7),
        (65, 8),
    ],
)
def test_valores_proximos_a_quadrados_perfeitos(n, esperado):
    assert raiz_quadrada_inteira(n) == esperado


# Verificação de diferentes quadrados perfeitos
@pytest.mark.parametrize(
    "n, esperado",
    [
        (16, 4),
        (36, 6),
        (49, 7),
        (64, 8),
        (81, 9),
        (121, 11),
        (144, 12),
        (169, 13),
        (196, 14),
        (225, 15),
        (400, 20),
        (900, 30),
    ],
)
def test_diferentes_quadrados_perfeitos(n, esperado):
    assert raiz_quadrada_inteira(n) == esperado


# Verificação de que o resultado é sempre o maior inteiro
# cujo quadrado é menor ou igual a n
@pytest.mark.parametrize(
    "n",
    [2, 3, 5, 8, 10, 15, 26, 50, 99, 150, 999, 1001],
)
def test_propriedade_da_raiz_quadrada_inteira(n):
    resultado = raiz_quadrada_inteira(n)

    assert resultado * resultado <= n
    assert (resultado + 1) * (resultado + 1) > n
import pytest
from artefatos.A12_eh_cubo_perfeito import eh_cubo_perfeito


# Cenários de execução normal
def test_cubo_perfeito_de_zero():
    assert eh_cubo_perfeito(0) is True


def test_cubo_perfeito_de_um():
    assert eh_cubo_perfeito(1) is True


def test_cubo_perfeito_de_oito():
    assert eh_cubo_perfeito(8) is True


def test_cubo_perfeito_de_vinte_e_sete():
    assert eh_cubo_perfeito(27) is True


def test_cubo_perfeito_de_sessenta_e_quatro():
    assert eh_cubo_perfeito(64) is True


def test_cubo_perfeito_de_cento_e_vinte_e_cinco():
    assert eh_cubo_perfeito(125) is True


# Cenários com números que não são cubos perfeitos
@pytest.mark.parametrize(
    "n",
    [
        2,
        3,
        4,
        5,
        9,
        10,
        26,
        28,
        63,
        65,
        100,
        126,
    ],
)
def test_numero_nao_e_cubo_perfeito(n):
    assert eh_cubo_perfeito(n) is False


# Cenários com números negativos
def test_cubo_perfeito_negativo():
    assert eh_cubo_perfeito(-8) is True


def test_cubo_perfeito_negativo_grande():
    assert eh_cubo_perfeito(-1000) is True


@pytest.mark.parametrize(
    "n",
    [
        -2,
        -3,
        -4,
        -9,
        -26,
        -28,
        -63,
        -65,
        -100,
        -999,
    ],
)
def test_numero_negativo_nao_e_cubo_perfeito(n):
    assert eh_cubo_perfeito(n) is False


# Casos extremos
def test_cubo_perfeito_com_numero_grande():
    assert eh_cubo_perfeito(1000000) is True


def test_numero_grande_nao_e_cubo_perfeito():
    assert eh_cubo_perfeito(1000001) is False


def test_cubo_perfeito_com_valor_muito_grande():
    assert eh_cubo_perfeito(10**18) is True


def test_numero_muito_grande_nao_e_cubo_perfeito():
    assert eh_cubo_perfeito(10**18 + 1) is False


def test_cubo_perfeito_negativo_muito_grande():
    assert eh_cubo_perfeito(-(10**18)) is True


# Verificação de diferentes cubos inteiros
@pytest.mark.parametrize(
    "n",
    [
        216,       # 6³
        343,       # 7³
        512,       # 8³
        729,       # 9³
        1000,      # 10³
        1331,      # 11³
        1728,      # 12³
        2197,      # 13³
        2744,      # 14³
        3375,      # 15³
    ],
)
def test_diferentes_cubos_perfeitos(n):
    assert eh_cubo_perfeito(n) is True


# Verificação de valores imediatamente próximos aos cubos perfeitos
@pytest.mark.parametrize(
    "n",
    [
        7,
        9,
        26,
        28,
        63,
        65,
        124,
        126,
        215,
        217,
        999,
        1001,
    ],
)
def test_valores_proximos_a_cubos_perfeitos(n):
    assert eh_cubo_perfeito(n) is False
import pytest
from artefatos.A27_teste_miller_rabin import teste_miller_rabin


@pytest.mark.parametrize(
    "n",
    [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        101, 103, 107, 109, 113, 127, 131, 997, 1009,
    ],
)
def test_teste_miller_rabin_numeros_primos(n):
    assert teste_miller_rabin(n) is True


@pytest.mark.parametrize(
    "n",
    [
        -10, -1, 0, 1,
        4, 6, 8, 9, 10, 12, 15, 21, 25, 27, 49,
        100, 121, 143, 169, 221, 341, 561, 1105,
    ],
)
def test_teste_miller_rabin_numeros_nao_primos(n):
    assert teste_miller_rabin(n) is False


@pytest.mark.parametrize(
    "n",
    [
        True,
        False,
        2.5,
        3.0,
        "17",
        "abc",
        None,
        [],
        {},
    ],
)
def test_teste_miller_rabin_entradas_invalidas(n):
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        teste_miller_rabin(n)


def test_teste_miller_rabin_bases_personalizadas_primo():
    assert teste_miller_rabin(101, bases=[2, 3, 5]) is True


def test_teste_miller_rabin_bases_personalizadas_nao_primo():
    assert teste_miller_rabin(91, bases=[2, 3, 5]) is False


def test_teste_miller_rabin_bases_vazias():
    with pytest.raises(ValueError, match="bases vazias"):
        teste_miller_rabin(101, bases=[])


def test_teste_miller_rabin_base_multipla_do_numero():
    assert teste_miller_rabin(101, bases=[101, 202, 303]) is True


def test_teste_miller_rabin_numero_primo_grande():
    assert teste_miller_rabin(104729) is True


def test_teste_miller_rabin_numero_composto_grande():
    assert teste_miller_rabin(104730) is False


def test_teste_miller_rabin_caminho_de_exponenciacao():
    assert teste_miller_rabin(97, bases=[2]) is True
    assert teste_miller_rabin(341, bases=[2]) is False


def test_teste_miller_rabin_numero_carmichael():
    assert teste_miller_rabin(561) is False
    assert teste_miller_rabin(1105) is False

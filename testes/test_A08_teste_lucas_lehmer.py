import pytest
from A08_teste_lucas_lehmer import teste_lucas_lehmer


@pytest.mark.parametrize("p", [-10, -1, 0, 1])
def test_valores_menores_que_dois(p):
    assert teste_lucas_lehmer(p) is False


def test_p_igual_a_dois():
    assert teste_lucas_lehmer(2) is True


@pytest.mark.parametrize("p", [3, 5, 7, 13, 17, 19, 31])
def test_numeros_de_mersenne_primos(p):
    assert teste_lucas_lehmer(p) is True


@pytest.mark.parametrize("p", [11, 23, 29])
def test_numeros_de_mersenne_compostos(p):
    assert teste_lucas_lehmer(p) is False


def test_p_igual_a_quatro():
    assert teste_lucas_lehmer(4) is False


def test_p_igual_a_nove():
    assert teste_lucas_lehmer(9) is False


def test_p_igual_a_dez():
    assert teste_lucas_lehmer(10) is False


def test_p_igual_a_tres():
    assert teste_lucas_lehmer(3) is True


def test_p_igual_a_cinco():
    assert teste_lucas_lehmer(5) is True


@pytest.mark.parametrize("p", [2.5, 3.5])
def test_entrada_float_nao_inteira(p):
    with pytest.raises(TypeError):
        teste_lucas_lehmer(p)


@pytest.mark.parametrize("p", ["3", "abc", None, [], {}])
def test_entradas_invalidas(p):
    with pytest.raises((TypeError, ValueError)):
        teste_lucas_lehmer(p)
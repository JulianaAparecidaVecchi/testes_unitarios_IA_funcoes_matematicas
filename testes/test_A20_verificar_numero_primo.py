import pytest
from A20_verificar_numero_primo import verificar_numero_primo


@pytest.mark.parametrize("n", [
    -10, -5, -1, 0, 1
])
def test_numeros_menores_que_dois(n):
    assert verificar_numero_primo(n) is False


@pytest.mark.parametrize("n", [
    2, 3
])
def test_numeros_primos_menores_que_quatro(n):
    assert verificar_numero_primo(n) is True


@pytest.mark.parametrize("n", [
    4, 6, 8, 10, 12, 18, 20, 100
])
def test_numeros_pares_nao_primos(n):
    assert verificar_numero_primo(n) is False


@pytest.mark.parametrize("n", [
    9, 15, 21, 27, 33, 45, 99
])
def test_multiplos_de_tres_nao_primos(n):
    assert verificar_numero_primo(n) is False


@pytest.mark.parametrize("n", [
    5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 97
])
def test_numeros_primos_maiores_que_tres(n):
    assert verificar_numero_primo(n) is True


@pytest.mark.parametrize("n", [
    25, 35, 49, 55, 77, 91, 121, 143, 169, 221
])
def test_numeros_compostos_divisiveis_por_outros_fatores(n):
    assert verificar_numero_primo(n) is False


@pytest.mark.parametrize("n", [
    25, 49, 121, 169, 289, 361
])
def test_quadrados_perfeitos_nao_primos(n):
    assert verificar_numero_primo(n) is False


@pytest.mark.parametrize("n", [
    101, 103, 107, 109, 127, 131, 149, 997
])
def test_numeros_primos_maiores_com_diferentes_caminhos(n):
    assert verificar_numero_primo(n) is True


@pytest.mark.parametrize("n", [
    121, 143, 187, 209, 221, 247, 299, 323
])
def test_numeros_compostos_no_laco_while(n):
    assert verificar_numero_primo(n) is False


@pytest.mark.parametrize("n", [
    1001, 1027, 1147, 1517, 1729
])
def test_numeros_compostos_maiores(n):
    assert verificar_numero_primo(n) is False


@pytest.mark.parametrize("n", [
    2.5, 3.0, -1.5, 10.7, "7", "abc", None, [], {}, (5,)
])
def test_entradas_invalidas_geram_type_error(n):
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        verificar_numero_primo(n)


@pytest.mark.parametrize("n", [
    True, False
])
def test_booleanos_geram_type_error(n):
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        verificar_numero_primo(n)


def test_numero_primo_grande():
    assert verificar_numero_primo(104729) is True


def test_numero_composto_grande():
    assert verificar_numero_primo(104730) is False


def test_numero_primo_proximo_de_limite_de_quadrado():
    assert verificar_numero_primo(9973) is True


def test_numero_composto_proximo_de_limite_de_quadrado():
    assert verificar_numero_primo(9991) is False
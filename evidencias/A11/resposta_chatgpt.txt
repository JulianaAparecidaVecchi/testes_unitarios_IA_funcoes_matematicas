
import pytest

from A11_fatorar_em_primos import fatorar_em_primos


@pytest.mark.parametrize(
    "n, esperado",
    [
        (2, [2]),
        (3, [3]),
        (5, [5]),
        (7, [7]),
        (11, [11]),
        (13, [13]),
        (17, [17]),
        (97, [97]),
    ],
)
def test_numeros_primos(n, esperado):
    assert fatorar_em_primos(n) == esperado


@pytest.mark.parametrize(
    "n, esperado",
    [
        (4, [2, 2]),
        (6, [2, 3]),
        (9, [3, 3]),
        (10, [2, 5]),
        (12, [2, 2, 3]),
        (15, [3, 5]),
        (18, [2, 3, 3]),
        (30, [2, 3, 5]),
        (60, [2, 2, 3, 5]),
        (100, [2, 2, 5, 5]),
    ],
)
def test_numeros_compostos(n, esperado):
    assert fatorar_em_primos(n) == esperado


@pytest.mark.parametrize(
    "n, esperado",
    [
        (8, [2, 2, 2]),
        (16, [2, 2, 2, 2]),
        (32, [2, 2, 2, 2, 2]),
        (64, [2, 2, 2, 2, 2, 2]),
        (81, [3, 3, 3, 3]),
        (125, [5, 5, 5]),
        (625, [5, 5, 5, 5]),
    ],
)
def test_potencias_de_primos(n, esperado):
    assert fatorar_em_primos(n) == esperado


@pytest.mark.parametrize(
    "n, esperado",
    [
        (25, [5, 5]),
        (49, [7, 7]),
        (121, [11, 11]),
        (169, [13, 13]),
    ],
)
def test_quadrados_de_primos(n, esperado):
    assert fatorar_em_primos(n) == esperado


@pytest.mark.parametrize(
    "n, esperado",
    [
        (14, [2, 7]),
        (21, [3, 7]),
        (35, [5, 7]),
        (77, [7, 11]),
        (143, [11, 13]),
        (210, [2, 3, 5, 7]),
        (2310, [2, 3, 5, 7, 11]),
    ],
)
def test_fatores_primos_distintos(n, esperado):
    assert fatorar_em_primos(n) == esperado


def test_menor_entrada_valida():
    assert fatorar_em_primos(2) == [2]


def test_numero_primo_grande():
    assert fatorar_em_primos(997) == [997]


def test_numero_composto_grande():
    assert fatorar_em_primos(1000) == [2, 2, 2, 5, 5, 5]


def test_fatores_em_ordem_crescente():
    resultado = fatorar_em_primos(420)
    assert resultado == [2, 2, 3, 5, 7]
    assert resultado == sorted(resultado)


def test_repeticao_de_fatores():
    assert fatorar_em_primos(72) == [2, 2, 2, 3, 3]


@pytest.mark.parametrize("n", [0, 1, -1, -2, -10, -100])
def test_entradas_inferiores_a_dois(n):
    with pytest.raises(ValueError, match="n deve ser maior ou igual a 2"):
        fatorar_em_primos(n)


@pytest.mark.parametrize("n", [0.0, 1.0, -2.5])
def test_entradas_decimais_invalidas(n):
    with pytest.raises(ValueError, match="n deve ser maior ou igual a 2"):
        fatorar_em_primos(n)


def test_entrada_string_invalida():
    with pytest.raises(TypeError):
        fatorar_em_primos("10")


def test_entrada_none_invalida():
    with pytest.raises(TypeError):
        fatorar_em_primos(None)


def test_entrada_lista_invalida():
    with pytest.raises(TypeError):
        fatorar_em_primos([10])


def test_entrada_dicionario_invalida():
    with pytest.raises(TypeError):
        fatorar_em_primos({"n": 10})


@pytest.mark.parametrize("n", [2, 3, 4, 6, 12, 30, 100, 360, 997])
def test_produto_dos_fatores_igual_ao_numero_original(n):
    fatores = fatorar_em_primos(n)
    produto = 1

    for fator in fatores:
        produto *= fator

    assert produto == n


@pytest.mark.parametrize("n", [2, 3, 4, 9, 12, 25, 60, 97, 100])
def test_todos_os_fatores_sao_primos(n):
    fatores = fatorar_em_primos(n)

    for fator in fatores:
        assert fator >= 2
        assert all(fator % divisor != 0 for divisor in range(2, int(fator ** 0.5) + 1))


def test_resultado_e_lista():
    resultado = fatorar_em_primos(30)
    assert isinstance(resultado, list)


def test_chamadas_independentes():
    primeiro = fatorar_em_primos(12)
    segundo = fatorar_em_primos(30)

    assert primeiro == [2, 2, 3]
    assert segundo == [2, 3, 5]
    assert primeiro == [2, 2, 3]

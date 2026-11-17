
import pytest
import math

from A29_resolver_sistema_linear import resolver_sistema_linear


def test_sistema_linear_1x1():
    resultado = resolver_sistema_linear([[2]], [10])
    assert resultado == pytest.approx([5.0])


def test_sistema_linear_2x2():
    A = [[2, 1], [1, 3]]
    b = [5, 6]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([1.8, 1.4])


def test_sistema_linear_3x3():
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([2.0, 3.0, -1.0])


def test_sistema_com_pivoteamento_parcial():
    A = [
        [0, 2],
        [1, 1]
    ]
    b = [4, 3]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([1.0, 2.0])


def test_sistema_que_exige_troca_de_linhas():
    A = [
        [0, 1],
        [2, 3]
    ]
    b = [2, 8]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([1.0, 2.0])


def test_sistema_com_matriz_identidade():
    A = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    b = [4, 5, 6]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([4.0, 5.0, 6.0])


def test_sistema_com_solucoes_negativas():
    A = [
        [1, 0],
        [0, 1]
    ]
    b = [-3, -7]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([-3.0, -7.0])


def test_sistema_com_valores_float():
    A = [
        [0.5, 1.5],
        [2.5, 3.5]
    ]
    b = [4.5, 10.5]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([1.5, 2.5])


def test_sistema_com_valores_zero():
    A = [
        [1, 0],
        [0, 2]
    ]
    b = [0, 0]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([0.0, 0.0])


def test_sistema_com_tolerancia_personalizada():
    A = [
        [2, 1],
        [1, 2]
    ]
    b = [5, 4]

    resultado = resolver_sistema_linear(A, b, tolerancia=1e-10)

    assert resultado == pytest.approx([2.0, 1.0])


def test_sistema_com_tolerancia_pequena():
    A = [[1e-10]]
    b = [2e-10]

    resultado = resolver_sistema_linear(A, b, tolerancia=1e-15)

    assert resultado == pytest.approx([2.0])


def test_sistema_com_matriz_diagonal():
    A = [
        [2, 0, 0],
        [0, 3, 0],
        [0, 0, 4]
    ]
    b = [4, 9, 16]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([2.0, 3.0, 4.0])


def test_sistema_com_fator_de_eliminacao_zero():
    A = [
        [2, 1],
        [0, 3]
    ]
    b = [5, 6]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([1.5, 2.0])


def test_sistema_singular():
    A = [
        [1, 2],
        [2, 4]
    ]
    b = [3, 6]

    with pytest.raises(ValueError, match="sistema singular ou sem solução única"):
        resolver_sistema_linear(A, b)


def test_sistema_sem_solucao_unica():
    A = [
        [1, 2],
        [2, 4]
    ]
    b = [3, 7]

    with pytest.raises(ValueError, match="sistema singular ou sem solução única"):
        resolver_sistema_linear(A, b)


def test_sistema_com_linha_nula():
    A = [
        [1, 2],
        [0, 0]
    ]
    b = [3, 0]

    with pytest.raises(ValueError, match="sistema singular ou sem solução única"):
        resolver_sistema_linear(A, b)


def test_sistema_vazio():
    with pytest.raises(ValueError, match="sistema vazio"):
        resolver_sistema_linear([], [])


def test_vetor_b_com_tamanho_diferente():
    A = [
        [1, 2],
        [3, 4]
    ]
    b = [5]

    with pytest.raises(ValueError, match="b deve ter o mesmo tamanho que A"):
        resolver_sistema_linear(A, b)


def test_matriz_nao_quadrada():
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    b = [7, 8]

    with pytest.raises(ValueError, match="A deve ser quadrada"):
        resolver_sistema_linear(A, b)


def test_matriz_com_linha_de_tamanho_incorreto():
    A = [
        [1, 2],
        [3]
    ]
    b = [4, 5]

    with pytest.raises(ValueError, match="A deve ser quadrada"):
        resolver_sistema_linear(A, b)


@pytest.mark.parametrize("tolerancia", [0, -1, -0.5, -1e-10])
def test_tolerancia_invalida(tolerancia):
    with pytest.raises(ValueError, match="tolerância deve ser positiva"):
        resolver_sistema_linear([[1]], [1], tolerancia=tolerancia)


@pytest.mark.parametrize("valor", [math.inf, -math.inf, math.nan])
def test_matriz_com_valores_nao_finitos(valor):
    with pytest.raises(ValueError, match="A contém valores não finitos"):
        resolver_sistema_linear([[valor]], [1])


@pytest.mark.parametrize("valor", [math.inf, -math.inf, math.nan])
def test_vetor_b_com_valores_nao_finitos(valor):
    with pytest.raises(ValueError, match="b contém valores não finitos"):
        resolver_sistema_linear([[1]], [valor])


def test_pivo_abaixo_da_tolerancia():
    A = [[1e-13]]
    b = [1]

    with pytest.raises(ValueError, match="sistema singular ou sem solução única"):
        resolver_sistema_linear(A, b, tolerancia=1e-12)


def test_pivo_igual_a_tolerancia():
    A = [[1e-12]]
    b = [1]

    resultado = resolver_sistema_linear(A, b, tolerancia=1e-12)

    assert resultado == pytest.approx([1e12])


def test_pivo_acima_da_tolerancia():
    A = [[2e-12]]
    b = [4e-12]

    resultado = resolver_sistema_linear(A, b, tolerancia=1e-12)

    assert resultado == pytest.approx([2.0])


def test_matriz_com_valores_inteiros():
    A = [
        [3, 2],
        [1, 2]
    ]
    b = [12, 8]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([2.0, 3.0])


def test_sistema_com_pivo_negativo():
    A = [
        [-2, 1],
        [1, 3]
    ]
    b = [-3, 7]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([2.0, 1.0])


def test_sistema_com_tres_variaveis_e_troca_de_linhas():
    A = [
        [0, 2, 1],
        [1, -2, -3],
        [2, 3, 1]
    ]
    b = [3, -6, 7]

    resultado = resolver_sistema_linear(A, b)

    assert resultado == pytest.approx([1.0, 1.0, 1.0])


def test_retorna_lista_de_floats():
    resultado = resolver_sistema_linear([[2]], [4])

    assert isinstance(resultado, list)
    assert all(isinstance(valor, float) for valor in resultado)


def test_nao_altera_matriz_original():
    A = [
        [2, 1],
        [1, 3]
    ]
    b = [5, 6]

    matriz_original = [linha[:] for linha in A]
    vetor_original = b[:]

    resolver_sistema_linear(A, b)

    assert A == matriz_original
    assert b == vetor_original

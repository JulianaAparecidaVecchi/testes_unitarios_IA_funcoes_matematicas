import pytest
from artefatos.A03_calcular_area_triangulo import calcular_area_triangulo


# Cenários de execução normal
def test_triangulo_equilatero():
    resultado = calcular_area_triangulo(2, 2, 2)
    assert resultado == pytest.approx(1.7320508076)


def test_triangulo_retangulo():
    resultado = calcular_area_triangulo(3, 4, 5)
    assert resultado == pytest.approx(6.0)


def test_triangulo_escaleno():
    resultado = calcular_area_triangulo(5, 6, 7)
    assert resultado == pytest.approx(14.6969384567)


def test_triangulo_com_lados_decimais():
    resultado = calcular_area_triangulo(2.5, 3.5, 4.0)
    assert resultado == pytest.approx(4.367717)


# Diferentes ordens dos lados
def test_lados_em_ordem_crescente():
    assert calcular_area_triangulo(3, 4, 5) == pytest.approx(6.0)


def test_lados_em_ordem_decrescente():
    assert calcular_area_triangulo(5, 4, 3) == pytest.approx(6.0)


def test_lados_em_ordem_aleatoria():
    assert calcular_area_triangulo(4, 3, 5) == pytest.approx(6.0)


# Casos extremos
def test_triangulo_com_lados_iguais_a_um():
    assert calcular_area_triangulo(1, 1, 1) == pytest.approx(
        0.4330127019
    )


def test_triangulo_com_lados_muito_grandes():
    resultado = calcular_area_triangulo(100000, 100000, 100000)
    assert resultado == pytest.approx(4330127015.621)


def test_triangulo_com_lados_muito_pequenos():
    resultado = calcular_area_triangulo(0.001, 0.001, 0.001)
    assert resultado == pytest.approx(4.330127e-7)


def test_triangulo_quase_degenerado():
    resultado = calcular_area_triangulo(2, 3, 4.999)
    assert resultado > 0


# Entradas inválidas: lados iguais a zero
@pytest.mark.parametrize(
    "a, b, c",
    [
        (0, 3, 4),
        (3, 0, 4),
        (3, 4, 0),
        (0, 0, 0),
    ],
)
def test_lados_iguais_a_zero(a, b, c):
    with pytest.raises(ValueError, match="lados não formam um triângulo"):
        calcular_area_triangulo(a, b, c)


# Entradas inválidas: lados negativos
@pytest.mark.parametrize(
    "a, b, c",
    [
        (-1, 3, 4),
        (3, -1, 4),
        (3, 4, -1),
        (-1, -2, -3),
    ],
)
def test_lados_negativos(a, b, c):
    with pytest.raises(ValueError, match="lados não formam um triângulo"):
        calcular_area_triangulo(a, b, c)


# Entradas inválidas: desigualdade triangular
@pytest.mark.parametrize(
    "a, b, c",
    [
        (1, 2, 3),
        (2, 3, 5),
        (1, 1, 3),
        (1, 5, 2),
        (10, 2, 3),
    ],
)
def test_lados_que_nao_formam_triangulo(a, b, c):
    with pytest.raises(ValueError, match="lados não formam um triângulo"):
        calcular_area_triangulo(a, b, c)


# Verificação de simetria: a ordem dos lados não altera a área
def test_permutacoes_dos_lados_produzem_mesma_area():
    resultado1 = calcular_area_triangulo(3, 4, 5)
    resultado2 = calcular_area_triangulo(4, 5, 3)
    resultado3 = calcular_area_triangulo(5, 3, 4)

    assert resultado1 == pytest.approx(resultado2)
    assert resultado2 == pytest.approx(resultado3)


# Verificação de mensagem de erro
def test_mensagem_erro_para_triangulo_invalido():
    with pytest.raises(ValueError) as erro:
        calcular_area_triangulo(1, 2, 3)

    assert str(erro.value) == "lados não formam um triângulo"

import pytest

from A06_calcular_raizes_quadraticas import calcular_raizes_quadraticas


def test_duas_raizes_reais_distintas():
    assert calcular_raizes_quadraticas(1, -5, 6) == (2.0, 3.0)


def test_duas_raizes_reais_negativas():
    assert calcular_raizes_quadraticas(1, 5, 6) == (-3.0, -2.0)


def test_duas_raizes_com_coeficiente_a_negativo():
    assert calcular_raizes_quadraticas(-1, 0, 4) == (-2.0, 2.0)


def test_delta_igual_a_zero():
    assert calcular_raizes_quadraticas(1, -2, 1) == (1.0,)


def test_delta_zero_com_raiz_negativa():
    assert calcular_raizes_quadraticas(1, 4, 4) == (-2.0,)


def test_delta_negativo():
    assert calcular_raizes_quadraticas(1, 0, 1) == ()


def test_delta_negativo_com_coeficientes_diferentes():
    assert calcular_raizes_quadraticas(2, 1, 3) == ()


def test_coeficiente_a_igual_a_zero():
    with pytest.raises(ValueError, match="a não pode ser zero"):
        calcular_raizes_quadraticas(0, 2, 1)


def test_todos_coeficientes_zero():
    with pytest.raises(ValueError, match="a não pode ser zero"):
        calcular_raizes_quadraticas(0, 0, 0)


def test_coeficiente_b_igual_a_zero():
    assert calcular_raizes_quadraticas(1, 0, -9) == (-3.0, 3.0)


def test_coeficiente_c_igual_a_zero():
    assert calcular_raizes_quadraticas(1, -4, 0) == (0.0, 4.0)


def test_coeficientes_b_e_c_iguais_a_zero():
    assert calcular_raizes_quadraticas(2, 0, 0) == (0.0,)


def test_raizes_fracionarias():
    assert calcular_raizes_quadraticas(2, -3, 1) == (0.5, 1.0)


def test_raizes_irracionais():
    resultado = calcular_raizes_quadraticas(1, 0, -2)

    assert resultado == pytest.approx(
        (-2**0.5, 2**0.5)
    )


def test_coeficientes_grandes():
    assert calcular_raizes_quadraticas(
        1000000, -5000000, 6000000
    ) == (2.0, 3.0)


def test_coeficientes_decimais():
    assert calcular_raizes_quadraticas(
        0.5, -1.5, 1.0
    ) == (1.0, 2.0)


def test_raizes_retornadas_em_ordem_crescente():
    resultado = calcular_raizes_quadraticas(1, -5, 6)

    assert resultado[0] < resultado[1]


def test_retorno_e_uma_tupla():
    resultado = calcular_raizes_quadraticas(1, -5, 6)

    assert isinstance(resultado, tuple)


@pytest.mark.parametrize(
    "a, b, c, esperado",
    [
        (1, -3, 2, (1.0, 2.0)),
        (1, 2, 1, (-1.0,)),
        (1, 0, 1, ()),
        (1, 0, -1, (-1.0, 1.0)),
        (2, -4, 2, (1.0,)),
        (1, -1, 0, (0.0, 1.0)),
    ],
)
def test_diferentes_equacoes_quadraticas(a, b, c, esperado):
    assert calcular_raizes_quadraticas(a, b, c) == esperado


@pytest.mark.parametrize(
    "a, b, c",
    [
        (0, 1, 1),
        (0, 0, 1),
        (0, 1, 0),
        (0, 0, 0),
    ],
)
def test_coeficiente_a_invalido(a, b, c):
    with pytest.raises(ValueError, match="a não pode ser zero"):
        calcular_raizes_quadraticas(a, b, c)


@pytest.mark.parametrize(
    "a, b, c",
    [
        ("a", 2, 1),
        (1, "b", 1),
        (1, 2, "c"),
        (None, 2, 1),
        (1, None, 1),
        (1, 2, None),
    ],
)
def test_entradas_com_tipos_invalidos(a, b, c):
    with pytest.raises(TypeError):
        calcular_raizes_quadraticas(a, b, c)

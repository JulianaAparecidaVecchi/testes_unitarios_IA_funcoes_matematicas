
import pytest
import math

from A18_calcular_media_geometrica import calcular_media_geometrica


def test_media_geometrica_dois_valores():
    assert calcular_media_geometrica([2, 8]) == pytest.approx(4.0)


def test_media_geometrica_varios_valores():
    assert calcular_media_geometrica([2, 4, 8]) == pytest.approx(4.0)


def test_media_geometrica_lista_com_um_valor():
    assert calcular_media_geometrica([5]) == pytest.approx(5.0)


def test_media_geometrica_valores_iguais():
    assert calcular_media_geometrica([3, 3, 3]) == pytest.approx(3.0)


def test_media_geometrica_com_zero():
    assert calcular_media_geometrica([2, 0, 8]) == 0.0


def test_media_geometrica_zero_no_inicio():
    assert calcular_media_geometrica([0, 5, 10]) == 0.0


def test_media_geometrica_zero_no_final():
    assert calcular_media_geometrica([5, 10, 0]) == 0.0


def test_media_geometrica_valores_decimais():
    assert calcular_media_geometrica([1.5, 6.0]) == pytest.approx(3.0)


def test_media_geometrica_valores_inteiros():
    assert calcular_media_geometrica([1, 4, 16]) == pytest.approx(4.0)


def test_media_geometrica_lista_vazia():
    with pytest.raises(ValueError, match="lista vazia"):
        calcular_media_geometrica([])


def test_media_geometrica_none():
    with pytest.raises(ValueError, match="lista vazia"):
        calcular_media_geometrica(None)


def test_media_geometrica_valor_negativo():
    with pytest.raises(ValueError, match="valores não podem ser negativos"):
        calcular_media_geometrica([-2, 4])


def test_media_geometrica_todos_valores_negativos():
    with pytest.raises(ValueError, match="valores não podem ser negativos"):
        calcular_media_geometrica([-1, -5, -10])


def test_media_geometrica_string():
    with pytest.raises(TypeError, match="valores devem ser numéricos"):
        calcular_media_geometrica([2, "4", 8])


def test_media_geometrica_lista_com_booleano():
    assert calcular_media_geometrica([True, 4]) == pytest.approx(2.0)


def test_media_geometrica_valor_none_na_lista():
    with pytest.raises(TypeError, match="valores devem ser numéricos"):
        calcular_media_geometrica([2, None, 4])


def test_media_geometrica_valor_complexo():
    with pytest.raises(TypeError, match="valores devem ser numéricos"):
        calcular_media_geometrica([2, 3 + 4j])


def test_media_geometrica_valor_infinito():
    assert math.isinf(calcular_media_geometrica([float("inf"), 2]))


def test_media_geometrica_nan():
    assert math.isnan(calcular_media_geometrica([float("nan"), 2]))


def test_media_geometrica_valores_muito_pequenos():
    resultado = calcular_media_geometrica([1e-100, 1e-100])
    assert resultado == pytest.approx(1e-100)


def test_media_geometrica_valores_muito_grandes():
    resultado = calcular_media_geometrica([1e100, 1e100])
    assert resultado == pytest.approx(1e100)


def test_media_geometrica_valor_zero_com_negativo():
    with pytest.raises(ValueError, match="valores não podem ser negativos"):
        calcular_media_geometrica([0, -2])


def test_media_geometrica_valor_zero_com_string():
    with pytest.raises(TypeError, match="valores devem ser numéricos"):
        calcular_media_geometrica([0, "5"])

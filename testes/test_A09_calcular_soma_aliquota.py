import pytest

from A09_calcular_soma_aliquota import calcular_soma_aliquota


def test_soma_valores_com_aliquota_positiva():
    assert calcular_soma_aliquota([100, 200, 300], 0.10) == 660.0


def test_soma_valores_com_aliquota_zero():
    assert calcular_soma_aliquota([100, 200, 300], 0) == 600.0


def test_soma_valores_com_aliquota_negativa():
    with pytest.raises(ValueError, match="alíquota não pode ser negativa"):
        calcular_soma_aliquota([100, 200], -0.10)


def test_valores_vazios():
    assert calcular_soma_aliquota([], 0.10) == 0.0


def test_valores_com_soma_zero():
    assert calcular_soma_aliquota([0, 0, 0], 0.10) == 0.0


def test_valor_individual():
    assert calcular_soma_aliquota([100], 0.10) == 110.0


def test_valor_zero():
    assert calcular_soma_aliquota([0], 0.10) == 0.0


def test_valores_com_numeros_decimais():
    assert calcular_soma_aliquota([10.50, 20.25, 30.75], 0.10) == 67.65


def test_arredondamento_para_duas_casas_decimais():
    assert calcular_soma_aliquota([10.123], 0.10) == 11.14


def test_valor_negativo_na_lista():
    with pytest.raises(ValueError, match="valores não podem ser negativos"):
        calcular_soma_aliquota([100, -50, 200], 0.10)


def test_primeiro_valor_negativo():
    with pytest.raises(ValueError, match="valores não podem ser negativos"):
        calcular_soma_aliquota([-10, 20, 30], 0.10)


def test_ultimo_valor_negativo():
    with pytest.raises(ValueError, match="valores não podem ser negativos"):
        calcular_soma_aliquota([10, 20, -30], 0.10)


def test_aliquota_zero_com_lista_vazia():
    assert calcular_soma_aliquota([], 0) == 0.0


def test_aliquota_alta():
    assert calcular_soma_aliquota([100], 1.0) == 200.0


def test_aliquota_muito_pequena():
    assert calcular_soma_aliquota([100], 0.001) == 100.1


def test_valores_grandes():
    assert calcular_soma_aliquota([1000000, 2000000], 0.10) == 3300000.0


def test_aliquota_negativa_com_lista_vazia():
    with pytest.raises(ValueError, match="alíquota não pode ser negativa"):
        calcular_soma_aliquota([], -0.01)


def test_aliquota_negativa_e_valor_negativo():
    with pytest.raises(ValueError, match="alíquota não pode ser negativa"):
        calcular_soma_aliquota([-10], -0.10)
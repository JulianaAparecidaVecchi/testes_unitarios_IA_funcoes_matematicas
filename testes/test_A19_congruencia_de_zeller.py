
import pytest

from A19_congruencia_de_zeller import congruencia_de_zeller


# Testes de datas normais
def test_data_conhecida_segunda_feira():
    assert congruencia_de_zeller(17, 11, 2025) == "segunda"


def test_data_conhecida_sabado():
    assert congruencia_de_zeller(1, 1, 2022) == "sábado"


def test_data_conhecida_domingo():
    assert congruencia_de_zeller(1, 1, 2023) == "domingo"


def test_data_conhecida_terca_feira():
    assert congruencia_de_zeller(1, 8, 2023) == "terça"


def test_data_conhecida_quarta_feira():
    assert congruencia_de_zeller(1, 2, 2023) == "quarta"


def test_data_conhecida_quinta_feira():
    assert congruencia_de_zeller(1, 6, 2023) == "quinta"


def test_data_conhecida_sexta_feira():
    assert congruencia_de_zeller(1, 9, 2023) == "sexta"


# Testes de anos bissextos
def test_fevereiro_ano_bissexto():
    assert congruencia_de_zeller(29, 2, 2024) == "quinta"


def test_fevereiro_ano_nao_bissexto():
    assert congruencia_de_zeller(28, 2, 2023) == "terça"


def test_ano_bissexto_divisivel_por_400():
    assert congruencia_de_zeller(29, 2, 2000) == "terça"


def test_ano_secular_nao_bissexto():
    with pytest.raises(ValueError, match="dia inválido"):
        congruencia_de_zeller(29, 2, 1900)


# Testes dos meses
@pytest.mark.parametrize("mes,dia", [
    (1, 31),
    (3, 31),
    (5, 31),
    (7, 31),
    (8, 31),
    (10, 31),
    (12, 31),
    (4, 30),
    (6, 30),
    (9, 30),
    (11, 30),
])
def test_ultimo_dia_valido_de_cada_mes(mes, dia):
    resultado = congruencia_de_zeller(dia, mes, 2024)
    assert resultado in [
        "sábado", "domingo", "segunda", "terça",
        "quarta", "quinta", "sexta"
    ]


# Testes de limites dos dias
def test_primeiro_dia_do_mes():
    assert congruencia_de_zeller(1, 1, 2024) == "segunda"


def test_ultimo_dia_de_fevereiro_bissexto():
    assert congruencia_de_zeller(29, 2, 2024) == "quinta"


def test_dia_zero():
    with pytest.raises(ValueError, match="dia inválido"):
        congruencia_de_zeller(0, 5, 2024)


def test_dia_negativo():
    with pytest.raises(ValueError, match="dia inválido"):
        congruencia_de_zeller(-1, 5, 2024)


def test_dia_acima_do_maximo():
    with pytest.raises(ValueError, match="dia inválido"):
        congruencia_de_zeller(32, 1, 2024)


def test_dia_31_em_mes_de_30_dias():
    with pytest.raises(ValueError, match="dia inválido"):
        congruencia_de_zeller(31, 4, 2024)


def test_dia_29_em_fevereiro_nao_bissexto():
    with pytest.raises(ValueError, match="dia inválido"):
        congruencia_de_zeller(29, 2, 2023)


# Testes de limites dos meses
def test_mes_zero():
    with pytest.raises(ValueError, match="mês inválido"):
        congruencia_de_zeller(10, 0, 2024)


def test_mes_negativo():
    with pytest.raises(ValueError, match="mês inválido"):
        congruencia_de_zeller(10, -1, 2024)


def test_mes_acima_de_12():
    with pytest.raises(ValueError, match="mês inválido"):
        congruencia_de_zeller(10, 13, 2024)


# Testes de transição de ano
def test_janeiro():
    assert congruencia_de_zeller(1, 1, 2024) == "segunda"


def test_fevereiro():
    assert congruencia_de_zeller(1, 2, 2024) == "quinta"


def test_marco():
    assert congruencia_de_zeller(1, 3, 2024) == "sexta"


# Testes de anos extremos
def test_ano_2000():
    assert congruencia_de_zeller(1, 1, 2000) == "sábado"


def test_ano_1900():
    assert congruencia_de_zeller(1, 1, 1900) == "segunda"


def test_ano_antes_de_1000():
    assert congruencia_de_zeller(1, 1, 500) == "sexta"


def test_ano_zero():
    resultado = congruencia_de_zeller(1, 1, 0)
    assert resultado in [
        "sábado", "domingo", "segunda", "terça",
        "quarta", "quinta", "sexta"
    ]
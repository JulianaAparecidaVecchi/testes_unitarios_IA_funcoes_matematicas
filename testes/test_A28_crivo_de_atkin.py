
import pytest

from A28_crivo_de_atkin import crivo_de_atkin


def test_limite_menor_que_dois():
    assert crivo_de_atkin(-10) == []
    assert crivo_de_atkin(-1) == []
    assert crivo_de_atkin(0) == []
    assert crivo_de_atkin(1) == []


def test_limite_igual_dois():
    assert crivo_de_atkin(2) == [2]


def test_limite_igual_tres():
    assert crivo_de_atkin(3) == [2, 3]


def test_limite_igual_quatro():
    assert crivo_de_atkin(4) == [2, 3]


def test_limite_igual_cinco():
    assert crivo_de_atkin(5) == [2, 3, 5]


def test_limite_igual_dez():
    assert crivo_de_atkin(10) == [2, 3, 5, 7]


def test_limite_igual_vinte():
    assert crivo_de_atkin(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_limite_igual_cem():
    assert crivo_de_atkin(100) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97
    ]


def test_limite_igual_ao_quadrado_de_primo():
    assert crivo_de_atkin(25) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23
    ]


def test_limite_com_multiplos_de_quadrados_perfeitos():
    resultado = crivo_de_atkin(100)
    assert 25 not in resultado
    assert 49 not in resultado
    assert 4 not in resultado
    assert 9 not in resultado
    assert 2 in resultado
    assert 3 in resultado
    assert 5 in resultado
    assert 7 in resultado


def test_resultado_em_ordem_crescente():
    resultado = crivo_de_atkin(200)
    assert resultado == sorted(resultado)


def test_todos_os_elementos_sao_primos():
    resultado = crivo_de_atkin(1000)

    for numero in resultado:
        assert numero >= 2
        assert all(
            numero % divisor != 0
            for divisor in range(2, int(numero ** 0.5) + 1)
        )


def test_quantidade_de_primos_ate_cem():
    assert len(crivo_de_atkin(100)) == 25


def test_quantidade_de_primos_ate_mil():
    assert len(crivo_de_atkin(1000)) == 168


def test_limite_maximo_permitido():
    resultado = crivo_de_atkin(10 ** 7)

    assert resultado[0] == 2
    assert resultado[1] == 3
    assert resultado[-1] == 9999991
    assert resultado == sorted(resultado)


@pytest.mark.parametrize("limite", [
    10 ** 7 + 1,
    10 ** 8,
    10 ** 10
])
def test_limite_maior_que_maximo_gera_value_error(limite):
    with pytest.raises(ValueError, match="limite grande demais"):
        crivo_de_atkin(limite)


@pytest.mark.parametrize("limite", [
    1.5,
    2.0,
    10.5,
    "10",
    "100",
    None,
    [],
    {},
    True,
    False
])
def test_entrada_nao_inteira_gera_type_error(limite):
    with pytest.raises(TypeError, match="limite deve ser inteiro"):
        crivo_de_atkin(limite)


def test_limite_como_inteiro_negativo():
    assert crivo_de_atkin(-100) == []


def test_limite_como_inteiro_muito_grande_negativo():
    assert crivo_de_atkin(-(10 ** 8)) == []


def test_limite_com_um_unico_primo():
    assert crivo_de_atkin(7) == [2, 3, 5, 7]


def test_limite_sem_novos_primos():
    assert crivo_de_atkin(8) == [2, 3, 5, 7]
    assert crivo_de_atkin(9) == [2, 3, 5, 7]

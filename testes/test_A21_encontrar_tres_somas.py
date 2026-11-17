import pytest
from A21_encontrar_tres_somas import encontrar_tres_somas


def test_encontrar_tres_somas_lista_com_tripla_valida():
    assert encontrar_tres_somas([-1, 0, 1, 2, -2, -4]) == [
        (-2, 0, 2),
        (-1, 0, 1)
    ]


def test_encontrar_tres_somas_alvo_padrao_zero():
    assert encontrar_tres_somas([-1, 0, 1]) == [(-1, 0, 1)]


def test_encontrar_tres_somas_alvo_personalizado():
    assert encontrar_tres_somas([1, 2, 3, 4, 5], alvo=9) == [
        (1, 3, 5),
        (2, 3, 4)
    ]


def test_encontrar_tres_somas_lista_vazia():
    assert encontrar_tres_somas([]) == []


def test_encontrar_tres_somas_lista_com_menos_de_tres_elementos():
    assert encontrar_tres_somas([1, 2]) == []


def test_encontrar_tres_somas_lista_com_exatamente_tres_elementos():
    assert encontrar_tres_somas([-1, 0, 1]) == [(-1, 0, 1)]


def test_encontrar_tres_somas_sem_combinacoes_validas():
    assert encontrar_tres_somas([1, 2, 3, 4, 5]) == []


def test_encontrar_tres_somas_com_numeros_duplicados():
    assert encontrar_tres_somas([-1, -1, 0, 1, 1]) == [
        (-1, 0, 1)
    ]


def test_encontrar_tres_somas_sem_triplas_duplicadas():
    assert encontrar_tres_somas([0, 0, 0, 0, 0]) == [
        (0, 0, 0)
    ]


def test_encontrar_tres_somas_com_todas_as_combinacoes():
    assert encontrar_tres_somas([-2, -1, 0, 1, 2, 3], alvo=0) == [
        (-2, -1, 3),
        (-2, 0, 2),
        (-1, 0, 1)
    ]


def test_encontrar_tres_somas_lista_desordenada():
    assert encontrar_tres_somas([3, -1, 0, 2, -2, 1]) == [
        (-2, -1, 3),
        (-2, 0, 2),
        (-1, 0, 1)
    ]


def test_encontrar_tres_somas_com_numeros_negativos():
    assert encontrar_tres_somas([-5, -4, -3, -2, -1], alvo=-9) == [
        (-5, -3, -1),
        (-5, -2, -2)
    ]


def test_encontrar_tres_somas_com_numeros_positivos():
    assert encontrar_tres_somas([1, 2, 3, 4, 5, 6], alvo=12) == [
        (1, 5, 6),
        (2, 4, 6),
        (3, 4, 5)
    ]


def test_encontrar_tres_somas_com_alvo_negativo():
    assert encontrar_tres_somas([-5, -3, -1, 0, 2], alvo=-8) == [
        (-5, -3, 0)
    ]


def test_encontrar_tres_somas_com_alvo_positivo():
    assert encontrar_tres_somas([1, 2, 3, 4, 5], alvo=6) == [
        (1, 2, 3)
    ]


def test_encontrar_tres_somas_com_numeros_grandes():
    assert encontrar_tres_somas(
        [-1000000, 0, 1000000, 2000000, -2000000]
    ) == [
        (-2000000, 0, 2000000),
        (-1000000, 0, 1000000)
    ]


def test_encontrar_tres_somas_com_lista_de_tamanho_grande():
    numeros = list(range(-100, 101))
    resultado = encontrar_tres_somas(numeros)

    assert resultado
    assert len(resultado) == len(set(resultado))
    assert all(sum(tripla) == 0 for tripla in resultado)


def test_encontrar_tres_somas_com_float():
    assert encontrar_tres_somas([-1.5, 0.5, 1.0], alvo=0) == [
        (-1.5, 0.5, 1.0)
    ]


def test_encontrar_tres_somas_com_todos_os_numeros_iguais():
    assert encontrar_tres_somas([2, 2, 2, 2, 2], alvo=6) == [
        (2, 2, 2)
    ]


def test_encontrar_tres_somas_com_alvo_impossivel():
    assert encontrar_tres_somas([1, 2, 3, 4, 5], alvo=100) == []


def test_encontrar_tres_somas_com_lista_de_tuplas_duplicadas():
    numeros = [0, -1, 1, -1, 0, 1, 0]

    resultado = encontrar_tres_somas(numeros)

    assert resultado == [(-1, 0, 1)]


def test_encontrar_tres_somas_nao_modifica_lista_original():
    numeros = [3, -1, 0, 2, -2, 1]
    copia = numeros.copy()

    encontrar_tres_somas(numeros)

    assert numeros == copia


def test_encontrar_tres_somas_com_lista_de_tres_zeros():
    assert encontrar_tres_somas([0, 0, 0]) == [
        (0, 0, 0)
    ]


def test_encontrar_tres_somas_com_dois_numeros_iguais_na_triple():
    assert encontrar_tres_somas([-2, 1, 1], alvo=0) == [
        (-2, 1, 1)
    ]


def test_encontrar_tres_somas_com_entrada_invalida_string():
    with pytest.raises(TypeError):
        encontrar_tres_somas(None)


def test_encontrar_tres_somas_com_alvo_invalido():
    with pytest.raises(TypeError):
        encontrar_tres_somas([1, 2, 3], alvo=None)
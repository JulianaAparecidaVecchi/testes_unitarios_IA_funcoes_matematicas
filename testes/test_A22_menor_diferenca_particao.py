import pytest

from artefatos.A22_menor_diferenca_particao import menor_diferenca_particao


def test_lista_vazia():
    assert menor_diferenca_particao([]) == 0


def test_tupla_vazia():
    assert menor_diferenca_particao(()) == 0


def test_lista_com_um_elemento():
    assert menor_diferenca_particao([5]) == 5


def test_tupla_com_um_elemento():
    assert menor_diferenca_particao((10,)) == 10


def test_dois_elementos_iguais():
    assert menor_diferenca_particao([5, 5]) == 0


def test_dois_elementos_diferentes():
    assert menor_diferenca_particao([3, 8]) == 5


def test_particao_com_diferenca_zero():
    assert menor_diferenca_particao([1, 2, 3]) == 0


def test_particao_com_diferenca_minima():
    assert menor_diferenca_particao([1, 2, 4]) == 1


def test_lista_com_elementos_iguais():
    assert menor_diferenca_particao([4, 4, 4, 4]) == 0


def test_lista_com_zeros():
    assert menor_diferenca_particao([0, 0, 0]) == 0


def test_lista_com_zeros_e_outros_valores():
    assert menor_diferenca_particao([0, 0, 5, 5]) == 0


def test_lista_com_um_zero():
    assert menor_diferenca_particao([0, 7]) == 7


def test_lista_com_valores_grandes():
    assert menor_diferenca_particao([1000, 2000, 3000]) == 0


def test_lista_com_valores_desbalanceados():
    assert menor_diferenca_particao([1, 1, 1, 10]) == 7


def test_tupla_com_multiplos_elementos():
    assert menor_diferenca_particao((2, 3, 7, 8, 10)) == 0


def test_lista_com_um_elemento_negativo():
    with pytest.raises(ValueError, match="números não podem ser negativos"):
        menor_diferenca_particao([1, -2, 3])


def test_lista_com_elementos_negativos():
    with pytest.raises(ValueError, match="números não podem ser negativos"):
        menor_diferenca_particao([-1, -2, -3])


def test_tipo_string_invalido():
    with pytest.raises(TypeError, match="numeros deve ser lista ou tupla"):
        menor_diferenca_particao("123")


def test_tipo_inteiro_invalido():
    with pytest.raises(TypeError, match="numeros deve ser lista ou tupla"):
        menor_diferenca_particao(10)


def test_tipo_float_invalido():
    with pytest.raises(TypeError, match="numeros deve ser lista ou tupla"):
        menor_diferenca_particao(10.5)


def test_tipo_none_invalido():
    with pytest.raises(TypeError, match="numeros deve ser lista ou tupla"):
        menor_diferenca_particao(None)


def test_dicionario_invalido():
    with pytest.raises(TypeError, match="numeros deve ser lista ou tupla"):
        menor_diferenca_particao({1: 2, 3: 4})


def test_conjunto_invalido():
    with pytest.raises(TypeError, match="numeros deve ser lista ou tupla"):
        menor_diferenca_particao({1, 2, 3})


def test_lista_com_string():
    with pytest.raises(TypeError):
        menor_diferenca_particao([1, "2", 3])


def test_lista_com_none():
    with pytest.raises(TypeError):
        menor_diferenca_particao([1, None, 3])


def test_lista_com_elementos_float():
    assert menor_diferenca_particao([1.5, 2.5]) == 0.0


def test_lista_com_booleanos():
    assert menor_diferenca_particao([True, False]) == 1


@pytest.mark.parametrize(
    "numeros, esperado",
    [
        ([1, 2], 1),
        ([1, 2, 3], 0),
        ([1, 2, 3, 4], 0),
        ([1, 2, 3, 4, 5], 1),
        ([2, 4, 6, 8], 0),
        ([3, 7, 9], 1),
        ([10, 20, 30, 40], 0),
        ([1, 100], 99),
        ([0, 0, 0, 0], 0),
        ([9, 9, 9], 9),
    ],
)
def test_varios_cenarios_de_particionamento(numeros, esperado):
    assert menor_diferenca_particao(numeros) == esperado


def test_lista_original_nao_e_modificada():
    numeros = [1, 2, 3, 4]
    original = numeros.copy()

    menor_diferenca_particao(numeros)

    assert numeros == original


def test_tupla_original_permanece_inalterada():
    numeros = (1, 2, 3, 4)
    original = numeros

    menor_diferenca_particao(numeros)

    assert numeros == original


def test_lista_com_elementos_repetidos():
    assert menor_diferenca_particao([2, 2, 2, 3, 3]) == 0


def test_lista_com_um_unico_valor_zero():
    assert menor_diferenca_particao([0]) == 0


def test_lista_com_valores_que_formam_particoes_distintas():
    assert menor_diferenca_particao([8, 6, 5, 5]) == 2

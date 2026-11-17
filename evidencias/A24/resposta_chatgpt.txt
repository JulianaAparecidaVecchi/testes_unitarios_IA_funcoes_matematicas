
import pytest

from A24_crivo_segmentado import crivo_segmentado


@pytest.mark.parametrize(
    "baixo, alto, esperado",
    [
        (2, 10, [2, 3, 5, 7]),
        (10, 30, [11, 13, 17, 19, 23, 29]),
        (20, 50, [23, 29, 31, 37, 41, 43, 47]),
        (100, 120, [101, 103, 107, 109, 113]),
        (2, 2, [2]),
        (3, 3, [3]),
        (4, 4, []),
        (0, 1, []),
        (0, 2, [2]),
        (1, 10, [2, 3, 5, 7]),
        (-10, 10, [2, 3, 5, 7]),
        (-10, -1, []),
        (-5, 1, []),
        (0, 0, []),
        (1, 1, []),
        (14, 16, []),
        (17, 17, [17]),
        (18, 18, []),
        (24, 28, []),
        (29, 29, [29]),
        (49, 49, []),
        (97, 97, [97]),
        (100, 100, []),
    ],
)
def test_crivo_segmentado_intervalos(baixo, alto, esperado):
    assert crivo_segmentado(baixo, alto) == esperado


def test_crivo_segmentado_intervalo_grande():
    resultado = crivo_segmentado(1, 100)

    assert resultado == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97,
    ]


def test_crivo_segmentado_intervalo_sem_primos():
    assert crivo_segmentado(90, 96) == []


def test_crivo_segmentado_primos_consecutivos():
    assert crivo_segmentado(2, 3) == [2, 3]


def test_crivo_segmentado_limite_quadrado_perfeito():
    assert crivo_segmentado(45, 50) == [47]


def test_crivo_segmentado_multiplos_de_primos():
    assert crivo_segmentado(25, 35) == [29, 31]


def test_crivo_segmentado_resultado_ordenado():
    resultado = crivo_segmentado(2, 200)

    assert resultado == sorted(resultado)


def test_crivo_segmentado_sem_repeticoes():
    resultado = crivo_segmentado(2, 200)

    assert len(resultado) == len(set(resultado))


def test_crivo_segmentado_resultado_dentro_do_intervalo():
    baixo, alto = 50, 150
    resultado = crivo_segmentado(baixo, alto)

    assert all(baixo <= primo <= alto for primo in resultado)


@pytest.mark.parametrize(
    "baixo, alto",
    [
        (10, 5),
        (3, 2),
        (1, 0),
        (0, -1),
        (-1, -5),
        (100, 99),
    ],
)
def test_crivo_segmentado_intervalo_invertido(baixo, alto):
    with pytest.raises(
        ValueError,
        match="baixo não pode ser maior que alto",
    ):
        crivo_segmentado(baixo, alto)


@pytest.mark.parametrize(
    "baixo, alto",
    [
        (2.5, 10),
        (2, 10.5),
        ("2", 10),
        (2, "10"),
        (None, 10),
        (2, None),
        ([2], 10),
        (2, [10]),
        ((2,), 10),
        (2, (10,)),
        ({}, 10),
        (2, {}),
        (complex(2, 1), 10),
        (2, complex(10, 1)),
    ],
)
def test_crivo_segmentado_entradas_invalidas(baixo, alto):
    with pytest.raises(
        TypeError,
        match="baixo e alto devem ser inteiros",
    ):
        crivo_segmentado(baixo, alto)


def test_crivo_segmentado_ambos_argumentos_invalidos():
    with pytest.raises(TypeError):
        crivo_segmentado("inicio", "fim")


def test_crivo_segmentado_tipo_retorno():
    resultado = crivo_segmentado(2, 20)

    assert isinstance(resultado, list)
    assert all(isinstance(primo, int) for primo in resultado)


def test_crivo_segmentado_intervalo_vazio_retorna_lista():
    resultado = crivo_segmentado(0, 1)

    assert resultado == []
    assert isinstance(resultado, list)


def test_crivo_segmentado_limite_superior_inclusivo():
    assert crivo_segmentado(10, 13) == [11, 13]


def test_crivo_segmentado_limite_inferior_inclusivo():
    assert crivo_segmentado(11, 20) == [11, 13, 17, 19]


def test_crivo_segmentado_nao_inclui_numeros_compostos():
    resultado = crivo_segmentado(2, 50)

    compostos = [4, 6, 8, 9, 10, 12, 15, 21, 25, 49]

    assert all(numero not in resultado for numero in compostos)


def test_crivo_segmentado_intervalo_com_primo_grande():
    assert crivo_segmentado(997, 1000) == [997]


def test_crivo_segmentado_intervalo_com_numeros_negativos():
    assert crivo_segmentado(-100, 3) == [2, 3]


def test_crivo_segmentado_entrada_booleana():
    assert crivo_segmentado(True, 3) == [2, 3]
    assert crivo_segmentado(False, True) == []

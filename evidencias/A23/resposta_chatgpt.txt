
import pytest

from A23_tonelli_shanks import tonelli_shanks


@pytest.mark.parametrize(
    "n, p, esperado",
    [
        (0, 2, 0),
        (1, 2, 1),
        (2, 2, 0),
        (3, 2, 1),
        (10, 2, 0),
        (-1, 2, 1),
        (-2, 2, 0),
    ],
)
def test_modulo_dois(n, p, esperado):
    assert tonelli_shanks(n, p) == esperado


@pytest.mark.parametrize(
    "n, p",
    [
        (0, 3),
        (0, 5),
        (0, 7),
        (0, 13),
        (5, 5),
        (14, 7),
        (26, 13),
        (-5, 5),
    ],
)
def test_resultado_zero(n, p):
    assert tonelli_shanks(n, p) == 0


@pytest.mark.parametrize(
    "n, p",
    [
        (1, 3),
        (2, 7),
        (4, 7),
        (9, 11),
        (5, 11),
        (1, 19),
        (16, 23),
        (25, 31),
    ],
)
def test_primos_congruentes_a_tres_modulo_quatro(n, p):
    resultado = tonelli_shanks(n, p)
    assert 0 <= resultado < p
    assert (resultado * resultado) % p == n % p


@pytest.mark.parametrize(
    "n, p",
    [
        (1, 5),
        (4, 5),
        (9, 13),
        (10, 13),
        (3, 13),
        (5, 41),
        (9, 41),
        (16, 41),
        (25, 41),
        (36, 41),
        (4, 17),
        (9, 17),
        (13, 17),
    ],
)
def test_primos_congruentes_a_um_modulo_quatro(n, p):
    resultado = tonelli_shanks(n, p)
    assert 0 <= resultado < p
    assert (resultado * resultado) % p == n % p


@pytest.mark.parametrize(
    "n, p",
    [
        (1, 3),
        (1, 5),
        (1, 7),
        (1, 13),
        (1, 17),
        (1, 41),
    ],
)
def test_residuo_quadratico_um(n, p):
    resultado = tonelli_shanks(n, p)
    assert (resultado * resultado) % p == 1


@pytest.mark.parametrize(
    "n, p",
    [
        (10, 7),
        (20, 7),
        (26, 13),
        (30, 13),
        (42, 41),
        (100, 13),
        (1000, 17),
    ],
)
def test_valores_maiores_que_modulo(n, p):
    resultado = tonelli_shanks(n, p)
    assert (resultado * resultado) % p == n % p


@pytest.mark.parametrize(
    "n, p",
    [
        (-1, 5),
        (-3, 7),
        (-4, 13),
        (-8, 17),
        (-9, 41),
    ],
)
def test_valores_negativos_com_residuo_quadratico(n, p):
    resultado = tonelli_shanks(n, p)
    assert (resultado * resultado) % p == n % p


@pytest.mark.parametrize(
    "n, p",
    [
        (2, 3),
        (3, 5),
        (3, 7),
        (2, 11),
        (2, 13),
        (3, 17),
        (3, 19),
        (3, 23),
    ],
)
def test_nao_residuos_quadraticos(n, p):
    with pytest.raises(
        ValueError,
        match="n não é resíduo quadrático módulo p",
    ):
        tonelli_shanks(n, p)


@pytest.mark.parametrize(
    "p",
    [
        -100,
        -10,
        -2,
        -1,
        0,
        1,
    ],
)
def test_modulos_menores_que_dois(p):
    with pytest.raises(ValueError, match="p deve ser primo"):
        tonelli_shanks(4, p)


@pytest.mark.parametrize(
    "p",
    [
        4,
        6,
        8,
        10,
        12,
        16,
        20,
        100,
    ],
)
def test_modulos_pares_nao_primos(p):
    with pytest.raises(ValueError, match="p deve ser primo"):
        tonelli_shanks(4, p)


@pytest.mark.parametrize(
    "n, p",
    [
        (4, 7),
        (9, 13),
        (16, 17),
        (25, 41),
        (36, 43),
        (100, 101),
        (144, 103),
        (225, 107),
    ],
)
def test_quadrados_perfeitos_modulares(n, p):
    resultado = tonelli_shanks(n, p)
    assert (resultado * resultado) % p == n % p


@pytest.mark.parametrize(
    "p",
    [
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ],
)
def test_todos_os_quadrados_modulares_para_primos(p):
    for x in range(p):
        n = (x * x) % p
        resultado = tonelli_shanks(n, p)

        assert isinstance(resultado, int)
        assert 0 <= resultado < p
        assert (resultado * resultado) % p == n


@pytest.mark.parametrize(
    "p",
    [
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
    ],
)
def test_todos_os_nao_residuos_modulares(p):
    residuos = {(x * x) % p for x in range(p)}

    for n in range(1, p):
        if n not in residuos:
            with pytest.raises(
                ValueError,
                match="n não é resíduo quadrático módulo p",
            ):
                tonelli_shanks(n, p)


@pytest.mark.parametrize(
    "n, p",
    [
        (4, 5),
        (10, 13),
        (13, 17),
        (5, 41),
        (9, 41),
        (36, 41),
    ],
)
def test_execucao_algoritmo_tonelli_shanks(n, p):
    resultado = tonelli_shanks(n, p)

    assert isinstance(resultado, int)
    assert (resultado * resultado) % p == n % p


@pytest.mark.parametrize(
    "n, p",
    [
        (4, 7),
        (9, 11),
        (10, 13),
        (13, 17),
        (5, 41),
    ],
)
def test_resultado_deterministico(n, p):
    primeiro = tonelli_shanks(n, p)
    segundo = tonelli_shanks(n, p)

    assert primeiro == segundo


@pytest.mark.parametrize(
    "n, p",
    [
        (4, 7),
        (9, 13),
        (16, 17),
        (25, 41),
    ],
)
def test_equivalencia_de_valores_modulares(n, p):
    resultado_original = tonelli_shanks(n, p)
    resultado_equivalente = tonelli_shanks(n + p, p)

    assert (
        resultado_original * resultado_original
    ) % p == n % p

    assert (
        resultado_equivalente * resultado_equivalente
    ) % p == n % p


@pytest.mark.parametrize(
    "n, p",
    [
        (4, 7),
        (9, 13),
        (16, 17),
        (25, 41),
    ],
)
def test_raiz_e_seu_oposto_modular(n, p):
    resultado = tonelli_shanks(n, p)
    oposto = (-resultado) % p

    assert (resultado * resultado) % p == n % p
    assert (oposto * oposto) % p == n % p

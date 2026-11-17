import pytest
from artefatos.A25_segmentos_se_intersectam import segmentos_se_intersectam


# Cenários de interseção normal
def test_segmentos_se_cruzam():
    p1 = (1, 1)
    q1 = (4, 4)
    p2 = (1, 4)
    q2 = (4, 1)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmentos_se_cruzam_perpendicularmente():
    p1 = (0, 2)
    q1 = (4, 2)
    p2 = (2, 0)
    q2 = (2, 4)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmentos_se_cruzam_em_ponto_interno():
    p1 = (0, 0)
    q1 = (6, 6)
    p2 = (0, 6)
    q2 = (6, 0)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


# Segmentos que não se intersectam
def test_segmentos_paralelos():
    p1 = (0, 0)
    q1 = (4, 0)
    p2 = (0, 2)
    q2 = (4, 2)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is False


def test_segmentos_distantes():
    p1 = (0, 0)
    q1 = (2, 2)
    p2 = (4, 4)
    q2 = (6, 6)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is False


def test_segmentos_em_direcoes_diferentes_sem_intersecao():
    p1 = (0, 0)
    q1 = (2, 2)
    p2 = (3, 0)
    q2 = (5, 2)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is False


# Interseção nas extremidades
def test_segmentos_se_tocam_na_extremidade():
    p1 = (0, 0)
    q1 = (2, 2)
    p2 = (2, 2)
    q2 = (4, 0)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmentos_compartilham_ponto_inicial():
    p1 = (0, 0)
    q1 = (4, 4)
    p2 = (0, 0)
    q2 = (4, 0)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmentos_compartilham_ponto_final():
    p1 = (0, 0)
    q1 = (4, 0)
    p2 = (2, 2)
    q2 = (4, 0)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


# Segmentos colineares
def test_segmentos_colineares_sobrepostos():
    p1 = (0, 0)
    q1 = (5, 0)
    p2 = (2, 0)
    q2 = (7, 0)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmentos_colineares_sem_sobreposicao():
    p1 = (0, 0)
    q1 = (2, 0)
    p2 = (4, 0)
    q2 = (6, 0)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is False


def test_segmentos_colineares_tocando_na_extremidade():
    p1 = (0, 0)
    q1 = (3, 0)
    p2 = (3, 0)
    q2 = (6, 0)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmentos_colineares_verticalmente():
    p1 = (2, 0)
    q1 = (2, 5)
    p2 = (2, 3)
    q2 = (2, 8)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


# Casos especiais com pontos iguais
def test_todos_os_pontos_iguais():
    p1 = (1, 1)
    q1 = (1, 1)
    p2 = (1, 1)
    q2 = (1, 1)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmento_comprimento_zero_sobre_outro_segmento():
    p1 = (2, 0)
    q1 = (2, 0)
    p2 = (0, 0)
    q2 = (4, 0)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmento_comprimento_zero_fora_de_outro_segmento():
    p1 = (5, 5)
    q1 = (5, 5)
    p2 = (0, 0)
    q2 = (4, 4)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is False


def test_dois_segmentos_de_comprimento_zero_em_pontos_diferentes():
    p1 = (0, 0)
    q1 = (0, 0)
    p2 = (2, 2)
    q2 = (2, 2)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is False


# Casos extremos
def test_segmentos_com_coordenadas_negativas():
    p1 = (-5, -5)
    q1 = (5, 5)
    p2 = (-5, 5)
    q2 = (5, -5)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmentos_com_coordenadas_muito_grandes():
    p1 = (0, 0)
    q1 = (10**9, 10**9)
    p2 = (0, 10**9)
    q2 = (10**9, 0)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


def test_segmentos_com_coordenadas_decimais():
    p1 = (0.5, 0.5)
    q1 = (4.5, 4.5)
    p2 = (0.5, 4.5)
    q2 = (4.5, 0.5)

    assert segmentos_se_intersectam(p1, q1, p2, q2) is True


# Diferentes orientações e posições
@pytest.mark.parametrize(
    "p1, q1, p2, q2, esperado",
    [
        ((0, 0), (4, 4), (0, 3), (4, 3), False),
        ((0, 0), (4, 4), (1, 1), (3, 3), True),
        ((0, 0), (4, 4), (5, 5), (7, 7), False),
        ((0, 4), (4, 0), (1, 1), (3, 3), True),
        ((0, 0), (0, 4), (-2, 2), (2, 2), True),
        ((0, 0), (0, 4), (1, 1), (3, 3), False),
        ((0, 0), (4, 0), (2, -2), (2, 2), True),
        ((0, 0), (4, 0), (5, -2), (5, 2), False),
    ],
)
def test_diferentes_cenarios_de_intersecao(p1, q1, p2, q2, esperado):
    assert segmentos_se_intersectam(p1, q1, p2, q2) is esperado


# Verificação da simetria da função
def test_intersecao_independe_da_ordem_dos_segmentos():
    p1 = (0, 0)
    q1 = (4, 4)
    p2 = (0, 4)
    q2 = (4, 0)

    resultado1 = segmentos_se_intersectam(p1, q1, p2, q2)
    resultado2 = segmentos_se_intersectam(p2, q2, p1, q1)

    assert resultado1 is True
    assert resultado2 is True


def test_intersecao_independe_da_ordem_dos_pontos():
    p1 = (0, 0)
    q1 = (4, 4)
    p2 = (0, 4)
    q2 = (4, 0)

    resultado1 = segmentos_se_intersectam(p1, q1, p2, q2)
    resultado2 = segmentos_se_intersectam(q1, p1, q2, p2)

    assert resultado1 is True
    assert resultado2 is True
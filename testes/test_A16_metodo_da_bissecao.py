import pytest

from artefatos.A16_metodo_da_bissecao import metodo_da_bissecao


def test_raiz_exata_no_extremo_esquerdo():
    f = lambda x: x**2 - 4

    resultado = metodo_da_bissecao(f, 2, 5)

    assert resultado == 2


def test_raiz_exata_no_meio_do_intervalo():
    f = lambda x: x**2 - 4

    resultado = metodo_da_bissecao(f, 0, 4)

    assert resultado == 2


def test_raiz_positiva():
    f = lambda x: x**2 - 9

    resultado = metodo_da_bissecao(f, 0, 5)

    assert resultado == pytest.approx(3, abs=1e-9)


def test_raiz_negativa():
    f = lambda x: x + 5

    resultado = metodo_da_bissecao(f, -10, 0)

    assert resultado == pytest.approx(-5, abs=1e-9)


def test_raiz_com_funcao_linear():
    f = lambda x: 2 * x - 6

    resultado = metodo_da_bissecao(f, 0, 5)

    assert resultado == pytest.approx(3, abs=1e-9)


def test_raiz_com_funcao_nao_linear():
    f = lambda x: x**3 - 8

    resultado = metodo_da_bissecao(f, 0, 5)

    assert resultado == pytest.approx(2, abs=1e-9)


def test_raiz_exata_no_extremo_direito():
    f = lambda x: x - 5

    resultado = metodo_da_bissecao(f, 0, 5)

    assert resultado == pytest.approx(5)


def test_intervalo_com_sinais_iguais_gera_value_error():
    f = lambda x: x**2 + 1

    with pytest.raises(
        ValueError,
        match="f\\(a\\) e f\\(b\\) devem ter sinais opostos"
    ):
        metodo_da_bissecao(f, -2, 2)


def test_intervalo_com_funcoes_positivas_gera_value_error():
    f = lambda x: x**2 + 2

    with pytest.raises(ValueError):
        metodo_da_bissecao(f, 1, 5)


def test_tolerancia_personalizada():
    f = lambda x: x**2 - 2

    resultado = metodo_da_bissecao(
        f, 0, 2, tolerancia=1e-5
    )

    assert resultado == pytest.approx(2**0.5, abs=1e-5)


def test_tolerancia_muito_pequena():
    f = lambda x: x**2 - 2

    resultado = metodo_da_bissecao(
        f, 0, 2, tolerancia=1e-12
    )

    assert resultado == pytest.approx(2**0.5, abs=1e-12)


def test_maximo_de_iteracoes():
    f = lambda x: x**2 - 2

    resultado = metodo_da_bissecao(
        f, 0, 2, tolerancia=1e-15, max_iteracoes=3
    )

    assert resultado == pytest.approx(1.375)


def test_zero_iteracoes():
    f = lambda x: x**2 - 2

    resultado = metodo_da_bissecao(
        f, 0, 2, max_iteracoes=0
    )

    assert resultado == pytest.approx(1.0)


def test_intervalo_muito_pequeno():
    f = lambda x: x - 1.5

    resultado = metodo_da_bissecao(
        f, 1.4, 1.6, tolerancia=1
    )

    assert resultado == pytest.approx(1.5)


def test_raiz_com_intervalo_negativo():
    f = lambda x: x**2 - 4

    resultado = metodo_da_bissecao(f, -3, -1)

    assert resultado == pytest.approx(-2, abs=1e-9)


def test_intervalo_com_extremos_iguais_e_raiz():
    f = lambda x: x - 2

    resultado = metodo_da_bissecao(f, 2, 2)

    assert resultado == 2


def test_intervalo_com_extremos_iguais_sem_raiz():
    f = lambda x: x + 1

    resultado = metodo_da_bissecao(f, 2, 2)

    assert resultado == pytest.approx(2)


def test_funcao_com_raiz_fracionaria():
    f = lambda x: 3 * x - 1

    resultado = metodo_da_bissecao(f, 0, 1)

    assert resultado == pytest.approx(1 / 3, abs=1e-9)


def test_funcao_com_raiz_zero():
    f = lambda x: x

    resultado = metodo_da_bissecao(f, -1, 1)

    assert resultado == pytest.approx(0)


def test_funcao_com_raiz_nao_exata_dentro_do_intervalo():
    f = lambda x: x**3 - 3 * x - 1

    resultado = metodo_da_bissecao(f, 1, 3)

    assert resultado == pytest.approx(1.879385, abs=1e-5)


def test_funcao_constante_positiva():
    f = lambda x: 5

    with pytest.raises(ValueError):
        metodo_da_bissecao(f, 0, 10)


def test_funcao_constante_negativa():
    f = lambda x: -5

    with pytest.raises(ValueError):
        metodo_da_bissecao(f, 0, 10)


def test_max_iteracoes_igual_a_um():
    f = lambda x: x**2 - 2

    resultado = metodo_da_bissecao(
        f, 0, 2, tolerancia=1e-15, max_iteracoes=1
    )

    assert resultado == pytest.approx(1.5)


def test_funcao_com_raiz_exata_na_primeira_bisseccao():
    f = lambda x: x - 3

    resultado = metodo_da_bissecao(f, 0, 6)

    assert resultado == 3


def test_funcao_com_valores_negativos_nos_extremos():
    f = lambda x: -(x**2 - 4)

    resultado = metodo_da_bissecao(f, 0, 5)

    assert resultado == pytest.approx(2, abs=1e-9)

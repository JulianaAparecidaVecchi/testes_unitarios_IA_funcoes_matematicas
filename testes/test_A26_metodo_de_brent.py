import pytest
from artefatos.A26_metodo_de_brent import metodo_de_brent


# Cenários de execução normal
def test_raiz_de_funcao_linear():
    f = lambda x: x - 2
    resultado = metodo_de_brent(f, 0, 4)

    assert resultado == pytest.approx(2.0, abs=1e-10)


def test_raiz_de_funcao_linear_com_raiz_negativa():
    f = lambda x: x + 3
    resultado = metodo_de_brent(f, -5, 0)

    assert resultado == pytest.approx(-3.0, abs=1e-10)


def test_raiz_de_funcao_quadratica():
    f = lambda x: x**2 - 4
    resultado = metodo_de_brent(f, 0, 3)

    assert resultado == pytest.approx(2.0, abs=1e-10)


def test_raiz_de_funcao_cubica():
    f = lambda x: x**3 - 8
    resultado = metodo_de_brent(f, 0, 3)

    assert resultado == pytest.approx(2.0, abs=1e-10)


def test_raiz_de_funcao_exponencial():
    import math

    f = lambda x: math.exp(x) - 2
    resultado = metodo_de_brent(f, 0, 2)

    assert resultado == pytest.approx(math.log(2), abs=1e-10)


def test_raiz_de_funcao_trigonometrica():
    import math

    f = lambda x: math.sin(x)
    resultado = metodo_de_brent(f, 3, 4)

    assert resultado == pytest.approx(math.pi, abs=1e-10)


# Raízes nos extremos do intervalo
def test_raiz_no_extremo_inferior():
    f = lambda x: x
    resultado = metodo_de_brent(f, 0, 5)

    assert resultado == 0


def test_raiz_no_extremo_superior():
    f = lambda x: x - 5
    resultado = metodo_de_brent(f, 0, 5)

    assert resultado == 5


# Entradas inválidas: intervalo sem mudança de sinal
@pytest.mark.parametrize(
    "f, a, b",
    [
        (lambda x: x**2 + 1, -2, 2),
        (lambda x: x**2 + 4, 0, 3),
        (lambda x: x + 5, 0, 3),
        (lambda x: x**2, 1, 3),
    ],
)
def test_intervalo_sem_mudanca_de_sinal(f, a, b):
    with pytest.raises(
        ValueError,
        match="f\\(a\\) e f\\(b\\) devem ter sinais opostos",
    ):
        metodo_de_brent(f, a, b)


# Casos extremos
def test_funcao_com_raiz_proxima_de_zero():
    f = lambda x: x - 1e-8
    resultado = metodo_de_brent(f, -1, 1)

    assert resultado == pytest.approx(1e-8, abs=1e-10)


def test_funcao_com_raiz_muito_grande():
    f = lambda x: x - 1000000
    resultado = metodo_de_brent(f, 0, 2000000)

    assert resultado == pytest.approx(1000000, abs=1e-8)


def test_funcao_com_intervalo_negativo():
    f = lambda x: x + 10
    resultado = metodo_de_brent(f, -15, -5)

    assert resultado == pytest.approx(-10, abs=1e-10)


def test_intervalo_muito_pequeno():
    f = lambda x: x - 1.5
    resultado = metodo_de_brent(f, 1, 2)

    assert resultado == pytest.approx(1.5, abs=1e-10)


# Diferentes tolerâncias
@pytest.mark.parametrize(
    "tolerancia",
    [
        1e-4,
        1e-6,
        1e-8,
        1e-10,
        1e-12,
    ],
)
def test_diferentes_valores_de_tolerancia(tolerancia):
    f = lambda x: x**2 - 9
    resultado = metodo_de_brent(
        f, 0, 5, tolerancia=tolerancia
    )

    assert resultado == pytest.approx(3.0, abs=tolerancia * 2)


# Diferentes limites de iterações
def test_com_limite_alto_de_iteracoes():
    f = lambda x: x**3 - 27
    resultado = metodo_de_brent(
        f, 1, 5, max_iteracoes=200
    )

    assert resultado == pytest.approx(3.0, abs=1e-10)


def test_com_limite_de_uma_iteracao():
    f = lambda x: x - 2
    resultado = metodo_de_brent(
        f, 0, 4, max_iteracoes=1
    )

    assert isinstance(resultado, (int, float))


def test_com_zero_iteracoes_retorna_extremo_ajustado():
    f = lambda x: x - 2
    resultado = metodo_de_brent(
        f, 0, 4, max_iteracoes=0
    )

    assert resultado == 4


# Verificação de diferentes caminhos de execução
def test_funcao_que_utiliza_interpolacao_linear():
    f = lambda x: x - 3
    resultado = metodo_de_brent(f, 0, 10)

    assert resultado == pytest.approx(3.0, abs=1e-10)


def test_funcao_que_utiliza_bisseccao():
    f = lambda x: x**3 - 2 * x - 5
    resultado = metodo_de_brent(f, 2, 3)

    assert resultado == pytest.approx(2.0945514815, abs=1e-8)


def test_funcao_com_raiz_irracional():
    f = lambda x: x**2 - 2
    resultado = metodo_de_brent(f, 1, 2)

    assert resultado == pytest.approx(2**0.5, abs=1e-10)


def test_funcao_com_mais_de_uma_raiz_no_intervalo():
    f = lambda x: (x - 1) * (x - 3)
    resultado = metodo_de_brent(f, 0, 2)

    assert resultado == pytest.approx(1.0, abs=1e-10)


# Verificação da precisão do resultado
@pytest.mark.parametrize(
    "f, a, b, raiz",
    [
        (lambda x: x**2 - 16, 2, 5, 4),
        (lambda x: x**3 - 64, 3, 5, 4),
        (lambda x: x**2 - 25, 0, 10, 5),
        (lambda x: x**3 + 27, -5, -1, -3),
        (lambda x: x**4 - 81, 1, 4, 3),
    ],
)
def test_precisao_de_diferentes_funcoes(f, a, b, raiz):
    resultado = metodo_de_brent(f, a, b)

    assert resultado == pytest.approx(raiz, abs=1e-10)
    assert abs(f(resultado)) < 1e-8
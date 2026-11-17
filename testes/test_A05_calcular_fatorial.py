import pytest

from artefatos.A05_calcular_fatorial import calcular_fatorial


@pytest.mark.parametrize(
    "n, esperado",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (10, 3628800),
    ],
)
def test_calcular_fatorial_valores_validos(n, esperado):
    assert calcular_fatorial(n) == esperado


def test_calcular_fatorial_numero_grande():
    assert calcular_fatorial(20) == 2432902008176640000


@pytest.mark.parametrize("n", [-1, -5, -100])
def test_calcular_fatorial_numeros_negativos(n):
    with pytest.raises(ValueError, match="n deve ser não negativo"):
        calcular_fatorial(n)


@pytest.mark.parametrize(
    "n",
    [1.0, 2.5, "5", None, [], {}, (5,), 1 + 2j],
)
def test_calcular_fatorial_tipos_invalidos(n):
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        calcular_fatorial(n)


def test_calcular_fatorial_booleano():
    assert calcular_fatorial(True) == 1

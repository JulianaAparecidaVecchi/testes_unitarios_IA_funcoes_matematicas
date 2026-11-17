import pytest
from artefatos.A07_exponenciacao_modular import exponenciacao_modular


@pytest.mark.parametrize(
    "base, expoente, modulo, esperado",
    [
        (2, 3, 5, 3),
        (2, 10, 1000, 24),
        (3, 4, 7, 4),
        (5, 0, 7, 1),
        (0, 5, 7, 0),
        (1, 100, 13, 1),
        (-2, 3, 5, 2),
        (-3, 2, 7, 2),
        (10, 1, 3, 1),
        (2, 20, 1, 0),
        (7, 5, 3, 1),
        (123456789, 123, 97, pow(123456789, 123, 97)),
    ],
)
def test_exponenciacao_modular_casos_validos(base, expoente, modulo, esperado):
    assert exponenciacao_modular(base, expoente, modulo) == esperado


@pytest.mark.parametrize(
    "base, expoente, modulo",
    [
        (2, -1, 5),
        (5, -10, 7),
        (0, -1, 3),
    ],
)
def test_exponenciacao_modular_expoente_negativo(base, expoente, modulo):
    with pytest.raises(ValueError, match="expoente deve ser não negativo"):
        exponenciacao_modular(base, expoente, modulo)


@pytest.mark.parametrize(
    "base, expoente, modulo",
    [
        (2, 3, 0),
        (5, 0, 0),
        (-2, 4, 0),
    ],
)
def test_exponenciacao_modular_modulo_zero(base, expoente, modulo):
    with pytest.raises(ZeroDivisionError):
        exponenciacao_modular(base, expoente, modulo)


@pytest.mark.parametrize(
    "base, expoente, modulo",
    [
        ("2", 3, 5),
        (2, "3", 5),
        (2, 3, "5"),
        (None, 3, 5),
        (2, None, 5),
        (2, 3, None),
    ],
)
def test_exponenciacao_modular_entradas_invalidas(base, expoente, modulo):
    with pytest.raises(TypeError):
        exponenciacao_modular(base, expoente, modulo)


import pytest
from A15_gerar_sequencia_collatz import gerar_sequencia_collatz


def test_numero_igual_a_um():
    assert gerar_sequencia_collatz(1) == [1]


def test_numero_par():
    assert gerar_sequencia_collatz(2) == [2, 1]


def test_numero_impar():
    assert gerar_sequencia_collatz(3) == [3, 10, 5, 16, 8, 4, 2, 1]


def test_numero_par_maior():
    assert gerar_sequencia_collatz(8) == [8, 4, 2, 1]


def test_numero_impar_maior():
    assert gerar_sequencia_collatz(7) == [
        7, 22, 11, 34, 17, 52, 26, 13,
        40, 20, 10, 5, 16, 8, 4, 2, 1
    ]


def test_numero_primo():
    assert gerar_sequencia_collatz(5) == [5, 16, 8, 4, 2, 1]


def test_numero_zero():
    with pytest.raises(ValueError, match="n deve ser positivo"):
        gerar_sequencia_collatz(0)


def test_numero_negativo():
    with pytest.raises(ValueError, match="n deve ser positivo"):
        gerar_sequencia_collatz(-5)


def test_numero_decimal():
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        gerar_sequencia_collatz(2.5)


def test_string():
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        gerar_sequencia_collatz("5")


def test_valor_none():
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        gerar_sequencia_collatz(None)


def test_booleano():
    assert gerar_sequencia_collatz(True) == [True]


def test_lista():
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        gerar_sequencia_collatz([5])


def test_tupla():
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        gerar_sequencia_collatz((5,))


def test_dicionario():
    with pytest.raises(TypeError, match="n deve ser inteiro"):
        gerar_sequencia_collatz({"n": 5})


def test_numero_grande():
    assert gerar_sequencia_collatz(16) == [
        16, 8, 4, 2, 1
    ]


def test_resultado_e_uma_lista():
    resultado = gerar_sequencia_collatz(6)

    assert isinstance(resultado, list)


def test_sequencia_termina_em_um():
    resultado = gerar_sequencia_collatz(11)

    assert resultado[-1] == 1


def test_primeiro_elemento_e_o_numero_inicial():
    numero = 13
    resultado = gerar_sequencia_collatz(numero)

    assert resultado[0] == numero


def test_todos_os_elementos_sao_inteiros():
    resultado = gerar_sequencia_collatz(9)

    assert all(isinstance(valor, int) for valor in resultado)

import pytest

from A30_pontos_para_polinomio import pontos_para_polinomio


def test_um_unico_ponto():
    assert pontos_para_polinomio([(2, 5)]) == [5.0]


def test_dois_pontos_reta_crescente():
    resultado = pontos_para_polinomio([(0, 1), (1, 3)])
    assert resultado == [1.0, 2.0]


def test_dois_pontos_reta_decrescente():
    resultado = pontos_para_polinomio([(0, 5), (2, 1)])
    assert resultado == [5.0, -2.0]


def test_polinomio_quadratico():
    # y = x² + 2x + 1
    pontos = [(-1, 0), (0, 1), (1, 4)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([1.0, 2.0, 1.0])


def test_polinomio_cubico():
    # y = x³ - 2x² + 3x - 4
    pontos = [
        (0, -4),
        (1, -2),
        (2, 2),
        (3, 14)
    ]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([-4.0, 3.0, -2.0, 1.0])


def test_pontos_com_coordenadas_negativas():
    # y = 2x + 3
    pontos = [(-2, -1), (-1, 1), (0, 3)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([3.0, 2.0])


def test_pontos_com_valores_float():
    # y = 0.5x + 1
    pontos = [(0.0, 1.0), (2.0, 2.0)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([1.0, 0.5])


def test_pontos_fora_de_ordem():
    # y = x² + 1
    pontos = [(2, 5), (-1, 2), (0, 1)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([1.0, 0.0, 1.0])


def test_coeficientes_zero():
    pontos = [(0, 0), (1, 0), (2, 0)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == [0.0]


def test_remocao_de_coeficientes_proximos_de_zero():
    # y = 2, com coeficientes de grau superior nulos
    pontos = [(0, 2), (1, 2), (2, 2)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == [2.0]


def test_reducao_do_grau_do_polinomio():
    # Os três pontos pertencem à reta y = 3x + 2
    pontos = [(0, 2), (1, 5), (2, 8)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([2.0, 3.0])


def test_pontos_com_valores_grandes():
    pontos = [(0, 1000000), (1, 1000002)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([1000000.0, 2.0])


def test_pontos_com_x_decimal():
    # y = 2x + 1
    pontos = [(0.5, 2.0), (1.5, 4.0)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([1.0, 2.0])


def test_pontos_com_y_zero():
    pontos = [(0, 0), (1, 2)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([0.0, 2.0])


def test_pontos_none():
    with pytest.raises(ValueError, match="é preciso informar ao menos um ponto"):
        pontos_para_polinomio(None)


def test_lista_vazia():
    with pytest.raises(ValueError, match="é preciso informar ao menos um ponto"):
        pontos_para_polinomio([])


def test_ponto_sem_coordenadas():
    with pytest.raises(ValueError, match="cada ponto deve ter \\(x, y\\)"):
        pontos_para_polinomio([()])


def test_ponto_com_apenas_uma_coordenada():
    with pytest.raises(ValueError, match="cada ponto deve ter \\(x, y\\)"):
        pontos_para_polinomio([(1,)])


def test_ponto_com_tres_coordenadas():
    with pytest.raises(ValueError, match="cada ponto deve ter \\(x, y\\)"):
        pontos_para_polinomio([(1, 2, 3)])


def test_pontos_com_tamanhos_diferentes():
    with pytest.raises(ValueError, match="cada ponto deve ter \\(x, y\\)"):
        pontos_para_polinomio([(1, 2), (3,)])


def test_coordenada_x_com_string():
    with pytest.raises(TypeError, match="coordenadas devem ser numéricas"):
        pontos_para_polinomio([("1", 2)])


def test_coordenada_y_com_string():
    with pytest.raises(TypeError, match="coordenadas devem ser numéricas"):
        pontos_para_polinomio([(1, "2")])


def test_coordenada_com_none():
    with pytest.raises(TypeError, match="coordenadas devem ser numéricas"):
        pontos_para_polinomio([(1, None)])


def test_coordenada_com_lista():
    with pytest.raises(TypeError, match="coordenadas devem ser numéricas"):
        pontos_para_polinomio([(1, [2])])


def test_coordenada_x_booleana():
    with pytest.raises(TypeError, match="coordenadas devem ser numéricas"):
        pontos_para_polinomio([(True, 2)])


def test_coordenada_y_booleana():
    with pytest.raises(TypeError, match="coordenadas devem ser numéricas"):
        pontos_para_polinomio([(1, False)])


def test_coordenada_nan():
    with pytest.raises(ValueError, match="coordenadas devem ser finitas"):
        pontos_para_polinomio([(float("nan"), 2)])


def test_coordenada_infinito_positivo():
    with pytest.raises(ValueError, match="coordenadas devem ser finitas"):
        pontos_para_polinomio([(1, float("inf"))])


def test_coordenada_infinito_negativo():
    with pytest.raises(ValueError, match="coordenadas devem ser finitas"):
        pontos_para_polinomio([(float("-inf"), 2)])


def test_x_duplicado():
    with pytest.raises(ValueError, match="valores de x devem ser distintos"):
        pontos_para_polinomio([(1, 2), (1, 5)])


def test_x_duplicado_com_tres_pontos():
    with pytest.raises(ValueError, match="valores de x devem ser distintos"):
        pontos_para_polinomio([(0, 1), (1, 2), (0, 3)])


def test_x_duplicado_com_int_e_float():
    with pytest.raises(ValueError, match="valores de x devem ser distintos"):
        pontos_para_polinomio([(1, 2), (1.0, 3)])


def test_pontos_com_tuplas_e_listas():
    # y = x + 1
    pontos = [(0, 1), [1, 2]]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([1.0, 1.0])


def test_pontos_com_inteiros_e_floats_misturados():
    # y = 2x + 1
    pontos = [(0, 1.0), (1.0, 3), (2, 5.0)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([1.0, 2.0])


def test_polinomio_com_coeficientes_fracionarios():
    # y = 0.5x² + 1.5x + 2
    pontos = [(0, 2), (1, 4), (2, 7)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([2.0, 1.5, 0.5])


def test_resultado_e_lista():
    resultado = pontos_para_polinomio([(0, 1), (1, 2)])

    assert isinstance(resultado, list)


def test_coeficientes_sao_floats():
    resultado = pontos_para_polinomio([(0, 1), (1, 2)])

    assert all(isinstance(c, float) for c in resultado)


def test_polinomio_de_grau_zero_com_multiplos_pontos():
    pontos = [(-2, 7), (0, 7), (3, 7), (5, 7)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([7.0])


def test_polinomio_com_raizes_na_origem():
    # y = x²
    pontos = [(0, 0), (1, 1), (-1, 1)]
    resultado = pontos_para_polinomio(pontos)

    assert resultado == pytest.approx([0.0, 0.0, 1.0])


def test_pontos_com_x_proximos():
    pontos = [(1.0, 2.0), (1.0001, 2.0002)]
    resultado = pontos_para_polinomio(pontos)

    assert len(resultado) == 2
    assert resultado == pytest.approx([0.0, 2.0], abs=1e-8)

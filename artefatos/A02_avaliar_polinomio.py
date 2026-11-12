def avaliar_polinomio(coeficientes, x):
    """Avalia o polinômio pelo método de Horner.

    coeficientes: do termo de maior grau para o de menor grau.
    """
    resultado = 0
    for c in coeficientes:
        resultado = resultado * x + c
    return resultado

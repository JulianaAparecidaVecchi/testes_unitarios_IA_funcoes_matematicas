import math


def pontos_para_polinomio(pontos):
    """Coeficientes do polinômio interpolador de Lagrange que passa pelos pontos (x, y).

    Retorna a lista do termo de menor grau para o de maior grau.
    """
    if pontos is None or len(pontos) == 0:
        raise ValueError("é preciso informar ao menos um ponto")
    if any(len(p) != 2 for p in pontos):
        raise ValueError("cada ponto deve ter (x, y)")
    if any(isinstance(c, bool) or not isinstance(c, (int, float)) for p in pontos for c in p):
        raise TypeError("coordenadas devem ser numéricas")
    if any(not math.isfinite(c) for p in pontos for c in p):
        raise ValueError("coordenadas devem ser finitas")
    xs = [p[0] for p in pontos]
    if len(set(xs)) != len(xs):
        raise ValueError("valores de x devem ser distintos")
    n = len(pontos)
    coeficientes = [0.0] * n
    for i in range(n):
        xi, yi = pontos[i]
        termo = [1.0]
        denominador = 1.0
        for j in range(n):
            if j == i:
                continue
            xj = pontos[j][0]
            novo = [0.0] * (len(termo) + 1)
            for k, c in enumerate(termo):
                novo[k] += -xj * c
                novo[k + 1] += c
            termo = novo
            denominador *= xi - xj
        for k in range(n):
            coeficientes[k] += yi * termo[k] / denominador
    coeficientes = [0.0 if abs(c) < 1e-12 else c for c in coeficientes]
    while len(coeficientes) > 1 and coeficientes[-1] == 0.0:
        coeficientes.pop()
    return coeficientes

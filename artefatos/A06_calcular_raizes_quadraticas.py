import math


def calcular_raizes_quadraticas(a, b, c):
    """Raízes reais de a*x^2 + b*x + c = 0, como tupla (vazia, com 1 ou 2 raízes)."""
    if a == 0:
        raise ValueError("a não pode ser zero")
    delta = b * b - 4 * a * c
    if delta < 0:
        return ()
    if delta == 0:
        return (-b / (2 * a),)
    raiz = math.sqrt(delta)
    return tuple(sorted(((-b - raiz) / (2 * a), (-b + raiz) / (2 * a))))

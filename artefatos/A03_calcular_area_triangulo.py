import math


def calcular_area_triangulo(a, b, c):
    """Área do triângulo pela fórmula de Heron. Levanta ValueError se os lados forem inválidos."""
    x, y, z = sorted((a, b, c))
    if x <= 0 or x + y <= z:
        raise ValueError("lados não formam um triângulo")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

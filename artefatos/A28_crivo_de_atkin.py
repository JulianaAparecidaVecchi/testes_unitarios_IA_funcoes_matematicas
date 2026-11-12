import math


def crivo_de_atkin(limite):
    """Lista de primos menores ou iguais a limite pelo crivo de Atkin."""
    if not isinstance(limite, int):
        raise TypeError("limite deve ser inteiro")
    if limite > 10 ** 7:
        raise ValueError("limite grande demais")
    if limite < 2:
        return []
    crivo = [False] * (limite + 1)
    raiz = math.isqrt(limite)
    for x in range(1, raiz + 1):
        for y in range(1, raiz + 1):
            n = 4 * x * x + y * y
            if n <= limite and n % 12 in (1, 5):
                crivo[n] = not crivo[n]
            n = 3 * x * x + y * y
            if n <= limite and n % 12 == 7:
                crivo[n] = not crivo[n]
            n = 3 * x * x - y * y
            if x > y and n <= limite and n % 12 == 11:
                crivo[n] = not crivo[n]
    for n in range(5, raiz + 1):
        if crivo[n]:
            for k in range(n * n, limite + 1, n * n):
                crivo[k] = False
    primos = [p for p in (2, 3) if p <= limite]
    primos += [n for n in range(5, limite + 1) if crivo[n]]
    return primos

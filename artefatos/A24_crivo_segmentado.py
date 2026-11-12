import math


def crivo_segmentado(baixo, alto):
    """Primos no intervalo [baixo, alto] pelo crivo segmentado."""
    if not (isinstance(baixo, int) and isinstance(alto, int)):
        raise TypeError("baixo e alto devem ser inteiros")
    if baixo > alto:
        raise ValueError("baixo não pode ser maior que alto")
    if alto < 2:
        return []
    baixo = max(baixo, 2)
    limite = math.isqrt(alto)
    base = [True] * (limite + 1)
    primos_base = []
    for i in range(2, limite + 1):
        if base[i]:
            primos_base.append(i)
            for j in range(i * i, limite + 1, i):
                base[j] = False
    segmento = [True] * (alto - baixo + 1)
    for p in primos_base:
        inicio = max(p * p, ((baixo + p - 1) // p) * p)
        for j in range(inicio, alto + 1, p):
            segmento[j - baixo] = False
    return [baixo + i for i, eh_primo in enumerate(segmento) if eh_primo]

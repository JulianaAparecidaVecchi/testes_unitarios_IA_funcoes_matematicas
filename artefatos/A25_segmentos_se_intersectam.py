def _orientacao(p, q, r):
    valor = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if valor == 0:
        return 0
    return 1 if valor > 0 else 2


def _no_segmento(p, q, r):
    return min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and min(p[1], q[1]) <= r[1] <= max(p[1], q[1])


def segmentos_se_intersectam(p1, q1, p2, q2):
    """Retorna True se o segmento p1-q1 intersecta o segmento p2-q2 (pontos como tuplas (x, y))."""
    if p1 == q1 == p2 == q2:
        return True
    o1 = _orientacao(p1, q1, p2)
    o2 = _orientacao(p1, q1, q2)
    o3 = _orientacao(p2, q2, p1)
    o4 = _orientacao(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and _no_segmento(p1, q1, p2):
        return True
    if o2 == 0 and _no_segmento(p1, q1, q2):
        return True
    if o3 == 0 and _no_segmento(p2, q2, p1):
        return True
    if o4 == 0 and _no_segmento(p2, q2, q1):
        return True
    return False

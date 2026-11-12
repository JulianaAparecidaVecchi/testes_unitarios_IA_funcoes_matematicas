def eh_cubo_perfeito(n):
    """Retorna True se n é cubo de um inteiro (aceita negativos)."""
    if n < 0:
        return eh_cubo_perfeito(-n)
    if n < 2:
        return True
    baixo, alto = 1, n
    while baixo <= alto:
        meio = (baixo + alto) // 2
        cubo = meio ** 3
        if cubo == n:
            return True
        if cubo < n:
            baixo = meio + 1
        else:
            alto = meio - 1
    return False

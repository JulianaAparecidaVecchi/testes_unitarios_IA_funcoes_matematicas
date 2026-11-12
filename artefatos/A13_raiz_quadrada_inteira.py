def raiz_quadrada_inteira(n):
    """Maior inteiro r tal que r*r <= n, por busca binária."""
    if not isinstance(n, int):
        raise TypeError("n deve ser inteiro")
    if n < 0:
        raise ValueError("n deve ser não negativo")
    if n < 2:
        return n
    baixo, alto = 1, n
    resposta = 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if meio * meio == n:
            return meio
        elif meio * meio < n:
            resposta = meio
            baixo = meio + 1
        else:
            alto = meio - 1
    return resposta

PRIMOS_PEQUENOS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def teste_miller_rabin(n, bases=None):
    """Teste de primalidade de Miller-Rabin (determinístico para n < 3.3e24 com as bases padrão)."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n deve ser inteiro")
    if n < 2:
        return False
    for p in PRIMOS_PEQUENOS:
        if n == p:
            return True
        if n % p == 0:
            return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    if bases is None:
        bases = PRIMOS_PEQUENOS
    if len(bases) == 0:
        raise ValueError("bases vazias")
    for a in bases:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

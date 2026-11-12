def coeficiente_binomial(n, k):
    """Coeficiente binomial C(n, k) calculado iterativamente."""
    if not (isinstance(n, int) and isinstance(k, int)):
        raise TypeError("n e k devem ser inteiros")
    if k < 0 or k > n:
        return 0
    if k == 0:
        return 1
    k = min(k, n - k)
    resultado = 1
    for i in range(1, k + 1):
        resultado = resultado * (n - k + i) // i
    return resultado

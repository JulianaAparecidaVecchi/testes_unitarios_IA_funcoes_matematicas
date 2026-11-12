def teste_lucas_lehmer(p):
    """Testa se o número de Mersenne 2**p - 1 é primo (p deve ser primo)."""
    if p < 2:
        return False
    if p == 2:
        return True
    m = (1 << p) - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % m
    return s == 0

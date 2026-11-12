def tonelli_shanks(n, p):
    """Raiz quadrada modular: r tal que r*r ≡ n (mod p), para p primo ímpar (ou 2)."""
    if p < 2:
        raise ValueError("p deve ser primo")
    if p % 2 == 0 and p != 2:
        raise ValueError("p deve ser primo")
    n %= p
    if p == 2 or n == 0:
        return n
    if pow(n, (p - 1) // 2, p) != 1:
        raise ValueError("n não é resíduo quadrático módulo p")
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        i, tt = 0, t
        while tt != 1:
            tt = tt * tt % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r

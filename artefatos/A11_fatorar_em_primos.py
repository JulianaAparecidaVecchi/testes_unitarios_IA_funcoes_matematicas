def fatorar_em_primos(n):
    """Lista de fatores primos de n (com repetição), em ordem crescente."""
    if n < 2:
        raise ValueError("n deve ser maior ou igual a 2")
    fatores = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            fatores.append(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        fatores.append(n)
    return fatores

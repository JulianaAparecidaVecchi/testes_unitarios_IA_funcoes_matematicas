def calcular_fatorial(n):
    """Fatorial de n (inteiro não negativo)."""
    if not isinstance(n, int):
        raise TypeError("n deve ser inteiro")
    if n < 0:
        raise ValueError("n deve ser não negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def gerar_sequencia_collatz(n):
    """Sequência de Collatz de n até chegar a 1."""
    if not isinstance(n, int):
        raise TypeError("n deve ser inteiro")
    if n < 1:
        raise ValueError("n deve ser positivo")
    sequencia = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequencia.append(n)
    return sequencia

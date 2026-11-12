def funcao_totiente_euler(n):
    """Função totiente de Euler: quantidade de inteiros em [1, n] coprimos com n."""
    if not isinstance(n, int) or n < 1:
        raise ValueError("n deve ser inteiro positivo")
    if n == 1:
        return 1
    resultado = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            resultado -= resultado // p
        p += 1
    if n > 1:
        resultado -= resultado // n
    return resultado

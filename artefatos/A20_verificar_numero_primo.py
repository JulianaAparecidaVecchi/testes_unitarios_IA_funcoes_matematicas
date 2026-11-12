def verificar_numero_primo(n):
    """Retorna True se n é primo (n deve ser inteiro)."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n deve ser inteiro")
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

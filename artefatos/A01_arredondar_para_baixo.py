def arredondar_para_baixo(x):
    """Retorna o maior inteiro menor ou igual a x (piso)."""
    inteiro = int(x)
    if inteiro > x:
        inteiro -= 1
    return inteiro

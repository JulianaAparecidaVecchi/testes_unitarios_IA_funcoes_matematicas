def exponenciacao_modular(base, expoente, modulo):
    """Calcula (base ** expoente) % modulo por exponenciação rápida."""
    if expoente < 0:
        raise ValueError("expoente deve ser não negativo")
    resultado = 1 % modulo
    base %= modulo
    while expoente > 0:
        if expoente & 1:
            resultado = (resultado * base) % modulo
        base = (base * base) % modulo
        expoente >>= 1
    return resultado

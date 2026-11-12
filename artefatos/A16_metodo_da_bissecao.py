def metodo_da_bissecao(f, a, b, tolerancia=1e-9, max_iteracoes=100):
    """Encontra uma raiz de f em [a, b] pelo método da bissecção."""
    fa, fb = f(a), f(b)
    if fa == 0:
        return a
    if fa * fb > 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos")
    for _ in range(max_iteracoes):
        c = (a + b) / 2
        fc = f(c)
        if fc == 0 or (b - a) / 2 < tolerancia:
            return c
        if fa * fc < 0:
            b = c
        else:
            a, fa = c, fc
    return (a + b) / 2

def metodo_de_brent(f, a, b, tolerancia=1e-12, max_iteracoes=100):
    """Encontra uma raiz de f em [a, b] pelo método de Brent."""
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos")
    if abs(fa) < abs(fb):
        a, b, fa, fb = b, a, fb, fa
    c, fc = a, fa
    d = c
    usou_bisseccao = True
    for _ in range(max_iteracoes):
        if fb == 0 or abs(b - a) < tolerancia:
            return b
        if fa != fc and fb != fc:
            s = (a * fb * fc / ((fa - fb) * (fa - fc))
                 + b * fa * fc / ((fb - fa) * (fb - fc))
                 + c * fa * fb / ((fc - fa) * (fc - fb)))
        else:
            s = b - fb * (b - a) / (fb - fa)
        limite = (3 * a + b) / 4
        fora_do_intervalo = not (min(limite, b) < s < max(limite, b))
        lento_1 = usou_bisseccao and abs(s - b) >= abs(b - c) / 2
        lento_2 = not usou_bisseccao and abs(s - b) >= abs(c - d) / 2
        if fora_do_intervalo or lento_1 or lento_2:
            s = (a + b) / 2
            usou_bisseccao = True
        else:
            usou_bisseccao = False
        fs = f(s)
        d, c, fc = c, b, fb
        if fa * fs < 0:
            b, fb = s, fs
        else:
            a, fa = s, fs
        if abs(fa) < abs(fb):
            a, b, fa, fb = b, a, fb, fa
    return b

import math


def resolver_sistema_linear(A, b, tolerancia=1e-12):
    """Resolve A x = b por eliminação de Gauss com pivoteamento parcial."""
    if tolerancia <= 0:
        raise ValueError("tolerância deve ser positiva")
    n = len(A)
    if n == 0:
        raise ValueError("sistema vazio")
    if len(b) != n:
        raise ValueError("b deve ter o mesmo tamanho que A")
    if any(len(linha) != n for linha in A):
        raise ValueError("A deve ser quadrada")
    if any(not math.isfinite(v) for linha in A for v in linha):
        raise ValueError("A contém valores não finitos")
    if any(not math.isfinite(v) for v in b):
        raise ValueError("b contém valores não finitos")
    M = [list(map(float, linha)) + [float(b[i])] for i, linha in enumerate(A)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[piv][col]) < tolerancia:
            raise ValueError("sistema singular ou sem solução única")
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
        for r in range(col + 1, n):
            fator = M[r][col] / M[col][col]
            if fator == 0:
                continue
            for c in range(col, n + 1):
                M[r][c] -= fator * M[col][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - soma) / M[i][i]
    return x

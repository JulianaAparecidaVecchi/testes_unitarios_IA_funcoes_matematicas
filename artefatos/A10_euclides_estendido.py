def euclides_estendido(a, b):
    """Retorna (mdc, x, y) tal que a*x + b*y = mdc."""
    if a == 0 and b == 0:
        raise ValueError("a e b não podem ser ambos zero")
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if a < 0:
        return -a, -x0, -y0
    return a, x0, y0

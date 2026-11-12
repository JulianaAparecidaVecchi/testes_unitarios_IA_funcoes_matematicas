import math


def calcular_media_geometrica(valores):
    """Média geométrica de uma lista de números não negativos."""
    if valores is None or len(valores) == 0:
        raise ValueError("lista vazia")
    if not all(isinstance(v, (int, float)) for v in valores):
        raise TypeError("valores devem ser numéricos")
    soma_log = 0.0
    for v in valores:
        if v < 0:
            raise ValueError("valores não podem ser negativos")
        if v == 0:
            return 0.0
        soma_log += math.log(v)
    return math.exp(soma_log / len(valores))

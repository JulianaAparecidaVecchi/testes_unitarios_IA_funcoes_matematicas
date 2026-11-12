def calcular_soma_aliquota(valores, aliquota):
    """Soma os valores e aplica a alíquota (ex.: 0.1 para 10%), arredondando em 2 casas."""
    if aliquota < 0:
        raise ValueError("alíquota não pode ser negativa")
    total = 0
    for v in valores:
        if v < 0:
            raise ValueError("valores não podem ser negativos")
        total += v
    if total == 0:
        return 0.0
    return round(total * (1 + aliquota), 2)

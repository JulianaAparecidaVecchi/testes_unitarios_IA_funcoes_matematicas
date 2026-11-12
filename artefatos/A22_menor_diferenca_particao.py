def menor_diferenca_particao(numeros):
    """Menor diferença absoluta entre as somas de duas partições da lista de inteiros não negativos."""
    if not isinstance(numeros, (list, tuple)):
        raise TypeError("numeros deve ser lista ou tupla")
    if not numeros:
        return 0
    if len(numeros) == 1:
        return numeros[0]
    if any(n < 0 for n in numeros):
        raise ValueError("números não podem ser negativos")
    total = sum(numeros)
    alvo = total // 2
    possivel = [False] * (alvo + 1)
    possivel[0] = True
    for n in numeros:
        for s in range(alvo, n - 1, -1):
            if possivel[s - n]:
                possivel[s] = True
    for s in range(alvo, -1, -1):
        if possivel[s]:
            return total - 2 * s
    return total

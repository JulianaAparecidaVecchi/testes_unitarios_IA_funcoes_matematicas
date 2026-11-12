def encontrar_tres_somas(numeros, alvo=0):
    """Triplas únicas (ordenadas) de números da lista cuja soma é igual a alvo."""
    numeros = sorted(numeros)
    resultado = []
    for i in range(len(numeros) - 2):
        if i > 0 and numeros[i] == numeros[i - 1]:
            continue
        esq, dir_ = i + 1, len(numeros) - 1
        while esq < dir_:
            soma = numeros[i] + numeros[esq] + numeros[dir_]
            if soma == alvo:
                resultado.append((numeros[i], numeros[esq], numeros[dir_]))
                while esq < dir_ and numeros[esq] == numeros[esq + 1]:
                    esq += 1
                while esq < dir_ and numeros[dir_] == numeros[dir_ - 1]:
                    dir_ -= 1
                esq += 1
                dir_ -= 1
            elif soma < alvo:
                esq += 1
            else:
                dir_ -= 1
    return resultado

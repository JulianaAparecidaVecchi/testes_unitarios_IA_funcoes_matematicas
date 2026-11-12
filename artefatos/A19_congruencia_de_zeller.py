NOMES_DIAS = ["sábado", "domingo", "segunda", "terça", "quarta", "quinta", "sexta"]


def congruencia_de_zeller(dia, mes, ano):
    """Dia da semana (calendário gregoriano) pela congruência de Zeller."""
    if not 1 <= mes <= 12:
        raise ValueError("mês inválido")
    bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
    if mes == 2:
        maximo = 29 if bissexto else 28
    elif mes in (4, 6, 9, 11):
        maximo = 30
    else:
        maximo = 31
    if not 1 <= dia <= maximo:
        raise ValueError("dia inválido")
    if mes < 3:
        mes += 12
        ano -= 1
    k = ano % 100
    j = ano // 100
    h = (dia + 13 * (mes + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    return NOMES_DIAS[h]

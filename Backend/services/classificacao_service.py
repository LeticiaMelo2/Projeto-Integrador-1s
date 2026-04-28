def calcular_prioridade(impacto, urgencia):

    tabela = {
        "Alta": 3,
        "Média": 2,
        "Baixa": 1
    }

    soma = tabela.get(impacto, 1) + tabela.get(urgencia, 1)

    if soma >= 6:
        return "Alta"
    elif soma == 5:
        return "Alta"
    elif soma == 4:
        return "Média"
    else:
        return "Baixa"
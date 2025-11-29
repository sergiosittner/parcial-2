def es_escalera(dados):
    dados_ord = sorted(dados)
    return dados_ord == [1, 2, 3, 4, 5] or dados_ord == [2, 3, 4, 5, 6]

def es_full(dados):
    conteos = [dados.count(i) for i in range(1, 7)]
    return (3 in conteos) and (2 in conteos)

def es_poker(dados):

    conteos = [dados.count(i) for i in range(1, 7)]
    return (4 in conteos) or (5 in conteos)

def es_generala(dados):
    
    return dados.count(dados[0]) == 5

def calcular_puntos(dados, categoria):
    
    if categoria.isdigit():
        numero = int(categoria)
        return dados.count(numero) * numero
    
    elif categoria == "ESCALERA":
        return 20 if es_escalera(dados) else 0
    elif categoria == "FULL":
        return 30 if es_full(dados) else 0
    elif categoria == "POKER":
        return 40 if es_poker(dados) else 0
    elif categoria == "GENERALA":
        return 50 if es_generala(dados) else 0
    return 0
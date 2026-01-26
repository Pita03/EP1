import random

def cria_pecas():

    lista = []

    i = 0
    while i < 7:
        j = i          # começa em i para evitar repetição
        while j < 7:
            lista.append([i, j])
            j += 1
        i += 1

    random.shuffle(lista)
    return lista
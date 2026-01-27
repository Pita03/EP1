import random

def cria_pecas():

    lista = []

    i = 0
    while i < 7:
        j = i         
        while j < 7:
            lista.append([i, j])
            j += 1
        i += 1

    random.shuffle(lista)
    return lista

def inicia_jogo(n_jogadores, pecas):

    jogo = {}
    jogadores = {}

    indice = 0

    jogador = 0
    while jogador < n_jogadores:

        mao = []
        k = 0
        while k < 7:
            mao.append(pecas[indice])
            indice += 1
            k += 1

        jogadores[jogador] = mao
        jogador += 1

    monte = []
    while indice < len(pecas):
        monte.append(pecas[indice])
        indice += 1

    jogo["jogadores"] = jogadores
    jogo["mesa"] = []
    jogo["monte"] = monte

    return jogo

def verifica_ganhador (jogadores):
    for jogador in jogadores:

        if len(jogadores[jogador]) == 0:
            return jogador

    return -1

def conta_pontos (lista):
    total = 0
    for peca in lista:
        total += peca[0] + peca[1]
    return total

def posicoes_possiveis (mesa, pecas):
    posicoes = []

    if len(mesa) == 0:
        return list(range(len(pecas)))

    esquerda = mesa[0][0]
    direita = mesa[-1][1]
    for i in range(len(pecas)):
        peca = pecas[i]

        if (peca[0] == esquerda or peca[1] == esquerda or
            peca[0] == direita or peca[1] == direita):
            posicoes.append(i)

    return posicoes

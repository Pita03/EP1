from funcoes import *
import random
from colorama import Fore, Style, init

init()


def cor_num(n):
    cores = {
        0: Fore.WHITE,
        1: Fore.BLUE,
        2: Fore.GREEN,
        3: Fore.CYAN,
        4: Fore.YELLOW,
        5: Fore.MAGENTA,
        6: Fore.RED,
    }

    return cores.get(n, Fore.WHITE) + str(n) + Style.RESET_ALL


def mostra_mesa(mesa):
    print("MESA:")
    for p in mesa:
        print(f"[{cor_num(p[0])}|{cor_num(p[1])}]", end="")
    print("\n")


def mostra_mao_usuario(mao, posicoes):
    print("Jogador: Você com", len(mao), "peça(s)")

    estrelas = ""
    for i in range(len(mao)):
        if i in posicoes:
            estrelas += "  *   "
        else:
            estrelas += "      "
    print(estrelas)

    for p in mao:
        print(f"[{cor_num(p[0])}|{cor_num(p[1])}]", end=" ")
    print()

    for i in range(len(mao)):
        print(f"  {i+1}  ", end=" ")
    print("\n")


def pede_indice(posicoes, total):
    while True:
        entrada = input("Escolha a peça: ")

        try:
            idx = int(entrada) - 1
        except ValueError:
            print("Digite um número válido.")
            continue

        if idx in posicoes:
            return idx

        print("Posição inválida!")
        print("Escolha a peça", [p + 1 for p in posicoes])


# ==================================
# LOOP PARA JOGAR NOVAMENTE
# ==================================

while True:

    # -------------------------
    # VALIDAR NUMERO DE JOGADORES
    # -------------------------
    while True:
        try:
            n = int(input("Quantos jogadores? (2-4) "))

            if 2 <= n <= 4:
                break
            else:
                print("Número inválido! Digite entre 2 e 4.")

        except ValueError:
            print("Entrada inválida! Digite um número.")

    # -------------------------
    # INICIAR JOGO
    # -------------------------
    pecas = cria_pecas()
    jogo = inicia_jogo(n, pecas)

    mesa = jogo["mesa"]
    monte = jogo["monte"]
    jogadores = jogo["jogadores"]

    jogador_atual = random.randint(0, n - 1)

    # ==================================
    # LOOP DA PARTIDA
    # ==================================

    while True:

        mao = jogadores[jogador_atual]

        print("--------------------------------")

        # BOT
        if jogador_atual != n - 1:

            print("Jogador:", jogador_atual + 1, "com", len(mao), "peça(s)")

            pos = posicoes_possiveis(mesa, mao)

            while len(pos) == 0 and len(monte) > 0:
                mao.append(monte.pop())
                pos = posicoes_possiveis(mesa, mao)

            if len(pos) == 0:
                print("Não tem peças possíveis. MONTE VAZIO - PULANDO A VEZ!")
            else:
                idx = pos[0]
                peca = mao.pop(idx)

                mesa[:] = adiciona_na_mesa(peca, mesa)
                print("Colocou:", f"[{cor_num(peca[0])}|{cor_num(peca[1])}]")

        # USUÁRIO
        else:

            pos = posicoes_possiveis(mesa, mao)

            while len(pos) == 0 and len(monte) > 0:
                print("Comprou do monte.")
                mao.append(monte.pop())
                pos = posicoes_possiveis(mesa, mao)

            if len(pos) == 0:
                print("Não tem peças possíveis. MONTE VAZIO - PULANDO A VEZ!")
            else:
                mostra_mao_usuario(mao, pos)

                idx = pede_indice(pos, len(mao))

                peca = mao.pop(idx)
                mesa[:] = adiciona_na_mesa(peca, mesa)

                print("Colocou:", f"[{cor_num(peca[0])}|{cor_num(peca[1])}]")

        mostra_mesa(mesa)

        vencedor = verifica_ganhador(jogadores)

        if vencedor != -1:
            print("\nRESULTADO FINAL:\n")

            menor = None
            vencedores = []

            for j in jogadores:
                pontos = conta_pontos(jogadores[j])
                print("Jogador:", "Você" if j == n - 1 else j + 1,
                      "com", jogadores[j],
                      "e", pontos, "pontos")

                if menor is None or pontos < menor:
                    menor = pontos
                    vencedores = [j]
                elif pontos == menor:
                    vencedores.append(j)

            print("\nVENCEDOR(ES):", end=" ")

            for v in vencedores:
                if v == n - 1:
                    print("Você", end=" ")
                else:
                    print(v + 1, end=" ")

            break

        jogador_atual = (jogador_atual + 1) % n

    # -------------------------
    # PERGUNTAR SE JOGA DE NOVO
    # -------------------------

    while True:
        resp = input("\nQuer jogar novamente? (s/n) ").strip().lower()

        if resp == "s":
            jogar_novamente = True
            break
        elif resp == "n":
            jogar_novamente = False
            break
        else:
            print("Digite apenas 's' ou 'n'.")

    if not jogar_novamente:
        print("Fim do jogo!")
        break

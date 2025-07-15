#Nome do projeto: JOGO DA VELHA

import random
import time as t

def linha():  
    print("=" * 70)

print("BEM VINDO AO JOGO DA VÉIA!!")
t.sleep(2)
linha()
print("Para começar, basta você ir e apagar essas aspas que estão nos jogos!")
print("Só para constar... Temos de 3x3 até 7x7! Boa sorte!!")
linha()

# MODO CLÁSSICO - 3x3

# exibe o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("----------------")
    print("|", tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2], "|")
    print("----------------")
    print("|", tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5], "|")
    print("----------------")
    print("|", tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8], "|")
    print("----------------")

# verifica se alguem ganhou
def verificar_vitoria(tabuleiro, jogador):
    comb_vitoria = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
                    [0, 4, 8], [2, 4, 6]]             # diagonais

    for comb in comb_vitoria:
        if tabuleiro[comb[0]] == tabuleiro[comb[1]] == tabuleiro[comb[2]] == jogador:
            return True
    return False

# verifica se o tabuleiro está cheio (empate)
def verificar_empate(tabuleiro):
    return all(posicao != ' ' for posicao in tabuleiro)

def obter_posicoes_vazias(tabuleiro):
    return [i for i, posicao in enumerate(tabuleiro) if posicao == ' ']

# Função Minimax
def minimax(tabuleiro, profundidade, jogador):
    if verificar_vitoria(tabuleiro, 'X'):
        return 1
    elif verificar_vitoria(tabuleiro, 'O'):
        return -1
    elif verificar_empate(tabuleiro):
        return 0

    if jogador == 'X':
        melhor_pontuacao = -float('inf')
        for posicao in obter_posicoes_vazias(tabuleiro):
            tabuleiro[posicao] = 'X'
            pontuacao = minimax(tabuleiro, profundidade + 1, 'O')
            tabuleiro[posicao] = ' '
            melhor_pontuacao = max(melhor_pontuacao, pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = float('inf')
        for posicao in obter_posicoes_vazias(tabuleiro):
            tabuleiro[posicao] = 'O'
            pontuacao = minimax(tabuleiro, profundidade + 1, 'X')
            tabuleiro[posicao] = ' '
            melhor_pontuacao = min(melhor_pontuacao, pontuacao)
        return melhor_pontuacao

# principal para executar o jogo
def jogar_jogo_da_velha():
    tabuleiro = [' ' for _ in range(9)]
    jogadores = ['X', 'O']
    jogador_atual = random.choice(jogadores)

    while True:
        exibir_tabuleiro(tabuleiro)

        if jogador_atual == 'X':
            posicao = int(input("Digite a posição (0-8): "))
            if 0 <= posicao <= 8 and tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = 'X'
                if verificar_vitoria(tabuleiro, 'X'):
                    exibir_tabuleiro(tabuleiro)
                    print("Você venceu!")
                    break
                elif verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break
                jogador_atual = 'O'
            else:
                print("Posição inválida. Tente novamente.")
        else:
            melhor_pontuacao = float('inf')
            melhor_jogada = None
            for posicao in obter_posicoes_vazias(tabuleiro):
                tabuleiro[posicao] = 'O'
                pontuacao = minimax(tabuleiro, 0, 'X')
                tabuleiro[posicao] = ' '
                if pontuacao < melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_jogada = posicao

            tabuleiro[melhor_jogada] = 'O'
            print(f"Computador jogou na posição {melhor_jogada}")

            if verificar_vitoria(tabuleiro, 'O'):
                exibir_tabuleiro(tabuleiro)
                print("O computador venceu!")
                break
            elif verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("Empate!")
                break
            jogador_atual = 'X'

jogar_jogo_da_velha()
#connect Four

import random
import time


#mostra o tabuleiro para os jogadores
def mostraMatriz(matriz):
    print('-'*20)    
    print('Este é o tabuleiro da sua partida! Que vença o melhor! ')    
    print('-'*20)  
    for lin in matrizGame:
        for el in lin:
            print(el, end=' ')
        print('')
    print('-'*20)   


#faz a jogada 
def jogada(jogador,matriz):
    linhaJogada = len(matriz) - 1
    if jogador == 1: 
        coluna = int(input('Jogador 1, escolha a coluna que deseja colocar a peça!: '))
        while linhaJogada >= 0:
            if matriz[linhaJogada][coluna] == 0:
                matriz[linhaJogada][coluna] = 2
                break
            linhaJogada -=1
    else:
        coluna = int(input('Jogador 2, escolha a coluna que deseja colocar a peça!: '))
        while linhaJogada >= 0:
            if matriz[linhaJogada][coluna] == 0:
                matriz[linhaJogada][coluna] = 1
                break
            linhaJogada -=1
    mostraMatriz(matriz)



#funcoes para fazer as analises de possiveis jogadas vencedoras
def analiseLinha(jogador,matriz):
    if jogador == 1:
        for linha in matriz:
            rep = 0
            for el in linha:
                if el == 2:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0
    else:
        for linha in matriz:
            rep = 0
            for el in linha:
                if el == 1:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0
    return False

def analiseColuna(matriz):
    for linha in matriz:
        



jogarNovamente = True

while jogarNovamente:

    #menu
    menu = input("Olá, bem vindo ao Ligue 4! Como deseja jogar?(digite 1 ou 2):\n 1 - Jogador X Jogador\n 2 - Jogador X Computador\n ")
    while menu not in '12':
        menu = input("Digite apenas 1 ou 2 para selecionar as opções!\n")

    winner = False

    if menu == '1':  
        while not winner:
            tabuleiro = input('Qual o tamanho do tabuleiro que os jogadores vão utilizar?(limite de 10x10, digite os números de largura e altura respectivamente, separados por espaço): ').split(' ')
            largura = int(tabuleiro[0])
            altura = int(tabuleiro[1])

            #verificacao de dimensoes do tabuleiro
            while largura > 10 or largura<=0 or altura > 10 or altura<=0:
                print('Medidas inválidas de tabuleiro, por favor digite novamente!')
                tabuleiro = input('Qual o tamanho do tabuleiro que os jogadores vão utilizar?(limite de 10x10, digite os números de largura e altura respectivamente, separados por espaço): ').split(' ')
            matrizGame = []
            qtdLinhas = 0

            #criacao do tabuleiro(matriz)
            while qtdLinhas < altura:
                qtdCol = 0
                linha = []
                while qtdCol < largura:
                    linha.append(0)
                    qtdCol+=1
                matrizGame.append(linha)
                qtdLinhas+=1

            mostraMatriz(matrizGame)

            # Decidindo qual jogador começa

            print('Para decidir qual jogador irá iniciar faremos um sorteio... ')
            sorteio = random.randint(-1,1)
            time.sleep(3)
            print('E o jogador que iniciará será...')
            time.sleep(3)
            if sorteio == 0:
                print('* Jogador 1! Você começa e ficará com as peças de número 1!')
                vez = 0
            else:
                print('* Jogador 2! Você começa e ficará com as peças de número 2!')
                vez = 1

            #iniciando o jogo
            espacosVazios = altura * largura
            while espacosVazios >= 0:
                if vez%2==0:
                    jogada(1,matrizGame)
                else:
                    jogada(2,matrizGame)
                vez+=1

                #condicao mínima para uma vitoria é de pelo menos 7 jogadas (4 do vencedor e 3 do perdedor)
                #inicia-se as verificacoes
                if vez >= 7:




                
                        
                

            


    else:
        xxx = 0








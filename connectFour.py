#connect Four

import random
import time


#=================== FUNCOES PARA O JOGO =================#

#mostra o tabuleiro para os jogadores
def mostraMatriz(matriz):
    print('-'*20)  
    for lin in matrizGame:
        for el in lin:
            print(el, end=' ')
        print('')
    print('-'*20)   


#faz a jogada 
def jogada(jogador,matriz):

    linhaJogada = len(matriz) - 1

    #jogador 1
    if jogador == 1: 
        coluna = int(input('Jogador 1, escolha a coluna que deseja colocar a peça!: '))
        while linhaJogada >= 0:
            if matriz[linhaJogada][coluna] == 0:
                matriz[linhaJogada][coluna] = 1
                break
            linhaJogada -=1
    #jogador 2
    else:
        coluna = int(input('Jogador 2, escolha a coluna que deseja colocar a peça!: '))
        while linhaJogada >= 0:
            if matriz[linhaJogada][coluna] == 0:
                matriz[linhaJogada][coluna] = 2
                break
            linhaJogada -=1
    mostraMatriz(matriz)



#funcoes para fazer as analises de possiveis jogadas vencedoras
def analiseLinhaColuna(jogador,matriz):
    if jogador == 1:
    #analise de linhas jogador 1
        for linha in matriz:
            rep = 0
            for el in linha:
                if el == 1:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0
    #analise de colunas jogador 1
        col = 0
        while col < len(matriz[0]):
            for linha in matriz:
                if linha[col] == 1:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0   
            col +=1

    #analise de diagonais jogador 1
        diag = 0




    else:
    #analise de linhas jogador 2
        for linha in matriz:
            rep = 0
            for el in linha:
                if el == 2:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0
    #analise de colunas jogador 2
        col = 0
        while col < len(matriz[0]):
            for linha in matriz:
                if linha[col] == 2:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0 
            col +=1     

    return False
#=================== FUNCOES PARA O JOGO =================#







#===================INICIO CODIGO JOGO=================#

jogarNovamente = True

while jogarNovamente:

    #menu
    menu = input("Olá, bem vindo ao Ligue 4! Como deseja jogar?(digite 1 ou 2):\n 1 - Jogador X Jogador\n 2 - Jogador X Computador\n ")
    while menu not in '12':
        menu = input("Digite apenas 1 ou 2 para selecionar as opções!\n")

    winner = False

    if menu == '1':  
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


        print('-'*20)    
        print('Este é o tabuleiro da sua partida! Que vença o melhor! ')  
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
            #condicao mínima para uma vitoria é de pelo menos 7 jogadas (4 do vencedor e 3 do perdedor)
            #inicia-se as verificacoes
            if vez >= 7:
                if vez % 2 ==0:
                    if analiseLinhaColuna(1,matrizGame):
                        print('==== Jogador 1 venceu! ====')
                        break
                else:
                    if analiseLinhaColuna(2,matrizGame):
                        print('==== Jogador 2 venceu! ====')
                        break
            vez+=1
            espacosVazios-=1
        if espacosVazios == 0:
            print('Nenhum dos jogadores chegaram na vitória e os espaços acabaram! EMPATE!')
    else:
        xxx = 0    

    #pergunta se o jogador deseja reiniciar o jogo                   
    jogarNovamente = input('Deseja jogar novamente?:\n 1 - SIM\n 2 - NAO\n ')
    if jogarNovamente in ['1','sim','SIM']:
        jogarNovamente = True
    elif jogarNovamente in ['2','nao','NAO']:
        jogarNovamente = False
    else:
        print('Opção inválida, jogo finalizado.')



                
                        
                

    


#===================FIM CODIGO JOGO=================#







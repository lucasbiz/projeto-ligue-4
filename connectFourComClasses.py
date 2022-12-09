#connect Four

import random #sorteia quem vai jogar primeiro
import time #faz as pausas dramáticas

#CLASSE QUE CRIA O TABULEIRO
class gameStart():

    def __init__(self):
        #cria uma matriz vazia
        self.tabuleiro = [] 

    #cria um tabuleiro com as dimensoes escolhidas pelo jogador
    def criaTab(self, larg, alt):

        self.largura = int(larg)
        self.altura = int(alt)
        #verificacao de dimencoes do tabuleiro
        while self.largura > 10 or self.largura<4 or self.altura > 10 or self.altura<4:
            print('Medidas inválidas de tabuleiro, por favor digite novamente!')
            self.tabuleiro = input('Qual o tamanho do tabuleiro que os jogadores vão utilizar?(limite de 10x10, digite os números de largura e altura respectivamente, separados por espaço): ').split(' ')
        qtdLinhas = 0

        #criacao do tabuleiro(matriz)
        while qtdLinhas < self.altura:
            qtdCol = 0
            linha = []
            while qtdCol < self.largura:
                linha.append(0)
                qtdCol+=1
            self.tabuleiro.append(linha)
            qtdLinhas+=1

        print('-'*20)    
        print('Este é o tabuleiro da sua partida! Que vença o melhor! ')  
        self.mostraTab()

    #mostra o tabuleiro
    def mostraTab(self):
        print('-'*20)  
        for lin in self.tabuleiro:
            for el in lin:
                print(el, end=' ')
            print('')
        print('-'*20)






#CLASSE QUE FAZ O JOGO FUNCIONAR
class gameFunctions():
    
    def __init__(self):
        # Decidindo qual jogador começa
        print('Para decidir qual jogador irá iniciar faremos um sorteio... ')
        sorteio = random.randint(0,1)
        time.sleep(2)
        print('E o jogador que iniciará será...')
        time.sleep(2)
        if sorteio == 0:
            print('* Jogador 1! Você começa e ficará com as peças de número 1!')
            self.vez = 0
        else:
            print('* Jogador 2! Você começa e ficará com as peças de número 2!')
            self.vez = 1


    def game(self,tab,modo):
        #iniciando o jogo
        #verifica quantos espacos vazios tem no tabuleiro para anunciar possiveis empates
        #executa a funcao jogada de acordo com a vez correspondente
        espacosVazios = len(tab[0]) * len(tab)
        while espacosVazios >= 0:
            if self.vez%2==0:
                self.jogada(1,tab)
            else:
                if modo == 1:
                    self.jogada(2,tab)
                else:
                    self.jogada(3,tab)
        #condicao mínima para uma vitoria é de pelo menos 7 jogadas (4 do vencedor e 3 do perdedor)
        #inicia-se as verificacoes
            if self.vez >= 6:
                if self.vez % 2 ==0:
                    if self.analiseLinhaColuna(1,tab) or self.analiseDiag(1,tab):
                        print('==== Jogador 1 venceu! ====')
                        break
                else:
                    if self.analiseLinhaColuna(2,tab) or self.analiseDiag(2,tab):
                        print('==== Jogador 2 venceu! ====')
                        break
            self.vez+=1
            espacosVazios-=1
        if espacosVazios == 0:
            print('Nenhum dos jogadores chegou na vitória e os espaços acabaram! EMPATE!')

    def jogada(self,jogador,matriz):
        validacao = 0
        #computador faz a jogada
        if jogador == 3:
            while validacao == 0:
                time.sleep(1)
                coluna = random.randint(0,len(matriz)-1)
                print(f'Jogador 2 escolhe a coluna {coluna}')
                linhaJogada = len(matriz) - 1
                while linhaJogada >= 0:
                    if matriz[linhaJogada][coluna] == 0:
                        matriz[linhaJogada][coluna] = 2
                        validacao = 1
                        break
                    linhaJogada -=1
                if validacao == 0:
                    print('Jogada inválida, tente novamente!')
        #jogador faz a jogada
        else:
            while validacao == 0:
                coluna = int(input(f'Jogador {jogador}, escolha a coluna que deseja colocar a peça!: '))
                while coluna < 0 or coluna >= len(matriz[0]):
                    print('Número de coluna inválido, tente novamente!')
                    coluna = int(input(f'Jogador {jogador}, escolha a coluna que deseja colocar a peça!: '))
                linhaJogada = len(matriz) - 1
                while linhaJogada >= 0:
                    if matriz[linhaJogada][coluna] == 0:
                        matriz[linhaJogada][coluna] = jogador
                        validacao = 1
                        break
                    linhaJogada -=1
                if validacao == 0:    
                    print('Coluna cheia, tente novamente!')

        #mostra o tabuleiro de uma forma didatica ao jogador
        print('-'*20)  
        for lin in matriz:
            for el in lin:
                print(el, end=' ')
            print('')
        print('-'*20)

    #funcoes de verificacao procuram se o numero de caracteres 1(jogador 1) ou 2(jogador 2) se repetem 
    #nas linhas, colunas ou diagonalmente, 4 caracteres iguais seguidos caracterizam uma vitoria
    def analiseLinhaColuna(self,jogador,matriz):
        #analise de linhas 
        for linha in matriz:
            rep = 0
            for el in linha:
                if el == jogador:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0
        #analise de colunas 
        col = 0
        rep = 0
        while col < len(matriz[0]):
            for linha in matriz:
                if linha[col] == jogador:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0   
            col +=1
        return False



    #funcao analise diagonais
    def analiseDiag(self,jogador,matriz):

        #analisa diagonal principal para baixo (sem contar a principal)
        cont = 1
        rep = 0
        while cont <len(matriz):
            col = 0
            linhaIni = cont
            while linhaIni < len(matriz):
                if matriz[linhaIni][col] ==jogador:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0
                col +=1
                linhaIni += 1
            cont +=1

        #analisa diagonal principal para cima (contando com a principal)
        cont = 0
        rep = 0
        while cont < len(matriz):
            col = len(matriz) - 1
            linhaIni = cont
            while linhaIni >= 0:
                if matriz[linhaIni][col] ==jogador:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0
                col -=1
                linhaIni -= 1
            cont +=1

        #analisa diagonal secundária (da secunda para baixo contando com ela)
        cont = len(matriz) - 1
        rep = 0
        while cont >= 0:
            col = 0
            linhaIni = cont
            while linhaIni >= 0:
                if matriz[linhaIni][col] ==jogador:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0 
                col +=1
                linhaIni -= 1
            cont -=1


        #analisa diagonal secundária (da secunda para cima sem contar com ela)
        cont = 0
        rep = 0
        while cont < len(matriz)-1:
            col = 0
            linhaIni = cont
            while linhaIni >= 0:
                if matriz[linhaIni][col] ==jogador:
                    rep +=1
                elif rep == 4:
                    return True
                else:
                    rep = 0
                col +=1
                linhaIni -= 1
            cont +=1
        return False




#===================INICIO DO JOGO=================#


jogarNovamente = True

while jogarNovamente:

    #menu
    menu = input("Olá, bem vindo ao Ligue 4! Como deseja jogar?(digite 1 ou 2):\n 1 - Jogador X Jogador\n 2 - Jogador X Computador\n ")
    while menu not in '12':
            menu = input("Digite apenas 1 ou 2 para selecionar as opções!\n")

    medidas = input('Qual o tamanho do tabuleiro que os jogadores vão utilizar?(limite de 10x10, digite os números de largura e altura respectivamente, separados por espaço): ').split(' ')
    while len(medidas) <2:
        medidas = input('Tamanho incorreto! Digite novamente!(limite de 10x10, digite os números de largura e altura respectivamente, separados por espaço): ').split(' ')

    matriz = gameStart()
    matriz.criaTab(int(medidas[0]),int(medidas[1]))

    jogar = gameFunctions()
    jogar.game(matriz.tabuleiro,int(menu))


    #pergunta se o jogador deseja reiniciar o jogo                   
    jogarNovamente = input('Deseja jogar novamente?:\n 1 - SIM\n 2 - NAO\n ')
    if jogarNovamente in ['1','sim','SIM']:
        jogarNovamente = True
    elif jogarNovamente in ['2','nao','NAO']:
        jogarNovamente = False
    else:
        print('Opção inválida, jogo finalizado.')



#===================FIM DO JOGO =D =================#
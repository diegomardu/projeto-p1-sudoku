from random import randint
def inicio_jogo(matriz,nivel,jogador):
    lista =[[0,0,0,0,0,0,0,0,0],  # essa lista servirá para atualizar a interface a cada jogada.
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0]]

    copia_lista =[[0,0,0,0,0,0,0,0,0], # essa lista vai receber os numeros que servem de dicas 
                  [0,0,0,0,0,0,0,0,0], # e ser usada para quando o jogador tentar alterar os numeros que servem de dicas nao conseguir.
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0]]

    lista_comparacao =[[0,0,0,0,0,0,0,0,0], # essa lista servirá para comparar com a lista1 e ver se o jogador concluiu o jogo.
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0]]


    if nivel == 1:
        sudoku_dicas = 35
    elif nivel == 2:
        sudoku_dicas = 25
    else:
        sudoku_dicas = 15
    n = 0
    i = 0
    while n < sudoku_dicas: # preenche a tabela zerada , com numeros aleatórios para servirem de dicas.
        t = randint(0, 8)
        v = "═ ",str(matriz[i][t])," ═"
        j = "".join(v)
        lista[i][t] = j
        copia_lista[i][t] = matriz[i][t]
        lista_comparacao[i][t] = matriz[i][t]
        n = n + 1
        if i < len(lista) - 1:
            i = i + 1
        else:
            i = 0
    sudoku = interface(lista) #mostra a tabela com os numeros que servem de dicas
    resultado = False
    tentativas = 0
    while resultado == False:
        jogar = input(" Continuar jogando?(1-Sim 2-Não):")
        if jogar == "1":
            tentativas = tentativas + 1
            try:
                coluna = int(input(" Digite o numero da coluna:"))
                linha = int(input(" Digite o numero da linha :"))
                if coluna and linha > 0:
                    while True:
                        if copia_lista[linha - 1][coluna - 1] != 0:
                            print(" Linha e coluna escolhida possui numero fixo que serve como dica e nao pode ser alterado, escolha outra linha e coluna ")
                            coluna = int(input(" Digite o numero da coluna:"))
                            linha = int(input(" Digite o numero da linha :"))
                        elif copia_lista[linha - 1][coluna - 1] == 0:
                            numero = int(input(" Digite o numero para a posiçao escolhida:"))
                            numero1 = str(numero)
                            if numero > 0 and numero <= 9:
                                lista_comparacao[linha - 1][coluna - 1] = numero1
                                letra = "  ",numero1,"  "
                                juntar = "".join(letra)
                                lista[linha - 1][coluna - 1] = juntar
                                break
                            else:
                                print(" VALOR INVÁLIDO , ESCOLHA UM NÚMERO ENTRE 1 e 9")
                            
                else:
                    print("\n                VALOR INVÁLIDO , ESCOLHA UM NÚMERO ENTRE 1 e 9")

                interface(lista) # atualiza a interface a cada jogada
                if lista_comparacao == matriz:
                    recorde(jogador,nivel,tentativas)
                    print(" ----- Parabéns",jogador,"------")
                    resultado = True

            except:
                print(" Valor Invalido!!!")
        
        elif jogar == "2":
            print(" Até logo %s você realizou %s jogada(s)"%(jogador,tentativas))
            break
        else:
            print(" Por favor digite o número 1 ou 2")

def nivel(n):#Função que define nivel de dificuldade do jogo.
    if n == 1:
        sudoku_resposta = 0 #Variavel recebera a matriz 9x9 "gabarito"
        op = randint(1,3)
        matriz = {1:[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]],
                  2:[["8","7","1","4","5","3","9","2","6"],["9","5","3","7","2","6","4","8","1"],["2","4","6","8","9","1","5","3","7"],["7","6","5","3","8","9","1","4","2"],["1","3","2","5","4","7","8","6","9"],["4","9","8","1","6","2","7","5","3"],["6","8","7","9","3","5","2","1","4"],["5","2","9","6","1","4","3","7","8"],["3","1","4","2","7","8","6","9","5"]],
                  3:[["3","5","2","4","7","6","8","1","9"],["1","6","8","3","5","9","4","7","2"],["4","9","7","8","2","1","6","3","5"],["2","4","5","9","6","7","3","8","1"],["9","8","6","1","4","3","5","2","7"],["7","3","1","2","8","5","9","6","4"],["6","2","3","7","9","4","1","5","8"],["5","7","9","6","1","8","2","4","3"],["8","1","4","5","3","2","7","9","6"]]}
        for i in matriz:
            if op == i:
                sudoku_resposta = (matriz[i])
                break
        return sudoku_resposta
    elif n == 2:
        sudoku_resposta = 0 #Variavel recebera a matriz 9x9 "gabarito"
        op = randint(1,3)

        matriz = {1:[["9","6","3","8","2","7","5","4","1"],["8","1","5","4","6","9","2","3","7"],["2","7","4","1","5","3","8","9","6"],["4","8","7","2","9","5","6","1","3"],["6","3","2","7","8","1","9","5","4"],["1","5","9","6","3","4","7","8","2"],["3","9","1","5","7","2","4","6","8"],["5","2","8","3","4","6","1","7","9"],["7","4","6","9","1","8","3","2","5"]],
                  2:[["8","9","2","5","7","3","6","1","4"],["7","4","6","9","2","1","8","3","5"],["3","1","5","4","6","8","9","7","2"],["4","5","7","6","8","2","3","9","1"],["9","6","8","1","3","5","2","4","7"],["1","2","3","7","4","9","5","6","8"],["2","7","1","8","9","6","4","5","3"],["5","3","9","2","1","4","7","8","6"],["6","8","4","3","5","7","1","2","9"]],
                  3:[["7","9","2","5","6","4","1","3","8"],["5","3","8","1","9","2","6","7","4"],["6","4","1","8","3","7","2","9","5"],["2","8","5","4","1","9","7","6","3"],["9","6","4","7","5","3","8","2","1"],["1","7","3","2","8","6","4","5","9"],["3","2","9","6","4","8","5","1","7"],["8","5","6","3","7","1","9","4","2"],["4","1","7","9","2","5","3","8","6"]]}
        for i in matriz:
            if op == i:
                sudoku_resposta = (matriz[i])
                break
        return sudoku_resposta
    elif n == 3:
        sudoku_resposta = 0 #Variavel recebera a matriz 9x9 "gabarito"
        op = randint(1,3)
        matriz = {1:[["5","8","1","7","9","2","6","4","3"],["7","9","2","6","3","4","8","1","5"],["4","3","6","5","1","8","2","9","7"],["9","5","8","1","4","7","3","6","2"],["2","6","7","3","5","9","1","8","4"],["3","1","4","2","8","6","5","7","9"],["6","4","5","9","2","1","7","3","8"],["1","2","9","8","7","3","4","5","6"],["8","7","3","4","6","5","9","2","1"]],
                  2:[["8","4","2","7","3","9","1","5","6"],["9","5","3","1","2","6","8","7","4"],["1","7","6","5","4","8","2","3","9"],["3","8","4","6","1","2","7","9","5"],["7","1","9","8","5","3","6","4","2"],["6","2","5","9","7","4","3","1","8"],["5","9","8","3","6","7","4","2","1"],["4","6","7","2","9","1","5","8","3"],["2","3","1","4","8","5","9","6","7"]],
                  3:[["7","4","1","6","9","8","3","2","5"],["5","3","8","2","4","1","6","7","9"],["9","2","6","3","7","5","4","1","8"],["4","1","3","8","2","6","9","5","7"],["2","6","7","5","3","9","8","4","1"],["8","5","9","4","1","7","2","3","6"],["1","9","2","7","8","3","5","6","4"],["3","7","5","9","6","4","1","8","2"],["6","8","4","1","5","2","7","9","3"]]}
        for i in matriz:
            if op == i:
                sudoku_resposta = (matriz[i])
                break
        return sudoku_resposta


def interface(lista):# funçao recebe uma lista de listas que no caso é a matriz e verifica cada posiçao.
                     # caso seja igual a "0" exibe um quadrado vazio , caso tenha numero, exibe um quadrado com o numero.

    z = 1              
    y = 0 # servirá para andar em todas as listas  
    x = 0
    l = 1
    print("   C1 ","     C2","    C3","       C4","     C5""      C6","       C7","      C8","     C9")  # coluna
    
    while x < len(lista): # loop onde será passado por cada posiçao das listas e atribuido a variável 
        a = lista[y][0]   # aqui a variável receberá o valor que está na posiçao solicitada
        b = lista[y][1]
        c = lista[y][2]
        d = lista[y][3]
        e = lista[y][4]
        f = lista[y][5]
        g = lista[y][6]
        h = lista[y][7]
        i = lista[y][8]
        if a == 0:          #condiçao caso a variável receba valor zero na lista ,o  valor será subtituido por espaço vazio.
            a = "     "
        if b == 0:
            b = "     "
        if c == 0:
            c = "     "
        if d == 0:
            d = "     "
        if e == 0:
            e = "     "
        if f == 0:
            f = "     "
        if g == 0:
            g = "     "
        if h == 0:
            h = "     "
        if i == 0:
            i = "     "
        
        print(" ╔═════╗"*3,""," ╔═════╗"*3,""," ╔═════╗"*3) # exibe a parte de cima de cada quadrado onde a cada 3 vezes dá um espaço até completar 9 quadrados
        j =" ║",str(a),"║"," ║",str(b),"║"," ║",str(c),"║","","   ║",str(d),"║ ","║",str(e),"║"," ║",str(f),"║ ","","  ║",str(g),"║"," ║",str(h),"║"," ║",str(i),"║"," L",str(l) #parte do meio do quadrado onde terá o numero  
        m = "".join(j)  # junta a parte do meio do quadrado com o numero da variável
        print(m)        # imprimi m que possui a parte do meio pronta
        print(" ╚═════╝"*3,""," ╚═════╝"*3,""," ╚═════╝"*3)
        if z == 3: # dá uma espaço a cada 3 linhas 
            print(" ")
            z = 0 # zera quando chega em 3 enquanto o loop continuar
        z = z + 1
        x = x + 1
        y = y + 1 
        l = l + 1 # exibirá numero da linha
        
def menu():#funçao menu onde mostra as opçoes para o jogador 
    print("""    ╔═══════════════════════════════════ BEM-VINDO AO JOGO SUDOKU ══════════════════════════════════╗
    ║                                                                                               ║
    ║                                    ╔═════╗ ╔═════╗ ╔═════╗                                    ║
    ║                                    ║     ║ ║     ║ ║     ║                                    ║
    ║                                    ╚═════╝ ╚═════╝ ╚═════╝                                    ║
    ║                                    ╔═════╗ ╔═════╗ ╔═════╗                                    ║
    ║                                    ║     ║ ║     ║ ║     ║                                    ║
    ║                                    ╚═════╝ ╚═════╝ ╚═════╝                                    ║
    ║                                    ╔═════╗ ╔═════╗ ╔═════╗                                    ║
    ║                                    ║     ║ ║     ║ ║     ║                                    ║
    ║                                    ╚═════╝ ╚═════╝ ╚═════╝                                    ║
    ║                                ╔═════════════════════════════╗                                ║
    ║                                ║ESCOLHA UMA DAS OPÇÕES ABAIXO║                                ║
    ║                                ╚═════════════════════════════╝                                ║
    ║═══════════════════════════════════════════════════════════════════════════════════════════════║
    ║  1-INICIAR JOGO  ║   2-AJUDA E INFORMAÇÕES  ║   3-CLASSIFICAÇÕES   ║ 4-CRÉDITOS   ║   5-SAIR  ║
    ╚═══════════════════════════════════════════════════════════════════════════════════════════════╝                          """)
    
    while True: # gerando um loop para que o jogador digite umas das opçoes de 1 a 4 .
        try:
            escolha = int(input("    |-> "))
            if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4 or escolha == 5: # se a escolha for de 1 a 5 encerra o loop e retornará a variável escolha
                break
            else:
                print("Valor Invalido!!!")  # caso diferente de 1 a 5  aparecerá valor inválido e retorna para o loop
        except ValueError:
            print("Valor Invalido!!!")
    
    return escolha 
    
def jogar ():
    while True:
        try:
            n = int(input("    SELECIONAR NÍVEL(1-INICIANTE 2-MÉDIO 3-AVANÇADO):"))
            if n == 1 or n == 2 or n == 3:
                break
            else:
                print("Valor Invalido!!!")
        except ValueError:
            print("Valor Invalido!!!")
    return n

def ajuda():
    print("""
    NO JOGO SUDOKU VOCÊ DEVERÁ COMPLETAR TODAS AS 81 CÉLULAS USANDO NÚMEROS DE 1 A 9,
    SEM REPETIR OS NÚMEROS NUMA MESMA LINHA, COLUNA E GRADE(3x3).
    PARA JOGAR BASTA APENAS DIGITAR O NÚMERO DA COLUNA E DA LINHA QUE DESEJA PREENCHER
    EXISTEM NÚMEROS NA TABELA QUE SERVEM DE DICAS ASSIM QUE INICIA O JOGO , ESSES NÚMEROS ESTÃO MARCADOS COM UM TRAÇO DE CADA LADO E
    NAO PODERÃO SER ALTERADOS.
    O JOGO POSSUI 3 NÍVEIS ,INICIANTE,MÉDIO E AVANÇADO,QUANTO MAIOR O NÍVEL MENOS NÚMEROS QUE SERVEM DE DICAS IRÃO APARECER.
    
    COLUNA: ╔═════╗         LINHA: ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗  GRADE(3x3): ╔═════╗ ╔═════╗ ╔═════╗
            ║═ 1 ═║                ║  3  ║ ║  6  ║ ║  4  ║ ║═ 8 ═║              ║  9  ║ ║  5  ║ ║═ 7 ═║
            ╚═════╝                ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝              ╚═════╝ ╚═════╝ ╚═════╝ 
            ╔═════╗                                                             ╔═════╗ ╔═════╗ ╔═════╗  
            ║  5  ║                                                             ║  4  ║ ║  2  ║ ║  6  ║
            ╚═════╝                                                             ╚═════╝ ╚═════╝ ╚═════╝ 
            ╔═════╗                                                             ╔═════╗ ╔═════╗ ╔═════╗ 
            ║  2  ║                                                             ║═ 8 ═║ ║  3  ║ ║  1  ║
            ╚═════╝                                                             ╚═════╝ ╚═════╝ ╚═════╝
            ╔═════╗
            ║═ 7 ═║
            ╚═════╝ 
   APÓS COMPLETAR TODA A TABELA CORRETAMENTE , VOCÊ FICARÁ SABENDO QUANTAS JOGADAS DEMOROU PARA TERMINAR O JOGO
   E SEU NOME FICARÁ NA LISTA DE CLASSIFICAÇAO DOS JOGADORES.


   Aperte ENTER , ou qualquer caracter e ENTER a qualquer momento para voltar para o menu""")

    input()

def creditos():
    print("""           \_______________________________________________________________________________________________/
            |                                                                                             | 
            |-------INSTITUTO FEDERAL DE EDUCAÇÃO,CIÊNCIA E TECNOLOGIA CAMPUS – CAMPINA GRANDE – PB       |
            |-------CURSO – TELEMÁTICA  2018.2                                                            |
            |-------DISCIPLINA – PROGRAMAÇAO I                                                            |
            |                                                                                             |
            |-------PROJETO DO JOGO SUDOKU ELABORADO PELOS ALUNOS:                                        |
            |-------FELIPE OLIVEIRA DE FARIAS                                                             |
            |-------DIEGO MARTINS DUARTE                                                                  |
            |                                                                                             |
            |-------PROFESSORA:                                                                           |
            |-------ELAINE CRISTINA JUVINO DE ARAUJO                                                      |
           \|_____________________________________________________________________________________________|/
           
    Aperte ENTER , ou qualquer caracter e ENTER a qualquer momento para voltar para o menu""")
    input()

def recorde(a,b,c):
    arquivo = open("record.txt","a")
    arquivo.write("Jogador:%s\nNivel:%s\nJogadas:%s"%(a,b,c))
    arquivo.close()
    
def classificacoes():
    arquivo = open("record.txt","r")
    print(arquivo.read())
    arquivo.close()

from functions import  *
import sys

while True:
    escolha = menu()
    if escolha == 1:
        jogador = input("    INFORME NOME DO JOGADOR:")
        selecao_nivel = jogar()
        sudoku_resposta = nivel(selecao_nivel)
        sudoku_dicas0 = selecao_nivel
        lista1 = sudoku_resposta
        inicio_jogo(lista1,sudoku_dicas0,jogador)
    elif escolha == 2:
        ajuda()
    elif escolha == 3:
        classificacoes()
    elif escolha == 4:
        creditos()
    elif escolha == 5:
        sys.exit()
        












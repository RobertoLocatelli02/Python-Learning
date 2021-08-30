from jogoDaVelha import criarBoard, fazMovimento, getInputValido, printBoard, verificaGanhador, verificaMovimento
from minimax import getPosicoes, movimentoIA, minimax

jogador = 0
board = criarBoard()
ganhador = verificaGanhador(board)
while(not ganhador):
    printBoard(board)
    print()
    
    if jogador == 0:
        i, j = movimentoIA(board, jogador)
    else:
        i = getInputValido("Digite a linha: ")
        j = getInputValido("Digite a coluna: ")
    
    if(verificaMovimento(board, i, j)):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("A posição informada já está ocupada.")
    
    ganhador = verificaGanhador(board)


print("=" * 15)
printBoard(board)
print("Ganhador = ", ganhador)
print("=" * 15)
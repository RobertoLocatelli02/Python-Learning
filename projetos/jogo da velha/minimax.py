from jogoDaVelha import blank, token, verificaGanhador

def movimentoIA(board, jogador):
    possibilidades = getPosicoes(board)
    melhorValor = None
    melhorMovimento = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = blank
        #print(possibilidade, valor)
        if melhorValor is None:
            melhorValor = valor
            melhorMovimento = possibilidade
        elif jogador == 0:
            if valor > melhorValor:
                melhorValor = valor
                melhorMovimento = possibilidade
        elif jogador == 1:
            if valor < melhorValor:
                melhorValor = valor
                melhorMovimento = possibilidade


    return melhorMovimento[0], melhorMovimento[1]

def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == blank:
                posicoes.append([i, j]) 
    
    return posicoes

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}

def minimax(board, jogador):
    ganhador = verificaGanhador(board)
    if(verificaGanhador(board)):
        if(ganhador):
            return score[ganhador]

    jogador = (jogador + 1) % 2

    melhorValor = None
    possibilidades = getPosicoes(board)
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = blank

        if melhorValor is None:
            melhorValor = valor
        elif jogador == 0:
            if valor > melhorValor:
                melhorValor = valor
        elif jogador == 1:
            if valor < melhorValor:
                melhorValor = valor

    return melhorValor
from typing import Sized
import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

from jogoDaVelha import criarBoard, fazMovimento, getInputValido, printBoard, verificaGanhador, verificaMovimento
from minimax import movimentoIA

pygame.font.init()

def drawBoard(win, board):
    height = 600
    width = 600
    tamanho = 600 / 3

    for i in range(1, 3):
        pygame.draw.line(win, (0,0,0), (0, i * tamanho), (width, i * tamanho), 3)
        pygame.draw.line(win, (0,0,0), (i * tamanho, 0), (i * tamanho, height), 3)

    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("comicsans", 100)

            x = j * tamanho
            y = i * tamanho

            text = font.render(board[i][j], 1, (0, 0, 128))
            win.blit(text, ((x + 75), (y + 75)))

def redraw_window(win, board):
    win.fill((255, 255, 255))
    drawBoard(win, board)

def main():
    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Jogo Da Velha")

    board = criarBoard()

    redraw_window(win, board)
    pygame.display.update()

    jogador = 0
    
    ganhador = verificaGanhador(board)
    
    while(not ganhador):
        printBoard(board)
        
        if jogador == 0:
            jogou = False
            while not jogou:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        return
                    elif event.type == pygame.MOUSEBUTTONUP:
                        posicao = pygame.mouse.get_pos()
                        i = int(posicao[1] / 200)
                        j = int(posicao[0] / 200)
                        jogou = True
        else:
            i, j = movimentoIA(board, jogador)
        
        if(verificaMovimento(board, i, j)):
            fazMovimento(board, i, j, jogador)
            jogador = (jogador + 1) % 2
        
        ganhador = verificaGanhador(board)

        redraw_window(win, board)
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

main()

import pygame
import sys
from pygame.locals import *
from config.config import xred, yred, xgreen, ygreen, ared, lred, tela
import sprites.redSprite.movement as movement
import sprites.redSprite.red as redSquare
import sprites.greenSprite.green as greenSquare
import sprites.obstaculos as obstaculos

pygame.init() #Inicia o jogo
clock = pygame.time.Clock()
running = True
colisao = False






while running: #Quando der o play
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    tela.fill("white")

    for obstaculo in obstaculos.obstaculos: # Desenhando os obstáculos
        pygame.draw.rect(tela, (255, 0, 0), obstaculo)

    redSquare.redSquare.x = xred # Atualizando as posições do redSquare
    redSquare.redSquare.y = yred

   
    pygame.draw.rect(tela, (255, 0, 0), redSquare.redSquare)  # Quadrado vermelho
    pygame.draw.rect(tela, (0, 255, 0), greenSquare.greenSquare)  # Quadrado verde


    xred, yred = movement.movementKeys(xred, yred) #Movimentação pelas teclas 
    xred, yred, ared, lred = movement.movementBoundary(xred, yred, ared, lred) #Limites da tela
    xred, yred, colisao = movement.walls(obstaculos, redSquare.redSquare, xred, yred, colisao) # Verifica colisões com obstáculos
    
    redSquare.redSquare, greenSquare, running = movement.greenSquareTaken(redSquare.redSquare, greenSquare, running)
    # Verifica se o quadrado verde foi pego

    pygame.display.flip() #Atualiza a tela
    clock.tick(60)  # Limita o FPS para 60

pygame.quit() #Fecha o jogo

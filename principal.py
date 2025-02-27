import pygame
import sys
from pygame.locals import *
from config.config import xred, yred, ared, lred, tela
import sprites.redSprite.movement as movement
import sprites.redSprite.red as redSquare
import sprites.greenSprite.green as greenSquare
import sprites.obstaculos as obstaculos

pygame.init()
clock = pygame.time.Clock()
running = True
colisao = False

# Definindo o quadrado verde
x_green = 315
y_green = 420

# Criando o retângulo verde
greenSquare = pygame.Rect(x_green, y_green, ared, lred)

# Lista de obstáculos (representados como pygame.Rect para colisão)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    

    tela.fill("white")

    # Desenhando os obstáculos (linhas representadas como retângulos)
    for obstaculo in obstaculos.obstaculos:
        pygame.draw.rect(tela, (255, 0, 0), obstaculo)

    # Atualizando as posições do redSquare
    redSquare.redSquare.x = xred
    redSquare.redSquare.y = yred

    # Desenhando os quadrados na tela
    pygame.draw.rect(tela, (255, 0, 0), redSquare.redSquare)  # Quadrado vermelho
    pygame.draw.rect(tela, (0, 255, 0), greenSquare)  # Quadrado verde

    # Movimentação
    xred, yred = movement.movementKeys(xred, yred)  
    xred, yred, ared, lred = movement.movementBoundary(xred, yred, ared, lred)

    # Verifica colisões com obstáculos
    xred, yred, colisao = movement.walls(obstaculos, redSquare.redSquare, xred, yred, colisao)

    # Verifica se o quadrado verde foi pego
    redSquare.redSquare, greenSquare, running = movement.greenSquareTaken(redSquare.redSquare, greenSquare, running)

    pygame.display.flip()
    clock.tick(60)  # Limita o FPS para 60

pygame.quit()

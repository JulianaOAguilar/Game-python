import pygame
from pygame.locals import *
from .red import redSquare
from sprites.greenSprite.green import greenSquare
import sprites.obstaculos as obstaculos

#essa seção indica tudo que tem a ver com movimento do sprite vermelho

def movementKeys(xred, yred): # Movimento pelas teclas
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        xred -= 5
    if keys[K_RIGHT]:
        xred += 5
    if keys[K_UP]:
        yred -= 5 
    if keys[K_DOWN]:
        yred += 5
    return xred, yred

def movementBoundary(x, y, a, l): # Limites da tela
    if x < 0:
        x = 0
    if x > 460 - a:
        x = 460 - a
    if y < 0:
        y = 0
    if y > 460 - l:
        y = 460 - l
    return x, y, a, l

def walls(obstaculos, redSquare, x, y, colisao): # Se tocar em qualquer obstáculo
    for obstaculo in obstaculos.obstaculos:
        if redSquare.colliderect(obstaculo):
            x = 10
            y = 10  
            colisao = True
            break
    return x, y, colisao
        
def greenSquareTaken(redSquare, greenSquare, running): # Se tocar no quadrado verde
    if redSquare.colliderect(greenSquare.greenSquare):
            print("Você venceu!")
            pygame.time.delay(2000)  
            running = False
    return redSquare, greenSquare, running
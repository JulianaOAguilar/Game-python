import pygame
import sys
from pygame.locals import *
import teste


pygame.init()
tela = pygame.display.set_mode((460, 460))
clock = pygame.time.Clock()
running = True
x_red = 10
y_red = 10
x_green = 315
y_green = 420
a_red = 20
l_red = 20
colisao = False
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tela.fill("purple")
    
    if x_red < 0:
        x_red = 0
    if x_red > 460 - a_red:
        x_red = 460 - a_red
    if y_red < 0:
        y_red = 0
    if y_red > 460 - l_red:
        y_red = 460 - l_red

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        x_red -= 5
    if keys[K_RIGHT]:
        x_red += 5
    if keys[K_UP]:
        y_red -= 5
    if keys[K_DOWN]:
        y_red += 5

    redSquare = pygame.draw.rect(tela, "red", (x_red, y_red, a_red, l_red))
    greenSquare = pygame.draw.rect(tela, "green", (x_green, y_green, a_red, l_red))

    
    obstaculos = [
    pygame.draw.line(tela, (255, 0, 0), (70, 200), (70, 0), 5),
    pygame.draw.line(tela, (255, 0, 0), (70, 200), (350, 200), 5),
    pygame.draw.line(tela, (255, 0, 0), (0, 250), (300, 250), 5),
    pygame.draw.line(tela, (255, 0, 0), (300, 450), (300, 250), 5), 
    pygame.draw.line(tela, (255, 0, 0), (350, 450), (350, 200), 5), 
    pygame.draw.line(tela, (255, 0, 0), (300, 450), (350, 450), 5),
    ]
    
    for obstaculo in obstaculos:
        if redSquare.colliderect(obstaculo):  # Se tocar em qualquer obstáculo
            x_red = 10
            y_red = 10  
            colisao = True
            break
    if redSquare.colliderect(greenSquare):
        tela.fill("green")
        print("Você venceu!")
        pygame.display.flip()  # Atualiza a tela para mostrar o verde
        pygame.time.delay(2000)  # Aguarda 2 segundos antes de fechar
        running = False
        
    
    
        
    pygame.display.flip()
    
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()
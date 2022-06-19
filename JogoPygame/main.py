import pygame
from pygame.locals import *
from sys import exit

pygame.init()

janela_largura = 640
janela_altura = 480

x = 0
y = 0

tela = pygame.display.set_mode((janela_largura, janela_altura))
pygame.display.set_caption('Era Of Magics')

while True:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255,0,0), (x,y,50,50))
    y = y + 1

    pygame.display.update()


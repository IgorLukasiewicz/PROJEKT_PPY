import pygame
from sys import exit


width = 1280
height = 720

pygame.init()

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Echo Pets')

window_icon = pygame.image.load('Assets\Images\Sprites\BushMonster.png')
pygame.display.set_icon(window_icon)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)


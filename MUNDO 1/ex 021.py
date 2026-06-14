import pygame
pygame.init()
#lembra desse momento  hoje é dia 16 de maio vc esta começando

pygame.mixer.music.load('nujabes.mpeg')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

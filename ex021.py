import pygame

pygame.init()

pygame.mixer.music.load('ex021/ex021.mp3')
pygame.mixer.music.play()

tela = pygame.display.set_mode([100, 100])

loop = True
while loop:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False

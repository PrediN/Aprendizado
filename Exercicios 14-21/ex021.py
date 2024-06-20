# Executor de arquivo mp3
import pygame

# Iniciando pygame

pygame.init()

# Chamando a faixa de audio

pygame.mixer.music.load('arq01.mp3')

# Inicio na faixa de audio

pygame.mixer.music.play()
input()
pygame.event.wait()

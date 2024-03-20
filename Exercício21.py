import pygame

pygame.init()
pygame.mixer.music.load('Exercício21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
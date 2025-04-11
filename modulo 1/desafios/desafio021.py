import pygame 

pygame.init()
pygame.mixer.music.set_volume(1.0)  # Volume máximo
pygame.mixer.music.load('D:\ProjetosAudios\BasesSemBaixo\AcendeOFogo.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
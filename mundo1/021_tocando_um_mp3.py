"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('mundo1/021.mp3')
pygame.mixer.music.play(loops=0, start=0.0) #Loops é quantas vezes a música rodará (0 por padrão, -1 toca pra sempre) e start é a minutagem de início (em segundos).
pygame.event.wait()

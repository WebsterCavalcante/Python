# faça um programa que abra e reproduza o audio de um arquivo mp3.
#                               PRIMEIRO PROGRAMA USANDO O PYGAME!
import pygame
pygame.init()
pygame.mixer.music.load('video-vlog.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()

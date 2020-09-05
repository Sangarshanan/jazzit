from utils import settings

import pygame

settings()


def fibonacci(n):
    if n < 0:
        raise Exception("BE POSITIVE !!!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


pygame.mixer.init()
pygame.mixer.music.load("tracks/Elevator Music.mp3")
pygame.mixer.music.play(loops=-1)
while pygame.mixer.music.get_busy() == True:
    for num in range(1, 100000):
        print(fibonacci(num))
    break

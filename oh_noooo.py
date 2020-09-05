from utils import settings

import time
import pygame
import random

settings()
pygame.mixer.init()


ohnoo_tracks = [("bruh.mp3", 1), ("Curb Your Enthusiasm.mp3", 7)]
random.shuffle(ohnoo_tracks)
track = ohnoo_tracks[0]

def bruh():
    pygame.mixer.music.load(f"tracks/{track[0]}")
    pygame.mixer.music.play()
    time.sleep(track[1])


try:
    impossible = 0 / 0
except Exception as e:
    raise e
finally:
    bruh()

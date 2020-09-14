import sys
import time
from playsound import playsound

track_path = sys.argv[1]

while True:
    playsound(track_path)
    time.sleep(0.1)

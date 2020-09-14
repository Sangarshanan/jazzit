import random
from jazzit import error_track

music, wait = random.choice([("curb_your_enthusiasm.mp3", 7), ("bruh.mp3", None)])


@error_track(music, wait)
def run():
    for num in reversed(range(10)):
        print(10 / num)


if __name__ == "__main__":
    run()

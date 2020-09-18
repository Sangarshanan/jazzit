import time
from multiprocessing import Process
from playsound import playsound


def remind_me(seconds):
    while True:
        playsound("examples/sad_violin.mp3")
        time.sleep(seconds)


class wait_track(object):
    def __init__(self, track=None):
        self.track = track
    def __call__(self, original_func):
        def wrapped_function(*args):
            process = Process(target=remind_me, args=(2,), daemon=True)
            try:
                process.start()
                original_func(*args)
            except KeyboardInterrupt:
                process.terminate()
                process.join()
                print("BRUH")

        return wrapped_function


@wait_track("examples/sad_violin.mp3")
def thread_stuff():
    for _ in range(0, 100):
        print("hello")
        time.sleep(1)


if __name__ == "__main__":
    thread_stuff()

try:
    import memory_profiler
except ImportError:
    raise ImportError("Module memory_profiler not found !!")

from time import time

from jazzit import waiting_track


def fibonacci(n):
    if n < 0:
        raise Exception("BE POSITIVE !!!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@profile
@waiting_track("elevator.mp3")
def run_music(limit):
    for num in range(1, limit):
        print(fibonacci(num), num)


@profile
def run_no_music(limit):
    for num in range(1, limit):
        print(fibonacci(num), num)


if __name__ == "__main__":
    start = time()
    run_no_music(30)
    end = time()
    print("Without Music", end - start)
    
    start = time()
    run_music(30)
    end = time()
    print("With Music", end - start)

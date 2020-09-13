from jazzit import waiting_track

def fibonacci(n):
    if n < 0:
        raise Exception("BE POSITIVE !!!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@waiting_track("elevator.mp3")
def run(limit):
    for num in range(1, limit):
        print(fibonacci(num))

if __name__ == "__main__":
    run(1000)


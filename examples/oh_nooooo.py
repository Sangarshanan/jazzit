from jazzit import error_track

@error_track("curb_your_enthusiasm.mp3", wait=7)
def run():
    for num in reversed(range(10)):
        print(10/num)

if __name__ == "__main__":
    run()

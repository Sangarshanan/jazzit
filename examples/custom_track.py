from jazzit import error_track

class SauceNotFound(Exception):
    pass

@error_track("examples/sad_violin.mp3", wait=5, ascii_err=True)
def run():
    raise SauceNotFound("No sauce for you")

if __name__ == "__main__":
    run()

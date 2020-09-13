from .settings import current_dir

import os
import sys
import time
import random
import traceback

import pygame
pygame.mixer.init()


def get_track_path(track):
    track_path = os.path.join(current_dir, "tracks", track)
    if os.path.exists(track_path):
        return track_path
    else:
        return track


class WaitingTrack(object):
    """Use on loooong scripts."""

    def __init__(self, track=None):
        self.track = "elevator.mp3"

    def __call__(self, original_func):
        def wrapped_function(*args):
            track_path = get_track_path(self.track)
            pygame.mixer.music.load(track_path)
            try:
                pygame.mixer.music.play(loops=-1)
                original_func(*args)
            except KeyboardInterrupt:
                pygame.mixer.music.stop()
            finally:
                pygame.mixer.music.stop()

        return wrapped_function


class ErrorTrack(object):
    """Use on potential oopsies."""

    def __init__(self, track=None, wait=None, ascii_err=False):
        self.track = track
        # Time (optional) will be infered by track length
        self.wait = wait
        # ascii_err (Optional) Print the exception as an ascii art
        self.ascii_err = ascii_err

    def __call__(self, original_func):
        def wrapped_function(*args):
            try:
                original_func(*args)
            except Exception as e:
                track_path = get_track_path(self.track)
                pygame.mixer.music.load(track_path)
                if self.ascii_err:
                    from pyfiglet import figlet_format

                    sys.stdout.write(figlet_format(e.__class__.__name__))
                traceback.print_exc()
                pygame.mixer.music.play()
                if self.wait is None:
                    from .utils import track_length

                    time.sleep(track_length(track_path))
                else:
                    time.sleep(self.wait)
                pygame.mixer.music.stop()
            finally:
                pass

        return wrapped_function

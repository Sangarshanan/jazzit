"""Handy Utilities."""

import os
import time
from playsound import playsound
from multiprocessing import Process

current_dir, _ = os.path.split(__file__)


def _track_length(track_path):
    """Get length of Track."""
    from mutagen.mp3 import MP3

    audio = MP3(track_path)
    return audio.info.length


def _get_track_path(track):
    """Get Track Path."""
    track_path = os.path.join(current_dir, "tracks", track)
    if os.path.exists(track_path):
        return track_path
    else:
        return track


def _play_music(track_path):
    """Play Music in a loop."""
    while True:
        playsound(track_path)
        time.sleep(0.1)


def _start_music(track_path, loop=True):
    """Start Music."""
    process = Process(target=_play_music, args=(track_path,), daemon=True)
    process.start()
    return process


def _stop_music(process):
    """Stop Music."""
    process.terminate()
    process.join()

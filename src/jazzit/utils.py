"""Handy Utilities."""

import os
import time
from multiprocessing import Process
from urllib.parse import urlparse

from playsound import playsound

_current_dir, _ = os.path.split(__file__)
_flags = {}


def _is_url(text):
    parsed = urlparse(text)
    return bool(parsed.scheme and parsed.netloc)


def _track_length(track_path):
    """Get length of Track."""
    from mutagen.mp3 import MP3

    try:
        audio = MP3(track_path)
        length = audio.info.length
    except Exception: # TODO: CHANGE NOT EXCEPTION
        # Default fallback
        length = 3
    return length


def _get_track_path(track):
    """Get Track Path."""
    if not _is_url(track):
        track_path = os.path.join(_current_dir, "tracks", track)
        if os.path.exists(track_path):
            track = track_path
    return track


def _in_notebook():
    """Are you in a notebook ?."""
    try:
        in_notebook = _flags["in_notebook"]
    except KeyError:
        in_notebook = True
        try:
            from IPython import get_ipython
            in_notebook = "IPKernelApp" in get_ipython().config
            
        except AttributeError:
            in_notebook = False
        _flags["in_notebook"] = in_notebook
    return in_notebook


def _play_music(track_path):
    """Play Music in a loop."""
    while True:
        playsound(track_path)
        time.sleep(0.1)


def _start_music(track_path, loop=True):
    """Start Music."""
    if _in_notebook():
        from .jupyter.player import _start_music

        process = _start_music(track_path)
    else:
        process = Process(target=_play_music, args=(track_path,), daemon=True)
        process.start()
    return process


def _stop_music(process):
    """Stop Music."""
    if _in_notebook():
        from .jupyter.player import _stop_music
        return _stop_music(process)

    process.terminate()
    process.join()

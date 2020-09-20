"""Duke Silver."""

import sys
import time
import traceback

from .utils import _get_track_path, _start_music, _stop_music


class WaitingTrack(object):
    """Use on loooong scripts."""

    def __init__(self, track=None):
        """Constructor."""
        self.track = track

    def __call__(self, original_func):
        """Wrap decorator."""

        def wrapped_function(*args):
            track_path = _get_track_path(self.track)
            process = _start_music(track_path)
            try:
                original_func(*args)
            except KeyboardInterrupt:
                _stop_music(process)
            finally:
                _stop_music(process)

        return wrapped_function


class ErrorTrack(object):
    """Use on potential oopsies."""

    def __init__(self, track=None, wait=None, ascii_err=False):
        """Constructor."""
        self.track = track
        self.wait = wait  # (optional) will be infered by track length
        self.ascii_err = ascii_err  # (Optional) Print the exception as an asciiart

    def __call__(self, original_func):
        """Wrap decorator."""

        def wrapped_function(*args):
            try:
                original_func(*args)
            except Exception as e:
                track_path = _get_track_path(self.track)
                if self.ascii_err:
                    from pyfiglet import figlet_format

                    sys.stdout.write(figlet_format(e.__class__.__name__))
                traceback.print_exc()
                try:
                    process = _start_music(track_path)
                    if self.wait is None:
                        from .utils import _track_length

                        time.sleep(_track_length(track_path))
                    else:
                        time.sleep(self.wait)
                except KeyboardInterrupt:
                    _stop_music(process)
            finally:
                _stop_music(process)

        return wrapped_function


class SuccessTrack(object):
    """Use on potential YAYs."""

    def __init__(self, track=None, wait=None):
        """Constructor."""
        self.track = track
        self.wait = wait  # (optional) will be infered by track length; defaults to 3

    def __call__(self, original_func):
        """Wrap decorator."""

        def wrapped_function(*args):
            track_path = _get_track_path(self.track)
            original_func(*args)
            try:
                process = _start_music(track_path)
                if self.wait is None:
                    from .utils import _track_length

                    time.sleep(_track_length(track_path))
                else:
                    time.sleep(self.wait)
            except KeyboardInterrupt:
                _stop_music(process)
            finally:
                _stop_music(process)

        return wrapped_function

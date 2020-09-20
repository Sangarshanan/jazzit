import uuid
from IPython.display import display, Audio, HTML

from ..utils import _get_track_path


class JupyterAudio(Audio):
    def _repr_html_(self):
        audio = super()._repr_html_()
        audio = audio.replace(
            "<audio",
            f'<audio controls loop onended="this.parentNode.removeChild(this)"',
        )
        return f'<div style="display:none">{audio}</div>'


class JupyterPlayer:
    def __init__(self, track):
        self.track = _get_track_path(track)
        self.display_id = str(uuid.uuid4())
        display(HTML(""), display_id=self.display_id)

    def play_music(self):
        sound = JupyterAudio(self.track, autoplay=True,)
        return display(sound, display_id=self.display_id)


def _stop_music(display):
    """Stop Music."""
    display.update(HTML(""))


def _start_music(track_path):
    """Play Music."""
    player = JupyterPlayer(track_path)
    display = player.play_music()
    return display

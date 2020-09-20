import uuid
from IPython.display import display, Audio, HTML

from ..utils import _get_track_path


class JupyterAudio(Audio):
    def __init__(self, *args, **kwargs):
        self.loop = kwargs.pop("loop", False)
        super().__init__(*args, **kwargs)

    def _repr_html_(self):
        audio = super()._repr_html_()
        if self.loop:
            loop = "controls loop"
        else:
            loop = ""
        audio = audio.replace(
            "<audio", f'<audio {loop} onended="this.parentNode.removeChild(this)"'
        )
        return f'<div style="display:none">{audio}</div>'


class JupyterPlayer:
    def __init__(self, track):
        self.track = _get_track_path(track)
        self.display_id = str(uuid.uuid4())
        display(HTML(""), display_id=self.display_id)

    def play_music(self, loop):
        sound = JupyterAudio(self.track, autoplay=True, loop=loop)
        return display(sound, display_id=self.display_id)


def _stop_music(display):
    """Stop Music."""
    display.update(HTML(""))


def _start_music(track_path, loop=False):
    """Play Music."""
    player = JupyterPlayer(track_path)
    display = player.play_music(loop=loop)
    return display

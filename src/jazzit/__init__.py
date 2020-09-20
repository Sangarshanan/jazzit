from .utils import _in_notebook

_in_notebook = _in_notebook()

if _in_notebook:
    from .jupyter.magic import JupyterJazz

    def load_ipython_extension(ipython):
        ipython.register_magics(JupyterJazz)


from .jazz import WaitingTrack as waiting_track  # noqa
from .jazz import ErrorTrack as error_track  # noqa
from .jazz import SuccessTrack as success_track  # noqa

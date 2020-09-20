import time
from IPython.core.magic import Magics, magics_class, line_cell_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

from .player import _start_music, _stop_music


@magics_class
class JupyterJazz(Magics):
    @magic_arguments()
    @argument(
        "-t", "--track", help="Track to Play"
    )
    @line_cell_magic
    def waiting_track(self, line, cell=None):
        args = parse_argstring(self.waiting_track, line)
        exec_val = line if cell is None else cell
        player = _start_music(args.track)
        self.shell.run_cell(exec_val)
        _stop_music(player)

    @magic_arguments()
    @argument("-t", "--track", help="Track to Play")
    @argument(
        "-w",
        "--wait",
        type=int,
        default=3,
        help="Wait for x seconds before cutting the music",
    )
    @line_cell_magic
    def error_track(self, line, cell=None):
        args = parse_argstring(self.error_track, line)
        exec_val = line if cell is None else cell
        execution = self.shell.run_cell(exec_val)
        if execution.error_in_exec:
            player = _start_music(args.track)
            if args.wait:
                time.sleep(args.wait)
                _stop_music(player)

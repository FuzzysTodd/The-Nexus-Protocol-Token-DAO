import os
import typing
from _typeshed import Incomplete

__all__ = ['DOT_BINARY', 'command']

DOT_BINARY: Incomplete

def command(engine: str, format_: str, *, renderer: str | None = None, formatter: str | None = None, neato_no_op: bool | int | None = None) -> typing.List[os.PathLike | str]:
    """Return ``subprocess.Popen`` argument list for rendering.

    See also:
        Upstream documentation:
        - https://www.graphviz.org/doc/info/command.html#-K
        - https://www.graphviz.org/doc/info/command.html#-T
        - https://www.graphviz.org/doc/info/command.html#-n
    """

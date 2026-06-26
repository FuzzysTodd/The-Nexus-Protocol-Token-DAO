from .. import util as util
from ..util import compat as compat
from typing import Callable

REVISION_SCRIPT_TOKEN: str

def register(name: str) -> Callable:
    """A function decorator that will register that function as a write hook.

    See the documentation linked below for an example.

    .. seealso::

        :ref:`post_write_hooks_custom`


    """
def console_scripts(path: str, options: dict, ignore_output: bool = False) -> None: ...
def exec_(path: str, options: dict, ignore_output: bool = False) -> None: ...

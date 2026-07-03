from . import embed as embed
from .ptutils import IPythonPTCompleter as IPythonPTCompleter
from .shortcuts import create_ipython_shortcuts as create_ipython_shortcuts
from IPython.core.completer import IPCompleter as IPCompleter
from IPython.core.debugger import Pdb as Pdb
from _typeshed import Incomplete

PTK3: Incomplete

class TerminalPdb(Pdb):
    """Standalone IPython debugger."""
    thread_executor: Incomplete
    def __init__(self, *args, pt_session_options: Incomplete | None = None, **kwargs) -> None: ...
    debugger_history: Incomplete
    pt_loop: Incomplete
    pt_app: Incomplete
    def pt_init(self, pt_session_options: Incomplete | None = None):
        """Initialize the prompt session and the prompt loop
        and store them in self.pt_app and self.pt_loop.

        Additional keyword arguments for the PromptSession class
        can be specified in pt_session_options.
        """
    intro: Incomplete
    def cmdloop(self, intro: Incomplete | None = None) -> None:
        """Repeatedly issue a prompt, accept input, parse an initial prefix
        off the received input, and dispatch to action methods, passing them
        the remainder of the line as argument.

        override the same methods from cmd.Cmd to provide prompt toolkit replacement.
        """
    def do_interact(self, arg) -> None: ...

def set_trace(frame: Incomplete | None = None) -> None:
    """
    Start debugging from `frame`.

    If frame is not specified, debugging starts from caller's frame.
    """

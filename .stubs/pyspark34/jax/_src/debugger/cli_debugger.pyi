import cmd
from _typeshed import Incomplete
from typing import Any, IO

DebuggerFrame: Incomplete

class CliDebugger(cmd.Cmd):
    """A text-based debugger."""
    prompt: str
    use_rawinput: Incomplete
    frames: Incomplete
    frame_index: int
    thread_id: Incomplete
    intro: str
    def __init__(self, frames: list[DebuggerFrame], thread_id, stdin: IO[str] | None = None, stdout: IO[str] | None = None, completekey: str = 'tab') -> None: ...
    def current_frame(self): ...
    def evaluate(self, expr): ...
    def default(self, arg) -> None:
        """Evaluates an expression."""
    def print_backtrace(self) -> None: ...
    def print_context(self, num_lines: int = 2) -> None: ...
    def do_p(self, arg) -> None:
        """p expression
    Evaluates and prints the value of an expression
    """
    def do_pp(self, arg) -> None:
        """pp expression
    Evaluates and pretty-prints the value of an expression
    """
    def do_up(self, _) -> None:
        """u(p)
    Move down a stack frame.
    """
    do_u = do_up
    def do_down(self, _) -> None:
        """d(own)
    Move down a stack frame.
    """
    do_d = do_down
    def do_list(self, _) -> None:
        """l(ist)
    List source code for the current file.
    """
    do_l = do_list
    def do_continue(self, _):
        """c(ont(inue))
    Continue the program's execution.
    """
    do_c = do_continue
    do_cont = do_continue
    def do_quit(self, _) -> None:
        """q(uit)
(exit)
    Quit the debugger. The program is given an exit command.
    """
    do_q = do_quit
    do_EOF = do_quit
    do_exit = do_quit
    def do_where(self, _) -> None:
        """w(here)
    Prints a stack trace with the most recent frame on the bottom.
    'bt' is an alias for this command.
    """
    do_w = do_where
    do_bt = do_where
    def run(self) -> None: ...

def run_debugger(frames: list[DebuggerFrame], thread_id: int | None, **kwargs: Any): ...

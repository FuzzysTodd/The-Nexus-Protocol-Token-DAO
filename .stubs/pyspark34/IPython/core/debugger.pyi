from IPython import get_ipython as get_ipython
from IPython.core.excolors import exception_colors as exception_colors
from IPython.utils import PyColorize as PyColorize, coloransi as coloransi, py3compat as py3compat
from _typeshed import Incomplete
from pdb import Pdb as OldPdb

__skip_doctest__: bool
prompt: str
DEBUGGERSKIP: str

def make_arrow(pad):
    """generate the leading arrow in front of traceback or debugger"""
def BdbQuit_excepthook(et, ev, tb, excepthook: Incomplete | None = None) -> None:
    """Exception hook which handles `BdbQuit` exceptions.

    All other exceptions are processed using the `excepthook`
    parameter.
    """
def BdbQuit_IPython_excepthook(self, et, ev, tb, tb_offset: Incomplete | None = None) -> None: ...

RGX_EXTRA_INDENT: Incomplete

def strip_indentation(multiline_string): ...
def decorate_fn_with_doc(new_fn, old_fn, additional_text: str = ''):
    """Make new_fn have old_fn's doc string. This is particularly useful
    for the ``do_...`` commands that hook into the help system.
    Adapted from from a comp.lang.python posting
    by Duncan Booth."""

class Pdb(OldPdb):
    """Modified Pdb class, does not load readline.

    for a standalone version that uses prompt_toolkit, see
    `IPython.terminal.debugger.TerminalPdb` and
    `IPython.terminal.debugger.set_trace()`


    This debugger can hide and skip frames that are tagged according to some predicates.
    See the `skip_predicates` commands.

    """
    default_predicates: Incomplete
    context: Incomplete
    shell: Incomplete
    aliases: Incomplete
    color_scheme_table: Incomplete
    parser: Incomplete
    prompt: Incomplete
    skip_hidden: bool
    report_skipped: bool
    def __init__(self, completekey: Incomplete | None = None, stdin: Incomplete | None = None, stdout: Incomplete | None = None, context: int = 5, **kwargs) -> None:
        """Create a new IPython debugger.

        Parameters
        ----------
        completekey : default None
            Passed to pdb.Pdb.
        stdin : default None
            Passed to pdb.Pdb.
        stdout : default None
            Passed to pdb.Pdb.
        context : int
            Number of lines of source code context to show when
            displaying stacktrace information.
        **kwargs
            Passed to pdb.Pdb.

        Notes
        -----
        The possibilities are python version dependent, see the python
        docs for more info.
        """
    def set_colors(self, scheme) -> None:
        """Shorthand access to the color table scheme selector method."""
    initial_frame: Incomplete
    def set_trace(self, frame: Incomplete | None = None): ...
    def hidden_frames(self, stack):
        """
        Given an index in the stack return whether it should be skipped.

        This is used in up/down and where to skip frames.
        """
    def interaction(self, frame, traceback) -> None: ...
    def precmd(self, line):
        """Perform useful escapes on the command before it is executed."""
    def new_do_frame(self, arg) -> None: ...
    def new_do_quit(self, arg): ...
    do_q: Incomplete
    do_quit: Incomplete
    def new_do_restart(self, arg):
        """Restart command. In the context of ipython this is exactly the same
        thing as 'quit'."""
    def print_stack_trace(self, context: Incomplete | None = None) -> None: ...
    def print_stack_entry(self, frame_lineno, prompt_prefix: str = '\n-> ', context: Incomplete | None = None) -> None: ...
    def format_stack_entry(self, frame_lineno, lprefix: str = ': ', context: Incomplete | None = None): ...
    lineno: Incomplete
    def print_list_lines(self, filename, first, last) -> None:
        """The printing (as opposed to the parsing part of a 'list'
        command."""
    def do_skip_predicates(self, args) -> None:
        """
        Turn on/off individual predicates as to whether a frame should be hidden/skip.

        The global option to skip (or not) hidden frames is set with skip_hidden

        To change the value of a predicate

            skip_predicates key [true|false]

        Call without arguments to see the current values.

        To permanently change the value of an option add the corresponding
        command to your ``~/.pdbrc`` file. If you are programmatically using the
        Pdb instance you can also change the ``default_predicates`` class
        attribute.
        """
    def do_skip_hidden(self, arg) -> None:
        """
        Change whether or not we should skip frames with the
        __tracebackhide__ attribute.
        """
    lastcmd: str
    def do_list(self, arg) -> None:
        """Print lines of code from the current stack frame
        """
    do_l = do_list
    def getsourcelines(self, obj): ...
    def do_longlist(self, arg) -> None:
        """Print lines of code from the current stack frame.

        Shows more lines than 'list' does.
        """
    do_ll = do_longlist
    def do_debug(self, arg) -> None:
        """debug code
        Enter a recursive debugger that steps through the code
        argument (which is an arbitrary expression or statement to be
        executed in the current environment).
        """
    def do_pdef(self, arg) -> None:
        """Print the call signature for any callable object.

        The debugger interface to %pdef"""
    def do_pdoc(self, arg) -> None:
        """Print the docstring for an object.

        The debugger interface to %pdoc."""
    def do_pfile(self, arg) -> None:
        """Print (or run through pager) the file where an object is defined.

        The debugger interface to %pfile.
        """
    def do_pinfo(self, arg) -> None:
        """Provide detailed information about an object.

        The debugger interface to %pinfo, i.e., obj?."""
    def do_pinfo2(self, arg) -> None:
        """Provide extra detailed information about an object.

        The debugger interface to %pinfo2, i.e., obj??."""
    def do_psource(self, arg) -> None:
        """Print (or run through pager) the source code for an object."""
    def do_where(self, arg) -> None:
        '''w(here)
        Print a stack trace, with the most recent frame at the bottom.
        An arrow indicates the "current frame", which determines the
        context of most commands. \'bt\' is an alias for this command.

        Take a number as argument as an (optional) number of context line to
        print'''
    do_w = do_where
    def break_anywhere(self, frame):
        """
        _stop_in_decorator_internals is overly restrictive, as we may still want
        to trace function calls, so we need to also update break_anywhere so
        that is we don't `stop_here`, because of debugger skip, we may still
        stop at any point inside the function

        """
    def stop_here(self, frame): ...
    def do_up(self, arg) -> None:
        """u(p) [count]
        Move the current frame count (default one) levels up in the
        stack trace (to an older frame).

        Will skip hidden frames.
        """
    def do_down(self, arg) -> None:
        """d(own) [count]
        Move the current frame count (default one) levels down in the
        stack trace (to a newer frame).

        Will skip hidden frames.
        """
    do_d = do_down
    do_u = do_up
    def do_context(self, context) -> None:
        """context number_of_lines
        Set the number of lines of source code to show when displaying
        stacktrace information.
        """

class InterruptiblePdb(Pdb):
    """Version of debugger where KeyboardInterrupt exits the debugger altogether."""
    stop_here: Incomplete
    quitting: bool
    def cmdloop(self, intro: Incomplete | None = None):
        """Wrap cmdloop() such that KeyboardInterrupt stops the debugger."""

def set_trace(frame: Incomplete | None = None) -> None:
    """
    Start debugging from `frame`.

    If frame is not specified, debugging starts from caller's frame.
    """

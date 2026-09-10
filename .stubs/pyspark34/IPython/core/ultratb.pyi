import IPython.utils.colorable as colorable
import types
from IPython import get_ipython as get_ipython
from IPython.core import debugger as debugger
from IPython.core.display_trap import DisplayTrap as DisplayTrap
from IPython.core.excolors import exception_colors as exception_colors
from IPython.utils import PyColorize as PyColorize, py3compat as py3compat
from IPython.utils.terminal import get_terminal_size as get_terminal_size
from _typeshed import Incomplete
from types import TracebackType
from typing import Any, List, Tuple

INDENT_SIZE: int
DEFAULT_SCHEME: str
FAST_THRESHOLD: int

def count_lines_in_py_file(filename: str) -> int:
    '''
    Given a filename, returns the number of lines in the file
    if it ends with the extension ".py". Otherwise, returns 0.
    '''
def get_line_number_of_frame(frame: types.FrameType) -> int:
    """
    Given a frame object, returns the total number of lines in the file
    containing the frame's code object, or the number of lines in the
    frame's source code if the file is not available.

    Parameters
    ----------
    frame : FrameType
        The frame object whose line number is to be determined.

    Returns
    -------
    int
        The total number of lines in the file containing the frame's
        code object, or the number of lines in the frame's source code
        if the file is not available.
    """

class TBTools(colorable.Colorable):
    """Basic tools used by all traceback printer classes."""
    tb_offset: int
    call_pdb: Incomplete
    color_scheme_table: Incomplete
    old_scheme: Incomplete
    debugger_cls: Incomplete
    pdb: Incomplete
    def __init__(self, color_scheme: str = 'NoColor', call_pdb: bool = False, ostream: Incomplete | None = None, parent: Incomplete | None = None, config: Incomplete | None = None, *, debugger_cls: Incomplete | None = None) -> None: ...
    ostream: Incomplete
    def get_parts_of_chained_exception(self, evalue) -> Tuple[type, BaseException, TracebackType] | None: ...
    def prepare_chained_exception_message(self, cause) -> List[Any]: ...
    @property
    def has_colors(self) -> bool: ...
    Colors: Incomplete
    def set_colors(self, *args, **kw) -> None:
        """Shorthand access to the color table scheme selector method."""
    def color_toggle(self) -> None:
        """Toggle between the currently active color scheme and NoColor."""
    def stb2text(self, stb):
        """Convert a structured traceback (a list) to a string."""
    def text(self, etype, value, tb, tb_offset: int | None = None, context: int = 5):
        """Return formatted traceback.

        Subclasses may override this if they add extra arguments.
        """
    def structured_traceback(self, etype: type, evalue: BaseException | None, etb: TracebackType | None = None, tb_offset: int | None = None, number_of_lines_of_context: int = 5):
        """Return a list of traceback frames.

        Must be implemented by each class.
        """

class ListTB(TBTools):
    """Print traceback information from a traceback list, with optional color.

    Calling requires 3 arguments: (etype, evalue, elist)
    as would be obtained by::

      etype, evalue, tb = sys.exc_info()
      if tb:
        elist = traceback.extract_tb(tb)
      else:
        elist = None

    It can thus be used by programs which need to process the traceback before
    printing (such as console replacements based on the code module from the
    standard library).

    Because they are meant to be called without a full traceback (only a
    list), instances of this class can't call the interactive pdb debugger."""
    def __call__(self, etype, value, elist) -> None: ...
    def structured_traceback(self, etype: type, evalue: BaseException | None, etb: TracebackType | None = None, tb_offset: int | None = None, context: int = 5):
        """Return a color formatted string with the traceback info.

        Parameters
        ----------
        etype : exception type
            Type of the exception raised.
        evalue : object
            Data stored in the exception
        etb : list | TracebackType | None
            If list: List of frames, see class docstring for details.
            If Traceback: Traceback of the exception.
        tb_offset : int, optional
            Number of frames in the traceback to skip.  If not given, the
            instance evalue is used (set in constructor).
        context : int, optional
            Number of lines of context information to print.

        Returns
        -------
        String with formatted exception.
        """
    def get_exception_only(self, etype, value):
        """Only print the exception type and message, without a traceback.

        Parameters
        ----------
        etype : exception type
        value : exception value
        """
    def show_exception_only(self, etype, evalue) -> None:
        """Only print the exception type and message, without a traceback.

        Parameters
        ----------
        etype : exception type
        evalue : exception value
        """

class FrameInfo:
    """
    Mirror of stack data's FrameInfo, but so that we can bypass highlighting on
    really long frames.
    """
    description: str | None
    filename: str | None
    lineno: Tuple[int]
    context: int | None
    frame: Incomplete
    code: Incomplete
    raw_lines: Incomplete
    def __init__(self, description: str | None, filename: str, lineno: Tuple[int], frame, code, *, sd: Incomplete | None = None, context: Incomplete | None = None) -> None: ...
    @property
    def variables_in_executing_piece(self): ...
    @property
    def lines(self): ...
    @property
    def executing(self): ...

class VerboseTB(TBTools):
    """A port of Ka-Ping Yee's cgitb.py module that outputs color text instead
    of HTML.  Requires inspect and pydoc.  Crazy, man.

    Modified version which optionally strips the topmost entries from the
    traceback, to be used with alternate interpreters (because their own code
    would appear in the traceback)."""
    tb_offset: Incomplete
    long_header: Incomplete
    include_vars: Incomplete
    check_cache: Incomplete
    skip_hidden: bool
    def __init__(self, color_scheme: str = 'Linux', call_pdb: bool = False, ostream: Incomplete | None = None, tb_offset: int = 0, long_header: bool = False, include_vars: bool = True, check_cache: Incomplete | None = None, debugger_cls: Incomplete | None = None, parent: Incomplete | None = None, config: Incomplete | None = None) -> None:
        """Specify traceback offset, headers and color scheme.

        Define how many frames to drop from the tracebacks. Calling it with
        tb_offset=1 allows use of this handler in interpreters which will have
        their own code at the top of the traceback (VerboseTB will first
        remove that frame before printing the traceback info)."""
    def format_record(self, frame_info: FrameInfo):
        """Format a single stack frame"""
    def prepare_header(self, etype: str, long_version: bool = False): ...
    def format_exception(self, etype, evalue): ...
    def format_exception_as_a_whole(self, etype: type, evalue: BaseException | None, etb: TracebackType | None, number_of_lines_of_context, tb_offset: int | None):
        """Formats the header, traceback and exception message for a single exception.

        This may be called multiple times by Python 3 exception chaining
        (PEP 3134).
        """
    def get_records(self, etb: TracebackType, number_of_lines_of_context: int, tb_offset: int): ...
    def structured_traceback(self, etype: type, evalue: BaseException | None, etb: TracebackType | None = None, tb_offset: int | None = None, number_of_lines_of_context: int = 5):
        """Return a nice text document describing the traceback."""
    pdb: Incomplete
    tb: Incomplete
    def debugger(self, force: bool = False):
        """Call up the pdb debugger if desired, always clean up the tb
        reference.

        Keywords:

          - force(False): by default, this routine checks the instance call_pdb
            flag and does not actually invoke the debugger if the flag is false.
            The 'force' option forces the debugger to activate even if the flag
            is false.

        If the call_pdb flag is set, the pdb interactive debugger is
        invoked. In all cases, the self.tb reference to the current traceback
        is deleted to prevent lingering references which hamper memory
        management.

        Note that each call to pdb() does an 'import readline', so if your app
        requires a special setup for the readline completers, you'll have to
        fix that by hand after invoking the exception handler."""
    def handler(self, info: Incomplete | None = None) -> None: ...
    def __call__(self, etype: Incomplete | None = None, evalue: Incomplete | None = None, etb: Incomplete | None = None) -> None:
        """This hook can replace sys.excepthook (for Python 2.1 or higher)."""

class FormattedTB(VerboseTB, ListTB):
    """Subclass ListTB but allow calling with a traceback.

    It can thus be used as a sys.excepthook for Python > 2.1.

    Also adds 'Context' and 'Verbose' modes, not available in ListTB.

    Allows a tb_offset to be specified. This is useful for situations where
    one needs to remove a number of topmost frames from the traceback (such as
    occurs with python programs that themselves execute other python code,
    like Python shells).  """
    mode: str
    valid_modes: Incomplete
    verbose_modes: Incomplete
    def __init__(self, mode: str = 'Plain', color_scheme: str = 'Linux', call_pdb: bool = False, ostream: Incomplete | None = None, tb_offset: int = 0, long_header: bool = False, include_vars: bool = False, check_cache: Incomplete | None = None, debugger_cls: Incomplete | None = None, parent: Incomplete | None = None, config: Incomplete | None = None) -> None: ...
    def structured_traceback(self, etype, value, tb, tb_offset: Incomplete | None = None, number_of_lines_of_context: int = 5): ...
    def stb2text(self, stb):
        """Convert a structured traceback (a list) to a string."""
    include_vars: Incomplete
    tb_join_char: Incomplete
    def set_mode(self, mode: str | None = None):
        """Switch to the desired mode.

        If mode is not specified, cycles through the available modes."""
    def plain(self) -> None: ...
    def context(self) -> None: ...
    def verbose(self) -> None: ...
    def minimal(self) -> None: ...

class AutoFormattedTB(FormattedTB):
    """A traceback printer which can be called on the fly.

    It will find out about exceptions by itself.

    A brief example::

        AutoTB = AutoFormattedTB(mode = 'Verbose',color_scheme='Linux')
        try:
          ...
        except:
          AutoTB()  # or AutoTB(out=logfile) where logfile is an open file object
    """
    def __call__(self, etype: Incomplete | None = None, evalue: Incomplete | None = None, etb: Incomplete | None = None, out: Incomplete | None = None, tb_offset: Incomplete | None = None) -> None:
        """Print out a formatted exception traceback.

        Optional arguments:
          - out: an open file-like object to direct output to.

          - tb_offset: the number of frames to skip over in the stack, on a
          per-call basis (this overrides temporarily the instance's tb_offset
          given at initialization time."""
    tb: Incomplete
    def structured_traceback(self, etype: type, evalue: BaseException | None, etb: TracebackType | None = None, tb_offset: int | None = None, number_of_lines_of_context: int = 5): ...

class ColorTB(FormattedTB):
    """Shorthand to initialize a FormattedTB in Linux colors mode."""
    def __init__(self, color_scheme: str = 'Linux', call_pdb: int = 0, **kwargs) -> None: ...

class SyntaxTB(ListTB):
    """Extension which holds some state: the last exception value"""
    last_syntax_error: Incomplete
    def __init__(self, color_scheme: str = 'NoColor', parent: Incomplete | None = None, config: Incomplete | None = None) -> None: ...
    def __call__(self, etype, value, elist) -> None: ...
    def structured_traceback(self, etype, value, elist, tb_offset: Incomplete | None = None, context: int = 5): ...
    def clear_err_state(self):
        """Return the current error state and clear it"""
    def stb2text(self, stb):
        """Convert a structured traceback (a list) to a string."""

def text_repr(value):
    """Hopefully pretty robust repr equivalent."""
def eqrepr(value, repr=...): ...
def nullrepr(value, repr=...): ...

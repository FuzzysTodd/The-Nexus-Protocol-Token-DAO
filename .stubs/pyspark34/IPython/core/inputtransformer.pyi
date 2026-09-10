import abc
from IPython.core.splitinput import LineInfo as LineInfo
from _typeshed import Incomplete
from collections.abc import Generator

ESC_SHELL: str
ESC_SH_CAP: str
ESC_HELP: str
ESC_HELP2: str
ESC_MAGIC: str
ESC_MAGIC2: str
ESC_QUOTE: str
ESC_QUOTE2: str
ESC_PAREN: str
ESC_SEQUENCES: Incomplete

class InputTransformer(metaclass=abc.ABCMeta):
    """Abstract base class for line-based input transformers."""
    @abc.abstractmethod
    def push(self, line):
        """Send a line of input to the transformer, returning the transformed
        input or None if the transformer is waiting for more input.

        Must be overridden by subclasses.

        Implementations may raise ``SyntaxError`` if the input is invalid. No
        other exceptions may be raised.
        """
    @abc.abstractmethod
    def reset(self):
        """Return, transformed any lines that the transformer has accumulated,
        and reset its internal state.

        Must be overridden by subclasses.
        """
    @classmethod
    def wrap(cls, func):
        """Can be used by subclasses as a decorator, to return a factory that
        will allow instantiation with the decorated object.
        """

class StatelessInputTransformer(InputTransformer):
    """Wrapper for a stateless input transformer implemented as a function."""
    func: Incomplete
    def __init__(self, func) -> None: ...
    def push(self, line):
        """Send a line of input to the transformer, returning the
        transformed input."""
    def reset(self) -> None:
        """No-op - exists for compatibility."""

class CoroutineInputTransformer(InputTransformer):
    """Wrapper for an input transformer implemented as a coroutine."""
    coro: Incomplete
    def __init__(self, coro, **kwargs) -> None: ...
    def push(self, line):
        """Send a line of input to the transformer, returning the
        transformed input or None if the transformer is waiting for more
        input.
        """
    def reset(self):
        """Return, transformed any lines that the transformer has
        accumulated, and reset its internal state.
        """

class TokenInputTransformer(InputTransformer):
    """Wrapper for a token-based input transformer.
    
    func should accept a list of tokens (5-tuples, see tokenize docs), and
    return an iterable which can be passed to tokenize.untokenize().
    """
    func: Incomplete
    buf: Incomplete
    def __init__(self, func) -> None: ...
    tokenizer: Incomplete
    def reset_tokenizer(self) -> None: ...
    def push(self, line): ...
    def output(self, tokens): ...
    def reset(self): ...

class assemble_python_lines(TokenInputTransformer):
    def __init__(self) -> None: ...
    def output(self, tokens): ...

def assemble_logical_lines() -> Generator[Incomplete, Incomplete, None]:
    """Join lines following explicit line continuations (\\)"""

tr: Incomplete

def escaped_commands(line):
    """Transform escaped commands - %magic, !system, ?help + various autocalls.
    """
def has_comment(src):
    """Indicate whether an input line has (i.e. ends in, or is) a comment.

    This uses tokenize, so it can distinguish comments from # inside strings.

    Parameters
    ----------
    src : string
        A single line input string.

    Returns
    -------
    comment : bool
        True if source has a comment.
    """
def ends_in_comment_or_string(src):
    """Indicates whether or not an input line ends in a comment or within
    a multiline string.

    Parameters
    ----------
    src : string
        A single line input string.

    Returns
    -------
    comment : bool
        True if source ends in a comment or multiline string.
    """
def help_end(line):
    """Translate lines with ?/?? at the end"""
def cellmagic(end_on_blank_line: bool = False) -> Generator[Incomplete, Incomplete, None]:
    """Captures & transforms cell magics.

    After a cell magic is started, this stores up any lines it gets until it is
    reset (sent None).
    """
def classic_prompt():
    """Strip the >>>/... prompts of the Python interactive shell."""
def ipy_prompt():
    """Strip IPython's In [1]:/...: prompts."""
def leading_indent() -> Generator[Incomplete, Incomplete, None]:
    """Remove leading indentation.

    If the first line starts with a spaces or tabs, the same whitespace will be
    removed from each following line until it is reset.
    """

assign_system_re: Incomplete
assign_system_template: str

def assign_from_system(line):
    """Transform assignment from system commands (e.g. files = !ls)"""

assign_magic_re: Incomplete
assign_magic_template: str

def assign_from_magic(line):
    """Transform assignment from magic commands (e.g. a = %who_ls)"""

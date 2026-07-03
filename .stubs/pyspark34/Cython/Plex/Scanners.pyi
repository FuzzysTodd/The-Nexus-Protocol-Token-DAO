from . import Errors as Errors
from .Regexps import BOL as BOL, EOF as EOF, EOL as EOL
from _typeshed import Incomplete

NOT_FOUND: Incomplete

class Scanner:
    """
    A Scanner is used to read tokens from a stream of characters
    using the token set specified by a Plex.Lexicon.

    Constructor:

      Scanner(lexicon, stream, name = '')

        See the docstring of the __init__ method for details.

    Methods:

      See the docstrings of the individual methods for more
      information.

      read() --> (value, text)
        Reads the next lexical token from the stream.

      position() --> (name, line, col)
        Returns the position of the last token read using the
        read() method.

      begin(state_name)
        Causes scanner to change state.

      produce(value [, text])
        Causes return of a token value to the caller of the
        Scanner.

    """
    trace: int
    buffer: str
    buf_start_pos: int
    next_pos: int
    cur_pos: int
    cur_line: int
    start_pos: int
    current_scanner_position_tuple: Incomplete
    last_token_position_tuple: Incomplete
    text: Incomplete
    state_name: Incomplete
    lexicon: Incomplete
    stream: Incomplete
    name: Incomplete
    queue: Incomplete
    initial_state: Incomplete
    cur_line_start: int
    cur_char: Incomplete
    input_state: int
    def __init__(self, lexicon, stream, name: str = '', initial_pos: Incomplete | None = None) -> None:
        """
        Scanner(lexicon, stream, name = '')

          |lexicon| is a Plex.Lexicon instance specifying the lexical tokens
          to be recognised.

          |stream| can be a file object or anything which implements a
          compatible read() method.

          |name| is optional, and may be the name of the file being
          scanned or any other identifying string.
        """
    def read(self):
        """
        Read the next lexical token from the stream and return a
        tuple (value, text), where |value| is the value associated with
        the token as specified by the Lexicon, and |text| is the actual
        string read from the stream. Returns (None, '') on end of file.
        """
    def unread(self, token, value, position) -> None: ...
    def get_current_scan_pos(self): ...
    def scan_a_token(self):
        """
        Read the next input sequence recognised by the machine
        and return (text, action). Returns ('', None) on end of
        file.
        """
    def run_machine_inlined(self):
        """
        Inlined version of run_machine for speed.
        """
    def next_char(self) -> None: ...
    def position(self):
        """
        Return a tuple (name, line, col) representing the location of
        the last token read using the read() method. |name| is the
        name that was provided to the Scanner constructor; |line|
        is the line number in the stream (1-based); |col| is the
        position within the line of the first character of the token
        (0-based).
        """
    def get_position(self):
        """
        Python accessible wrapper around position(), only for error reporting.
        """
    def begin(self, state_name) -> None:
        """Set the current state of the scanner to the named state."""
    def produce(self, value, text: Incomplete | None = None) -> None:
        """
        Called from an action procedure, causes |value| to be returned
        as the token value from read(). If |text| is supplied, it is
        returned in place of the scanned text.

        produce() can be called more than once during a single call to an action
        procedure, in which case the tokens are queued up and returned one
        at a time by subsequent calls to read(), until the queue is empty,
        whereupon scanning resumes.
        """
    def eof(self) -> None:
        """
        Override this method if you want something to be done at
        end of file.
        """
    @property
    def start_line(self): ...

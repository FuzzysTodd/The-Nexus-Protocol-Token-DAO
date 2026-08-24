from .ansi import AnsiBack as AnsiBack, AnsiFore as AnsiFore, AnsiStyle as AnsiStyle, BEL as BEL, Style as Style
from .win32 import winapi_test as winapi_test, windll as windll
from .winterm import WinColor as WinColor, WinStyle as WinStyle, WinTerm as WinTerm, enable_vt_processing as enable_vt_processing
from _typeshed import Incomplete

winterm: Incomplete

class StreamWrapper:
    """
    Wraps a stream (such as stdout), acting as a transparent proxy for all
    attribute access apart from method 'write()', which is delegated to our
    Converter instance.
    """
    def __init__(self, wrapped, converter) -> None: ...
    def __getattr__(self, name): ...
    def __enter__(self, *args, **kwargs): ...
    def __exit__(self, *args, **kwargs): ...
    def write(self, text) -> None: ...
    def isatty(self): ...
    @property
    def closed(self): ...

class AnsiToWin32:
    """
    Implements a 'write()' method which, on Windows, will strip ANSI character
    sequences from the text, and if outputting to a tty, will convert them into
    win32 function calls.
    """
    ANSI_CSI_RE: Incomplete
    ANSI_OSC_RE: Incomplete
    wrapped: Incomplete
    autoreset: Incomplete
    stream: Incomplete
    strip: Incomplete
    convert: Incomplete
    win32_calls: Incomplete
    on_stderr: Incomplete
    def __init__(self, wrapped, convert: Incomplete | None = None, strip: Incomplete | None = None, autoreset: bool = False) -> None: ...
    def should_wrap(self):
        """
        True if this class is actually needed. If false, then the output
        stream will not be affected, nor will win32 calls be issued, so
        wrapping stdout is not actually required. This will generally be
        False on non-Windows platforms, unless optional functionality like
        autoreset has been requested using kwargs to init()
        """
    def get_win32_calls(self): ...
    def write(self, text) -> None: ...
    def reset_all(self) -> None: ...
    def write_and_convert(self, text) -> None:
        """
        Write the given text to our wrapped stream, stripping any ANSI
        sequences from the text, and optionally converting them into win32
        calls.
        """
    def write_plain_text(self, text, start, end) -> None: ...
    def convert_ansi(self, paramstring, command) -> None: ...
    def extract_params(self, command, paramstring): ...
    def call_win32(self, command, params) -> None: ...
    def convert_osc(self, text): ...
    def flush(self) -> None: ...

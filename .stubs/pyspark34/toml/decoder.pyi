from _typeshed import Incomplete
from toml.tz import TomlTz as TomlTz

unicode = str
basestring = str
unichr = chr
FNFError = FileNotFoundError
FNFError = IOError
TIME_RE: Incomplete

class TomlDecodeError(ValueError):
    """Base toml Exception / Error."""
    msg: Incomplete
    doc: Incomplete
    pos: Incomplete
    lineno: Incomplete
    colno: Incomplete
    def __init__(self, msg, doc, pos) -> None: ...

class CommentValue:
    val: Incomplete
    comment: Incomplete
    def __init__(self, val, comment, beginline, _dict) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def dump(self, dump_value_func): ...

def load(f, _dict=..., decoder: Incomplete | None = None):
    """Parses named file or files as toml and returns a dictionary

    Args:
        f: Path to the file to open, array of files to read into single dict
           or a file descriptor
        _dict: (optional) Specifies the class of the returned toml dictionary
        decoder: The decoder to use

    Returns:
        Parsed toml file represented as a dictionary

    Raises:
        TypeError -- When f is invalid type
        TomlDecodeError: Error while decoding toml
        IOError / FileNotFoundError -- When an array with no valid (existing)
        (Python 2 / Python 3)          file paths is passed
    """
def loads(s, _dict=..., decoder: Incomplete | None = None):
    """Parses string as toml

    Args:
        s: String to be parsed
        _dict: (optional) Specifies the class of the returned toml dictionary

    Returns:
        Parsed toml file represented as a dictionary

    Raises:
        TypeError: When a non-string is passed
        TomlDecodeError: Error while decoding toml
    """

class InlineTableDict:
    """Sentinel subclass of dict for inline tables."""

class TomlDecoder:
    def __init__(self, _dict=...) -> None: ...
    def get_empty_table(self): ...
    def get_empty_inline_table(self): ...
    def load_inline_object(self, line, currentlevel, multikey: bool = False, multibackslash: bool = False) -> None: ...
    def load_line(self, line, currentlevel, multikey, multibackslash): ...
    def load_value(self, v, strictly_valid: bool = True): ...
    def bounded_string(self, s): ...
    def load_array(self, a): ...
    def preserve_comment(self, line_no, key, comment, beginline) -> None: ...
    def embed_comments(self, idx, currentlevel) -> None: ...

class TomlPreserveCommentDecoder(TomlDecoder):
    saved_comments: Incomplete
    def __init__(self, _dict=...) -> None: ...
    def preserve_comment(self, line_no, key, comment, beginline) -> None: ...
    def embed_comments(self, idx, currentlevel) -> None: ...

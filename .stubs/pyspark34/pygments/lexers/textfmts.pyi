from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer
from pygments.token import Operator, String, Text

__all__ = ['IrcLogsLexer', 'TodotxtLexer', 'HttpLexer', 'GettextLexer', 'NotmuchLexer', 'KernelLogLexer']

class IrcLogsLexer(RegexLexer):
    """
    Lexer for IRC logs in *irssi*, *xchat* or *weechat* style.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    timestamp: str
    tokens: Incomplete

class GettextLexer(RegexLexer):
    """
    Lexer for Gettext catalog files.

    .. versionadded:: 0.9
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class HttpLexer(RegexLexer):
    """
    Lexer for HTTP sessions.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    flags: Incomplete
    content_type: Incomplete
    def get_tokens_unprocessed(self, text, stack=('root',)):
        """Reset the content-type state."""
    def header_callback(self, match) -> Generator[Incomplete, None, None]: ...
    def continuous_header_callback(self, match) -> Generator[Incomplete, None, None]: ...
    def content_callback(self, match) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete
    def analyse_text(text): ...

class TodotxtLexer(RegexLexer):
    """
    Lexer for Todo.txt todo list format.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    CompleteTaskText = Operator
    IncompleteTaskText = Text
    Priority: Incomplete
    Date: Incomplete
    Project: Incomplete
    Context = String
    date_regex: str
    priority_regex: str
    project_regex: str
    context_regex: str
    complete_one_date_regex: Incomplete
    complete_two_date_regex: Incomplete
    priority_date_regex: Incomplete
    tokens: Incomplete

class NotmuchLexer(RegexLexer):
    """
    For Notmuch email text format.

    .. versionadded:: 2.5

    Additional options accepted:

    `body_lexer`
        If given, highlight the contents of the message body with the specified
        lexer, else guess it according to the body content (default: ``None``).
    """
    name: str
    url: str
    aliases: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
    body_lexer: Incomplete
    def __init__(self, **options) -> None: ...

class KernelLogLexer(RegexLexer):
    '''
    For Linux Kernel log ("dmesg") output.

    .. versionadded:: 2.6
    '''
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

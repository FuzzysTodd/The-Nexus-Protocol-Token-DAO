from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['MIMELexer']

class MIMELexer(RegexLexer):
    """
    Lexer for Multipurpose Internet Mail Extensions (MIME) data. This lexer is
    designed to process nested multipart data.

    It assumes that the given data contains both header and body (and is
    split at an empty line). If no valid header is found, then the entire data
    will be treated as body.

    Additional options accepted:

    `MIME-max-level`
        Max recursion level for nested MIME structure. Any negative number
        would treated as unlimited. (default: -1)

    `Content-Type`
        Treat the data as a specific content type. Useful when header is
        missing, or this lexer would try to parse from header. (default:
        `text/plain`)

    `Multipart-Boundary`
        Set the default multipart boundary delimiter. This option is only used
        when `Content-Type` is `multipart` and header is missing. This lexer
        would try to parse from header by default. (default: None)

    `Content-Transfer-Encoding`
        Treat the data as a specific encoding. Or this lexer would try to parse
        from header by default. (default: None)

    .. versionadded:: 2.5
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    boundary: Incomplete
    content_transfer_encoding: Incomplete
    content_type: Incomplete
    max_nested_level: Incomplete
    def __init__(self, **options) -> None: ...
    def get_header_tokens(self, match) -> Generator[Incomplete, None, None]: ...
    def get_body_tokens(self, match) -> Generator[Incomplete, None, None]: ...
    def get_bodypart_tokens(self, text): ...
    def store_content_type(self, match) -> Generator[Incomplete, None, None]: ...
    def get_content_type_subtokens(self, match) -> Generator[Incomplete, None, None]: ...
    def store_content_transfer_encoding(self, match) -> Generator[Incomplete, None, None]: ...
    attention_headers: Incomplete
    tokens: Incomplete

from _typeshed import Incomplete

class UserAgent:
    """Represents a parsed user agent header value.

    The default implementation does no parsing, only the :attr:`string`
    attribute is set. A subclass may parse the string to set the
    common attributes or expose other information. Set
    :attr:`werkzeug.wrappers.Request.user_agent_class` to use a
    subclass.

    :param string: The header value to parse.

    .. versionadded:: 2.0
        This replaces the previous ``useragents`` module, but does not
        provide a built-in parser.
    """
    platform: str | None
    browser: str | None
    version: str | None
    language: str | None
    string: Incomplete
    def __init__(self, string: str) -> None: ...
    def __bool__(self) -> bool: ...
    def to_header(self) -> str:
        """Convert to a header value."""

import string
import typing as t
import typing_extensions as te
from _typeshed import Incomplete

class HasHTML(te.Protocol):
    def __html__(self) -> str: ...

__version__: str

class Markup(str):
    '''A string that is ready to be safely inserted into an HTML or XML
    document, either because it was escaped or because it was marked
    safe.

    Passing an object to the constructor converts it to text and wraps
    it to mark it safe without escaping. To escape the text, use the
    :meth:`escape` class method instead.

    >>> Markup("Hello, <em>World</em>!")
    Markup(\'Hello, <em>World</em>!\')
    >>> Markup(42)
    Markup(\'42\')
    >>> Markup.escape("Hello, <em>World</em>!")
    Markup(\'Hello &lt;em&gt;World&lt;/em&gt;!\')

    This implements the ``__html__()`` interface that some frameworks
    use. Passing an object that implements ``__html__()`` will wrap the
    output of that method, marking it safe.

    >>> class Foo:
    ...     def __html__(self):
    ...         return \'<a href="/foo">foo</a>\'
    ...
    >>> Markup(Foo())
    Markup(\'<a href="/foo">foo</a>\')

    This is a subclass of :class:`str`. It has the same methods, but
    escapes their arguments and returns a ``Markup`` instance.

    >>> Markup("<em>%s</em>") % ("foo & bar",)
    Markup(\'<em>foo &amp; bar</em>\')
    >>> Markup("<em>Hello</em> ") + "<foo>"
    Markup(\'<em>Hello</em> &lt;foo&gt;\')
    '''
    def __new__(cls, base: t.Any = '', encoding: str | None = None, errors: str = 'strict') -> te.Self: ...
    def __html__(self) -> te.Self: ...
    def __add__(self, other: str | HasHTML) -> te.Self: ...
    def __radd__(self, other: str | HasHTML) -> te.Self: ...
    def __mul__(self, num: te.SupportsIndex) -> te.Self: ...
    __rmul__ = __mul__
    def __mod__(self, arg: t.Any) -> te.Self: ...
    def join(self, seq: t.Iterable[str | HasHTML]) -> te.Self: ...
    def split(self, sep: str | None = None, maxsplit: int = -1) -> t.List['te.Self']: ...
    def rsplit(self, sep: str | None = None, maxsplit: int = -1) -> t.List['te.Self']: ...
    def splitlines(self, keepends: bool = False) -> t.List['te.Self']: ...
    def unescape(self) -> str:
        '''Convert escaped markup back into a text string. This replaces
        HTML entities with the characters they represent.

        >>> Markup("Main &raquo; <em>About</em>").unescape()
        \'Main » <em>About</em>\'
        '''
    def striptags(self) -> str:
        ''':meth:`unescape` the markup, remove tags, and normalize
        whitespace to single spaces.

        >>> Markup("Main &raquo;\t<em>About</em>").striptags()
        \'Main » About\'
        '''
    @classmethod
    def escape(cls, s: t.Any) -> te.Self:
        """Escape a string. Calls :func:`escape` and ensures that for
        subclasses the correct type is returned.
        """
    __getitem__: Incomplete
    capitalize: Incomplete
    title: Incomplete
    lower: Incomplete
    upper: Incomplete
    replace: Incomplete
    ljust: Incomplete
    rjust: Incomplete
    lstrip: Incomplete
    rstrip: Incomplete
    center: Incomplete
    strip: Incomplete
    translate: Incomplete
    expandtabs: Incomplete
    swapcase: Incomplete
    zfill: Incomplete
    casefold: Incomplete
    removeprefix: Incomplete
    removesuffix: Incomplete
    def partition(self, sep: str) -> t.Tuple['te.Self', 'te.Self', 'te.Self']: ...
    def rpartition(self, sep: str) -> t.Tuple['te.Self', 'te.Self', 'te.Self']: ...
    def format(self, *args: t.Any, **kwargs: t.Any) -> te.Self: ...
    def format_map(self, map: t.Mapping[str, t.Any]) -> te.Self: ...
    def __html_format__(self, format_spec: str) -> te.Self: ...

class EscapeFormatter(string.Formatter):
    escape: Incomplete
    def __init__(self, escape: t.Callable[[t.Any], Markup]) -> None: ...
    def format_field(self, value: t.Any, format_spec: str) -> str: ...

class _MarkupEscapeHelper:
    """Helper for :meth:`Markup.__mod__`."""
    obj: Incomplete
    escape: Incomplete
    def __init__(self, obj: t.Any, escape: t.Callable[[t.Any], Markup]) -> None: ...
    def __getitem__(self, item: t.Any) -> te.Self: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...

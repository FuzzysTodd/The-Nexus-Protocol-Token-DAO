from _typeshed import Incomplete
from collections.abc import Generator

def yield_lines(iterable):
    """
    Yield valid lines of a string or iterable.

    >>> list(yield_lines(''))
    []
    >>> list(yield_lines(['foo', 'bar']))
    ['foo', 'bar']
    >>> list(yield_lines('foo\\nbar'))
    ['foo', 'bar']
    >>> list(yield_lines('\\nfoo\\n#bar\\nbaz #comment'))
    ['foo', 'baz #comment']
    >>> list(yield_lines(['foo\\nbar', 'baz', 'bing\\n\\n\\n']))
    ['foo', 'bar', 'baz', 'bing']
    """
def _(text): ...
def drop_comment(line):
    """
    Drop comments.

    >>> drop_comment('foo # bar')
    'foo'

    A hash without a space may be in a URL.

    >>> drop_comment('http://example.com/foo#bar')
    'http://example.com/foo#bar'
    """
def join_continuation(lines) -> Generator[Incomplete, None, None]:
    """
    Join lines continued by a trailing backslash.

    >>> list(join_continuation(['foo \\\\', 'bar', 'baz']))
    ['foobar', 'baz']
    >>> list(join_continuation(['foo \\\\', 'bar', 'baz']))
    ['foobar', 'baz']
    >>> list(join_continuation(['foo \\\\', 'bar \\\\', 'baz']))
    ['foobarbaz']

    Not sure why, but...
    The character preceeding the backslash is also elided.

    >>> list(join_continuation(['goo\\\\', 'dly']))
    ['godly']

    A terrible idea, but...
    If no line is available to continue, suppress the lines.

    >>> list(join_continuation(['foo', 'bar\\\\', 'baz\\\\']))
    ['foo']
    """

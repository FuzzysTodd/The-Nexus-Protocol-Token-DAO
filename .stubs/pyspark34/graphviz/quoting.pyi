from _typeshed import Incomplete

__all__ = ['quote', 'quote_edge', 'a_list', 'attr_list', 'escape', 'nohtml']

def quote(identifier: str, is_html_string=..., is_valid_id=..., dot_keywords=..., endswith_odd_number_of_backslashes=..., escape_unescaped_quotes=...) -> str:
    '''Return DOT identifier from string, quote if needed.

    >>> quote(\'\')  # doctest: +NO_EXE
    \'""\'

    >>> quote(\'spam\')
    \'spam\'

    >>> quote(\'spam spam\')
    \'"spam spam"\'

    >>> quote(\'-4.2\')
    \'-4.2\'

    >>> quote(\'.42\')
    \'.42\'

    >>> quote(\'<<b>spam</b>>\')
    \'<<b>spam</b>>\'

    >>> quote(nohtml(\'<>\'))
    \'"<>"\'

    >>> print(quote(\'"\'))
    "\\""

    >>> print(quote(\'\\\\"\'))
    "\\""

    >>> print(quote(\'\\\\\\\\"\'))
    "\\\\\\""

    >>> print(quote(\'\\\\\\\\\\\\"\'))
    "\\\\\\""
    '''
def quote_edge(identifier: str) -> str:
    '''Return DOT edge statement node_id from string, quote if needed.

    >>> quote_edge(\'spam\')  # doctest: +NO_EXE
    \'spam\'

    >>> quote_edge(\'spam spam:eggs eggs\')
    \'"spam spam":"eggs eggs"\'

    >>> quote_edge(\'spam:eggs:s\')
    \'spam:eggs:s\'
    '''
def a_list(label: str | None = None, kwargs: Incomplete | None = None, attributes: Incomplete | None = None) -> str:
    '''Return assembled DOT a_list string.

    >>> a_list(\'spam\', kwargs={\'spam\': None, \'ham\': \'ham ham\', \'eggs\': \'\'})  # doctest: +NO_EXE
    \'label=spam eggs="" ham="ham ham"\'
    '''
def attr_list(label: str | None = None, kwargs: Incomplete | None = None, attributes: Incomplete | None = None) -> str:
    '''Return assembled DOT attribute list string.

    Sorts ``kwargs`` and ``attributes`` if they are plain dicts
    (to avoid unpredictable order from hash randomization in Python < 3.7).

    >>> attr_list()  # doctest: +NO_EXE
    \'\'

    >>> attr_list(\'spam spam\', kwargs={\'eggs\': \'eggs\', \'ham\': \'ham ham\'})
    \' [label="spam spam" eggs=eggs ham="ham ham"]\'

    >>> attr_list(kwargs={\'spam\': None, \'eggs\': \'\'})
    \' [eggs=""]\'
    '''

class Quote:
    """Quote strings to be valid DOT identifiers, assemble quoted attribute lists."""

def escape(s: str) -> str:
    """Return string disabling special meaning of backslashes and ``'<...>'``.

    Args:
        s: String in which backslashes and ``'<...>'``
            should be treated as literal.

    Returns:
        Escaped string subclass instance.

    Raises:
        TypeError: If ``s`` is not a ``str``.

    Example:
        >>> import graphviz  # doctest: +NO_EXE
        >>> print(graphviz.escape(r'\\l'))
        \\\\l

    See also:
        Upstream documentation:
        https://www.graphviz.org/doc/info/attrs.html#k:escString
    """

class NoHtml(str):
    """String subclass that does not treat ``'<...>'`` as DOT HTML string."""

def nohtml(s: str) -> str:
    '''Return string not treating ``\'<...>\'`` as DOT HTML string in quoting.

    Args:
        s: String in which leading ``\'<\'`` and trailing ``\'>\'``
            should be treated as literal.

    Returns:
        String subclass instance.

    Raises:
        TypeError: If ``s`` is not a ``str``.

    Example:
        >>> import graphviz  # doctest: +NO_EXE
        >>> g = graphviz.Graph()
        >>> g.node(graphviz.nohtml(\'<>-*-<>\'))
        >>> print(g.source)  # doctest: +NORMALIZE_WHITESPACE
        graph {
            "<>-*-<>"
        }
    '''

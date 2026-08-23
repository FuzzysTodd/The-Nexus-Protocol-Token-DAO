from .serializer import serialize_identifier as serialize_identifier, serialize_name as serialize_name
from _typeshed import Incomplete

class Node:
    """Every node type inherits from this class,
    which is never instantiated directly.

    .. attribute:: type

        Each child class has a :attr:`type` class attribute
        with a unique string value.
        This allows checking for the node type with code like:

        .. code-block:: python

            if node.type == 'whitespace':

        instead of the more verbose:

        .. code-block:: python

            from tinycss2.ast import WhitespaceToken
            if isinstance(node, WhitespaceToken):

    Every node also has these attributes and methods,
    which are not repeated for brevity:

    .. attribute:: source_line

        The line number of the start of the node in the CSS source.
        Starts at 1.

    .. attribute:: source_column

        The column number within :attr:`source_line` of the start of the node
        in the CSS source.
        Starts at 1.

    .. automethod:: serialize

    """
    source_line: Incomplete
    source_column: Incomplete
    def __init__(self, source_line, source_column) -> None: ...
    def serialize(self):
        """Serialize this node to CSS syntax and return a Unicode string."""

class ParseError(Node):
    """A syntax error of some sort. May occur anywhere in the tree.

    Syntax errors are not fatal in the parser
    to allow for different error handling behaviors.
    For example, an error in a Selector list makes the whole rule invalid,
    but an error in a Media Query list only replaces one comma-separated query
    with ``not all``.

    .. autoattribute:: type

    .. attribute:: kind

        Machine-readable string indicating the type of error.
        Example: ``'bad-url'``.

    .. attribute:: message

        Human-readable explanation of the error, as a string.
        Could be translated, expanded to include details, etc.

    """
    type: str
    repr_format: str
    kind: Incomplete
    message: Incomplete
    def __init__(self, line, column, kind, message) -> None: ...

class Comment(Node):
    """A CSS comment.

    Comments can be ignored by passing ``skip_comments=True``
    to functions such as :func:`~tinycss2.parse_component_value_list`.

    .. autoattribute:: type

    .. attribute:: value

        The content of the comment, between ``/*`` and ``*/``, as a string.

    """
    type: str
    repr_format: str
    value: Incomplete
    def __init__(self, line, column, value) -> None: ...

class WhitespaceToken(Node):
    """A :diagram:`whitespace-token`.

    .. autoattribute:: type

    .. attribute:: value

        The whitespace sequence, as a string, as in the original CSS source.


    """
    type: str
    repr_format: str
    value: Incomplete
    def __init__(self, line, column, value) -> None: ...

class LiteralToken(Node):
    """Token that represents one or more characters as in the CSS source.

    .. autoattribute:: type

    .. attribute:: value

        A string of one to four characters.

    Instances compare equal to their :attr:`value`,
    so that these are equivalent:

    .. code-block:: python

        if node == ';':
        if node.type == 'literal' and node.value == ';':

    This regroups what `the specification`_ defines as separate token types:

    .. _the specification: https://drafts.csswg.org/css-syntax-3/

    * *<colon-token>* ``:``
    * *<semicolon-token>* ``;``
    * *<comma-token>* ``,``
    * *<cdc-token>* ``-->``
    * *<cdo-token>* ``<!--``
    * *<include-match-token>* ``~=``
    * *<dash-match-token>* ``|=``
    * *<prefix-match-token>* ``^=``
    * *<suffix-match-token>* ``$=``
    * *<substring-match-token>* ``*=``
    * *<column-token>* ``||``
    * *<delim-token>* (a single ASCII character not part of any another token)

    """
    type: str
    repr_format: str
    value: Incomplete
    def __init__(self, line, column, value) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class IdentToken(Node):
    """An :diagram:`ident-token`.

    .. autoattribute:: type

    .. attribute:: value

        The unescaped value, as a Unicode string.

    .. attribute:: lower_value

        Same as :attr:`value` but normalized to *ASCII lower case*,
        see :func:`~webencodings.ascii_lower`.
        This is the value to use when comparing to a CSS keyword.

    """
    type: str
    repr_format: str
    value: Incomplete
    lower_value: Incomplete
    def __init__(self, line, column, value) -> None: ...

class AtKeywordToken(Node):
    """An :diagram:`at-keyword-token`.

    .. code-block:: text

        '@' <value>

    .. autoattribute:: type

    .. attribute:: value

        The unescaped value, as a Unicode string, without the preceding ``@``.

    .. attribute:: lower_value

        Same as :attr:`value` but normalized to *ASCII lower case*,
        see :func:`~webencodings.ascii_lower`.
        This is the value to use when comparing to a CSS at-keyword.

        .. code-block:: python

            if node.type == 'at-keyword' and node.lower_value == 'import':

    """
    type: str
    repr_format: str
    value: Incomplete
    lower_value: Incomplete
    def __init__(self, line, column, value) -> None: ...

class HashToken(Node):
    """A :diagram:`hash-token`.

    .. code-block:: text

        '#' <value>

    .. autoattribute:: type

    .. attribute:: value

        The unescaped value, as a Unicode string, without the preceding ``#``.

    .. attribute:: is_identifier

        A boolean, true if the CSS source for this token
        was ``#`` followed by a valid identifier.
        (Only such hash tokens are valid ID selectors.)

    """
    type: str
    repr_format: str
    value: Incomplete
    is_identifier: Incomplete
    def __init__(self, line, column, value, is_identifier) -> None: ...

class StringToken(Node):
    '''A :diagram:`string-token`.

    .. code-block:: text

        \'"\' <value> \'"\'

    .. autoattribute:: type

    .. attribute:: value

        The unescaped value, as a Unicode string, without the quotes.

    '''
    type: str
    repr_format: str
    value: Incomplete
    representation: Incomplete
    def __init__(self, line, column, value, representation) -> None: ...

class URLToken(Node):
    """An :diagram:`url-token`.

    .. code-block:: text

        'url(' <value> ')'

    .. autoattribute:: type

    .. attribute:: value

        The unescaped URL, as a Unicode string, without the ``url(`` and ``)``
        markers.

    """
    type: str
    repr_format: str
    value: Incomplete
    representation: Incomplete
    def __init__(self, line, column, value, representation) -> None: ...

class UnicodeRangeToken(Node):
    """A `unicode-range token <https://www.w3.org/TR/css-syntax-3/#urange>`_.

    .. autoattribute:: type

    .. attribute:: start

        The start of the range, as an integer between 0 and 1114111.

    .. attribute:: end

        The end of the range, as an integer between 0 and 1114111.
        Same as :attr:`start` if the source only specified one value.

    """
    type: str
    repr_format: str
    start: Incomplete
    end: Incomplete
    def __init__(self, line, column, start, end) -> None: ...

class NumberToken(Node):
    """A :diagram:`number-token`.

    .. autoattribute:: type

    .. attribute:: value

        The numeric value as a :class:`float`.

    .. attribute:: int_value

        The numeric value as an :class:`int`
        if :attr:`is_integer` is true, :obj:`None` otherwise.

    .. attribute:: is_integer

        Whether the token was syntactically an integer, as a boolean.

    .. attribute:: representation

        The CSS representation of the value, as a Unicode string.

    """
    type: str
    repr_format: str
    value: Incomplete
    int_value: Incomplete
    is_integer: Incomplete
    representation: Incomplete
    def __init__(self, line, column, value, int_value, representation) -> None: ...

class PercentageToken(Node):
    """A :diagram:`percentage-token`.

    .. code-block:: text

        <representation> '%'

    .. autoattribute:: type

    .. attribute:: value

        The value numeric as a :class:`float`.

    .. attribute:: int_value

        The numeric value as an :class:`int`
        if the token was syntactically an integer,
        or :obj:`None`.

    .. attribute:: is_integer

        Whether the token’s value was syntactically an integer, as a boolean.

    .. attribute:: representation

        The CSS representation of the value without the unit,
        as a Unicode string.

    """
    type: str
    repr_format: str
    value: Incomplete
    int_value: Incomplete
    is_integer: Incomplete
    representation: Incomplete
    def __init__(self, line, column, value, int_value, representation) -> None: ...

class DimensionToken(Node):
    """A :diagram:`dimension-token`.

    .. code-block:: text

        <representation> <unit>

    .. autoattribute:: type

    .. attribute:: value

        The value numeric as a :class:`float`.

    .. attribute:: int_value

        The numeric value as an :class:`int`
        if the token was syntactically an integer,
        or :obj:`None`.

    .. attribute:: is_integer

        Whether the token’s value was syntactically an integer, as a boolean.

    .. attribute:: representation

        The CSS representation of the value without the unit,
        as a Unicode string.

    .. attribute:: unit

        The unescaped unit, as a Unicode string.

    .. attribute:: lower_unit

        Same as :attr:`unit` but normalized to *ASCII lower case*,
        see :func:`~webencodings.ascii_lower`.
        This is the value to use when comparing to a CSS unit.

        .. code-block:: python

            if node.type == 'dimension' and node.lower_unit == 'px':

    """
    type: str
    repr_format: str
    value: Incomplete
    int_value: Incomplete
    is_integer: Incomplete
    representation: Incomplete
    unit: Incomplete
    lower_unit: Incomplete
    def __init__(self, line, column, value, int_value, representation, unit) -> None: ...

class ParenthesesBlock(Node):
    """A :diagram:`()-block`.

    .. code-block:: text

        '(' <content> ')'

    .. autoattribute:: type

    .. attribute:: content

        The content of the block, as list of :term:`component values`.
        The ``(`` and ``)`` markers themselves are not represented in the list.

    """
    type: str
    repr_format: str
    content: Incomplete
    def __init__(self, line, column, content) -> None: ...

class SquareBracketsBlock(Node):
    """A :diagram:`[]-block`.

    .. code-block:: text

        '[' <content> ']'

    .. autoattribute:: type

    .. attribute:: content

        The content of the block, as list of :term:`component values`.
        The ``[`` and ``]`` markers themselves are not represented in the list.

    """
    type: str
    repr_format: str
    content: Incomplete
    def __init__(self, line, column, content) -> None: ...

class CurlyBracketsBlock(Node):
    """A :diagram:`{}-block`.

    .. code-block:: text

        '{' <content> '}'

    .. autoattribute:: type

    .. attribute:: content

        The content of the block, as list of :term:`component values`.
        The ``[`` and ``]`` markers themselves are not represented in the list.

    """
    type: str
    repr_format: str
    content: Incomplete
    def __init__(self, line, column, content) -> None: ...

class FunctionBlock(Node):
    """A :diagram:`function-block`.

    .. code-block:: text

        <name> '(' <arguments> ')'

    .. autoattribute:: type

    .. attribute:: name

        The unescaped name of the function, as a Unicode string.

    .. attribute:: lower_name

        Same as :attr:`name` but normalized to *ASCII lower case*,
        see :func:`~webencodings.ascii_lower`.
        This is the value to use when comparing to a CSS function name.

    .. attribute:: arguments

        The arguments of the function, as list of :term:`component values`.
        The ``(`` and ``)`` markers themselves are not represented in the list.
        Commas are not special, but represented as :obj:`LiteralToken` objects
        in the list.

    """
    type: str
    repr_format: str
    name: Incomplete
    lower_name: Incomplete
    arguments: Incomplete
    def __init__(self, line, column, name, arguments) -> None: ...

class Declaration(Node):
    """A (property or descriptor) :diagram:`declaration`.

    .. code-block:: text

        <name> ':' <value>
        <name> ':' <value> '!important'

    .. autoattribute:: type

    .. attribute:: name

        The unescaped name, as a Unicode string.

    .. attribute:: lower_name

        Same as :attr:`name` but normalized to *ASCII lower case*,
        see :func:`~webencodings.ascii_lower`.
        This is the value to use when comparing to
        a CSS property or descriptor name.

        .. code-block:: python

            if node.type == 'declaration' and node.lower_name == 'color':

    .. attribute:: value

        The declaration value as a list of :term:`component values`:
        anything between ``:`` and
        the end of the declaration, or ``!important``.

    .. attribute:: important

        A boolean, true if the declaration had an ``!important`` marker.
        It is up to the consumer to reject declarations that do not accept
        this flag, such as non-property descriptor declarations.

    """
    type: str
    repr_format: str
    name: Incomplete
    lower_name: Incomplete
    value: Incomplete
    important: Incomplete
    def __init__(self, line, column, name, lower_name, value, important) -> None: ...

class QualifiedRule(Node):
    """A :diagram:`qualified rule`.

    .. code-block:: text

        <prelude> '{' <content> '}'

    The interpretation of qualified rules depend on their context.
    At the top-level of a stylesheet
    or in a conditional rule such as ``@media``,
    they are **style rules** where the :attr:`prelude` is Selectors list
    and the :attr:`content` is a list of property declarations.

    .. autoattribute:: type

    .. attribute:: prelude

        The rule’s prelude, the part before the {} block,
        as a list of :term:`component values`.

    .. attribute:: content

        The rule’s content, the part inside the {} block,
        as a list of :term:`component values`.

    """
    type: str
    repr_format: str
    prelude: Incomplete
    content: Incomplete
    def __init__(self, line, column, prelude, content) -> None: ...

class AtRule(Node):
    """An :diagram:`at-rule`.

    .. code-block:: text

        @<at_keyword> <prelude> '{' <content> '}'
        @<at_keyword> <prelude> ';'

    The interpretation of at-rules depend on their at-keyword
    as well as their context.
    Most types of at-rules (ie. at-keyword values)
    are only allowed in some context,
    and must either end with a {} block or a semicolon.

    .. autoattribute:: type

    .. attribute:: at_keyword

        The unescaped value of the rule’s at-keyword,
        without the ``@`` symbol, as a Unicode string.

    .. attribute:: lower_at_keyword

        Same as :attr:`at_keyword` but normalized to *ASCII lower case*,
        see :func:`~webencodings.ascii_lower`.
        This is the value to use when comparing to a CSS at-keyword.

        .. code-block:: python

            if node.type == 'at-rule' and node.lower_at_keyword == 'import':

    .. attribute:: prelude

        The rule’s prelude, the part before the {} block or semicolon,
        as a list of :term:`component values`.

    .. attribute:: content

        The rule’s content, if any.
        The block’s content as a list of :term:`component values`
        for at-rules with a {} block,
        or :obj:`None` for at-rules ending with a semicolon.

    """
    type: str
    repr_format: str
    at_keyword: Incomplete
    lower_at_keyword: Incomplete
    prelude: Incomplete
    content: Incomplete
    def __init__(self, line, column, at_keyword, lower_at_keyword, prelude, content) -> None: ...

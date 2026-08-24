from _typeshed import Incomplete

class Undecidable(ValueError): ...

def filldedent(s, w: int = 70, **kwargs):
    """
    Strips leading and trailing empty lines from a copy of ``s``, then dedents,
    fills and returns it.

    Empty line stripping serves to deal with docstrings like this one that
    start with a newline after the initial triple quote, inserting an empty
    line at the beginning of the string.

    Additional keyword arguments will be passed to ``textwrap.fill()``.

    See Also
    ========
    strlines, rawlines

    """
def strlines(s, c: int = 64, short: bool = False):
    """Return a cut-and-pastable string that, when printed, is
    equivalent to the input.  The lines will be surrounded by
    parentheses and no line will be longer than c (default 64)
    characters. If the line contains newlines characters, the
    `rawlines` result will be returned.  If ``short`` is True
    (default is False) then if there is one line it will be
    returned without bounding parentheses.

    Examples
    ========

    >>> from sympy.utilities.misc import strlines
    >>> q = 'this is a long string that should be broken into shorter lines'
    >>> print(strlines(q, 40))
    (
    'this is a long string that should be b'
    'roken into shorter lines'
    )
    >>> q == (
    ... 'this is a long string that should be b'
    ... 'roken into shorter lines'
    ... )
    True

    See Also
    ========
    filldedent, rawlines
    """
def rawlines(s):
    '''Return a cut-and-pastable string that, when printed, is equivalent
    to the input. Use this when there is more than one line in the
    string. The string returned is formatted so it can be indented
    nicely within tests; in some cases it is wrapped in the dedent
    function which has to be imported from textwrap.

    Examples
    ========

    Note: because there are characters in the examples below that need
    to be escaped because they are themselves within a triple quoted
    docstring, expressions below look more complicated than they would
    be if they were printed in an interpreter window.

    >>> from sympy.utilities.misc import rawlines
    >>> from sympy import TableForm
    >>> s = str(TableForm([[1, 10]], headings=(None, [\'a\', \'bee\'])))
    >>> print(rawlines(s))
    (
        \'a bee\\n\'
        \'-----\\n\'
        \'1 10 \'
    )
    >>> print(rawlines(\'\'\'this
    ... that\'\'\'))
    dedent(\'\'\'\\\n        this
        that\'\'\')

    >>> print(rawlines(\'\'\'this
    ... that
    ... \'\'\'))
    dedent(\'\'\'\\\n        this
        that
        \'\'\')

    >>> s = """this
    ... is a triple \'\'\'
    ... """
    >>> print(rawlines(s))
    dedent("""\\\n        this
        is a triple \'\'\'
        """)

    >>> print(rawlines(\'\'\'this
    ... that
    ...     \'\'\'))
    (
        \'this\\n\'
        \'that\\n\'
        \'    \'
    )

    See Also
    ========
    filldedent, strlines
    '''

ARCH: Incomplete
HASH_RANDOMIZATION: Incomplete

def debug_decorator(func):
    """If SYMPY_DEBUG is True, it will print a nice execution tree with
    arguments and results of all decorated functions, else do nothing.
    """
def debug(*args) -> None:
    """
    Print ``*args`` if SYMPY_DEBUG is True, else do nothing.
    """
def debugf(string, args) -> None:
    """
    Print ``string%args`` if SYMPY_DEBUG is True, else do nothing. This is
    intended for debug messages using formatted strings.
    """
def find_executable(executable, path: Incomplete | None = None):
    """Try to find 'executable' in the directories listed in 'path' (a
    string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH']).  Returns the complete filename or None if not
    found
    """
def func_name(x, short: bool = False):
    """Return function name of `x` (if defined) else the `type(x)`.
    If short is True and there is a shorter alias for the result,
    return the alias.

    Examples
    ========

    >>> from sympy.utilities.misc import func_name
    >>> from sympy import Matrix
    >>> from sympy.abc import x
    >>> func_name(Matrix.eye(3))
    'MutableDenseMatrix'
    >>> func_name(x < 1)
    'StrictLessThan'
    >>> func_name(x < 1, short=True)
    'Lt'
    """
def replace(string, *reps):
    '''Return ``string`` with all keys in ``reps`` replaced with
    their corresponding values, longer strings first, irrespective
    of the order they are given.  ``reps`` may be passed as tuples
    or a single mapping.

    Examples
    ========

    >>> from sympy.utilities.misc import replace
    >>> replace(\'foo\', {\'oo\': \'ar\', \'f\': \'b\'})
    \'bar\'
    >>> replace("spamham sha", ("spam", "eggs"), ("sha","md5"))
    \'eggsham md5\'

    There is no guarantee that a unique answer will be
    obtained if keys in a mapping overlap (i.e. are the same
    length and have some identical sequence at the
    beginning/end):

    >>> reps = [
    ...     (\'ab\', \'x\'),
    ...     (\'bc\', \'y\')]
    >>> replace(\'abc\', *reps) in (\'xc\', \'ay\')
    True

    References
    ==========

    .. [1] https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
    '''
def translate(s, a, b: Incomplete | None = None, c: Incomplete | None = None):
    """Return ``s`` where characters have been replaced or deleted.

    SYNTAX
    ======

    translate(s, None, deletechars):
        all characters in ``deletechars`` are deleted
    translate(s, map [,deletechars]):
        all characters in ``deletechars`` (if provided) are deleted
        then the replacements defined by map are made; if the keys
        of map are strings then the longer ones are handled first.
        Multicharacter deletions should have a value of ''.
    translate(s, oldchars, newchars, deletechars)
        all characters in ``deletechars`` are deleted
        then each character in ``oldchars`` is replaced with the
        corresponding character in ``newchars``

    Examples
    ========

    >>> from sympy.utilities.misc import translate
    >>> abc = 'abc'
    >>> translate(abc, None, 'a')
    'bc'
    >>> translate(abc, {'a': 'x'}, 'c')
    'xb'
    >>> translate(abc, {'abc': 'x', 'a': 'y'})
    'x'

    >>> translate('abcd', 'ac', 'AC', 'd')
    'AbC'

    There is no guarantee that a unique answer will be
    obtained if keys in a mapping overlap are the same
    length and have some identical sequences at the
    beginning/end:

    >>> translate(abc, {'ab': 'x', 'bc': 'y'}) in ('xc', 'ay')
    True
    """
def ordinal(num):
    """Return ordinal number string of num, e.g. 1 becomes 1st.
    """
def as_int(n, strict: bool = True):
    """
    Convert the argument to a builtin integer.

    The return value is guaranteed to be equal to the input. ValueError is
    raised if the input has a non-integral value. When ``strict`` is True, this
    uses `__index__ <https://docs.python.org/3/reference/datamodel.html#object.__index__>`_
    and when it is False it uses ``int``.


    Examples
    ========

    >>> from sympy.utilities.misc import as_int
    >>> from sympy import sqrt, S

    The function is primarily concerned with sanitizing input for
    functions that need to work with builtin integers, so anything that
    is unambiguously an integer should be returned as an int:

    >>> as_int(S(3))
    3

    Floats, being of limited precision, are not assumed to be exact and
    will raise an error unless the ``strict`` flag is False. This
    precision issue becomes apparent for large floating point numbers:

    >>> big = 1e23
    >>> type(big) is float
    True
    >>> big == int(big)
    True
    >>> as_int(big)
    Traceback (most recent call last):
    ...
    ValueError: ... is not an integer
    >>> as_int(big, strict=False)
    99999999999999991611392

    Input that might be a complex representation of an integer value is
    also rejected by default:

    >>> one = sqrt(3 + 2*sqrt(2)) - sqrt(2)
    >>> int(one) == 1
    True
    >>> as_int(one)
    Traceback (most recent call last):
    ...
    ValueError: ... is not an integer
    """

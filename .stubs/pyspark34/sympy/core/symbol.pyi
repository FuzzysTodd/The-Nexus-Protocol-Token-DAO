from .assumptions import StdFactKB as StdFactKB
from .basic import Atom as Atom, Basic as Basic
from .cache import cacheit as cacheit
from .containers import Tuple as Tuple
from .expr import AtomicExpr as AtomicExpr, Expr as Expr
from .function import AppliedUndef as AppliedUndef, FunctionClass as FunctionClass
from .kind import NumberKind as NumberKind, UndefinedKind as UndefinedKind
from .logic import fuzzy_bool as fuzzy_bool
from .singleton import S as S
from .sorting import ordered as ordered
from .sympify import sympify as sympify
from _typeshed import Incomplete
from sympy.logic.boolalg import Boolean as Boolean
from sympy.utilities.iterables import is_sequence as is_sequence, sift as sift
from sympy.utilities.misc import filldedent as filldedent
from typing import Any

class Str(Atom):
    """
    Represents string in SymPy.

    Explanation
    ===========

    Previously, ``Symbol`` was used where string is needed in ``args`` of SymPy
    objects, e.g. denoting the name of the instance. However, since ``Symbol``
    represents mathematical scalar, this class should be used instead.

    """
    def __new__(cls, name, **kwargs): ...
    def __getnewargs__(self): ...

def uniquely_named_symbol(xname, exprs=(), compare=..., modify: Incomplete | None = None, **assumptions):
    """
    Return a symbol whose name is derivated from *xname* but is unique
    from any other symbols in *exprs*.

    *xname* and symbol names in *exprs* are passed to *compare* to be
    converted to comparable forms. If ``compare(xname)`` is not unique,
    it is recursively passed to *modify* until unique name is acquired.

    Parameters
    ==========

    xname : str or Symbol
        Base name for the new symbol.

    exprs : Expr or iterable of Expr
        Expressions whose symbols are compared to *xname*.

    compare : function
        Unary function which transforms *xname* and symbol names from
        *exprs* to comparable form.

    modify : function
        Unary function which modifies the string. Default is appending
        the number, or increasing the number if exists.

    Examples
    ========

    By default, a number is appended to *xname* to generate unique name.
    If the number already exists, it is recursively increased.

    >>> from sympy.core.symbol import uniquely_named_symbol, Symbol
    >>> uniquely_named_symbol('x', Symbol('x'))
    x0
    >>> uniquely_named_symbol('x', (Symbol('x'), Symbol('x0')))
    x1
    >>> uniquely_named_symbol('x0', (Symbol('x1'), Symbol('x0')))
    x2

    Name generation can be controlled by passing *modify* parameter.

    >>> from sympy.abc import x
    >>> uniquely_named_symbol('x', x, modify=lambda s: 2*s)
    xx

    """

class Symbol(AtomicExpr, Boolean):
    """
    Assumptions:
       commutative = True

    You can override the default assumptions in the constructor.

    Examples
    ========

    >>> from sympy import symbols
    >>> A,B = symbols('A,B', commutative = False)
    >>> bool(A*B != B*A)
    True
    >>> bool(A*B*2 == 2*A*B) == True # multiplication by scalars is commutative
    True

    """
    is_comparable: bool
    name: str
    is_Symbol: bool
    is_symbol: bool
    @property
    def kind(self): ...
    def __new__(cls, name, **assumptions):
        '''Symbols are identified by name and assumptions::

        >>> from sympy import Symbol
        >>> Symbol("x") == Symbol("x")
        True
        >>> Symbol("x", real=True) == Symbol("x", real=False)
        False

        '''
    @staticmethod
    def __xnew__(cls, name, **assumptions): ...
    def __getnewargs_ex__(self): ...
    @property
    def assumptions0(self): ...
    def sort_key(self, order: Incomplete | None = None): ...
    def as_dummy(self): ...
    def as_real_imag(self, deep: bool = True, **hints): ...
    def is_constant(self, *wrt, **flags): ...
    @property
    def free_symbols(self): ...
    binary_symbols = free_symbols
    def as_set(self): ...

class Dummy(Symbol):
    '''Dummy symbols are each unique, even if they have the same name:

    Examples
    ========

    >>> from sympy import Dummy
    >>> Dummy("x") == Dummy("x")
    False

    If a name is not supplied then a string value of an internal count will be
    used. This is useful when a temporary variable is needed and the name
    of the variable used in the expression is not important.

    >>> Dummy() #doctest: +SKIP
    _Dummy_10

    '''
    is_Dummy: bool
    def __new__(cls, name: Incomplete | None = None, dummy_index: Incomplete | None = None, **assumptions): ...
    def __getnewargs_ex__(self): ...
    def sort_key(self, order: Incomplete | None = None): ...

class Wild(Symbol):
    """
    A Wild symbol matches anything, or anything
    without whatever is explicitly excluded.

    Parameters
    ==========

    name : str
        Name of the Wild instance.

    exclude : iterable, optional
        Instances in ``exclude`` will not be matched.

    properties : iterable of functions, optional
        Functions, each taking an expressions as input
        and returns a ``bool``. All functions in ``properties``
        need to return ``True`` in order for the Wild instance
        to match the expression.

    Examples
    ========

    >>> from sympy import Wild, WildFunction, cos, pi
    >>> from sympy.abc import x, y, z
    >>> a = Wild('a')
    >>> x.match(a)
    {a_: x}
    >>> pi.match(a)
    {a_: pi}
    >>> (3*x**2).match(a*x)
    {a_: 3*x}
    >>> cos(x).match(a)
    {a_: cos(x)}
    >>> b = Wild('b', exclude=[x])
    >>> (3*x**2).match(b*x)
    >>> b.match(a)
    {a_: b_}
    >>> A = WildFunction('A')
    >>> A.match(a)
    {a_: A_}

    Tips
    ====

    When using Wild, be sure to use the exclude
    keyword to make the pattern more precise.
    Without the exclude pattern, you may get matches
    that are technically correct, but not what you
    wanted. For example, using the above without
    exclude:

    >>> from sympy import symbols
    >>> a, b = symbols('a b', cls=Wild)
    >>> (2 + 3*y).match(a*x + b*y)
    {a_: 2/x, b_: 3}

    This is technically correct, because
    (2/x)*x + 3*y == 2 + 3*y, but you probably
    wanted it to not match at all. The issue is that
    you really did not want a and b to include x and y,
    and the exclude parameter lets you specify exactly
    this.  With the exclude parameter, the pattern will
    not match.

    >>> a = Wild('a', exclude=[x, y])
    >>> b = Wild('b', exclude=[x, y])
    >>> (2 + 3*y).match(a*x + b*y)

    Exclude also helps remove ambiguity from matches.

    >>> E = 2*x**3*y*z
    >>> a, b = symbols('a b', cls=Wild)
    >>> E.match(a*b)
    {a_: 2*y*z, b_: x**3}
    >>> a = Wild('a', exclude=[x, y])
    >>> E.match(a*b)
    {a_: z, b_: 2*x**3*y}
    >>> a = Wild('a', exclude=[x, y, z])
    >>> E.match(a*b)
    {a_: 2, b_: x**3*y*z}

    Wild also accepts a ``properties`` parameter:

    >>> a = Wild('a', properties=[lambda k: k.is_Integer])
    >>> E.match(a*b)
    {a_: 2, b_: x**3*y*z}

    """
    is_Wild: bool
    def __new__(cls, name, exclude=(), properties=(), **assumptions): ...
    def __getnewargs__(self): ...
    @staticmethod
    def __xnew__(cls, name, exclude, properties, **assumptions): ...
    def matches(self, expr, repl_dict: Incomplete | None = None, old: bool = False): ...

def symbols(names, *, cls=..., **args) -> Any:
    """
    Transform strings into instances of :class:`Symbol` class.

    :func:`symbols` function returns a sequence of symbols with names taken
    from ``names`` argument, which can be a comma or whitespace delimited
    string, or a sequence of strings::

        >>> from sympy import symbols, Function

        >>> x, y, z = symbols('x,y,z')
        >>> a, b, c = symbols('a b c')

    The type of output is dependent on the properties of input arguments::

        >>> symbols('x')
        x
        >>> symbols('x,')
        (x,)
        >>> symbols('x,y')
        (x, y)
        >>> symbols(('a', 'b', 'c'))
        (a, b, c)
        >>> symbols(['a', 'b', 'c'])
        [a, b, c]
        >>> symbols({'a', 'b', 'c'})
        {a, b, c}

    If an iterable container is needed for a single symbol, set the ``seq``
    argument to ``True`` or terminate the symbol name with a comma::

        >>> symbols('x', seq=True)
        (x,)

    To reduce typing, range syntax is supported to create indexed symbols.
    Ranges are indicated by a colon and the type of range is determined by
    the character to the right of the colon. If the character is a digit
    then all contiguous digits to the left are taken as the nonnegative
    starting value (or 0 if there is no digit left of the colon) and all
    contiguous digits to the right are taken as 1 greater than the ending
    value::

        >>> symbols('x:10')
        (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)

        >>> symbols('x5:10')
        (x5, x6, x7, x8, x9)
        >>> symbols('x5(:2)')
        (x50, x51)

        >>> symbols('x5:10,y:5')
        (x5, x6, x7, x8, x9, y0, y1, y2, y3, y4)

        >>> symbols(('x5:10', 'y:5'))
        ((x5, x6, x7, x8, x9), (y0, y1, y2, y3, y4))

    If the character to the right of the colon is a letter, then the single
    letter to the left (or 'a' if there is none) is taken as the start
    and all characters in the lexicographic range *through* the letter to
    the right are used as the range::

        >>> symbols('x:z')
        (x, y, z)
        >>> symbols('x:c')  # null range
        ()
        >>> symbols('x(:c)')
        (xa, xb, xc)

        >>> symbols(':c')
        (a, b, c)

        >>> symbols('a:d, x:z')
        (a, b, c, d, x, y, z)

        >>> symbols(('a:d', 'x:z'))
        ((a, b, c, d), (x, y, z))

    Multiple ranges are supported; contiguous numerical ranges should be
    separated by parentheses to disambiguate the ending number of one
    range from the starting number of the next::

        >>> symbols('x:2(1:3)')
        (x01, x02, x11, x12)
        >>> symbols(':3:2')  # parsing is from left to right
        (00, 01, 10, 11, 20, 21)

    Only one pair of parentheses surrounding ranges are removed, so to
    include parentheses around ranges, double them. And to include spaces,
    commas, or colons, escape them with a backslash::

        >>> symbols('x((a:b))')
        (x(a), x(b))
        >>> symbols(r'x(:1\\,:2)')  # or r'x((:1)\\,(:2))'
        (x(0,0), x(0,1))

    All newly created symbols have assumptions set according to ``args``::

        >>> a = symbols('a', integer=True)
        >>> a.is_integer
        True

        >>> x, y, z = symbols('x,y,z', real=True)
        >>> x.is_real and y.is_real and z.is_real
        True

    Despite its name, :func:`symbols` can create symbol-like objects like
    instances of Function or Wild classes. To achieve this, set ``cls``
    keyword argument to the desired type::

        >>> symbols('f,g,h', cls=Function)
        (f, g, h)

        >>> type(_[0])
        <class 'sympy.core.function.UndefinedFunction'>

    """
def var(names, **args):
    """
    Create symbols and inject them into the global namespace.

    Explanation
    ===========

    This calls :func:`symbols` with the same arguments and puts the results
    into the *global* namespace. It's recommended not to use :func:`var` in
    library code, where :func:`symbols` has to be used::

    Examples
    ========

    >>> from sympy import var

    >>> var('x')
    x
    >>> x # noqa: F821
    x

    >>> var('a,ab,abc')
    (a, ab, abc)
    >>> abc # noqa: F821
    abc

    >>> var('x,y', real=True)
    (x, y)
    >>> x.is_real and y.is_real # noqa: F821
    True

    See :func:`symbols` documentation for more details on what kinds of
    arguments can be passed to :func:`var`.

    """
def disambiguate(*iter):
    """
    Return a Tuple containing the passed expressions with symbols
    that appear the same when printed replaced with numerically
    subscripted symbols, and all Dummy symbols replaced with Symbols.

    Parameters
    ==========

    iter: list of symbols or expressions.

    Examples
    ========

    >>> from sympy.core.symbol import disambiguate
    >>> from sympy import Dummy, Symbol, Tuple
    >>> from sympy.abc import y

    >>> tup = Symbol('_x'), Dummy('x'), Dummy('x')
    >>> disambiguate(*tup)
    (x_2, x, x_1)

    >>> eqs = Tuple(Symbol('x')/y, Dummy('x')/y)
    >>> disambiguate(*eqs)
    (x_1/y, x/y)

    >>> ix = Symbol('x', integer=True)
    >>> vx = Symbol('x')
    >>> disambiguate(vx + ix)
    (x + x_1,)

    To make your own mapping of symbols to use, pass only the free symbols
    of the expressions and create a dictionary:

    >>> free = eqs.free_symbols
    >>> mapping = dict(zip(free, disambiguate(*free)))
    >>> eqs.xreplace(mapping)
    (x_1/y, x/y)

    """

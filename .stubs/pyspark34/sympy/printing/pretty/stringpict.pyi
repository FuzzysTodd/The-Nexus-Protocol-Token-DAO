from .pretty_symbology import hobj as hobj, line_width as line_width, pretty_use_unicode as pretty_use_unicode, vobj as vobj, xobj as xobj, xsym as xsym
from _typeshed import Incomplete
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning

class stringPict:
    """An ASCII picture.
    The pictures are represented as a list of equal length strings.
    """
    LINE: str
    s: Incomplete
    picture: Incomplete
    baseline: Incomplete
    binding: Incomplete
    def __init__(self, s, baseline: int = 0) -> None:
        """Initialize from string.
        Multiline strings are centered.
        """
    @staticmethod
    def equalLengths(lines): ...
    def height(self):
        """The height of the picture in characters."""
    def width(self):
        """The width of the picture in characters."""
    @staticmethod
    def next(*args):
        """Put a string of stringPicts next to each other.
        Returns string, baseline arguments for stringPict.
        """
    def right(self, *args):
        '''Put pictures next to this one.
        Returns string, baseline arguments for stringPict.
        (Multiline) strings are allowed, and are given a baseline of 0.

        Examples
        ========

        >>> from sympy.printing.pretty.stringpict import stringPict
        >>> print(stringPict("10").right(" + ",stringPict("1\\r-\\r2",1))[0])
             1
        10 + -
             2

        '''
    def left(self, *args):
        """Put pictures (left to right) at left.
        Returns string, baseline arguments for stringPict.
        """
    @staticmethod
    def stack(*args):
        """Put pictures on top of each other,
        from top to bottom.
        Returns string, baseline arguments for stringPict.
        The baseline is the baseline of the second picture.
        Everything is centered.
        Baseline is the baseline of the second picture.
        Strings are allowed.
        The special value stringPict.LINE is a row of '-' extended to the width.
        """
    def below(self, *args):
        '''Put pictures under this picture.
        Returns string, baseline arguments for stringPict.
        Baseline is baseline of top picture

        Examples
        ========

        >>> from sympy.printing.pretty.stringpict import stringPict
        >>> print(stringPict("x+3").below(
        ...       stringPict.LINE, \'3\')[0]) #doctest: +NORMALIZE_WHITESPACE
        x+3
        ---
         3

        '''
    def above(self, *args):
        """Put pictures above this picture.
        Returns string, baseline arguments for stringPict.
        Baseline is baseline of bottom picture.
        """
    def parens(self, left: str = '(', right: str = ')', ifascii_nougly: bool = False):
        """Put parentheses around self.
        Returns string, baseline arguments for stringPict.

        left or right can be None or empty string which means 'no paren from
        that side'
        """
    def leftslash(self):
        """Precede object by a slash of the proper size.
        """
    def root(self, n: Incomplete | None = None):
        """Produce a nice root symbol.
        Produces ugly results for big n inserts.
        """
    def render(self, *args, **kwargs):
        """Return the string form of self.

           Unless the argument line_break is set to False, it will
           break the expression in a form that can be printed
           on the terminal without being broken up.
         """
    def terminal_width(self):
        """Return the terminal width if possible, otherwise return 0.
        """
    def __eq__(self, o): ...
    def __hash__(self): ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...

class prettyForm(stringPict):
    '''
    Extension of the stringPict class that knows about basic math applications,
    optimizing double minus signs.

    "Binding" is interpreted as follows::

        ATOM this is an atom: never needs to be parenthesized
        FUNC this is a function application: parenthesize if added (?)
        DIV  this is a division: make wider division if divided
        POW  this is a power: only parenthesize if exponent
        MUL  this is a multiplication: parenthesize if powered
        ADD  this is an addition: parenthesize if multiplied or powered
        NEG  this is a negative number: optimize if added, parenthesize if
             multiplied or powered
        OPEN this is an open object: parenthesize if added, multiplied, or
             powered (example: Piecewise)
    '''
    ATOM: Incomplete
    FUNC: Incomplete
    DIV: Incomplete
    POW: Incomplete
    MUL: Incomplete
    ADD: Incomplete
    NEG: Incomplete
    OPEN: Incomplete
    binding: Incomplete
    def __init__(self, s, baseline: int = 0, binding: int = 0, unicode: Incomplete | None = None) -> None:
        """Initialize from stringPict and binding power."""
    @property
    def unicode(self): ...
    def __add__(self, *others):
        """Make a pretty addition.
        Addition of negative numbers is simplified.
        """
    def __truediv__(self, den, slashed: bool = False):
        """Make a pretty division; stacked or slashed.
        """
    def __mul__(self, *others):
        """Make a pretty multiplication.
        Parentheses are needed around +, - and neg.
        """
    def __pow__(self, b):
        """Make a pretty power.
        """
    simpleFunctions: Incomplete
    @staticmethod
    def apply(function, *args):
        """Functions of one or more variables.
        """

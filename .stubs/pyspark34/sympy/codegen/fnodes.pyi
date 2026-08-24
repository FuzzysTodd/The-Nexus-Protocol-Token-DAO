from _typeshed import Incomplete
from sympy.codegen.ast import Attribute as Attribute, CodeBlock as CodeBlock, FunctionCall as FunctionCall, Node as Node, String as String, Token as Token, Variable as Variable, none as none
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.function import Function as Function
from sympy.core.numbers import Float as Float, Integer as Integer
from sympy.core.symbol import Str as Str
from sympy.core.sympify import sympify as sympify
from sympy.logic import false as false, true as true
from sympy.utilities.iterables import iterable as iterable

pure: Incomplete
elemental: Incomplete
intent_in: Incomplete
intent_out: Incomplete
intent_inout: Incomplete
allocatable: Incomplete

class Program(Token):
    """ Represents a 'program' block in Fortran.

    Examples
    ========

    >>> from sympy.codegen.ast import Print
    >>> from sympy.codegen.fnodes import Program
    >>> prog = Program('myprogram', [Print([42])])
    >>> from sympy import fcode
    >>> print(fcode(prog, source_format='free'))
    program myprogram
        print *, 42
    end program

    """
class use_rename(Token):
    ''' Represents a renaming in a use statement in Fortran.

    Examples
    ========

    >>> from sympy.codegen.fnodes import use_rename, use
    >>> from sympy import fcode
    >>> ren = use_rename("thingy", "convolution2d")
    >>> print(fcode(ren, source_format=\'free\'))
    thingy => convolution2d
    >>> full = use(\'signallib\', only=[\'snr\', ren])
    >>> print(fcode(full, source_format=\'free\'))
    use signallib, only: snr, thingy => convolution2d

    '''

class use(Token):
    """ Represents a use statement in Fortran.

    Examples
    ========

    >>> from sympy.codegen.fnodes import use
    >>> from sympy import fcode
    >>> fcode(use('signallib'), source_format='free')
    'use signallib'
    >>> fcode(use('signallib', [('metric', 'snr')]), source_format='free')
    'use signallib, metric => snr'
    >>> fcode(use('signallib', only=['snr', 'convolution2d']), source_format='free')
    'use signallib, only: snr, convolution2d'

    """
    defaults: Incomplete

class Module(Token):
    """ Represents a module in Fortran.

    Examples
    ========

    >>> from sympy.codegen.fnodes import Module
    >>> from sympy import fcode
    >>> print(fcode(Module('signallib', ['implicit none'], []), source_format='free'))
    module signallib
    implicit none
    <BLANKLINE>
    contains
    <BLANKLINE>
    <BLANKLINE>
    end module

    """
    defaults: Incomplete

class Subroutine(Node):
    """ Represents a subroutine in Fortran.

    Examples
    ========

    >>> from sympy import fcode, symbols
    >>> from sympy.codegen.ast import Print
    >>> from sympy.codegen.fnodes import Subroutine
    >>> x, y = symbols('x y', real=True)
    >>> sub = Subroutine('mysub', [x, y], [Print([x**2 + y**2, x*y])])
    >>> print(fcode(sub, source_format='free', standard=2003))
    subroutine mysub(x, y)
    real*8 :: x
    real*8 :: y
    print *, x**2 + y**2, x*y
    end subroutine

    """
class SubroutineCall(Token):
    """ Represents a call to a subroutine in Fortran.

    Examples
    ========

    >>> from sympy.codegen.fnodes import SubroutineCall
    >>> from sympy import fcode
    >>> fcode(SubroutineCall('mysub', 'x y'.split()))
    '       call mysub(x, y)'

    """

class Do(Token):
    """ Represents a Do loop in in Fortran.

    Examples
    ========

    >>> from sympy import fcode, symbols
    >>> from sympy.codegen.ast import aug_assign, Print
    >>> from sympy.codegen.fnodes import Do
    >>> i, n = symbols('i n', integer=True)
    >>> r = symbols('r', real=True)
    >>> body = [aug_assign(r, '+', 1/i), Print([i, r])]
    >>> do1 = Do(body, i, 1, n)
    >>> print(fcode(do1, source_format='free'))
    do i = 1, n
        r = r + 1d0/i
        print *, i, r
    end do
    >>> do2 = Do(body, i, 1, n, 2)
    >>> print(fcode(do2, source_format='free'))
    do i = 1, n, 2
        r = r + 1d0/i
        print *, i, r
    end do

    """
    defaults: Incomplete

class ArrayConstructor(Token):
    """ Represents an array constructor.

    Examples
    ========

    >>> from sympy import fcode
    >>> from sympy.codegen.fnodes import ArrayConstructor
    >>> ac = ArrayConstructor([1, 2, 3])
    >>> fcode(ac, standard=95, source_format='free')
    '(/1, 2, 3/)'
    >>> fcode(ac, standard=2003, source_format='free')
    '[1, 2, 3]'

    """

class ImpliedDoLoop(Token):
    """ Represents an implied do loop in Fortran.

    Examples
    ========

    >>> from sympy import Symbol, fcode
    >>> from sympy.codegen.fnodes import ImpliedDoLoop, ArrayConstructor
    >>> i = Symbol('i', integer=True)
    >>> idl = ImpliedDoLoop(i**3, i, -3, 3, 2)  # -27, -1, 1, 27
    >>> ac = ArrayConstructor([-28, idl, 28]) # -28, -27, -1, 1, 27, 28
    >>> fcode(ac, standard=2003, source_format='free')
    '[-28, (i**3, i = -3, 3, 2), 28]'

    """
    defaults: Incomplete

class Extent(Basic):
    """ Represents a dimension extent.

    Examples
    ========

    >>> from sympy.codegen.fnodes import Extent
    >>> e = Extent(-3, 3)  # -3, -2, -1, 0, 1, 2, 3
    >>> from sympy import fcode
    >>> fcode(e, source_format='free')
    '-3:3'
    >>> from sympy.codegen.ast import Variable, real
    >>> from sympy.codegen.fnodes import dimension, intent_out
    >>> dim = dimension(e, e)
    >>> arr = Variable('x', real, attrs=[dim, intent_out])
    >>> fcode(arr.as_Declaration(), source_format='free', standard=2003)
    'real*8, dimension(-3:3, -3:3), intent(out) :: x'

    """
    def __new__(cls, *args): ...

assumed_extent: Incomplete

def dimension(*args):
    """ Creates a 'dimension' Attribute with (up to 7) extents.

    Examples
    ========

    >>> from sympy import fcode
    >>> from sympy.codegen.fnodes import dimension, intent_in
    >>> dim = dimension('2', ':')  # 2 rows, runtime determined number of columns
    >>> from sympy.codegen.ast import Variable, integer
    >>> arr = Variable('a', integer, attrs=[dim, intent_in])
    >>> fcode(arr.as_Declaration(), source_format='free', standard=2003)
    'integer*4, dimension(2, :), intent(in) :: a'

    """

assumed_size: Incomplete

def array(symbol, dim, intent: Incomplete | None = None, *, attrs=(), value: Incomplete | None = None, type: Incomplete | None = None):
    """ Convenience function for creating a Variable instance for a Fortran array.

    Parameters
    ==========

    symbol : symbol
    dim : Attribute or iterable
        If dim is an ``Attribute`` it need to have the name 'dimension'. If it is
        not an ``Attribute``, then it is passed to :func:`dimension` as ``*dim``
    intent : str
        One of: 'in', 'out', 'inout' or None
    \\*\\*kwargs:
        Keyword arguments for ``Variable`` ('type' & 'value')

    Examples
    ========

    >>> from sympy import fcode
    >>> from sympy.codegen.ast import integer, real
    >>> from sympy.codegen.fnodes import array
    >>> arr = array('a', '*', 'in', type=integer)
    >>> print(fcode(arr.as_Declaration(), source_format='free', standard=2003))
    integer*4, dimension(*), intent(in) :: a
    >>> x = array('x', [3, ':', ':'], intent='out', type=real)
    >>> print(fcode(x.as_Declaration(value=1), source_format='free', standard=2003))
    real*8, dimension(3, :, :), intent(out) :: x = 1

    """
def allocated(array):
    ''' Creates an AST node for a function call to Fortran\'s "allocated(...)"

    Examples
    ========

    >>> from sympy import fcode
    >>> from sympy.codegen.fnodes import allocated
    >>> alloc = allocated(\'x\')
    >>> fcode(alloc, source_format=\'free\')
    \'allocated(x)\'

    '''
def lbound(array, dim: Incomplete | None = None, kind: Incomplete | None = None):
    ''' Creates an AST node for a function call to Fortran\'s "lbound(...)"

    Parameters
    ==========

    array : Symbol or String
    dim : expr
    kind : expr

    Examples
    ========

    >>> from sympy import fcode
    >>> from sympy.codegen.fnodes import lbound
    >>> lb = lbound(\'arr\', dim=2)
    >>> fcode(lb, source_format=\'free\')
    \'lbound(arr, 2)\'

    '''
def ubound(array, dim: Incomplete | None = None, kind: Incomplete | None = None): ...
def shape(source, kind: Incomplete | None = None):
    ''' Creates an AST node for a function call to Fortran\'s "shape(...)"

    Parameters
    ==========

    source : Symbol or String
    kind : expr

    Examples
    ========

    >>> from sympy import fcode
    >>> from sympy.codegen.fnodes import shape
    >>> shp = shape(\'x\')
    >>> fcode(shp, source_format=\'free\')
    \'shape(x)\'

    '''
def size(array, dim: Incomplete | None = None, kind: Incomplete | None = None):
    ''' Creates an AST node for a function call to Fortran\'s "size(...)"

    Examples
    ========

    >>> from sympy import fcode, Symbol
    >>> from sympy.codegen.ast import FunctionDefinition, real, Return
    >>> from sympy.codegen.fnodes import array, sum_, size
    >>> a = Symbol(\'a\', real=True)
    >>> body = [Return((sum_(a**2)/size(a))**.5)]
    >>> arr = array(a, dim=[\':\'], intent=\'in\')
    >>> fd = FunctionDefinition(real, \'rms\', [arr], body)
    >>> print(fcode(fd, source_format=\'free\', standard=2003))
    real*8 function rms(a)
    real*8, dimension(:), intent(in) :: a
    rms = sqrt(sum(a**2)*1d0/size(a))
    end function

    '''
def reshape(source, shape, pad: Incomplete | None = None, order: Incomplete | None = None):
    ''' Creates an AST node for a function call to Fortran\'s "reshape(...)"

    Parameters
    ==========

    source : Symbol or String
    shape : ArrayExpr

    '''
def bind_C(name: Incomplete | None = None):
    ''' Creates an Attribute ``bind_C`` with a name.

    Parameters
    ==========

    name : str

    Examples
    ========

    >>> from sympy import fcode, Symbol
    >>> from sympy.codegen.ast import FunctionDefinition, real, Return
    >>> from sympy.codegen.fnodes import array, sum_, bind_C
    >>> a = Symbol(\'a\', real=True)
    >>> s = Symbol(\'s\', integer=True)
    >>> arr = array(a, dim=[s], intent=\'in\')
    >>> body = [Return((sum_(a**2)/s)**.5)]
    >>> fd = FunctionDefinition(real, \'rms\', [arr, s], body, attrs=[bind_C(\'rms\')])
    >>> print(fcode(fd, source_format=\'free\', standard=2003))
    real*8 function rms(a, s) bind(C, name="rms")
    real*8, dimension(s), intent(in) :: a
    integer*4 :: s
    rms = sqrt(sum(a**2)/s)
    end function

    '''

class GoTo(Token):
    """ Represents a goto statement in Fortran

    Examples
    ========

    >>> from sympy.codegen.fnodes import GoTo
    >>> go = GoTo([10, 20, 30], 'i')
    >>> from sympy import fcode
    >>> fcode(go, source_format='free')
    'go to (10, 20, 30), i'

    """
    defaults: Incomplete

class FortranReturn(Token):
    ''' AST node explicitly mapped to a fortran "return".

    Explanation
    ===========

    Because a return statement in fortran is different from C, and
    in order to aid reuse of our codegen ASTs the ordinary
    ``.codegen.ast.Return`` is interpreted as assignment to
    the result variable of the function. If one for some reason needs
    to generate a fortran RETURN statement, this node should be used.

    Examples
    ========

    >>> from sympy.codegen.fnodes import FortranReturn
    >>> from sympy import fcode
    >>> fcode(FortranReturn(\'x\'))
    \'       return x\'

    '''
    defaults: Incomplete

class FFunction(Function): ...
class F95Function(FFunction): ...

class isign(FFunction):
    """ Fortran sign intrinsic for integer arguments. """
    nargs: int

class dsign(FFunction):
    """ Fortran sign intrinsic for double precision arguments. """
    nargs: int

class cmplx(FFunction):
    """ Fortran complex conversion function. """
    nargs: int

class kind(FFunction):
    """ Fortran kind function. """
    nargs: int

class merge(F95Function):
    """ Fortran merge function """
    nargs: int

class _literal(Float): ...
class literal_sp(_literal):
    """ Fortran single precision real literal """
class literal_dp(_literal):
    """ Fortran double precision real literal """

class sum_(Token, Expr):
    defaults: Incomplete

class product_(Token, Expr):
    defaults: Incomplete

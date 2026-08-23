from _typeshed import Incomplete
from sympy.core.numbers import Integer as Integer, Rational as Rational
from sympy.core.sympify import sympify as sympify
from sympy.matrices.dense import MutableDenseMatrix as MutableDenseMatrix
from sympy.polys.domainmatrix import DomainMatrix as DomainMatrix
from sympy.polys.domains import EX as EX, QQ as QQ, ZZ as ZZ
from sympy.polys.polyerrors import NotInvertible as NotInvertible
from sympy.polys.rings import sring as sring
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import connected_components as connected_components

class PolyNonlinearError(Exception):
    """Raised by solve_lin_sys for nonlinear equations"""

class RawMatrix(MutableDenseMatrix):
    """
    .. deprecated:: 1.9

       This class fundamentally is broken by design. Use ``DomainMatrix`` if
       you want a matrix over the polys domains or ``Matrix`` for a matrix
       with ``Expr`` elements. The ``RawMatrix`` class will be removed/broken
       in future in order to reestablish the invariant that the elements of a
       Matrix should be of type ``Expr``.

    """
    ring: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

def eqs_to_matrix(eqs_coeffs, eqs_rhs, gens, domain):
    """Get matrix from linear equations in dict format.

    Explanation
    ===========

    Get the matrix representation of a system of linear equations represented
    as dicts with low-level DomainElement coefficients. This is an
    *internal* function that is used by solve_lin_sys.

    Parameters
    ==========

    eqs_coeffs: list[dict[Symbol, DomainElement]]
        The left hand sides of the equations as dicts mapping from symbols to
        coefficients where the coefficients are instances of
        DomainElement.
    eqs_rhs: list[DomainElements]
        The right hand sides of the equations as instances of
        DomainElement.
    gens: list[Symbol]
        The unknowns in the system of equations.
    domain: Domain
        The domain for coefficients of both lhs and rhs.

    Returns
    =======

    The augmented matrix representation of the system as a DomainMatrix.

    Examples
    ========

    >>> from sympy import symbols, ZZ
    >>> from sympy.polys.solvers import eqs_to_matrix
    >>> x, y = symbols('x, y')
    >>> eqs_coeff = [{x:ZZ(1), y:ZZ(1)}, {x:ZZ(1), y:ZZ(-1)}]
    >>> eqs_rhs = [ZZ(0), ZZ(-1)]
    >>> eqs_to_matrix(eqs_coeff, eqs_rhs, [x, y], ZZ)
    DomainMatrix([[1, 1, 0], [1, -1, 1]], (2, 3), ZZ)

    See also
    ========

    solve_lin_sys: Uses :func:`~eqs_to_matrix` internally
    """
def sympy_eqs_to_ring(eqs, symbols):
    """Convert a system of equations from Expr to a PolyRing

    Explanation
    ===========

    High-level functions like ``solve`` expect Expr as inputs but can use
    ``solve_lin_sys`` internally. This function converts equations from
    ``Expr`` to the low-level poly types used by the ``solve_lin_sys``
    function.

    Parameters
    ==========

    eqs: List of Expr
        A list of equations as Expr instances
    symbols: List of Symbol
        A list of the symbols that are the unknowns in the system of
        equations.

    Returns
    =======

    Tuple[List[PolyElement], Ring]: The equations as PolyElement instances
    and the ring of polynomials within which each equation is represented.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.polys.solvers import sympy_eqs_to_ring
    >>> a, x, y = symbols('a, x, y')
    >>> eqs = [x-y, x+a*y]
    >>> eqs_ring, ring = sympy_eqs_to_ring(eqs, [x, y])
    >>> eqs_ring
    [x - y, x + a*y]
    >>> type(eqs_ring[0])
    <class 'sympy.polys.rings.PolyElement'>
    >>> ring
    ZZ(a)[x,y]

    With the equations in this form they can be passed to ``solve_lin_sys``:

    >>> from sympy.polys.solvers import solve_lin_sys
    >>> solve_lin_sys(eqs_ring, ring)
    {y: 0, x: 0}
    """
def solve_lin_sys(eqs, ring, _raw: bool = True):
    """Solve a system of linear equations from a PolynomialRing

    Explanation
    ===========

    Solves a system of linear equations given as PolyElement instances of a
    PolynomialRing. The basic arithmetic is carried out using instance of
    DomainElement which is more efficient than :class:`~sympy.core.expr.Expr`
    for the most common inputs.

    While this is a public function it is intended primarily for internal use
    so its interface is not necessarily convenient. Users are suggested to use
    the :func:`sympy.solvers.solveset.linsolve` function (which uses this
    function internally) instead.

    Parameters
    ==========

    eqs: list[PolyElement]
        The linear equations to be solved as elements of a
        PolynomialRing (assumed equal to zero).
    ring: PolynomialRing
        The polynomial ring from which eqs are drawn. The generators of this
        ring are the unknowns to be solved for and the domain of the ring is
        the domain of the coefficients of the system of equations.
    _raw: bool
        If *_raw* is False, the keys and values in the returned dictionary
        will be of type Expr (and the unit of the field will be removed from
        the keys) otherwise the low-level polys types will be returned, e.g.
        PolyElement: PythonRational.

    Returns
    =======

    ``None`` if the system has no solution.

    dict[Symbol, Expr] if _raw=False

    dict[Symbol, DomainElement] if _raw=True.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.polys.solvers import solve_lin_sys, sympy_eqs_to_ring
    >>> x, y = symbols('x, y')
    >>> eqs = [x - y, x + y - 2]
    >>> eqs_ring, ring = sympy_eqs_to_ring(eqs, [x, y])
    >>> solve_lin_sys(eqs_ring, ring)
    {y: 1, x: 1}

    Passing ``_raw=False`` returns the same result except that the keys are
    ``Expr`` rather than low-level poly types.

    >>> solve_lin_sys(eqs_ring, ring, _raw=False)
    {x: 1, y: 1}

    See also
    ========

    sympy_eqs_to_ring: prepares the inputs to ``solve_lin_sys``.
    linsolve: ``linsolve`` uses ``solve_lin_sys`` internally.
    sympy.solvers.solvers.solve: ``solve`` uses ``solve_lin_sys`` internally.
    """

from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple, TupleKind as TupleKind
from sympy.core.decorators import sympify_method_args as sympify_method_args, sympify_return as sympify_return
from sympy.core.evalf import EvalfMixin as EvalfMixin
from sympy.core.expr import Expr as Expr
from sympy.core.function import Lambda as Lambda
from sympy.core.kind import Kind as Kind, NumberKind as NumberKind, UndefinedKind as UndefinedKind
from sympy.core.logic import FuzzyBool as FuzzyBool, fuzzy_and as fuzzy_and, fuzzy_bool as fuzzy_bool, fuzzy_not as fuzzy_not, fuzzy_or as fuzzy_or
from sympy.core.numbers import Float as Float, Integer as Integer
from sympy.core.operations import LatticeOp as LatticeOp
from sympy.core.parameters import global_parameters as global_parameters
from sympy.core.relational import Eq as Eq, Ne as Ne, is_lt as is_lt
from sympy.core.singleton import S as S, Singleton as Singleton
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, symbols as symbols, uniquely_named_symbol as uniquely_named_symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.logic.boolalg import And as And, Not as Not, Or as Or, Xor as Xor, false as false, true as true
from sympy.utilities.decorator import deprecated as deprecated
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import iproduct as iproduct, iterable as iterable, roundrobin as roundrobin, sift as sift, subsets as subsets
from sympy.utilities.misc import filldedent as filldedent, func_name as func_name
from typing import Any, Callable

tfn: Incomplete

class Set(Basic, EvalfMixin):
    """
    The base class for any kind of set.

    Explanation
    ===========

    This is not meant to be used directly as a container of items. It does not
    behave like the builtin ``set``; see :class:`FiniteSet` for that.

    Real intervals are represented by the :class:`Interval` class and unions of
    sets by the :class:`Union` class. The empty set is represented by the
    :class:`EmptySet` class and available as a singleton as ``S.EmptySet``.
    """
    is_number: bool
    is_iterable: bool
    is_interval: bool
    is_FiniteSet: bool
    is_Interval: bool
    is_ProductSet: bool
    is_Union: bool
    is_Intersection: FuzzyBool
    is_UniversalSet: FuzzyBool
    is_Complement: FuzzyBool
    is_ComplexRegion: bool
    is_empty: FuzzyBool
    is_finite_set: FuzzyBool
    @property
    def is_EmptySet(self) -> None: ...
    def union(self, other):
        """
        Returns the union of ``self`` and ``other``.

        Examples
        ========

        As a shortcut it is possible to use the ``+`` operator:

        >>> from sympy import Interval, FiniteSet
        >>> Interval(0, 1).union(Interval(2, 3))
        Union(Interval(0, 1), Interval(2, 3))
        >>> Interval(0, 1) + Interval(2, 3)
        Union(Interval(0, 1), Interval(2, 3))
        >>> Interval(1, 2, True, True) + FiniteSet(2, 3)
        Union({3}, Interval.Lopen(1, 2))

        Similarly it is possible to use the ``-`` operator for set differences:

        >>> Interval(0, 2) - Interval(0, 1)
        Interval.Lopen(1, 2)
        >>> Interval(1, 3) - FiniteSet(2)
        Union(Interval.Ropen(1, 2), Interval.Lopen(2, 3))

        """
    def intersect(self, other):
        """
        Returns the intersection of 'self' and 'other'.

        Examples
        ========

        >>> from sympy import Interval

        >>> Interval(1, 3).intersect(Interval(1, 2))
        Interval(1, 2)

        >>> from sympy import imageset, Lambda, symbols, S
        >>> n, m = symbols('n m')
        >>> a = imageset(Lambda(n, 2*n), S.Integers)
        >>> a.intersect(imageset(Lambda(m, 2*m + 1), S.Integers))
        EmptySet

        """
    def intersection(self, other):
        """
        Alias for :meth:`intersect()`
        """
    def is_disjoint(self, other):
        """
        Returns True if ``self`` and ``other`` are disjoint.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 2).is_disjoint(Interval(1, 2))
        False
        >>> Interval(0, 2).is_disjoint(Interval(3, 4))
        True

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Disjoint_sets
        """
    def isdisjoint(self, other):
        """
        Alias for :meth:`is_disjoint()`
        """
    def complement(self, universe):
        """
        The complement of 'self' w.r.t the given universe.

        Examples
        ========

        >>> from sympy import Interval, S
        >>> Interval(0, 1).complement(S.Reals)
        Union(Interval.open(-oo, 0), Interval.open(1, oo))

        >>> Interval(0, 1).complement(S.UniversalSet)
        Complement(UniversalSet, Interval(0, 1))

        """
    def symmetric_difference(self, other):
        """
        Returns symmetric difference of ``self`` and ``other``.

        Examples
        ========

        >>> from sympy import Interval, S
        >>> Interval(1, 3).symmetric_difference(S.Reals)
        Union(Interval.open(-oo, 1), Interval.open(3, oo))
        >>> Interval(1, 10).symmetric_difference(S.Reals)
        Union(Interval.open(-oo, 1), Interval.open(10, oo))

        >>> from sympy import S, EmptySet
        >>> S.Reals.symmetric_difference(EmptySet)
        Reals

        References
        ==========
        .. [1] https://en.wikipedia.org/wiki/Symmetric_difference

        """
    @property
    def inf(self):
        """
        The infimum of ``self``.

        Examples
        ========

        >>> from sympy import Interval, Union
        >>> Interval(0, 1).inf
        0
        >>> Union(Interval(0, 1), Interval(2, 3)).inf
        0

        """
    @property
    def sup(self):
        """
        The supremum of ``self``.

        Examples
        ========

        >>> from sympy import Interval, Union
        >>> Interval(0, 1).sup
        1
        >>> Union(Interval(0, 1), Interval(2, 3)).sup
        3

        """
    def contains(self, other):
        """
        Returns a SymPy value indicating whether ``other`` is contained
        in ``self``: ``true`` if it is, ``false`` if it is not, else
        an unevaluated ``Contains`` expression (or, as in the case of
        ConditionSet and a union of FiniteSet/Intervals, an expression
        indicating the conditions for containment).

        Examples
        ========

        >>> from sympy import Interval, S
        >>> from sympy.abc import x

        >>> Interval(0, 1).contains(0.5)
        True

        As a shortcut it is possible to use the ``in`` operator, but that
        will raise an error unless an affirmative true or false is not
        obtained.

        >>> Interval(0, 1).contains(x)
        (0 <= x) & (x <= 1)
        >>> x in Interval(0, 1)
        Traceback (most recent call last):
        ...
        TypeError: did not evaluate to a bool: None

        The result of 'in' is a bool, not a SymPy value

        >>> 1 in Interval(0, 2)
        True
        >>> _ is S.true
        False
        """
    def is_subset(self, other):
        """
        Returns True if ``self`` is a subset of ``other``.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 0.5).is_subset(Interval(0, 1))
        True
        >>> Interval(0, 1).is_subset(Interval(0, 1, left_open=True))
        False

        """
    def issubset(self, other):
        """
        Alias for :meth:`is_subset()`
        """
    def is_proper_subset(self, other):
        """
        Returns True if ``self`` is a proper subset of ``other``.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 0.5).is_proper_subset(Interval(0, 1))
        True
        >>> Interval(0, 1).is_proper_subset(Interval(0, 1))
        False

        """
    def is_superset(self, other):
        """
        Returns True if ``self`` is a superset of ``other``.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 0.5).is_superset(Interval(0, 1))
        False
        >>> Interval(0, 1).is_superset(Interval(0, 1, left_open=True))
        True

        """
    def issuperset(self, other):
        """
        Alias for :meth:`is_superset()`
        """
    def is_proper_superset(self, other):
        """
        Returns True if ``self`` is a proper superset of ``other``.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 1).is_proper_superset(Interval(0, 0.5))
        True
        >>> Interval(0, 1).is_proper_superset(Interval(0, 1))
        False

        """
    def powerset(self):
        """
        Find the Power set of ``self``.

        Examples
        ========

        >>> from sympy import EmptySet, FiniteSet, Interval

        A power set of an empty set:

        >>> A = EmptySet
        >>> A.powerset()
        {EmptySet}

        A power set of a finite set:

        >>> A = FiniteSet(1, 2)
        >>> a, b, c = FiniteSet(1), FiniteSet(2), FiniteSet(1, 2)
        >>> A.powerset() == FiniteSet(a, b, c, EmptySet)
        True

        A power set of an interval:

        >>> Interval(1, 2).powerset()
        PowerSet(Interval(1, 2))

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Power_set

        """
    @property
    def measure(self):
        """
        The (Lebesgue) measure of ``self``.

        Examples
        ========

        >>> from sympy import Interval, Union
        >>> Interval(0, 1).measure
        1
        >>> Union(Interval(0, 1), Interval(2, 3)).measure
        2

        """
    @property
    def kind(self):
        """
        The kind of a Set

        Explanation
        ===========

        Any :class:`Set` will have kind :class:`SetKind` which is
        parametrised by the kind of the elements of the set. For example
        most sets are sets of numbers and will have kind
        ``SetKind(NumberKind)``. If elements of sets are different in kind than
        their kind will ``SetKind(UndefinedKind)``. See
        :class:`sympy.core.kind.Kind` for an explanation of the kind system.

        Examples
        ========

        >>> from sympy import Interval, Matrix, FiniteSet, EmptySet, ProductSet, PowerSet

        >>> FiniteSet(Matrix([1, 2])).kind
        SetKind(MatrixKind(NumberKind))

        >>> Interval(1, 2).kind
        SetKind(NumberKind)

        >>> EmptySet.kind
        SetKind()

        A :class:`sympy.sets.powerset.PowerSet` is a set of sets:

        >>> PowerSet({1, 2, 3}).kind
        SetKind(SetKind(NumberKind))

        A :class:`ProductSet` represents the set of tuples of elements of
        other sets. Its kind is :class:`sympy.core.containers.TupleKind`
        parametrised by the kinds of the elements of those sets:

        >>> p = ProductSet(FiniteSet(1, 2), FiniteSet(3, 4))
        >>> list(p)
        [(1, 3), (2, 3), (1, 4), (2, 4)]
        >>> p.kind
        SetKind(TupleKind(NumberKind, NumberKind))

        When all elements of the set do not have same kind, the kind
        will be returned as ``SetKind(UndefinedKind)``:

        >>> FiniteSet(0, Matrix([1, 2])).kind
        SetKind(UndefinedKind)

        The kind of the elements of a set are given by the ``element_kind``
        attribute of ``SetKind``:

        >>> Interval(1, 2).kind.element_kind
        NumberKind

        See Also
        ========

        NumberKind
        sympy.core.kind.UndefinedKind
        sympy.core.containers.TupleKind
        MatrixKind
        sympy.matrices.expressions.sets.MatrixSet
        sympy.sets.conditionset.ConditionSet
        Rationals
        Naturals
        Integers
        sympy.sets.fancysets.ImageSet
        sympy.sets.fancysets.Range
        sympy.sets.fancysets.ComplexRegion
        sympy.sets.powerset.PowerSet
        sympy.sets.sets.ProductSet
        sympy.sets.sets.Interval
        sympy.sets.sets.Union
        sympy.sets.sets.Intersection
        sympy.sets.sets.Complement
        sympy.sets.sets.EmptySet
        sympy.sets.sets.UniversalSet
        sympy.sets.sets.FiniteSet
        sympy.sets.sets.SymmetricDifference
        sympy.sets.sets.DisjointUnion
        """
    @property
    def boundary(self):
        """
        The boundary or frontier of a set.

        Explanation
        ===========

        A point x is on the boundary of a set S if

        1.  x is in the closure of S.
            I.e. Every neighborhood of x contains a point in S.
        2.  x is not in the interior of S.
            I.e. There does not exist an open set centered on x contained
            entirely within S.

        There are the points on the outer rim of S.  If S is open then these
        points need not actually be contained within S.

        For example, the boundary of an interval is its start and end points.
        This is true regardless of whether or not the interval is open.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 1).boundary
        {0, 1}
        >>> Interval(0, 1, True, False).boundary
        {0, 1}
        """
    @property
    def is_open(self):
        """
        Property method to check whether a set is open.

        Explanation
        ===========

        A set is open if and only if it has an empty intersection with its
        boundary. In particular, a subset A of the reals is open if and only
        if each one of its points is contained in an open interval that is a
        subset of A.

        Examples
        ========
        >>> from sympy import S
        >>> S.Reals.is_open
        True
        >>> S.Rationals.is_open
        False
        """
    @property
    def is_closed(self):
        """
        A property method to check whether a set is closed.

        Explanation
        ===========

        A set is closed if its complement is an open set. The closedness of a
        subset of the reals is determined with respect to R and its standard
        topology.

        Examples
        ========
        >>> from sympy import Interval
        >>> Interval(0, 1).is_closed
        True
        """
    @property
    def closure(self):
        """
        Property method which returns the closure of a set.
        The closure is defined as the union of the set itself and its
        boundary.

        Examples
        ========
        >>> from sympy import S, Interval
        >>> S.Reals.closure
        Reals
        >>> Interval(0, 1).closure
        Interval(0, 1)
        """
    @property
    def interior(self):
        """
        Property method which returns the interior of a set.
        The interior of a set S consists all points of S that do not
        belong to the boundary of S.

        Examples
        ========
        >>> from sympy import Interval
        >>> Interval(0, 1).interior
        Interval.open(0, 1)
        >>> Interval(0, 1).boundary.interior
        EmptySet
        """
    def __add__(self, other): ...
    def __or__(self, other): ...
    def __and__(self, other): ...
    def __mul__(self, other): ...
    def __xor__(self, other): ...
    def __pow__(self, exp): ...
    def __sub__(self, other): ...
    def __contains__(self, other) -> bool: ...

class ProductSet(Set):
    """
    Represents a Cartesian Product of Sets.

    Explanation
    ===========

    Returns a Cartesian product given several sets as either an iterable
    or individual arguments.

    Can use ``*`` operator on any sets for convenient shorthand.

    Examples
    ========

    >>> from sympy import Interval, FiniteSet, ProductSet
    >>> I = Interval(0, 5); S = FiniteSet(1, 2, 3)
    >>> ProductSet(I, S)
    ProductSet(Interval(0, 5), {1, 2, 3})

    >>> (2, 2) in ProductSet(I, S)
    True

    >>> Interval(0, 1) * Interval(0, 1) # The unit square
    ProductSet(Interval(0, 1), Interval(0, 1))

    >>> coin = FiniteSet('H', 'T')
    >>> set(coin**2)
    {(H, H), (H, T), (T, H), (T, T)}

    The Cartesian product is not commutative or associative e.g.:

    >>> I*S == S*I
    False
    >>> (I*I)*I == I*(I*I)
    False

    Notes
    =====

    - Passes most operations down to the argument sets

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Cartesian_product
    """
    is_ProductSet: bool
    def __new__(cls, *sets, **assumptions): ...
    @property
    def sets(self): ...
    def flatten(self): ...
    def as_relational(self, *symbols): ...
    @property
    def is_iterable(self):
        """
        A property method which tests whether a set is iterable or not.
        Returns True if set is iterable, otherwise returns False.

        Examples
        ========

        >>> from sympy import FiniteSet, Interval
        >>> I = Interval(0, 1)
        >>> A = FiniteSet(1, 2, 3, 4, 5)
        >>> I.is_iterable
        False
        >>> A.is_iterable
        True

        """
    def __iter__(self):
        """
        A method which implements is_iterable property method.
        If self.is_iterable returns True (both constituent sets are iterable),
        then return the Cartesian Product. Otherwise, raise TypeError.
        """
    @property
    def is_empty(self): ...
    @property
    def is_finite_set(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...

class Interval(Set):
    """
    Represents a real interval as a Set.

    Usage:
        Returns an interval with end points ``start`` and ``end``.

        For ``left_open=True`` (default ``left_open`` is ``False``) the interval
        will be open on the left. Similarly, for ``right_open=True`` the interval
        will be open on the right.

    Examples
    ========

    >>> from sympy import Symbol, Interval
    >>> Interval(0, 1)
    Interval(0, 1)
    >>> Interval.Ropen(0, 1)
    Interval.Ropen(0, 1)
    >>> Interval.Ropen(0, 1)
    Interval.Ropen(0, 1)
    >>> Interval.Lopen(0, 1)
    Interval.Lopen(0, 1)
    >>> Interval.open(0, 1)
    Interval.open(0, 1)

    >>> a = Symbol('a', real=True)
    >>> Interval(0, a)
    Interval(0, a)

    Notes
    =====
    - Only real end points are supported
    - ``Interval(a, b)`` with $a > b$ will return the empty set
    - Use the ``evalf()`` method to turn an Interval into an mpmath
      ``mpi`` interval instance

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Interval_%28mathematics%29
    """
    is_Interval: bool
    def __new__(cls, start, end, left_open: bool = False, right_open: bool = False): ...
    @property
    def start(self):
        """
        The left end point of the interval.

        This property takes the same value as the ``inf`` property.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 1).start
        0

        """
    @property
    def end(self):
        """
        The right end point of the interval.

        This property takes the same value as the ``sup`` property.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 1).end
        1

        """
    @property
    def left_open(self):
        """
        True if interval is left-open.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 1, left_open=True).left_open
        True
        >>> Interval(0, 1, left_open=False).left_open
        False

        """
    @property
    def right_open(self):
        """
        True if interval is right-open.

        Examples
        ========

        >>> from sympy import Interval
        >>> Interval(0, 1, right_open=True).right_open
        True
        >>> Interval(0, 1, right_open=False).right_open
        False

        """
    @classmethod
    def open(cls, a, b):
        """Return an interval including neither boundary."""
    @classmethod
    def Lopen(cls, a, b):
        """Return an interval not including the left boundary."""
    @classmethod
    def Ropen(cls, a, b):
        """Return an interval not including the right boundary."""
    @property
    def left(self): ...
    @property
    def right(self): ...
    @property
    def is_empty(self): ...
    @property
    def is_finite_set(self): ...
    def as_relational(self, x):
        """Rewrite an interval in terms of inequalities and logic operators."""
    def to_mpi(self, prec: int = 53): ...
    @property
    def is_left_unbounded(self):
        """Return ``True`` if the left endpoint is negative infinity. """
    @property
    def is_right_unbounded(self):
        """Return ``True`` if the right endpoint is positive infinity. """

class Union(Set, LatticeOp):
    """
    Represents a union of sets as a :class:`Set`.

    Examples
    ========

    >>> from sympy import Union, Interval
    >>> Union(Interval(1, 2), Interval(3, 4))
    Union(Interval(1, 2), Interval(3, 4))

    The Union constructor will always try to merge overlapping intervals,
    if possible. For example:

    >>> Union(Interval(1, 2), Interval(2, 3))
    Interval(1, 3)

    See Also
    ========

    Intersection

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Union_%28set_theory%29
    """
    is_Union: bool
    @property
    def identity(self): ...
    @property
    def zero(self): ...
    def __new__(cls, *args, **kwargs): ...
    @property
    def args(self): ...
    @property
    def is_empty(self): ...
    @property
    def is_finite_set(self): ...
    def is_subset(self, other): ...
    def as_relational(self, symbol):
        """Rewrite a Union in terms of equalities and logic operators. """
    @property
    def is_iterable(self): ...
    def __iter__(self): ...

class Intersection(Set, LatticeOp):
    """
    Represents an intersection of sets as a :class:`Set`.

    Examples
    ========

    >>> from sympy import Intersection, Interval
    >>> Intersection(Interval(1, 3), Interval(2, 4))
    Interval(2, 3)

    We often use the .intersect method

    >>> Interval(1,3).intersect(Interval(2,4))
    Interval(2, 3)

    See Also
    ========

    Union

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Intersection_%28set_theory%29
    """
    is_Intersection: bool
    @property
    def identity(self): ...
    @property
    def zero(self): ...
    def __new__(cls, *args, **kwargs): ...
    @property
    def args(self): ...
    @property
    def is_iterable(self): ...
    @property
    def is_finite_set(self): ...
    def __iter__(self): ...
    def as_relational(self, symbol):
        """Rewrite an Intersection in terms of equalities and logic operators"""

class Complement(Set):
    """Represents the set difference or relative complement of a set with
    another set.

    $$A - B = \\{x \\in A \\mid x \\notin B\\}$$


    Examples
    ========

    >>> from sympy import Complement, FiniteSet
    >>> Complement(FiniteSet(0, 1, 2), FiniteSet(1))
    {0, 2}

    See Also
    =========

    Intersection, Union

    References
    ==========

    .. [1] https://mathworld.wolfram.com/ComplementSet.html
    """
    is_Complement: bool
    def __new__(cls, a, b, evaluate: bool = True): ...
    @staticmethod
    def reduce(A, B):
        """
        Simplify a :class:`Complement`.

        """
    def as_relational(self, symbol):
        """Rewrite a complement in terms of equalities and logic
        operators"""
    @property
    def is_iterable(self): ...
    @property
    def is_finite_set(self): ...
    def __iter__(self): ...

class EmptySet(Set, metaclass=Singleton):
    """
    Represents the empty set. The empty set is available as a singleton
    as ``S.EmptySet``.

    Examples
    ========

    >>> from sympy import S, Interval
    >>> S.EmptySet
    EmptySet

    >>> Interval(1, 2).intersect(S.EmptySet)
    EmptySet

    See Also
    ========

    UniversalSet

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Empty_set
    """
    is_empty: bool
    is_finite_set: bool
    is_FiniteSet: bool
    @property
    def is_EmptySet(self): ...
    def as_relational(self, symbol): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...

class UniversalSet(Set, metaclass=Singleton):
    """
    Represents the set of all things.
    The universal set is available as a singleton as ``S.UniversalSet``.

    Examples
    ========

    >>> from sympy import S, Interval
    >>> S.UniversalSet
    UniversalSet

    >>> Interval(1, 2).intersect(S.UniversalSet)
    Interval(1, 2)

    See Also
    ========

    EmptySet

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Universal_set
    """
    is_UniversalSet: bool
    is_empty: bool
    is_finite_set: bool
    def as_relational(self, symbol): ...

class FiniteSet(Set):
    """
    Represents a finite set of Sympy expressions.

    Examples
    ========

    >>> from sympy import FiniteSet, Symbol, Interval, Naturals0
    >>> FiniteSet(1, 2, 3, 4)
    {1, 2, 3, 4}
    >>> 3 in FiniteSet(1, 2, 3, 4)
    True
    >>> FiniteSet(1, (1, 2), Symbol('x'))
    {1, x, (1, 2)}
    >>> FiniteSet(Interval(1, 2), Naturals0, {1, 2})
    FiniteSet({1, 2}, Interval(1, 2), Naturals0)
    >>> members = [1, 2, 3, 4]
    >>> f = FiniteSet(*members)
    >>> f
    {1, 2, 3, 4}
    >>> f - FiniteSet(2)
    {1, 3, 4}
    >>> f + FiniteSet(2, 5)
    {1, 2, 3, 4, 5}

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Finite_set
    """
    is_FiniteSet: bool
    is_iterable: bool
    is_empty: bool
    is_finite_set: bool
    def __new__(cls, *args, **kwargs): ...
    def __iter__(self): ...
    @property
    def measure(self): ...
    def __len__(self) -> int: ...
    def as_relational(self, symbol):
        """Rewrite a FiniteSet in terms of equalities and logic operators. """
    def compare(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def __eq__(self, other): ...
    __hash__: Callable[[Basic], Any]

class SymmetricDifference(Set):
    """Represents the set of elements which are in either of the
    sets and not in their intersection.

    Examples
    ========

    >>> from sympy import SymmetricDifference, FiniteSet
    >>> SymmetricDifference(FiniteSet(1, 2, 3), FiniteSet(3, 4, 5))
    {1, 2, 4, 5}

    See Also
    ========

    Complement, Union

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Symmetric_difference
    """
    is_SymmetricDifference: bool
    def __new__(cls, a, b, evaluate: bool = True): ...
    @staticmethod
    def reduce(A, B): ...
    def as_relational(self, symbol):
        """Rewrite a symmetric_difference in terms of equalities and
        logic operators"""
    @property
    def is_iterable(self): ...
    def __iter__(self): ...

class DisjointUnion(Set):
    """ Represents the disjoint union (also known as the external disjoint union)
    of a finite number of sets.

    Examples
    ========

    >>> from sympy import DisjointUnion, FiniteSet, Interval, Union, Symbol
    >>> A = FiniteSet(1, 2, 3)
    >>> B = Interval(0, 5)
    >>> DisjointUnion(A, B)
    DisjointUnion({1, 2, 3}, Interval(0, 5))
    >>> DisjointUnion(A, B).rewrite(Union)
    Union(ProductSet({1, 2, 3}, {0}), ProductSet(Interval(0, 5), {1}))
    >>> C = FiniteSet(Symbol('x'), Symbol('y'), Symbol('z'))
    >>> DisjointUnion(C, C)
    DisjointUnion({x, y, z}, {x, y, z})
    >>> DisjointUnion(C, C).rewrite(Union)
    ProductSet({x, y, z}, {0, 1})

    References
    ==========

    https://en.wikipedia.org/wiki/Disjoint_union
    """
    def __new__(cls, *sets): ...
    @property
    def sets(self): ...
    @property
    def is_empty(self): ...
    @property
    def is_finite_set(self): ...
    @property
    def is_iterable(self): ...
    def __iter__(self): ...
    def __len__(self) -> int:
        """
        Returns the length of the disjoint union, i.e., the number of elements in the set.

        Examples
        ========

        >>> from sympy import FiniteSet, DisjointUnion, EmptySet
        >>> D1 = DisjointUnion(FiniteSet(1, 2, 3, 4), EmptySet, FiniteSet(3, 4, 5))
        >>> len(D1)
        7
        >>> D2 = DisjointUnion(FiniteSet(3, 5, 7), EmptySet, FiniteSet(3, 5, 7))
        >>> len(D2)
        6
        >>> D3 = DisjointUnion(EmptySet, EmptySet)
        >>> len(D3)
        0

        Adds up the lengths of the constituent sets.
        """

def imageset(*args):
    """
    Return an image of the set under transformation ``f``.

    Explanation
    ===========

    If this function cannot compute the image, it returns an
    unevaluated ImageSet object.

    .. math::
        \\{ f(x) \\mid x \\in \\mathrm{self} \\}

    Examples
    ========

    >>> from sympy import S, Interval, imageset, sin, Lambda
    >>> from sympy.abc import x

    >>> imageset(x, 2*x, Interval(0, 2))
    Interval(0, 4)

    >>> imageset(lambda x: 2*x, Interval(0, 2))
    Interval(0, 4)

    >>> imageset(Lambda(x, sin(x)), Interval(-2, 1))
    ImageSet(Lambda(x, sin(x)), Interval(-2, 1))

    >>> imageset(sin, Interval(-2, 1))
    ImageSet(Lambda(x, sin(x)), Interval(-2, 1))
    >>> imageset(lambda y: x + y, Interval(-2, 1))
    ImageSet(Lambda(y, x + y), Interval(-2, 1))

    Expressions applied to the set of Integers are simplified
    to show as few negatives as possible and linear expressions
    are converted to a canonical form. If this is not desirable
    then the unevaluated ImageSet should be used.

    >>> imageset(x, -2*x + 5, S.Integers)
    ImageSet(Lambda(x, 2*x + 1), Integers)

    See Also
    ========

    sympy.sets.fancysets.ImageSet

    """
def is_function_invertible_in_set(func, setv):
    """
    Checks whether function ``func`` is invertible when the domain is
    restricted to set ``setv``.
    """
def simplify_union(args):
    """
    Simplify a :class:`Union` using known rules.

    Explanation
    ===========

    We first start with global rules like 'Merge all FiniteSets'

    Then we iterate through all pairs and ask the constituent sets if they
    can simplify themselves with any other constituent.  This process depends
    on ``union_sets(a, b)`` functions.
    """
def simplify_intersection(args):
    """
    Simplify an intersection using known rules.

    Explanation
    ===========

    We first start with global rules like
    'if any empty sets return empty set' and 'distribute any unions'

    Then we iterate through all pairs and ask the constituent sets if they
    can simplify themselves with any other constituent
    """
def set_add(x, y): ...
def set_sub(x, y): ...
def set_mul(x, y): ...
def set_div(x, y): ...
def set_pow(x, y): ...
def set_function(f, x): ...

class SetKind(Kind):
    """
    SetKind is kind for all Sets

    Every instance of Set will have kind ``SetKind`` parametrised by the kind
    of the elements of the ``Set``. The kind of the elements might be
    ``NumberKind``, or ``TupleKind`` or something else. When not all elements
    have the same kind then the kind of the elements will be given as
    ``UndefinedKind``.

    Parameters
    ==========

    element_kind: Kind (optional)
        The kind of the elements of the set. In a well defined set all elements
        will have the same kind. Otherwise the kind should
        :class:`sympy.core.kind.UndefinedKind`. The ``element_kind`` argument is optional but
        should only be omitted in the case of ``EmptySet`` whose kind is simply
        ``SetKind()``

    Examples
    ========

    >>> from sympy import Interval
    >>> Interval(1, 2).kind
    SetKind(NumberKind)
    >>> Interval(1,2).kind.element_kind
    NumberKind

    See Also
    ========

    sympy.core.kind.NumberKind
    sympy.matrices.common.MatrixKind
    sympy.core.containers.TupleKind
    """
    def __new__(cls, element_kind: Incomplete | None = None): ...

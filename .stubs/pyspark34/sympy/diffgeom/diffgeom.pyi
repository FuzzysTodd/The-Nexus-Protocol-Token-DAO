from _typeshed import Incomplete
from sympy.combinatorics import Permutation as Permutation
from sympy.core import Add as Add, Basic as Basic, Dict as Dict, Expr as Expr, Function as Function, Lambda as Lambda, Mul as Mul, Pow as Pow, S as S, Tuple as Tuple, diff as diff
from sympy.core.cache import cacheit as cacheit
from sympy.core.symbol import Dummy as Dummy, Str as Str, Symbol as Symbol
from sympy.functions import factorial as factorial
from sympy.simplify.simplify import simplify as simplify
from sympy.solvers import solve as solve
from sympy.tensor.array import ImmutableDenseNDimArray as ImmutableDenseNDimArray
from sympy.utilities.exceptions import SymPyDeprecationWarning as SymPyDeprecationWarning, ignore_warnings as ignore_warnings, sympy_deprecation_warning as sympy_deprecation_warning
from typing import Any

class Manifold(Basic):
    """
    A mathematical manifold.

    Explanation
    ===========

    A manifold is a topological space that locally resembles
    Euclidean space near each point [1].
    This class does not provide any means to study the topological
    characteristics of the manifold that it represents, though.

    Parameters
    ==========

    name : str
        The name of the manifold.

    dim : int
        The dimension of the manifold.

    Examples
    ========

    >>> from sympy.diffgeom import Manifold
    >>> m = Manifold('M', 2)
    >>> m
    M
    >>> m.dim
    2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Manifold
    """
    def __new__(cls, name, dim, **kwargs): ...
    @property
    def name(self): ...
    @property
    def dim(self): ...

class Patch(Basic):
    """
    A patch on a manifold.

    Explanation
    ===========

    Coordinate patch, or patch in short, is a simply-connected open set around
    a point in the manifold [1]. On a manifold one can have many patches that
    do not always include the whole manifold. On these patches coordinate
    charts can be defined that permit the parameterization of any point on the
    patch in terms of a tuple of real numbers (the coordinates).

    This class does not provide any means to study the topological
    characteristics of the patch that it represents.

    Parameters
    ==========

    name : str
        The name of the patch.

    manifold : Manifold
        The manifold on which the patch is defined.

    Examples
    ========

    >>> from sympy.diffgeom import Manifold, Patch
    >>> m = Manifold('M', 2)
    >>> p = Patch('P', m)
    >>> p
    P
    >>> p.dim
    2

    References
    ==========

    .. [1] G. Sussman, J. Wisdom, W. Farr, Functional Differential Geometry
           (2013)

    """
    def __new__(cls, name, manifold, **kwargs): ...
    @property
    def name(self): ...
    @property
    def manifold(self): ...
    @property
    def dim(self): ...

class CoordSystem(Basic):
    """
    A coordinate system defined on the patch.

    Explanation
    ===========

    Coordinate system is a system that uses one or more coordinates to uniquely
    determine the position of the points or other geometric elements on a
    manifold [1].

    By passing ``Symbols`` to *symbols* parameter, user can define the name and
    assumptions of coordinate symbols of the coordinate system. If not passed,
    these symbols are generated automatically and are assumed to be real valued.

    By passing *relations* parameter, user can define the transform relations of
    coordinate systems. Inverse transformation and indirect transformation can
    be found automatically. If this parameter is not passed, coordinate
    transformation cannot be done.

    Parameters
    ==========

    name : str
        The name of the coordinate system.

    patch : Patch
        The patch where the coordinate system is defined.

    symbols : list of Symbols, optional
        Defines the names and assumptions of coordinate symbols.

    relations : dict, optional
        Key is a tuple of two strings, who are the names of the systems where
        the coordinates transform from and transform to.
        Value is a tuple of the symbols before transformation and a tuple of
        the expressions after transformation.

    Examples
    ========

    We define two-dimensional Cartesian coordinate system and polar coordinate
    system.

    >>> from sympy import symbols, pi, sqrt, atan2, cos, sin
    >>> from sympy.diffgeom import Manifold, Patch, CoordSystem
    >>> m = Manifold('M', 2)
    >>> p = Patch('P', m)
    >>> x, y = symbols('x y', real=True)
    >>> r, theta = symbols('r theta', nonnegative=True)
    >>> relation_dict = {
    ... ('Car2D', 'Pol'): [(x, y), (sqrt(x**2 + y**2), atan2(y, x))],
    ... ('Pol', 'Car2D'): [(r, theta), (r*cos(theta), r*sin(theta))]
    ... }
    >>> Car2D = CoordSystem('Car2D', p, (x, y), relation_dict)
    >>> Pol = CoordSystem('Pol', p, (r, theta), relation_dict)

    ``symbols`` property returns ``CoordinateSymbol`` instances. These symbols
    are not same with the symbols used to construct the coordinate system.

    >>> Car2D
    Car2D
    >>> Car2D.dim
    2
    >>> Car2D.symbols
    (x, y)
    >>> _[0].func
    <class 'sympy.diffgeom.diffgeom.CoordinateSymbol'>

    ``transformation()`` method returns the transformation function from
    one coordinate system to another. ``transform()`` method returns the
    transformed coordinates.

    >>> Car2D.transformation(Pol)
    Lambda((x, y), Matrix([
    [sqrt(x**2 + y**2)],
    [      atan2(y, x)]]))
    >>> Car2D.transform(Pol)
    Matrix([
    [sqrt(x**2 + y**2)],
    [      atan2(y, x)]])
    >>> Car2D.transform(Pol, [1, 2])
    Matrix([
    [sqrt(5)],
    [atan(2)]])

    ``jacobian()`` method returns the Jacobian matrix of coordinate
    transformation between two systems. ``jacobian_determinant()`` method
    returns the Jacobian determinant of coordinate transformation between two
    systems.

    >>> Pol.jacobian(Car2D)
    Matrix([
    [cos(theta), -r*sin(theta)],
    [sin(theta),  r*cos(theta)]])
    >>> Pol.jacobian(Car2D, [1, pi/2])
    Matrix([
    [0, -1],
    [1,  0]])
    >>> Car2D.jacobian_determinant(Pol)
    1/sqrt(x**2 + y**2)
    >>> Car2D.jacobian_determinant(Pol, [1,0])
    1

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Coordinate_system

    """
    def __new__(cls, name, patch, symbols: Incomplete | None = None, relations={}, **kwargs): ...
    @property
    def name(self): ...
    @property
    def patch(self): ...
    @property
    def manifold(self): ...
    @property
    def symbols(self): ...
    @property
    def relations(self): ...
    @property
    def dim(self): ...
    def transformation(self, sys):
        """
        Return coordinate transformation function from *self* to *sys*.

        Parameters
        ==========

        sys : CoordSystem

        Returns
        =======

        sympy.Lambda

        Examples
        ========

        >>> from sympy.diffgeom.rn import R2_r, R2_p
        >>> R2_r.transformation(R2_p)
        Lambda((x, y), Matrix([
        [sqrt(x**2 + y**2)],
        [      atan2(y, x)]]))

        """
    def connect_to(self, to_sys, from_coords, to_exprs, inverse: bool = True, fill_in_gaps: bool = False) -> None: ...
    def transform(self, sys, coordinates: Incomplete | None = None):
        """
        Return the result of coordinate transformation from *self* to *sys*.
        If coordinates are not given, coordinate symbols of *self* are used.

        Parameters
        ==========

        sys : CoordSystem

        coordinates : Any iterable, optional.

        Returns
        =======

        sympy.ImmutableDenseMatrix containing CoordinateSymbol

        Examples
        ========

        >>> from sympy.diffgeom.rn import R2_r, R2_p
        >>> R2_r.transform(R2_p)
        Matrix([
        [sqrt(x**2 + y**2)],
        [      atan2(y, x)]])
        >>> R2_r.transform(R2_p, [0, 1])
        Matrix([
        [   1],
        [pi/2]])

        """
    def coord_tuple_transform_to(self, to_sys, coords):
        """Transform ``coords`` to coord system ``to_sys``."""
    def jacobian(self, sys, coordinates: Incomplete | None = None):
        """
        Return the jacobian matrix of a transformation on given coordinates.
        If coordinates are not given, coordinate symbols of *self* are used.

        Parameters
        ==========

        sys : CoordSystem

        coordinates : Any iterable, optional.

        Returns
        =======

        sympy.ImmutableDenseMatrix

        Examples
        ========

        >>> from sympy.diffgeom.rn import R2_r, R2_p
        >>> R2_p.jacobian(R2_r)
        Matrix([
        [cos(theta), -rho*sin(theta)],
        [sin(theta),  rho*cos(theta)]])
        >>> R2_p.jacobian(R2_r, [1, 0])
        Matrix([
        [1, 0],
        [0, 1]])

        """
    jacobian_matrix = jacobian
    def jacobian_determinant(self, sys, coordinates: Incomplete | None = None):
        """
        Return the jacobian determinant of a transformation on given
        coordinates. If coordinates are not given, coordinate symbols of *self*
        are used.

        Parameters
        ==========

        sys : CoordSystem

        coordinates : Any iterable, optional.

        Returns
        =======

        sympy.Expr

        Examples
        ========

        >>> from sympy.diffgeom.rn import R2_r, R2_p
        >>> R2_r.jacobian_determinant(R2_p)
        1/sqrt(x**2 + y**2)
        >>> R2_r.jacobian_determinant(R2_p, [1, 0])
        1

        """
    def point(self, coords):
        """Create a ``Point`` with coordinates given in this coord system."""
    def point_to_coords(self, point):
        """Calculate the coordinates of a point in this coord system."""
    def base_scalar(self, coord_index):
        """Return ``BaseScalarField`` that takes a point and returns one of the coordinates."""
    coord_function = base_scalar
    def base_scalars(self):
        """Returns a list of all coordinate functions.
        For more details see the ``base_scalar`` method of this class."""
    coord_functions = base_scalars
    def base_vector(self, coord_index):
        """Return a basis vector field.
        The basis vector field for this coordinate system. It is also an
        operator on scalar fields."""
    def base_vectors(self):
        """Returns a list of all base vectors.
        For more details see the ``base_vector`` method of this class."""
    def base_oneform(self, coord_index):
        """Return a basis 1-form field.
        The basis one-form field for this coordinate system. It is also an
        operator on vector fields."""
    def base_oneforms(self):
        """Returns a list of all base oneforms.
        For more details see the ``base_oneform`` method of this class."""

class CoordinateSymbol(Symbol):
    """A symbol which denotes an abstract value of i-th coordinate of
    the coordinate system with given context.

    Explanation
    ===========

    Each coordinates in coordinate system are represented by unique symbol,
    such as x, y, z in Cartesian coordinate system.

    You may not construct this class directly. Instead, use `symbols` method
    of CoordSystem.

    Parameters
    ==========

    coord_sys : CoordSystem

    index : integer

    Examples
    ========

    >>> from sympy import symbols, Lambda, Matrix, sqrt, atan2, cos, sin
    >>> from sympy.diffgeom import Manifold, Patch, CoordSystem
    >>> m = Manifold('M', 2)
    >>> p = Patch('P', m)
    >>> x, y = symbols('x y', real=True)
    >>> r, theta = symbols('r theta', nonnegative=True)
    >>> relation_dict = {
    ... ('Car2D', 'Pol'): Lambda((x, y), Matrix([sqrt(x**2 + y**2), atan2(y, x)])),
    ... ('Pol', 'Car2D'): Lambda((r, theta), Matrix([r*cos(theta), r*sin(theta)]))
    ... }
    >>> Car2D = CoordSystem('Car2D', p, [x, y], relation_dict)
    >>> Pol = CoordSystem('Pol', p, [r, theta], relation_dict)
    >>> x, y = Car2D.symbols

    ``CoordinateSymbol`` contains its coordinate symbol and index.

    >>> x.name
    'x'
    >>> x.coord_sys == Car2D
    True
    >>> x.index
    0
    >>> x.is_real
    True

    You can transform ``CoordinateSymbol`` into other coordinate system using
    ``rewrite()`` method.

    >>> x.rewrite(Pol)
    r*cos(theta)
    >>> sqrt(x**2 + y**2).rewrite(Pol).simplify()
    r

    """
    def __new__(cls, coord_sys, index, **assumptions): ...
    def __getnewargs__(self): ...

class Point(Basic):
    """Point defined in a coordinate system.

    Explanation
    ===========

    Mathematically, point is defined in the manifold and does not have any coordinates
    by itself. Coordinate system is what imbues the coordinates to the point by coordinate
    chart. However, due to the difficulty of realizing such logic, you must supply
    a coordinate system and coordinates to define a Point here.

    The usage of this object after its definition is independent of the
    coordinate system that was used in order to define it, however due to
    limitations in the simplification routines you can arrive at complicated
    expressions if you use inappropriate coordinate systems.

    Parameters
    ==========

    coord_sys : CoordSystem

    coords : list
        The coordinates of the point.

    Examples
    ========

    >>> from sympy import pi
    >>> from sympy.diffgeom import Point
    >>> from sympy.diffgeom.rn import R2, R2_r, R2_p
    >>> rho, theta = R2_p.symbols

    >>> p = Point(R2_p, [rho, 3*pi/4])

    >>> p.manifold == R2
    True

    >>> p.coords()
    Matrix([
    [   rho],
    [3*pi/4]])
    >>> p.coords(R2_r)
    Matrix([
    [-sqrt(2)*rho/2],
    [ sqrt(2)*rho/2]])

    """
    def __new__(cls, coord_sys, coords, **kwargs): ...
    @property
    def patch(self): ...
    @property
    def manifold(self): ...
    @property
    def dim(self): ...
    def coords(self, sys: Incomplete | None = None):
        """
        Coordinates of the point in given coordinate system. If coordinate system
        is not passed, it returns the coordinates in the coordinate system in which
        the poin was defined.
        """
    @property
    def free_symbols(self): ...

class BaseScalarField(Expr):
    """Base scalar field over a manifold for a given coordinate system.

    Explanation
    ===========

    A scalar field takes a point as an argument and returns a scalar.
    A base scalar field of a coordinate system takes a point and returns one of
    the coordinates of that point in the coordinate system in question.

    To define a scalar field you need to choose the coordinate system and the
    index of the coordinate.

    The use of the scalar field after its definition is independent of the
    coordinate system in which it was defined, however due to limitations in
    the simplification routines you may arrive at more complicated
    expression if you use unappropriate coordinate systems.
    You can build complicated scalar fields by just building up SymPy
    expressions containing ``BaseScalarField`` instances.

    Parameters
    ==========

    coord_sys : CoordSystem

    index : integer

    Examples
    ========

    >>> from sympy import Function, pi
    >>> from sympy.diffgeom import BaseScalarField
    >>> from sympy.diffgeom.rn import R2_r, R2_p
    >>> rho, _ = R2_p.symbols
    >>> point = R2_p.point([rho, 0])
    >>> fx, fy = R2_r.base_scalars()
    >>> ftheta = BaseScalarField(R2_r, 1)

    >>> fx(point)
    rho
    >>> fy(point)
    0

    >>> (fx**2+fy**2).rcall(point)
    rho**2

    >>> g = Function('g')
    >>> fg = g(ftheta-pi)
    >>> fg.rcall(point)
    g(-pi)

    """
    is_commutative: bool
    def __new__(cls, coord_sys, index, **kwargs): ...
    @property
    def coord_sys(self): ...
    @property
    def index(self): ...
    @property
    def patch(self): ...
    @property
    def manifold(self): ...
    @property
    def dim(self): ...
    def __call__(self, *args):
        """Evaluating the field at a point or doing nothing.
        If the argument is a ``Point`` instance, the field is evaluated at that
        point. The field is returned itself if the argument is any other
        object. It is so in order to have working recursive calling mechanics
        for all fields (check the ``__call__`` method of ``Expr``).
        """
    free_symbols: set[Any]

class BaseVectorField(Expr):
    """Base vector field over a manifold for a given coordinate system.

    Explanation
    ===========

    A vector field is an operator taking a scalar field and returning a
    directional derivative (which is also a scalar field).
    A base vector field is the same type of operator, however the derivation is
    specifically done with respect to a chosen coordinate.

    To define a base vector field you need to choose the coordinate system and
    the index of the coordinate.

    The use of the vector field after its definition is independent of the
    coordinate system in which it was defined, however due to limitations in the
    simplification routines you may arrive at more complicated expression if you
    use unappropriate coordinate systems.

    Parameters
    ==========
    coord_sys : CoordSystem

    index : integer

    Examples
    ========

    >>> from sympy import Function
    >>> from sympy.diffgeom.rn import R2_p, R2_r
    >>> from sympy.diffgeom import BaseVectorField
    >>> from sympy import pprint

    >>> x, y = R2_r.symbols
    >>> rho, theta = R2_p.symbols
    >>> fx, fy = R2_r.base_scalars()
    >>> point_p = R2_p.point([rho, theta])
    >>> point_r = R2_r.point([x, y])

    >>> g = Function('g')
    >>> s_field = g(fx, fy)

    >>> v = BaseVectorField(R2_r, 1)
    >>> pprint(v(s_field))
    / d           \\|
    |---(g(x, xi))||
    \\dxi          /|xi=y
    >>> pprint(v(s_field).rcall(point_r).doit())
    d
    --(g(x, y))
    dy
    >>> pprint(v(s_field).rcall(point_p))
    / d                        \\|
    |---(g(rho*cos(theta), xi))||
    \\dxi                       /|xi=rho*sin(theta)

    """
    is_commutative: bool
    def __new__(cls, coord_sys, index, **kwargs): ...
    @property
    def coord_sys(self): ...
    @property
    def index(self): ...
    @property
    def patch(self): ...
    @property
    def manifold(self): ...
    @property
    def dim(self): ...
    def __call__(self, scalar_field):
        """Apply on a scalar field.
        The action of a vector field on a scalar field is a directional
        differentiation.
        If the argument is not a scalar field an error is raised.
        """

class Commutator(Expr):
    """Commutator of two vector fields.

    Explanation
    ===========

    The commutator of two vector fields `v_1` and `v_2` is defined as the
    vector field `[v_1, v_2]` that evaluated on each scalar field `f` is equal
    to `v_1(v_2(f)) - v_2(v_1(f))`.

    Examples
    ========


    >>> from sympy.diffgeom.rn import R2_p, R2_r
    >>> from sympy.diffgeom import Commutator
    >>> from sympy import simplify

    >>> fx, fy = R2_r.base_scalars()
    >>> e_x, e_y = R2_r.base_vectors()
    >>> e_r = R2_p.base_vector(0)

    >>> c_xy = Commutator(e_x, e_y)
    >>> c_xr = Commutator(e_x, e_r)
    >>> c_xy
    0

    Unfortunately, the current code is not able to compute everything:

    >>> c_xr
    Commutator(e_x, e_rho)
    >>> simplify(c_xr(fy**2))
    -2*cos(theta)*y**2/(x**2 + y**2)

    """
    def __new__(cls, v1, v2): ...
    @property
    def v1(self): ...
    @property
    def v2(self): ...
    def __call__(self, scalar_field):
        """Apply on a scalar field.
        If the argument is not a scalar field an error is raised.
        """

class Differential(Expr):
    """Return the differential (exterior derivative) of a form field.

    Explanation
    ===========

    The differential of a form (i.e. the exterior derivative) has a complicated
    definition in the general case.
    The differential `df` of the 0-form `f` is defined for any vector field `v`
    as `df(v) = v(f)`.

    Examples
    ========

    >>> from sympy import Function
    >>> from sympy.diffgeom.rn import R2_r
    >>> from sympy.diffgeom import Differential
    >>> from sympy import pprint

    >>> fx, fy = R2_r.base_scalars()
    >>> e_x, e_y = R2_r.base_vectors()
    >>> g = Function('g')
    >>> s_field = g(fx, fy)
    >>> dg = Differential(s_field)

    >>> dg
    d(g(x, y))
    >>> pprint(dg(e_x))
    / d           \\|
    |---(g(xi, y))||
    \\dxi          /|xi=x
    >>> pprint(dg(e_y))
    / d           \\|
    |---(g(x, xi))||
    \\dxi          /|xi=y

    Applying the exterior derivative operator twice always results in:

    >>> Differential(dg)
    0
    """
    is_commutative: bool
    def __new__(cls, form_field): ...
    @property
    def form_field(self): ...
    def __call__(self, *vector_fields):
        """Apply on a list of vector_fields.

        Explanation
        ===========

        If the number of vector fields supplied is not equal to 1 + the order of
        the form field inside the differential the result is undefined.

        For 1-forms (i.e. differentials of scalar fields) the evaluation is
        done as `df(v)=v(f)`. However if `v` is ``None`` instead of a vector
        field, the differential is returned unchanged. This is done in order to
        permit partial contractions for higher forms.

        In the general case the evaluation is done by applying the form field
        inside the differential on a list with one less elements than the number
        of elements in the original list. Lowering the number of vector fields
        is achieved through replacing each pair of fields by their
        commutator.

        If the arguments are not vectors or ``None``s an error is raised.
        """

class TensorProduct(Expr):
    """Tensor product of forms.

    Explanation
    ===========

    The tensor product permits the creation of multilinear functionals (i.e.
    higher order tensors) out of lower order fields (e.g. 1-forms and vector
    fields). However, the higher tensors thus created lack the interesting
    features provided by the other type of product, the wedge product, namely
    they are not antisymmetric and hence are not form fields.

    Examples
    ========

    >>> from sympy.diffgeom.rn import R2_r
    >>> from sympy.diffgeom import TensorProduct

    >>> fx, fy = R2_r.base_scalars()
    >>> e_x, e_y = R2_r.base_vectors()
    >>> dx, dy = R2_r.base_oneforms()

    >>> TensorProduct(dx, dy)(e_x, e_y)
    1
    >>> TensorProduct(dx, dy)(e_y, e_x)
    0
    >>> TensorProduct(dx, fx*dy)(fx*e_x, e_y)
    x**2
    >>> TensorProduct(e_x, e_y)(fx**2, fy**2)
    4*x*y
    >>> TensorProduct(e_y, dx)(fy)
    dx

    You can nest tensor products.

    >>> tp1 = TensorProduct(dx, dy)
    >>> TensorProduct(tp1, dx)(e_x, e_y, e_x)
    1

    You can make partial contraction for instance when 'raising an index'.
    Putting ``None`` in the second argument of ``rcall`` means that the
    respective position in the tensor product is left as it is.

    >>> TP = TensorProduct
    >>> metric = TP(dx, dx) + 3*TP(dy, dy)
    >>> metric.rcall(e_y, None)
    3*dy

    Or automatically pad the args with ``None`` without specifying them.

    >>> metric.rcall(e_y)
    3*dy

    """
    def __new__(cls, *args): ...
    def __call__(self, *fields):
        """Apply on a list of fields.

        If the number of input fields supplied is not equal to the order of
        the tensor product field, the list of arguments is padded with ``None``'s.

        The list of arguments is divided in sublists depending on the order of
        the forms inside the tensor product. The sublists are provided as
        arguments to these forms and the resulting expressions are given to the
        constructor of ``TensorProduct``.

        """

class WedgeProduct(TensorProduct):
    """Wedge product of forms.

    Explanation
    ===========

    In the context of integration only completely antisymmetric forms make
    sense. The wedge product permits the creation of such forms.

    Examples
    ========

    >>> from sympy.diffgeom.rn import R2_r
    >>> from sympy.diffgeom import WedgeProduct

    >>> fx, fy = R2_r.base_scalars()
    >>> e_x, e_y = R2_r.base_vectors()
    >>> dx, dy = R2_r.base_oneforms()

    >>> WedgeProduct(dx, dy)(e_x, e_y)
    1
    >>> WedgeProduct(dx, dy)(e_y, e_x)
    -1
    >>> WedgeProduct(dx, fx*dy)(fx*e_x, e_y)
    x**2
    >>> WedgeProduct(e_x, e_y)(fy, None)
    -e_x

    You can nest wedge products.

    >>> wp1 = WedgeProduct(dx, dy)
    >>> WedgeProduct(wp1, dx)(e_x, e_y, e_x)
    0

    """
    def __call__(self, *fields):
        """Apply on a list of vector_fields.
        The expression is rewritten internally in terms of tensor products and evaluated."""

class LieDerivative(Expr):
    """Lie derivative with respect to a vector field.

    Explanation
    ===========

    The transport operator that defines the Lie derivative is the pushforward of
    the field to be derived along the integral curve of the field with respect
    to which one derives.

    Examples
    ========

    >>> from sympy.diffgeom.rn import R2_r, R2_p
    >>> from sympy.diffgeom import (LieDerivative, TensorProduct)

    >>> fx, fy = R2_r.base_scalars()
    >>> e_x, e_y = R2_r.base_vectors()
    >>> e_rho, e_theta = R2_p.base_vectors()
    >>> dx, dy = R2_r.base_oneforms()

    >>> LieDerivative(e_x, fy)
    0
    >>> LieDerivative(e_x, fx)
    1
    >>> LieDerivative(e_x, e_x)
    0

    The Lie derivative of a tensor field by another tensor field is equal to
    their commutator:

    >>> LieDerivative(e_x, e_rho)
    Commutator(e_x, e_rho)
    >>> LieDerivative(e_x + e_y, fx)
    1

    >>> tp = TensorProduct(dx, dy)
    >>> LieDerivative(e_x, tp)
    LieDerivative(e_x, TensorProduct(dx, dy))
    >>> LieDerivative(e_x, tp)
    LieDerivative(e_x, TensorProduct(dx, dy))

    """
    def __new__(cls, v_field, expr): ...
    @property
    def v_field(self): ...
    @property
    def expr(self): ...
    def __call__(self, *args): ...

class BaseCovarDerivativeOp(Expr):
    """Covariant derivative operator with respect to a base vector.

    Examples
    ========

    >>> from sympy.diffgeom.rn import R2_r
    >>> from sympy.diffgeom import BaseCovarDerivativeOp
    >>> from sympy.diffgeom import metric_to_Christoffel_2nd, TensorProduct

    >>> TP = TensorProduct
    >>> fx, fy = R2_r.base_scalars()
    >>> e_x, e_y = R2_r.base_vectors()
    >>> dx, dy = R2_r.base_oneforms()

    >>> ch = metric_to_Christoffel_2nd(TP(dx, dx) + TP(dy, dy))
    >>> ch
    [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    >>> cvd = BaseCovarDerivativeOp(R2_r, 0, ch)
    >>> cvd(fx)
    1
    >>> cvd(fx*e_x)
    e_x
    """
    def __new__(cls, coord_sys, index, christoffel): ...
    @property
    def coord_sys(self): ...
    @property
    def index(self): ...
    @property
    def christoffel(self): ...
    def __call__(self, field):
        """Apply on a scalar field.

        The action of a vector field on a scalar field is a directional
        differentiation.
        If the argument is not a scalar field the behaviour is undefined.
        """

class CovarDerivativeOp(Expr):
    """Covariant derivative operator.

    Examples
    ========

    >>> from sympy.diffgeom.rn import R2_r
    >>> from sympy.diffgeom import CovarDerivativeOp
    >>> from sympy.diffgeom import metric_to_Christoffel_2nd, TensorProduct
    >>> TP = TensorProduct
    >>> fx, fy = R2_r.base_scalars()
    >>> e_x, e_y = R2_r.base_vectors()
    >>> dx, dy = R2_r.base_oneforms()
    >>> ch = metric_to_Christoffel_2nd(TP(dx, dx) + TP(dy, dy))

    >>> ch
    [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    >>> cvd = CovarDerivativeOp(fx*e_x, ch)
    >>> cvd(fx)
    x
    >>> cvd(fx*e_x)
    x*e_x

    """
    def __new__(cls, wrt, christoffel): ...
    @property
    def wrt(self): ...
    @property
    def christoffel(self): ...
    def __call__(self, field): ...

def intcurve_series(vector_field, param, start_point, n: int = 6, coord_sys: Incomplete | None = None, coeffs: bool = False):
    """Return the series expansion for an integral curve of the field.

    Explanation
    ===========

    Integral curve is a function `\\gamma` taking a parameter in `R` to a point
    in the manifold. It verifies the equation:

    `V(f)\\big(\\gamma(t)\\big) = \\frac{d}{dt}f\\big(\\gamma(t)\\big)`

    where the given ``vector_field`` is denoted as `V`. This holds for any
    value `t` for the parameter and any scalar field `f`.

    This equation can also be decomposed of a basis of coordinate functions
    `V(f_i)\\big(\\gamma(t)\\big) = \\frac{d}{dt}f_i\\big(\\gamma(t)\\big) \\quad \\forall i`

    This function returns a series expansion of `\\gamma(t)` in terms of the
    coordinate system ``coord_sys``. The equations and expansions are necessarily
    done in coordinate-system-dependent way as there is no other way to
    represent movement between points on the manifold (i.e. there is no such
    thing as a difference of points for a general manifold).

    Parameters
    ==========
    vector_field
        the vector field for which an integral curve will be given

    param
        the argument of the function `\\gamma` from R to the curve

    start_point
        the point which corresponds to `\\gamma(0)`

    n
        the order to which to expand

    coord_sys
        the coordinate system in which to expand
        coeffs (default False) - if True return a list of elements of the expansion

    Examples
    ========

    Use the predefined R2 manifold:

    >>> from sympy.abc import t, x, y
    >>> from sympy.diffgeom.rn import R2_p, R2_r
    >>> from sympy.diffgeom import intcurve_series

    Specify a starting point and a vector field:

    >>> start_point = R2_r.point([x, y])
    >>> vector_field = R2_r.e_x

    Calculate the series:

    >>> intcurve_series(vector_field, t, start_point, n=3)
    Matrix([
    [t + x],
    [    y]])

    Or get the elements of the expansion in a list:

    >>> series = intcurve_series(vector_field, t, start_point, n=3, coeffs=True)
    >>> series[0]
    Matrix([
    [x],
    [y]])
    >>> series[1]
    Matrix([
    [t],
    [0]])
    >>> series[2]
    Matrix([
    [0],
    [0]])

    The series in the polar coordinate system:

    >>> series = intcurve_series(vector_field, t, start_point,
    ...             n=3, coord_sys=R2_p, coeffs=True)
    >>> series[0]
    Matrix([
    [sqrt(x**2 + y**2)],
    [      atan2(y, x)]])
    >>> series[1]
    Matrix([
    [t*x/sqrt(x**2 + y**2)],
    [   -t*y/(x**2 + y**2)]])
    >>> series[2]
    Matrix([
    [t**2*(-x**2/(x**2 + y**2)**(3/2) + 1/sqrt(x**2 + y**2))/2],
    [                                t**2*x*y/(x**2 + y**2)**2]])

    See Also
    ========

    intcurve_diffequ

    """
def intcurve_diffequ(vector_field, param, start_point, coord_sys: Incomplete | None = None):
    """Return the differential equation for an integral curve of the field.

    Explanation
    ===========

    Integral curve is a function `\\gamma` taking a parameter in `R` to a point
    in the manifold. It verifies the equation:

    `V(f)\\big(\\gamma(t)\\big) = \\frac{d}{dt}f\\big(\\gamma(t)\\big)`

    where the given ``vector_field`` is denoted as `V`. This holds for any
    value `t` for the parameter and any scalar field `f`.

    This function returns the differential equation of `\\gamma(t)` in terms of the
    coordinate system ``coord_sys``. The equations and expansions are necessarily
    done in coordinate-system-dependent way as there is no other way to
    represent movement between points on the manifold (i.e. there is no such
    thing as a difference of points for a general manifold).

    Parameters
    ==========

    vector_field
        the vector field for which an integral curve will be given

    param
        the argument of the function `\\gamma` from R to the curve

    start_point
        the point which corresponds to `\\gamma(0)`

    coord_sys
        the coordinate system in which to give the equations

    Returns
    =======

    a tuple of (equations, initial conditions)

    Examples
    ========

    Use the predefined R2 manifold:

    >>> from sympy.abc import t
    >>> from sympy.diffgeom.rn import R2, R2_p, R2_r
    >>> from sympy.diffgeom import intcurve_diffequ

    Specify a starting point and a vector field:

    >>> start_point = R2_r.point([0, 1])
    >>> vector_field = -R2.y*R2.e_x + R2.x*R2.e_y

    Get the equation:

    >>> equations, init_cond = intcurve_diffequ(vector_field, t, start_point)
    >>> equations
    [f_1(t) + Derivative(f_0(t), t), -f_0(t) + Derivative(f_1(t), t)]
    >>> init_cond
    [f_0(0), f_1(0) - 1]

    The series in the polar coordinate system:

    >>> equations, init_cond = intcurve_diffequ(vector_field, t, start_point, R2_p)
    >>> equations
    [Derivative(f_0(t), t), Derivative(f_1(t), t) - 1]
    >>> init_cond
    [f_0(0) - 1, f_1(0) - pi/2]

    See Also
    ========

    intcurve_series

    """
def dummyfy(args, exprs): ...
def contravariant_order(expr, _strict: bool = False):
    """Return the contravariant order of an expression.

    Examples
    ========

    >>> from sympy.diffgeom import contravariant_order
    >>> from sympy.diffgeom.rn import R2
    >>> from sympy.abc import a

    >>> contravariant_order(a)
    0
    >>> contravariant_order(a*R2.x + 2)
    0
    >>> contravariant_order(a*R2.x*R2.e_y + R2.e_x)
    1

    """
def covariant_order(expr, _strict: bool = False):
    """Return the covariant order of an expression.

    Examples
    ========

    >>> from sympy.diffgeom import covariant_order
    >>> from sympy.diffgeom.rn import R2
    >>> from sympy.abc import a

    >>> covariant_order(a)
    0
    >>> covariant_order(a*R2.x + 2)
    0
    >>> covariant_order(a*R2.x*R2.dy + R2.dx)
    1

    """
def vectors_in_basis(expr, to_sys):
    """Transform all base vectors in base vectors of a specified coord basis.
    While the new base vectors are in the new coordinate system basis, any
    coefficients are kept in the old system.

    Examples
    ========

    >>> from sympy.diffgeom import vectors_in_basis
    >>> from sympy.diffgeom.rn import R2_r, R2_p

    >>> vectors_in_basis(R2_r.e_x, R2_p)
    -y*e_theta/(x**2 + y**2) + x*e_rho/sqrt(x**2 + y**2)
    >>> vectors_in_basis(R2_p.e_r, R2_r)
    sin(theta)*e_y + cos(theta)*e_x

    """
def twoform_to_matrix(expr):
    """Return the matrix representing the twoform.

    For the twoform `w` return the matrix `M` such that `M[i,j]=w(e_i, e_j)`,
    where `e_i` is the i-th base vector field for the coordinate system in
    which the expression of `w` is given.

    Examples
    ========

    >>> from sympy.diffgeom.rn import R2
    >>> from sympy.diffgeom import twoform_to_matrix, TensorProduct
    >>> TP = TensorProduct

    >>> twoform_to_matrix(TP(R2.dx, R2.dx) + TP(R2.dy, R2.dy))
    Matrix([
    [1, 0],
    [0, 1]])
    >>> twoform_to_matrix(R2.x*TP(R2.dx, R2.dx) + TP(R2.dy, R2.dy))
    Matrix([
    [x, 0],
    [0, 1]])
    >>> twoform_to_matrix(TP(R2.dx, R2.dx) + TP(R2.dy, R2.dy) - TP(R2.dx, R2.dy)/2)
    Matrix([
    [   1, 0],
    [-1/2, 1]])

    """
def metric_to_Christoffel_1st(expr):
    """Return the nested list of Christoffel symbols for the given metric.
    This returns the Christoffel symbol of first kind that represents the
    Levi-Civita connection for the given metric.

    Examples
    ========

    >>> from sympy.diffgeom.rn import R2
    >>> from sympy.diffgeom import metric_to_Christoffel_1st, TensorProduct
    >>> TP = TensorProduct

    >>> metric_to_Christoffel_1st(TP(R2.dx, R2.dx) + TP(R2.dy, R2.dy))
    [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    >>> metric_to_Christoffel_1st(R2.x*TP(R2.dx, R2.dx) + TP(R2.dy, R2.dy))
    [[[1/2, 0], [0, 0]], [[0, 0], [0, 0]]]

    """
def metric_to_Christoffel_2nd(expr):
    """Return the nested list of Christoffel symbols for the given metric.
    This returns the Christoffel symbol of second kind that represents the
    Levi-Civita connection for the given metric.

    Examples
    ========

    >>> from sympy.diffgeom.rn import R2
    >>> from sympy.diffgeom import metric_to_Christoffel_2nd, TensorProduct
    >>> TP = TensorProduct

    >>> metric_to_Christoffel_2nd(TP(R2.dx, R2.dx) + TP(R2.dy, R2.dy))
    [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    >>> metric_to_Christoffel_2nd(R2.x*TP(R2.dx, R2.dx) + TP(R2.dy, R2.dy))
    [[[1/(2*x), 0], [0, 0]], [[0, 0], [0, 0]]]

    """
def metric_to_Riemann_components(expr):
    """Return the components of the Riemann tensor expressed in a given basis.

    Given a metric it calculates the components of the Riemann tensor in the
    canonical basis of the coordinate system in which the metric expression is
    given.

    Examples
    ========

    >>> from sympy import exp
    >>> from sympy.diffgeom.rn import R2
    >>> from sympy.diffgeom import metric_to_Riemann_components, TensorProduct
    >>> TP = TensorProduct

    >>> metric_to_Riemann_components(TP(R2.dx, R2.dx) + TP(R2.dy, R2.dy))
    [[[[0, 0], [0, 0]], [[0, 0], [0, 0]]], [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]]
    >>> non_trivial_metric = exp(2*R2.r)*TP(R2.dr, R2.dr) +         R2.r**2*TP(R2.dtheta, R2.dtheta)
    >>> non_trivial_metric
    exp(2*rho)*TensorProduct(drho, drho) + rho**2*TensorProduct(dtheta, dtheta)
    >>> riemann = metric_to_Riemann_components(non_trivial_metric)
    >>> riemann[0, :, :, :]
    [[[0, 0], [0, 0]], [[0, exp(-2*rho)*rho], [-exp(-2*rho)*rho, 0]]]
    >>> riemann[1, :, :, :]
    [[[0, -1/rho], [1/rho, 0]], [[0, 0], [0, 0]]]

    """
def metric_to_Ricci_components(expr):
    """Return the components of the Ricci tensor expressed in a given basis.

    Given a metric it calculates the components of the Ricci tensor in the
    canonical basis of the coordinate system in which the metric expression is
    given.

    Examples
    ========

    >>> from sympy import exp
    >>> from sympy.diffgeom.rn import R2
    >>> from sympy.diffgeom import metric_to_Ricci_components, TensorProduct
    >>> TP = TensorProduct

    >>> metric_to_Ricci_components(TP(R2.dx, R2.dx) + TP(R2.dy, R2.dy))
    [[0, 0], [0, 0]]
    >>> non_trivial_metric = exp(2*R2.r)*TP(R2.dr, R2.dr) +                              R2.r**2*TP(R2.dtheta, R2.dtheta)
    >>> non_trivial_metric
    exp(2*rho)*TensorProduct(drho, drho) + rho**2*TensorProduct(dtheta, dtheta)
    >>> metric_to_Ricci_components(non_trivial_metric)
    [[1/rho, 0], [0, exp(-2*rho)*rho]]

    """

class _deprecated_container:
    message: Incomplete
    def __init__(self, message, data) -> None: ...
    def warn(self) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __contains__(self, key) -> bool: ...

class _deprecated_list(_deprecated_container, list): ...
class _deprecated_dict(_deprecated_container, dict): ...

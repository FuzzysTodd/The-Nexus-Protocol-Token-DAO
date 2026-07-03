from _typeshed import Incomplete
from sympy.abc import x as x, y as y, z as z
from sympy.core import Expr as Expr, S as S, Symbol as Symbol, diff as diff
from sympy.geometry import Point as Point, Point2D as Point2D, Polygon as Polygon, Segment2D as Segment2D
from sympy.polys.polytools import LC as LC, Poly as Poly, degree_list as degree_list, gcd_list as gcd_list
from sympy.simplify.simplify import nsimplify as nsimplify

def polytope_integrate(poly, expr: Incomplete | None = None, *, clockwise: bool = False, max_degree: Incomplete | None = None):
    """Integrates polynomials over 2/3-Polytopes.

    Explanation
    ===========

    This function accepts the polytope in ``poly`` and the function in ``expr``
    (uni/bi/trivariate polynomials are implemented) and returns
    the exact integral of ``expr`` over ``poly``.

    Parameters
    ==========

    poly : The input Polygon.

    expr : The input polynomial.

    clockwise : Binary value to sort input points of 2-Polytope clockwise.(Optional)

    max_degree : The maximum degree of any monomial of the input polynomial.(Optional)

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy import Point, Polygon
    >>> from sympy.integrals.intpoly import polytope_integrate
    >>> polygon = Polygon(Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
    >>> polys = [1, x, y, x*y, x**2*y, x*y**2]
    >>> expr = x*y
    >>> polytope_integrate(polygon, expr)
    1/4
    >>> polytope_integrate(polygon, polys, max_degree=3)
    {1: 1, x: 1/2, y: 1/2, x*y: 1/4, x*y**2: 1/6, x**2*y: 1/6}
    """
def strip(monom): ...
def main_integrate3d(expr, facets, vertices, hp_params, max_degree: Incomplete | None = None):
    """Function to translate the problem of integrating uni/bi/tri-variate
    polynomials over a 3-Polytope to integrating over its faces.
    This is done using Generalized Stokes' Theorem and Euler's Theorem.

    Parameters
    ==========

    expr :
        The input polynomial.
    facets :
        Faces of the 3-Polytope(expressed as indices of `vertices`).
    vertices :
        Vertices that constitute the Polytope.
    hp_params :
        Hyperplane Parameters of the facets.
    max_degree : optional
        Max degree of constituent monomial in given list of polynomial.

    Examples
    ========

    >>> from sympy.integrals.intpoly import main_integrate3d,     hyperplane_parameters
    >>> cube = [[(0, 0, 0), (0, 0, 5), (0, 5, 0), (0, 5, 5), (5, 0, 0),                (5, 0, 5), (5, 5, 0), (5, 5, 5)],                [2, 6, 7, 3], [3, 7, 5, 1], [7, 6, 4, 5], [1, 5, 4, 0],                [3, 1, 0, 2], [0, 4, 6, 2]]
    >>> vertices = cube[0]
    >>> faces = cube[1:]
    >>> hp_params = hyperplane_parameters(faces, vertices)
    >>> main_integrate3d(1, faces, vertices, hp_params)
    -125
    """
def main_integrate(expr, facets, hp_params, max_degree: Incomplete | None = None):
    """Function to translate the problem of integrating univariate/bivariate
    polynomials over a 2-Polytope to integrating over its boundary facets.
    This is done using Generalized Stokes's Theorem and Euler's Theorem.

    Parameters
    ==========

    expr :
        The input polynomial.
    facets :
        Facets(Line Segments) of the 2-Polytope.
    hp_params :
        Hyperplane Parameters of the facets.
    max_degree : optional
        The maximum degree of any monomial of the input polynomial.

    >>> from sympy.abc import x, y
    >>> from sympy.integrals.intpoly import main_integrate,    hyperplane_parameters
    >>> from sympy import Point, Polygon
    >>> triangle = Polygon(Point(0, 3), Point(5, 3), Point(1, 1))
    >>> facets = triangle.sides
    >>> hp_params = hyperplane_parameters(triangle)
    >>> main_integrate(x**2 + y**2, facets, hp_params)
    325/6
    """
def polygon_integrate(facet, hp_param, index, facets, vertices, expr, degree):
    """Helper function to integrate the input uni/bi/trivariate polynomial
    over a certain face of the 3-Polytope.

    Parameters
    ==========

    facet :
        Particular face of the 3-Polytope over which ``expr`` is integrated.
    index :
        The index of ``facet`` in ``facets``.
    facets :
        Faces of the 3-Polytope(expressed as indices of `vertices`).
    vertices :
        Vertices that constitute the facet.
    expr :
        The input polynomial.
    degree :
        Degree of ``expr``.

    Examples
    ========

    >>> from sympy.integrals.intpoly import polygon_integrate
    >>> cube = [[(0, 0, 0), (0, 0, 5), (0, 5, 0), (0, 5, 5), (5, 0, 0),                 (5, 0, 5), (5, 5, 0), (5, 5, 5)],                 [2, 6, 7, 3], [3, 7, 5, 1], [7, 6, 4, 5], [1, 5, 4, 0],                 [3, 1, 0, 2], [0, 4, 6, 2]]
    >>> facet = cube[1]
    >>> facets = cube[1:]
    >>> vertices = cube[0]
    >>> polygon_integrate(facet, [(0, 1, 0), 5], 0, facets, vertices, 1, 0)
    -25
    """
def distance_to_side(point, line_seg, A):
    """Helper function to compute the signed distance between given 3D point
    and a line segment.

    Parameters
    ==========

    point : 3D Point
    line_seg : Line Segment

    Examples
    ========

    >>> from sympy.integrals.intpoly import distance_to_side
    >>> point = (0, 0, 0)
    >>> distance_to_side(point, [(0, 0, 1), (0, 1, 0)], (1, 0, 0))
    -sqrt(2)/2
    """
def lineseg_integrate(polygon, index, line_seg, expr, degree):
    """Helper function to compute the line integral of ``expr`` over ``line_seg``.

    Parameters
    ===========

    polygon :
        Face of a 3-Polytope.
    index :
        Index of line_seg in polygon.
    line_seg :
        Line Segment.

    Examples
    ========

    >>> from sympy.integrals.intpoly import lineseg_integrate
    >>> polygon = [(0, 5, 0), (5, 5, 0), (5, 5, 5), (0, 5, 5)]
    >>> line_seg = [(0, 5, 0), (5, 5, 0)]
    >>> lineseg_integrate(polygon, 0, line_seg, 1, 0)
    5
    """
def integration_reduction(facets, index, a, b, expr, dims, degree):
    """Helper method for main_integrate. Returns the value of the input
    expression evaluated over the polytope facet referenced by a given index.

    Parameters
    ===========

    facets :
        List of facets of the polytope.
    index :
        Index referencing the facet to integrate the expression over.
    a :
        Hyperplane parameter denoting direction.
    b :
        Hyperplane parameter denoting distance.
    expr :
        The expression to integrate over the facet.
    dims :
        List of symbols denoting axes.
    degree :
        Degree of the homogeneous polynomial.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.integrals.intpoly import integration_reduction,    hyperplane_parameters
    >>> from sympy import Point, Polygon
    >>> triangle = Polygon(Point(0, 3), Point(5, 3), Point(1, 1))
    >>> facets = triangle.sides
    >>> a, b = hyperplane_parameters(triangle)[0]
    >>> integration_reduction(facets, 0, a, b, 1, (x, y), 0)
    5
    """
def left_integral2D(m, index, facets, x0, expr, gens):
    """Computes the left integral of Eq 10 in Chin et al.
    For the 2D case, the integral is just an evaluation of the polynomial
    at the intersection of two facets which is multiplied by the distance
    between the first point of facet and that intersection.

    Parameters
    ==========

    m :
        No. of hyperplanes.
    index :
        Index of facet to find intersections with.
    facets :
        List of facets(Line Segments in 2D case).
    x0 :
        First point on facet referenced by index.
    expr :
        Input polynomial
    gens :
        Generators which generate the polynomial

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.integrals.intpoly import left_integral2D
    >>> from sympy import Point, Polygon
    >>> triangle = Polygon(Point(0, 3), Point(5, 3), Point(1, 1))
    >>> facets = triangle.sides
    >>> left_integral2D(3, 0, facets, facets[0].points[0], 1, (x, y))
    5
    """
def integration_reduction_dynamic(facets, index, a, b, expr, degree, dims, x_index, y_index, max_index, x0, monomial_values, monom_index, vertices: Incomplete | None = None, hp_param: Incomplete | None = None):
    """The same integration_reduction function which uses a dynamic
    programming approach to compute terms by using the values of the integral
    of previously computed terms.

    Parameters
    ==========

    facets :
        Facets of the Polytope.
    index :
        Index of facet to find intersections with.(Used in left_integral()).
    a, b :
        Hyperplane parameters.
    expr :
        Input monomial.
    degree :
        Total degree of ``expr``.
    dims :
        Tuple denoting axes variables.
    x_index :
        Exponent of 'x' in ``expr``.
    y_index :
        Exponent of 'y' in ``expr``.
    max_index :
        Maximum exponent of any monomial in ``monomial_values``.
    x0 :
        First point on ``facets[index]``.
    monomial_values :
        List of monomial values constituting the polynomial.
    monom_index :
        Index of monomial whose integration is being found.
    vertices : optional
        Coordinates of vertices constituting the 3-Polytope.
    hp_param : optional
        Hyperplane Parameter of the face of the facets[index].

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.integrals.intpoly import (integration_reduction_dynamic,             hyperplane_parameters)
    >>> from sympy import Point, Polygon
    >>> triangle = Polygon(Point(0, 3), Point(5, 3), Point(1, 1))
    >>> facets = triangle.sides
    >>> a, b = hyperplane_parameters(triangle)[0]
    >>> x0 = facets[0].points[0]
    >>> monomial_values = [[0, 0, 0, 0], [1, 0, 0, 5],                           [y, 0, 1, 15], [x, 1, 0, None]]
    >>> integration_reduction_dynamic(facets, 0, a, b, x, 1, (x, y), 1, 0, 1,                                      x0, monomial_values, 3)
    25/2
    """
def left_integral3D(facets, index, expr, vertices, hp_param, degree):
    """Computes the left integral of Eq 10 in Chin et al.

    Explanation
    ===========

    For the 3D case, this is the sum of the integral values over constituting
    line segments of the face (which is accessed by facets[index]) multiplied
    by the distance between the first point of facet and that line segment.

    Parameters
    ==========

    facets :
        List of faces of the 3-Polytope.
    index :
        Index of face over which integral is to be calculated.
    expr :
        Input polynomial.
    vertices :
        List of vertices that constitute the 3-Polytope.
    hp_param :
        The hyperplane parameters of the face.
    degree :
        Degree of the ``expr``.

    Examples
    ========

    >>> from sympy.integrals.intpoly import left_integral3D
    >>> cube = [[(0, 0, 0), (0, 0, 5), (0, 5, 0), (0, 5, 5), (5, 0, 0),                 (5, 0, 5), (5, 5, 0), (5, 5, 5)],                 [2, 6, 7, 3], [3, 7, 5, 1], [7, 6, 4, 5], [1, 5, 4, 0],                 [3, 1, 0, 2], [0, 4, 6, 2]]
    >>> facets = cube[1:]
    >>> vertices = cube[0]
    >>> left_integral3D(facets, 3, 1, vertices, ([0, -1, 0], -5), 0)
    -50
    """
def gradient_terms(binomial_power: int = 0, no_of_gens: int = 2):
    """Returns a list of all the possible monomials between
    0 and y**binomial_power for 2D case and z**binomial_power
    for 3D case.

    Parameters
    ==========

    binomial_power :
        Power upto which terms are generated.
    no_of_gens :
        Denotes whether terms are being generated for 2D or 3D case.

    Examples
    ========

    >>> from sympy.integrals.intpoly import gradient_terms
    >>> gradient_terms(2)
    [[1, 0, 0, 0], [y, 0, 1, 0], [y**2, 0, 2, 0], [x, 1, 0, 0],
    [x*y, 1, 1, 0], [x**2, 2, 0, 0]]
    >>> gradient_terms(2, 3)
    [[[[1, 0, 0, 0, 0, 0, 0, 0]]], [[[y, 0, 1, 0, 1, 0, 0, 0],
    [z, 0, 0, 1, 1, 0, 1, 0]], [[x, 1, 0, 0, 1, 1, 0, 0]]],
    [[[y**2, 0, 2, 0, 2, 0, 0, 0], [y*z, 0, 1, 1, 2, 0, 1, 0],
    [z**2, 0, 0, 2, 2, 0, 2, 0]], [[x*y, 1, 1, 0, 2, 1, 0, 0],
    [x*z, 1, 0, 1, 2, 1, 1, 0]], [[x**2, 2, 0, 0, 2, 2, 0, 0]]]]
    """
def hyperplane_parameters(poly, vertices: Incomplete | None = None):
    """A helper function to return the hyperplane parameters
    of which the facets of the polytope are a part of.

    Parameters
    ==========

    poly :
        The input 2/3-Polytope.
    vertices :
        Vertex indices of 3-Polytope.

    Examples
    ========

    >>> from sympy import Point, Polygon
    >>> from sympy.integrals.intpoly import hyperplane_parameters
    >>> hyperplane_parameters(Polygon(Point(0, 3), Point(5, 3), Point(1, 1)))
    [((0, 1), 3), ((1, -2), -1), ((-2, -1), -3)]
    >>> cube = [[(0, 0, 0), (0, 0, 5), (0, 5, 0), (0, 5, 5), (5, 0, 0),                (5, 0, 5), (5, 5, 0), (5, 5, 5)],                [2, 6, 7, 3], [3, 7, 5, 1], [7, 6, 4, 5], [1, 5, 4, 0],                [3, 1, 0, 2], [0, 4, 6, 2]]
    >>> hyperplane_parameters(cube[1:], cube[0])
    [([0, -1, 0], -5), ([0, 0, -1], -5), ([-1, 0, 0], -5),
    ([0, 1, 0], 0), ([1, 0, 0], 0), ([0, 0, 1], 0)]
    """
def cross_product(v1, v2, v3):
    """Returns the cross-product of vectors (v2 - v1) and (v3 - v1)
    That is : (v2 - v1) X (v3 - v1)
    """
def best_origin(a, b, lineseg, expr):
    """Helper method for polytope_integrate. Currently not used in the main
    algorithm.

    Explanation
    ===========

    Returns a point on the lineseg whose vector inner product with the
    divergence of `expr` yields an expression with the least maximum
    total power.

    Parameters
    ==========

    a :
        Hyperplane parameter denoting direction.
    b :
        Hyperplane parameter denoting distance.
    lineseg :
        Line segment on which to find the origin.
    expr :
        The expression which determines the best point.

    Algorithm(currently works only for 2D use case)
    ===============================================

    1 > Firstly, check for edge cases. Here that would refer to vertical
        or horizontal lines.

    2 > If input expression is a polynomial containing more than one generator
        then find out the total power of each of the generators.

        x**2 + 3 + x*y + x**4*y**5 ---> {x: 7, y: 6}

        If expression is a constant value then pick the first boundary point
        of the line segment.

    3 > First check if a point exists on the line segment where the value of
        the highest power generator becomes 0. If not check if the value of
        the next highest becomes 0. If none becomes 0 within line segment
        constraints then pick the first boundary point of the line segment.
        Actually, any point lying on the segment can be picked as best origin
        in the last case.

    Examples
    ========

    >>> from sympy.integrals.intpoly import best_origin
    >>> from sympy.abc import x, y
    >>> from sympy import Point, Segment2D
    >>> l = Segment2D(Point(0, 3), Point(1, 1))
    >>> expr = x**3*y**7
    >>> best_origin((2, 1), 3, l, expr)
    (0, 3.0)
    """
def decompose(expr, separate: bool = False):
    """Decomposes an input polynomial into homogeneous ones of
    smaller or equal degree.

    Explanation
    ===========

    Returns a dictionary with keys as the degree of the smaller
    constituting polynomials. Values are the constituting polynomials.

    Parameters
    ==========

    expr : Expr
        Polynomial(SymPy expression).
    separate : bool
        If True then simply return a list of the constituent monomials
        If not then break up the polynomial into constituent homogeneous
        polynomials.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.integrals.intpoly import decompose
    >>> decompose(x**2 + x*y + x + y + x**3*y**2 + y**5)
    {1: x + y, 2: x**2 + x*y, 5: x**3*y**2 + y**5}
    >>> decompose(x**2 + x*y + x + y + x**3*y**2 + y**5, True)
    {x, x**2, y, y**5, x*y, x**3*y**2}
    """
def point_sort(poly, normal: Incomplete | None = None, clockwise: bool = True):
    """Returns the same polygon with points sorted in clockwise or
    anti-clockwise order.

    Note that it's necessary for input points to be sorted in some order
    (clockwise or anti-clockwise) for the integration algorithm to work.
    As a convention algorithm has been implemented keeping clockwise
    orientation in mind.

    Parameters
    ==========

    poly:
        2D or 3D Polygon.
    normal : optional
        The normal of the plane which the 3-Polytope is a part of.
    clockwise : bool, optional
        Returns points sorted in clockwise order if True and
        anti-clockwise if False.

    Examples
    ========

    >>> from sympy.integrals.intpoly import point_sort
    >>> from sympy import Point
    >>> point_sort([Point(0, 0), Point(1, 0), Point(1, 1)])
    [Point2D(1, 1), Point2D(1, 0), Point2D(0, 0)]
    """
def norm(point):
    """Returns the Euclidean norm of a point from origin.

    Parameters
    ==========

    point:
        This denotes a point in the dimension_al spac_e.

    Examples
    ========

    >>> from sympy.integrals.intpoly import norm
    >>> from sympy import Point
    >>> norm(Point(2, 7))
    sqrt(53)
    """
def intersection(geom_1, geom_2, intersection_type):
    '''Returns intersection between geometric objects.

    Explanation
    ===========

    Note that this function is meant for use in integration_reduction and
    at that point in the calling function the lines denoted by the segments
    surely intersect within segment boundaries. Coincident lines are taken
    to be non-intersecting. Also, the hyperplane intersection for 2D case is
    also implemented.

    Parameters
    ==========

    geom_1, geom_2:
        The input line segments.

    Examples
    ========

    >>> from sympy.integrals.intpoly import intersection
    >>> from sympy import Point, Segment2D
    >>> l1 = Segment2D(Point(1, 1), Point(3, 5))
    >>> l2 = Segment2D(Point(2, 0), Point(2, 5))
    >>> intersection(l1, l2, "segment2D")
    (2, 3)
    >>> p1 = ((-1, 0), 0)
    >>> p2 = ((0, 1), 1)
    >>> intersection(p1, p2, "plane2D")
    (0, 1)
    '''
def is_vertex(ent):
    """If the input entity is a vertex return True.

    Parameter
    =========

    ent :
        Denotes a geometric entity representing a point.

    Examples
    ========

    >>> from sympy import Point
    >>> from sympy.integrals.intpoly import is_vertex
    >>> is_vertex((2, 3))
    True
    >>> is_vertex((2, 3, 6))
    True
    >>> is_vertex(Point(2, 3))
    True
    """
def plot_polytope(poly) -> None:
    """Plots the 2D polytope using the functions written in plotting
    module which in turn uses matplotlib backend.

    Parameter
    =========

    poly:
        Denotes a 2-Polytope.
    """
def plot_polynomial(expr) -> None:
    """Plots the polynomial using the functions written in
    plotting module which in turn uses matplotlib backend.

    Parameter
    =========

    expr:
        Denotes a polynomial(SymPy expression).
    """

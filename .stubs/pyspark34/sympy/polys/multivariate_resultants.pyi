from _typeshed import Incomplete
from sympy.core.mul import Mul as Mul
from sympy.functions.combinatorial.factorials import binomial as binomial
from sympy.matrices.dense import Matrix as Matrix, diag as diag
from sympy.polys.monomials import itermonomials as itermonomials, monomial_deg as monomial_deg
from sympy.polys.orderings import monomial_key as monomial_key
from sympy.polys.polytools import Poly as Poly, degree_list as degree_list, poly_from_expr as poly_from_expr, rem as rem, total_degree as total_degree
from sympy.simplify.simplify import simplify as simplify
from sympy.tensor.indexed import IndexedBase as IndexedBase
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning

class DixonResultant:
    """
    A class for retrieving the Dixon's resultant of a multivariate
    system.

    Examples
    ========

    >>> from sympy import symbols

    >>> from sympy.polys.multivariate_resultants import DixonResultant
    >>> x, y = symbols('x, y')

    >>> p = x + y
    >>> q = x ** 2 + y ** 3
    >>> h = x ** 2 + y

    >>> dixon = DixonResultant(variables=[x, y], polynomials=[p, q, h])
    >>> poly = dixon.get_dixon_polynomial()
    >>> matrix = dixon.get_dixon_matrix(polynomial=poly)
    >>> matrix
    Matrix([
    [ 0,  0, -1,  0, -1],
    [ 0, -1,  0, -1,  0],
    [-1,  0,  1,  0,  0],
    [ 0, -1,  0,  0,  1],
    [-1,  0,  0,  1,  0]])
    >>> matrix.det()
    0

    See Also
    ========

    Notebook in examples: sympy/example/notebooks.

    References
    ==========

    .. [1] [Kapur1994]_
    .. [2] [Palancz08]_

    """
    polynomials: Incomplete
    variables: Incomplete
    n: Incomplete
    m: Incomplete
    dummy_variables: Incomplete
    def __init__(self, polynomials, variables) -> None:
        """
        A class that takes two lists, a list of polynomials and list of
        variables. Returns the Dixon matrix of the multivariate system.

        Parameters
        ----------
        polynomials : list of polynomials
            A  list of m n-degree polynomials
        variables: list
            A list of all n variables
        """
    @property
    def max_degrees(self): ...
    def get_dixon_polynomial(self):
        """
        Returns
        =======

        dixon_polynomial: polynomial
            Dixon's polynomial is calculated as:

            delta = Delta(A) / ((x_1 - a_1) ... (x_n - a_n)) where,

            A =  |p_1(x_1,... x_n), ..., p_n(x_1,... x_n)|
                 |p_1(a_1,... x_n), ..., p_n(a_1,... x_n)|
                 |...             , ...,              ...|
                 |p_1(a_1,... a_n), ..., p_n(a_1,... a_n)|
        """
    def get_upper_degree(self): ...
    def get_max_degrees(self, polynomial):
        """
        Returns a list of the maximum degree of each variable appearing
        in the coefficients of the Dixon polynomial. The coefficients are
        viewed as polys in $x_1, x_2, \\dots, x_n$.
        """
    def get_dixon_matrix(self, polynomial):
        """
        Construct the Dixon matrix from the coefficients of polynomial
        \\alpha. Each coefficient is viewed as a polynomial of x_1, ...,
        x_n.
        """
    def KSY_precondition(self, matrix):
        """
        Test for the validity of the Kapur-Saxena-Yang precondition.

        The precondition requires that the column corresponding to the
        monomial 1 = x_1 ^ 0 * x_2 ^ 0 * ... * x_n ^ 0 is not a linear
        combination of the remaining ones. In SymPy notation this is
        the last column. For the precondition to hold the last non-zero
        row of the rref matrix should be of the form [0, 0, ..., 1].
        """
    def delete_zero_rows_and_columns(self, matrix):
        """Remove the zero rows and columns of the matrix."""
    def product_leading_entries(self, matrix):
        """Calculate the product of the leading entries of the matrix."""
    def get_KSY_Dixon_resultant(self, matrix):
        """Calculate the Kapur-Saxena-Yang approach to the Dixon Resultant."""

class MacaulayResultant:
    """
    A class for calculating the Macaulay resultant. Note that the
    polynomials must be homogenized and their coefficients must be
    given as symbols.

    Examples
    ========

    >>> from sympy import symbols

    >>> from sympy.polys.multivariate_resultants import MacaulayResultant
    >>> x, y, z = symbols('x, y, z')

    >>> a_0, a_1, a_2 = symbols('a_0, a_1, a_2')
    >>> b_0, b_1, b_2 = symbols('b_0, b_1, b_2')
    >>> c_0, c_1, c_2,c_3, c_4 = symbols('c_0, c_1, c_2, c_3, c_4')

    >>> f = a_0 * y -  a_1 * x + a_2 * z
    >>> g = b_1 * x ** 2 + b_0 * y ** 2 - b_2 * z ** 2
    >>> h = c_0 * y * z ** 2 - c_1 * x ** 3 + c_2 * x ** 2 * z - c_3 * x * z ** 2 + c_4 * z ** 3

    >>> mac = MacaulayResultant(polynomials=[f, g, h], variables=[x, y, z])
    >>> mac.monomial_set
    [x**4, x**3*y, x**3*z, x**2*y**2, x**2*y*z, x**2*z**2, x*y**3,
    x*y**2*z, x*y*z**2, x*z**3, y**4, y**3*z, y**2*z**2, y*z**3, z**4]
    >>> matrix = mac.get_matrix()
    >>> submatrix = mac.get_submatrix(matrix)
    >>> submatrix
    Matrix([
    [-a_1,  a_0,  a_2,    0],
    [   0, -a_1,    0,    0],
    [   0,    0, -a_1,    0],
    [   0,    0,    0, -a_1]])

    See Also
    ========

    Notebook in examples: sympy/example/notebooks.

    References
    ==========

    .. [1] [Bruce97]_
    .. [2] [Stiller96]_

    """
    polynomials: Incomplete
    variables: Incomplete
    n: Incomplete
    degrees: Incomplete
    degree_m: Incomplete
    monomials_size: Incomplete
    monomial_set: Incomplete
    def __init__(self, polynomials, variables) -> None:
        """
        Parameters
        ==========

        variables: list
            A list of all n variables
        polynomials : list of SymPy polynomials
            A  list of m n-degree polynomials
        """
    def get_size(self):
        """
        Returns
        =======

        size: int
            The size of set T. Set T is the set of all possible
            monomials of the n variables for degree equal to the
            degree_m
        """
    def get_monomials_of_certain_degree(self, degree):
        """
        Returns
        =======

        monomials: list
            A list of monomials of a certain degree.
        """
    def get_row_coefficients(self):
        """
        Returns
        =======

        row_coefficients: list
            The row coefficients of Macaulay's matrix
        """
    def get_matrix(self):
        """
        Returns
        =======

        macaulay_matrix: Matrix
            The Macaulay numerator matrix
        """
    def get_reduced_nonreduced(self):
        """
        Returns
        =======

        reduced: list
            A list of the reduced monomials
        non_reduced: list
            A list of the monomials that are not reduced

        Definition
        ==========

        A polynomial is said to be reduced in x_i, if its degree (the
        maximum degree of its monomials) in x_i is less than d_i. A
        polynomial that is reduced in all variables but one is said
        simply to be reduced.
        """
    def get_submatrix(self, matrix):
        """
        Returns
        =======

        macaulay_submatrix: Matrix
            The Macaulay denominator matrix. Columns that are non reduced are kept.
            The row which contains one of the a_{i}s is dropped. a_{i}s
            are the coefficients of x_i ^ {d_i}.
        """

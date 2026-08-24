from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.numbers import pi as pi
from sympy.core.singleton import S as S
from sympy.core.sympify import sympify as sympify
from sympy.external import import_module as import_module
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.special.gamma_functions import multigamma as multigamma
from sympy.matrices import Determinant as Determinant, ImmutableMatrix as ImmutableMatrix, Inverse as Inverse, MatrixBase as MatrixBase, MatrixSet as MatrixSet, MatrixSymbol as MatrixSymbol, Trace as Trace, Transpose as Transpose, matrix2numpy as matrix2numpy
from sympy.stats.rv import Distribution as Distribution, MatrixDomain as MatrixDomain, NamedArgsMixin as NamedArgsMixin, PSpace as PSpace, RandomMatrixSymbol as RandomMatrixSymbol

class MatrixPSpace(PSpace):
    """
    Represents probability space for
    Matrix Distributions.
    """
    def __new__(cls, sym, distribution, dim_n, dim_m): ...
    distribution: Incomplete
    symbol: Incomplete
    @property
    def domain(self): ...
    @property
    def value(self): ...
    @property
    def values(self): ...
    def compute_density(self, expr, *args): ...
    def sample(self, size=(), library: str = 'scipy', seed: Incomplete | None = None):
        """
        Internal sample method

        Returns dictionary mapping RandomMatrixSymbol to realization value.
        """

def rv(symbol, cls, args): ...

class SampleMatrixScipy:
    """Returns the sample from scipy of the given distribution"""
    def __new__(cls, dist, size, seed: Incomplete | None = None): ...

class SampleMatrixNumpy:
    """Returns the sample from numpy of the given distribution"""
    def __new__(cls, dist, size, seed: Incomplete | None = None): ...

class SampleMatrixPymc:
    """Returns the sample from pymc of the given distribution"""
    def __new__(cls, dist, size, seed: Incomplete | None = None): ...

class MatrixDistribution(Distribution, NamedArgsMixin):
    """
    Abstract class for Matrix Distribution.
    """
    def __new__(cls, *args): ...
    @staticmethod
    def check(*args) -> None: ...
    def __call__(self, expr): ...
    def sample(self, size=(), library: str = 'scipy', seed: Incomplete | None = None):
        """
        Internal sample method

        Returns dictionary mapping RandomSymbol to realization value.
        """

class MatrixGammaDistribution(MatrixDistribution):
    @staticmethod
    def check(alpha, beta, scale_matrix) -> None: ...
    @property
    def set(self): ...
    @property
    def dimension(self): ...
    def pdf(self, x): ...

def MatrixGamma(symbol, alpha, beta, scale_matrix):
    """
    Creates a random variable with Matrix Gamma Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    alpha: Positive Real number
        Shape Parameter
    beta: Positive Real number
        Scale Parameter
    scale_matrix: Positive definite real square matrix
        Scale Matrix

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, MatrixGamma
    >>> from sympy import MatrixSymbol, symbols
    >>> a, b = symbols('a b', positive=True)
    >>> M = MatrixGamma('M', a, b, [[2, 1], [1, 2]])
    >>> X = MatrixSymbol('X', 2, 2)
    >>> density(M)(X).doit()
    exp(Trace(Matrix([
    [-2/3,  1/3],
    [ 1/3, -2/3]])*X)/b)*Determinant(X)**(a - 3/2)/(3**a*sqrt(pi)*b**(2*a)*gamma(a)*gamma(a - 1/2))
    >>> density(M)([[1, 0], [0, 1]]).doit()
    exp(-4/(3*b))/(3**a*sqrt(pi)*b**(2*a)*gamma(a)*gamma(a - 1/2))


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Matrix_gamma_distribution

    """

class WishartDistribution(MatrixDistribution):
    @staticmethod
    def check(n, scale_matrix) -> None: ...
    @property
    def set(self): ...
    @property
    def dimension(self): ...
    def pdf(self, x): ...

def Wishart(symbol, n, scale_matrix):
    """
    Creates a random variable with Wishart Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    n: Positive Real number
        Represents degrees of freedom
    scale_matrix: Positive definite real square matrix
        Scale Matrix

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, Wishart
    >>> from sympy import MatrixSymbol, symbols
    >>> n = symbols('n', positive=True)
    >>> W = Wishart('W', n, [[2, 1], [1, 2]])
    >>> X = MatrixSymbol('X', 2, 2)
    >>> density(W)(X).doit()
    exp(Trace(Matrix([
    [-1/3,  1/6],
    [ 1/6, -1/3]])*X))*Determinant(X)**(n/2 - 3/2)/(2**n*3**(n/2)*sqrt(pi)*gamma(n/2)*gamma(n/2 - 1/2))
    >>> density(W)([[1, 0], [0, 1]]).doit()
    exp(-2/3)/(2**n*3**(n/2)*sqrt(pi)*gamma(n/2)*gamma(n/2 - 1/2))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Wishart_distribution

    """

class MatrixNormalDistribution(MatrixDistribution):
    @staticmethod
    def check(location_matrix, scale_matrix_1, scale_matrix_2) -> None: ...
    @property
    def set(self): ...
    @property
    def dimension(self): ...
    def pdf(self, x): ...

def MatrixNormal(symbol, location_matrix, scale_matrix_1, scale_matrix_2):
    """
    Creates a random variable with Matrix Normal Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    location_matrix: Real ``n x p`` matrix
        Represents degrees of freedom
    scale_matrix_1: Positive definite matrix
        Scale Matrix of shape ``n x n``
    scale_matrix_2: Positive definite matrix
        Scale Matrix of shape ``p x p``

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy import MatrixSymbol
    >>> from sympy.stats import density, MatrixNormal
    >>> M = MatrixNormal('M', [[1, 2]], [1], [[1, 0], [0, 1]])
    >>> X = MatrixSymbol('X', 1, 2)
    >>> density(M)(X).doit()
    exp(-Trace((Matrix([
    [-1],
    [-2]]) + X.T)*(Matrix([[-1, -2]]) + X))/2)/(2*pi)
    >>> density(M)([[3, 4]]).doit()
    exp(-4)/(2*pi)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Matrix_normal_distribution

    """

class MatrixStudentTDistribution(MatrixDistribution):
    @staticmethod
    def check(nu, location_matrix, scale_matrix_1, scale_matrix_2) -> None: ...
    @property
    def set(self): ...
    @property
    def dimension(self): ...
    def pdf(self, x): ...

def MatrixStudentT(symbol, nu, location_matrix, scale_matrix_1, scale_matrix_2):
    """
    Creates a random variable with Matrix Gamma Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    nu: Positive Real number
        degrees of freedom
    location_matrix: Positive definite real square matrix
        Location Matrix of shape ``n x p``
    scale_matrix_1: Positive definite real square matrix
        Scale Matrix of shape ``p x p``
    scale_matrix_2: Positive definite real square matrix
        Scale Matrix of shape ``n x n``

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy import MatrixSymbol,symbols
    >>> from sympy.stats import density, MatrixStudentT
    >>> v = symbols('v',positive=True)
    >>> M = MatrixStudentT('M', v, [[1, 2]], [[1, 0], [0, 1]], [1])
    >>> X = MatrixSymbol('X', 1, 2)
    >>> density(M)(X)
    gamma(v/2 + 1)*Determinant((Matrix([[-1, -2]]) + X)*(Matrix([
    [-1],
    [-2]]) + X.T) + Matrix([[1]]))**(-v/2 - 1)/(pi**1.0*gamma(v/2)*Determinant(Matrix([[1]]))**1.0*Determinant(Matrix([
    [1, 0],
    [0, 1]]))**0.5)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Matrix_t-distribution

    """

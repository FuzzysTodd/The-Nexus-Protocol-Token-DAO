from _typeshed import Incomplete
from sympy.core.basic import Basic

__all__ = ['CircularEnsemble', 'CircularUnitaryEnsemble', 'CircularOrthogonalEnsemble', 'CircularSymplecticEnsemble', 'GaussianEnsemble', 'GaussianUnitaryEnsemble', 'GaussianOrthogonalEnsemble', 'GaussianSymplecticEnsemble', 'joint_eigen_distribution', 'JointEigenDistribution', 'level_spacing_distribution']

class RandomMatrixEnsembleModel(Basic):
    """
    Base class for random matrix ensembles.
    It acts as an umbrella and contains
    the methods common to all the ensembles
    defined in sympy.stats.random_matrix_models.
    """
    def __new__(cls, sym, dim: Incomplete | None = None): ...
    symbol: Incomplete
    dimension: Incomplete
    def density(self, expr): ...
    def __call__(self, expr): ...

class GaussianEnsembleModel(RandomMatrixEnsembleModel):
    """
    Abstract class for Gaussian ensembles.
    Contains the properties common to all the
    gaussian ensembles.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Random_matrix#Gaussian_ensembles
    .. [2] https://arxiv.org/pdf/1712.07903.pdf
    """

class GaussianUnitaryEnsembleModel(GaussianEnsembleModel):
    @property
    def normalization_constant(self): ...
    def density(self, expr): ...
    def joint_eigen_distribution(self): ...
    def level_spacing_distribution(self): ...

class GaussianOrthogonalEnsembleModel(GaussianEnsembleModel):
    @property
    def normalization_constant(self): ...
    def density(self, expr): ...
    def joint_eigen_distribution(self): ...
    def level_spacing_distribution(self): ...

class GaussianSymplecticEnsembleModel(GaussianEnsembleModel):
    @property
    def normalization_constant(self): ...
    def density(self, expr): ...
    def joint_eigen_distribution(self): ...
    def level_spacing_distribution(self): ...

def GaussianEnsemble(sym, dim): ...
def GaussianUnitaryEnsemble(sym, dim):
    """
    Represents Gaussian Unitary Ensembles.

    Examples
    ========

    >>> from sympy.stats import GaussianUnitaryEnsemble as GUE, density
    >>> from sympy import MatrixSymbol
    >>> G = GUE('U', 2)
    >>> X = MatrixSymbol('X', 2, 2)
    >>> density(G)(X)
    exp(-Trace(X**2))/(2*pi**2)
    """
def GaussianOrthogonalEnsemble(sym, dim):
    """
    Represents Gaussian Orthogonal Ensembles.

    Examples
    ========

    >>> from sympy.stats import GaussianOrthogonalEnsemble as GOE, density
    >>> from sympy import MatrixSymbol
    >>> G = GOE('U', 2)
    >>> X = MatrixSymbol('X', 2, 2)
    >>> density(G)(X)
    exp(-Trace(X**2)/2)/Integral(exp(-Trace(_H**2)/2), _H)
    """
def GaussianSymplecticEnsemble(sym, dim):
    """
    Represents Gaussian Symplectic Ensembles.

    Examples
    ========

    >>> from sympy.stats import GaussianSymplecticEnsemble as GSE, density
    >>> from sympy import MatrixSymbol
    >>> G = GSE('U', 2)
    >>> X = MatrixSymbol('X', 2, 2)
    >>> density(G)(X)
    exp(-2*Trace(X**2))/Integral(exp(-2*Trace(_H**2)), _H)
    """

class CircularEnsembleModel(RandomMatrixEnsembleModel):
    """
    Abstract class for Circular ensembles.
    Contains the properties and methods
    common to all the circular ensembles.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Circular_ensemble
    """
    def density(self, expr) -> None: ...

class CircularUnitaryEnsembleModel(CircularEnsembleModel):
    def joint_eigen_distribution(self): ...

class CircularOrthogonalEnsembleModel(CircularEnsembleModel):
    def joint_eigen_distribution(self): ...

class CircularSymplecticEnsembleModel(CircularEnsembleModel):
    def joint_eigen_distribution(self): ...

def CircularEnsemble(sym, dim): ...
def CircularUnitaryEnsemble(sym, dim):
    """
    Represents Circular Unitary Ensembles.

    Examples
    ========

    >>> from sympy.stats import CircularUnitaryEnsemble as CUE
    >>> from sympy.stats import joint_eigen_distribution
    >>> C = CUE('U', 1)
    >>> joint_eigen_distribution(C)
    Lambda(t[1], Product(Abs(exp(I*t[_j]) - exp(I*t[_k]))**2, (_j, _k + 1, 1), (_k, 1, 0))/(2*pi))

    Note
    ====

    As can be seen above in the example, density of CiruclarUnitaryEnsemble
    is not evaluated because the exact definition is based on haar measure of
    unitary group which is not unique.
    """
def CircularOrthogonalEnsemble(sym, dim):
    """
    Represents Circular Orthogonal Ensembles.

    Examples
    ========

    >>> from sympy.stats import CircularOrthogonalEnsemble as COE
    >>> from sympy.stats import joint_eigen_distribution
    >>> C = COE('O', 1)
    >>> joint_eigen_distribution(C)
    Lambda(t[1], Product(Abs(exp(I*t[_j]) - exp(I*t[_k])), (_j, _k + 1, 1), (_k, 1, 0))/(2*pi))

    Note
    ====

    As can be seen above in the example, density of CiruclarOrthogonalEnsemble
    is not evaluated because the exact definition is based on haar measure of
    unitary group which is not unique.
    """
def CircularSymplecticEnsemble(sym, dim):
    """
    Represents Circular Symplectic Ensembles.

    Examples
    ========

    >>> from sympy.stats import CircularSymplecticEnsemble as CSE
    >>> from sympy.stats import joint_eigen_distribution
    >>> C = CSE('S', 1)
    >>> joint_eigen_distribution(C)
    Lambda(t[1], Product(Abs(exp(I*t[_j]) - exp(I*t[_k]))**4, (_j, _k + 1, 1), (_k, 1, 0))/(2*pi))

    Note
    ====

    As can be seen above in the example, density of CiruclarSymplecticEnsemble
    is not evaluated because the exact definition is based on haar measure of
    unitary group which is not unique.
    """
def joint_eigen_distribution(mat):
    """
    For obtaining joint probability distribution
    of eigen values of random matrix.

    Parameters
    ==========

    mat: RandomMatrixSymbol
        The matrix symbol whose eigen values are to be considered.

    Returns
    =======

    Lambda

    Examples
    ========

    >>> from sympy.stats import GaussianUnitaryEnsemble as GUE
    >>> from sympy.stats import joint_eigen_distribution
    >>> U = GUE('U', 2)
    >>> joint_eigen_distribution(U)
    Lambda((l[1], l[2]), exp(-l[1]**2 - l[2]**2)*Product(Abs(l[_i] - l[_j])**2, (_j, _i + 1, 2), (_i, 1, 1))/pi)
    """
def JointEigenDistribution(mat):
    """
    Creates joint distribution of eigen values of matrices with random
    expressions.

    Parameters
    ==========

    mat: Matrix
        The matrix under consideration.

    Returns
    =======

    JointDistributionHandmade

    Examples
    ========

    >>> from sympy.stats import Normal, JointEigenDistribution
    >>> from sympy import Matrix
    >>> A = [[Normal('A00', 0, 1), Normal('A01', 0, 1)],
    ... [Normal('A10', 0, 1), Normal('A11', 0, 1)]]
    >>> JointEigenDistribution(Matrix(A))
    JointDistributionHandmade(-sqrt(A00**2 - 2*A00*A11 + 4*A01*A10 + A11**2)/2
    + A00/2 + A11/2, sqrt(A00**2 - 2*A00*A11 + 4*A01*A10 + A11**2)/2 + A00/2 + A11/2)

    """
def level_spacing_distribution(mat):
    """
    For obtaining distribution of level spacings.

    Parameters
    ==========

    mat: RandomMatrixSymbol
        The random matrix symbol whose eigen values are
        to be considered for finding the level spacings.

    Returns
    =======

    Lambda

    Examples
    ========

    >>> from sympy.stats import GaussianUnitaryEnsemble as GUE
    >>> from sympy.stats import level_spacing_distribution
    >>> U = GUE('U', 2)
    >>> level_spacing_distribution(U)
    Lambda(_s, 32*_s**2*exp(-4*_s**2/pi)/pi**2)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Random_matrix#Distribution_of_level_spacings
    """

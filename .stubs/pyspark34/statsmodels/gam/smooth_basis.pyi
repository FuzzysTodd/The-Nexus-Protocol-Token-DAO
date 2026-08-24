import abc
from _typeshed import Incomplete
from statsmodels.compat.python import with_metaclass as with_metaclass
from statsmodels.tools.linalg import transf_constraints as transf_constraints

def compute_all_knots(x, df, degree): ...
def make_bsplines_basis(x, df, degree):
    """ make a spline basis for x """
def get_knots_bsplines(x: Incomplete | None = None, df: Incomplete | None = None, knots: Incomplete | None = None, degree: int = 3, spacing: str = 'quantile', lower_bound: Incomplete | None = None, upper_bound: Incomplete | None = None, all_knots: Incomplete | None = None):
    """knots for use in B-splines

    There are two main options for the knot placement

    - quantile spacing with multiplicity of boundary knots
    - equal spacing extended to boundary or exterior knots

    The first corresponds to splines as used by patsy. the second is the
    knot spacing for P-Splines.
    """
def get_covder2(smoother, k_points: int = 4, integration_points: Incomplete | None = None, skip_ctransf: bool = False, deriv: int = 2):
    """
    Approximate integral of cross product of second derivative of smoother

    This uses scipy.integrate simps to compute an approximation to the
    integral of the smoother derivative cross-product at knots plus k_points
    in between knots.
    """
def make_poly_basis(x, degree, intercept: bool = True):
    """
    given a vector x returns poly=(1, x, x^2, ..., x^degree)
    and its first and second derivative
    """

class UnivariateGamSmoother(Incomplete, metaclass=abc.ABCMeta):
    """Base Class for single smooth component
    """
    x: Incomplete
    constraints: Incomplete
    variable_name: Incomplete
    ctransf: Incomplete
    basis: Incomplete
    der_basis: Incomplete
    der2_basis: Incomplete
    cov_der2: Incomplete
    dim_basis: Incomplete
    col_names: Incomplete
    def __init__(self, x, constraints: Incomplete | None = None, variable_name: str = 'x') -> None: ...

class UnivariateGenericSmoother(UnivariateGamSmoother):
    """Generic single smooth component
    """
    basis: Incomplete
    der_basis: Incomplete
    der2_basis: Incomplete
    cov_der2: Incomplete
    def __init__(self, x, basis, der_basis, der2_basis, cov_der2, variable_name: str = 'x') -> None: ...

class UnivariatePolynomialSmoother(UnivariateGamSmoother):
    """polynomial single smooth component
    """
    degree: Incomplete
    def __init__(self, x, degree, variable_name: str = 'x') -> None: ...

class UnivariateBSplines(UnivariateGamSmoother):
    """B-Spline single smooth component

    This creates and holds the B-Spline basis function for one
    component.

    Parameters
    ----------
    x : ndarray, 1-D
        underlying explanatory variable for smooth terms.
    df : int
        number of basis functions or degrees of freedom
    degree : int
        degree of the spline
    include_intercept : bool
        If False, then the basis functions are transformed so that they
        do not include a constant. This avoids perfect collinearity if
        a constant or several components are included in the model.
    constraints : {None, str, array}
        Constraints are used to transform the basis functions to satisfy
        those constraints.
        `constraints = 'center'` applies a linear transform to remove the
        constant and center the basis functions.
    variable_name : {None, str}
        The name for the underlying explanatory variable, x, used in for
        creating the column and parameter names for the basis functions.
    covder2_kwds : {None, dict}
        options for computing the penalty matrix from the second derivative
        of the spline.
    knot_kwds : {None, list[dict]}
        option for the knot selection.
        By default knots are selected in the same way as in patsy, however the
        number of knots is independent of keeping or removing the constant.
        Interior knot selection is based on quantiles of the data and is the
        same in patsy and mgcv. Boundary points are at the limits of the data
        range.
        The available options use with `get_knots_bsplines` are

        - knots : None or array
          interior knots
        - spacing : 'quantile' or 'equal'
        - lower_bound : None or float
          location of lower boundary knots, all boundary knots are at the same
          point
        - upper_bound : None or float
          location of upper boundary knots, all boundary knots are at the same
          point
        - all_knots : None or array
          If all knots are provided, then those will be taken as given and
          all other options will be ignored.
    """
    degree: Incomplete
    df: Incomplete
    include_intercept: Incomplete
    knots: Incomplete
    covder2_kwds: Incomplete
    def __init__(self, x, df, degree: int = 3, include_intercept: bool = False, constraints: Incomplete | None = None, variable_name: str = 'x', covder2_kwds: Incomplete | None = None, **knot_kwds) -> None: ...
    def transform(self, x_new, deriv: int = 0, skip_ctransf: bool = False):
        """create the spline basis for new observations

        The main use of this stateful transformation is for prediction
        using the same specification of the spline basis.

        Parameters
        ----------
        x_new : ndarray
            observations of the underlying explanatory variable
        deriv : int
            which derivative of the spline basis to compute
            This is an options for internal computation.
        skip_ctransf : bool
            whether to skip the constraint transform
            This is an options for internal computation.

        Returns
        -------
        basis : ndarray
            design matrix for the spline basis for given ``x_new``
        """

class UnivariateCubicSplines(UnivariateGamSmoother):
    """Cubic Spline single smooth component

    Cubic splines as described in the wood's book in chapter 3
    """
    degree: int
    df: Incomplete
    transform_data_method: Incomplete
    x: Incomplete
    knots: Incomplete
    def __init__(self, x, df, constraints: Incomplete | None = None, transform: str = 'domain', variable_name: str = 'x') -> None: ...
    domain_low: Incomplete
    domain_upp: Incomplete
    domain_diff: Incomplete
    def transform_data(self, x, initialize: bool = False): ...
    def transform(self, x_new): ...

class UnivariateCubicCyclicSplines(UnivariateGamSmoother):
    """cyclic cubic regression spline single smooth component

    This creates and holds the Cyclic CubicSpline basis function for one
    component.

    Parameters
    ----------
    x : ndarray, 1-D
        underlying explanatory variable for smooth terms.
    df : int
        number of basis functions or degrees of freedom
    degree : int
        degree of the spline
    include_intercept : bool
        If False, then the basis functions are transformed so that they
        do not include a constant. This avoids perfect collinearity if
        a constant or several components are included in the model.
    constraints : {None, str, array}
        Constraints are used to transform the basis functions to satisfy
        those constraints.
        `constraints = 'center'` applies a linear transform to remove the
        constant and center the basis functions.
    variable_name : None or str
        The name for the underlying explanatory variable, x, used in for
        creating the column and parameter names for the basis functions.
    """
    degree: int
    df: Incomplete
    x: Incomplete
    knots: Incomplete
    def __init__(self, x, df, constraints: Incomplete | None = None, variable_name: str = 'x') -> None: ...
    def transform(self, x_new): ...

class AdditiveGamSmoother(Incomplete, metaclass=abc.ABCMeta):
    """Base class for additive smooth components
    """
    x: Incomplete
    include_intercept: Incomplete
    variable_names: Incomplete
    smoothers: Incomplete
    basis: Incomplete
    dim_basis: Incomplete
    penalty_matrices: Incomplete
    col_names: Incomplete
    mask: Incomplete
    def __init__(self, x, variable_names: Incomplete | None = None, include_intercept: bool = False, **kwargs) -> None: ...
    def transform(self, x_new):
        """create the spline basis for new observations

        The main use of this stateful transformation is for prediction
        using the same specification of the spline basis.

        Parameters
        ----------
        x_new: ndarray
            observations of the underlying explanatory variable

        Returns
        -------
        basis : ndarray
            design matrix for the spline basis for given ``x_new``.
        """

class GenericSmoothers(AdditiveGamSmoother):
    """generic class for additive smooth components for GAM
    """
    smoothers: Incomplete
    def __init__(self, x, smoothers) -> None: ...

class PolynomialSmoother(AdditiveGamSmoother):
    """additive polynomial components for GAM
    """
    degrees: Incomplete
    def __init__(self, x, degrees, variable_names: Incomplete | None = None) -> None: ...

class BSplines(AdditiveGamSmoother):
    """additive smooth components using B-Splines

    This creates and holds the B-Spline basis function for several
    components.

    Parameters
    ----------
    x : array_like, 1-D or 2-D
        underlying explanatory variable for smooth terms.
        If 2-dimensional, then observations should be in rows and
        explanatory variables in columns.
    df :  {int, array_like[int]}
        number of basis functions or degrees of freedom; should be equal
        in length to the number of columns of `x`; may be an integer if
        `x` has one column or is 1-D.
    degree : {int, array_like[int]}
        degree(s) of the spline; the same length and type rules apply as
        to `df`
    include_intercept : bool
        If False, then the basis functions are transformed so that they
        do not include a constant. This avoids perfect collinearity if
        a constant or several components are included in the model.
    constraints : {None, str, array}
        Constraints are used to transform the basis functions to satisfy
        those constraints.
        `constraints = 'center'` applies a linear transform to remove the
        constant and center the basis functions.
    variable_names : {list[str], None}
        The names for the underlying explanatory variables, x used in for
        creating the column and parameter names for the basis functions.
        If ``x`` is a pandas object, then the names will be taken from it.
    knot_kwds : None or list of dict
        option for the knot selection.
        By default knots are selected in the same way as in patsy, however the
        number of knots is independent of keeping or removing the constant.
        Interior knot selection is based on quantiles of the data and is the
        same in patsy and mgcv. Boundary points are at the limits of the data
        range.
        The available options use with `get_knots_bsplines` are

        - knots : None or array
          interior knots
        - spacing : 'quantile' or 'equal'
        - lower_bound : None or float
          location of lower boundary knots, all boundary knots are at the same
          point
        - upper_bound : None or float
          location of upper boundary knots, all boundary knots are at the same
          point
        - all_knots : None or array
          If all knots are provided, then those will be taken as given and
          all other options will be ignored.


    Attributes
    ----------
    smoothers : list of univariate smooth component instances
    basis : design matrix, array of spline bases columns for all components
    penalty_matrices : list of penalty matrices, one for each smooth term
    dim_basis : number of columns in the basis
    k_variables : number of smooth components
    col_names : created names for the basis columns

    There are additional attributes about the specification of the splines
    and some attributes mainly for internal use.

    Notes
    -----
    A constant in the spline basis function can be removed in two different
    ways.
    The first is by dropping one basis column and normalizing the
    remaining columns. This is obtained by the default
    ``include_intercept=False, constraints=None``
    The second option is by using the centering transform which is a linear
    transformation of all basis functions. As a consequence of the
    transformation, the B-spline basis functions do not have locally bounded
    support anymore. This is obtained ``constraints='center'``. In this case
    ``include_intercept`` will be automatically set to True to avoid
    dropping an additional column.
    """
    degrees: Incomplete
    dfs: Incomplete
    knot_kwds: Incomplete
    constraints: Incomplete
    def __init__(self, x, df, degree, include_intercept: bool = False, constraints: Incomplete | None = None, variable_names: Incomplete | None = None, knot_kwds: Incomplete | None = None) -> None: ...

class CubicSplines(AdditiveGamSmoother):
    """additive smooth components using cubic splines as in Wood 2006.

    Note, these splines do NOT use the same spline basis as
    ``Cubic Regression Splines``.
    """
    dfs: Incomplete
    constraints: Incomplete
    transform: Incomplete
    def __init__(self, x, df, constraints: str = 'center', transform: str = 'domain', variable_names: Incomplete | None = None) -> None: ...

class CyclicCubicSplines(AdditiveGamSmoother):
    """additive smooth components using cyclic cubic regression splines

    This spline basis is the same as in patsy.

    Parameters
    ----------
    x : array_like, 1-D or 2-D
        underlying explanatory variable for smooth terms.
        If 2-dimensional, then observations should be in rows and
        explanatory variables in columns.
    df :  int
        numer of basis functions or degrees of freedom
    constraints : {None, str, array}
        Constraints are used to transform the basis functions to satisfy
        those constraints.
    variable_names : {list[str], None}
        The names for the underlying explanatory variables, x used in for
        creating the column and parameter names for the basis functions.
        If ``x`` is a pandas object, then the names will be taken from it.
    """
    dfs: Incomplete
    constraints: Incomplete
    def __init__(self, x, df, constraints: Incomplete | None = None, variable_names: Incomplete | None = None) -> None: ...

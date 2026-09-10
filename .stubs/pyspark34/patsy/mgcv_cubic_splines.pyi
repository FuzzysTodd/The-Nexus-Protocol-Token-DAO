from _typeshed import Incomplete

__all__ = ['cr', 'cc', 'te']

class CubicRegressionSpline:
    """Base class for cubic regression spline stateful transforms

    This class contains all the functionality for the following stateful
    transforms:
     - ``cr(x, df=None, knots=None, lower_bound=None, upper_bound=None, constraints=None)``
       for natural cubic regression spline
     - ``cc(x, df=None, knots=None, lower_bound=None, upper_bound=None, constraints=None)``
       for cyclic cubic regression spline
    """
    common_doc: str
    def __init__(self, name, cyclic) -> None: ...
    def memorize_chunk(self, x, df: Incomplete | None = None, knots: Incomplete | None = None, lower_bound: Incomplete | None = None, upper_bound: Incomplete | None = None, constraints: Incomplete | None = None) -> None: ...
    def memorize_finish(self) -> None: ...
    def transform(self, x, df: Incomplete | None = None, knots: Incomplete | None = None, lower_bound: Incomplete | None = None, upper_bound: Incomplete | None = None, constraints: Incomplete | None = None): ...

class CR(CubicRegressionSpline):
    """cr(x, df=None, knots=None, lower_bound=None, upper_bound=None, constraints=None)

    Generates a natural cubic spline basis for ``x``
    (with the option of absorbing centering or more general parameters
    constraints), allowing non-linear fits. The usual usage is something like::

      y ~ 1 + cr(x, df=5, constraints='center')

    to fit ``y`` as a smooth function of ``x``, with 5 degrees of freedom
    given to the smooth, and centering constraint absorbed in
    the resulting design matrix. Note that in this example, due to the centering
    constraint, 6 knots will get computed from the input data ``x``
    to achieve 5 degrees of freedom.


    .. note:: This function reproduce the cubic regression splines 'cr' and 'cs'
      as implemented in the R package 'mgcv' (GAM modelling).

    """
    def __init__(self) -> None: ...

cr: Incomplete

class CC(CubicRegressionSpline):
    """cc(x, df=None, knots=None, lower_bound=None, upper_bound=None, constraints=None)

    Generates a cyclic cubic spline basis for ``x``
    (with the option of absorbing centering or more general parameters
    constraints), allowing non-linear fits. The usual usage is something like::

      y ~ 1 + cc(x, df=7, constraints='center')

    to fit ``y`` as a smooth function of ``x``, with 7 degrees of freedom
    given to the smooth, and centering constraint absorbed in
    the resulting design matrix. Note that in this example, due to the centering
    and cyclic constraints, 9 knots will get computed from the input data ``x``
    to achieve 7 degrees of freedom.

    .. note:: This function reproduce the cubic regression splines 'cc'
      as implemented in the R package 'mgcv' (GAM modelling).

    """
    def __init__(self) -> None: ...

cc: Incomplete

class TE:
    """te(s1, .., sn, constraints=None)

    Generates smooth of several covariates as a tensor product of the bases
    of marginal univariate smooths ``s1, .., sn``. The marginal smooths are
    required to transform input univariate data into some kind of smooth
    functions basis producing a 2-d array output with the ``(i, j)`` element
    corresponding to the value of the ``j`` th basis function at the ``i`` th
    data point.
    The resulting basis dimension is the product of the basis dimensions of
    the marginal smooths. The usual usage is something like::

      y ~ 1 + te(cr(x1, df=5), cc(x2, df=6), constraints='center')

    to fit ``y`` as a smooth function of both ``x1`` and ``x2``, with a natural
    cubic spline for ``x1`` marginal smooth and a cyclic cubic spline for
    ``x2`` (and centering constraint absorbed in the resulting design matrix).

    :arg constraints: Either a 2-d array defining general linear constraints
     (that is ``np.dot(constraints, betas)`` is zero, where ``betas`` denotes
     the array of *initial* parameters, corresponding to the *initial*
     unconstrained design matrix), or the string
     ``'center'`` indicating that we should apply a centering constraint
     (this constraint will be computed from the input data, remembered and
     re-used for prediction from the fitted model).
     The constraints are absorbed in the resulting design matrix which means
     that the model is actually rewritten in terms of
     *unconstrained* parameters. For more details see :ref:`spline-regression`.

    Using this function requires scipy be installed.

    .. note:: This function reproduce the tensor product smooth 'te' as
      implemented in the R package 'mgcv' (GAM modelling).
      See also 'Generalized Additive Models', Simon N. Wood, 2006, pp 158-163

    .. versionadded:: 0.3.0
    """
    def __init__(self) -> None: ...
    def memorize_chunk(self, *args, **kwargs) -> None: ...
    def memorize_finish(self) -> None: ...
    def transform(self, *args, **kwargs): ...

te: Incomplete

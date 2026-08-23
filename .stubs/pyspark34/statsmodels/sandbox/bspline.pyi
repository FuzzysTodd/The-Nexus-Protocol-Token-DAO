from _typeshed import Incomplete

class BSpline:
    '''

    Bsplines of a given order and specified knots.

    Implementation is based on description in Chapter 5 of

    Hastie, Tibshirani and Friedman (2001). "The Elements of Statistical
    Learning." Springer-Verlag. 536 pages.


    INPUTS:
       knots  -- a sorted array of knots with knots[0] the lower boundary,
                 knots[1] the upper boundary and knots[1:-1] the internal
                 knots.
       order  -- order of the Bspline, default is 4 which yields cubic
                 splines
       M      -- number of additional boundary knots, if None it defaults
                 to order
       coef   -- an optional array of real-valued coefficients for the Bspline
                 of shape (knots.shape + 2 * (M - 1) - order,).
       x      -- an optional set of x values at which to evaluate the
                 Bspline to avoid extra evaluation in the __call__ method

    '''
    m: Incomplete
    M: Incomplete
    tau: Incomplete
    K: Incomplete
    coef: Incomplete
    x: Incomplete
    def __init__(self, knots, order: int = 4, M: Incomplete | None = None, coef: Incomplete | None = None, x: Incomplete | None = None) -> None: ...
    def __call__(self, *args):
        """
        Evaluate the BSpline at a given point, yielding
        a matrix B and return

        B * self.coef


        INPUTS:
           args -- optional arguments. If None, it returns self._basisx,
                   the BSpline evaluated at the x values passed in __init__.
                   Otherwise, return the BSpline evaluated at the
                   first argument args[0].

        OUTPUTS: y
           y    -- value of Bspline at specified x values

        BUGS:
           If self has no attribute x, an exception will be raised
           because self has no attribute _basisx.
        """
    def basis_element(self, x, i, d: int = 0):
        """
        Evaluate a particular basis element of the BSpline,
        or its derivative.

        INPUTS:
           x  -- x values at which to evaluate the basis element
           i  -- which element of the BSpline to return
           d  -- the order of derivative

        OUTPUTS: y
           y  -- value of d-th derivative of the i-th basis element
                 of the BSpline at specified x values
        """
    def basis(self, x, d: int = 0, lower: Incomplete | None = None, upper: Incomplete | None = None):
        """
        Evaluate the basis of the BSpline or its derivative.
        If lower or upper is specified, then only
        the [lower:upper] elements of the basis are returned.

        INPUTS:
           x     -- x values at which to evaluate the basis element
           i     -- which element of the BSpline to return
           d     -- the order of derivative
           lower -- optional lower limit of the set of basis
                    elements
           upper -- optional upper limit of the set of basis
                    elements

        OUTPUTS: y
           y  -- value of d-th derivative of the basis elements
                 of the BSpline at specified x values
        """
    g: Incomplete
    d: Incomplete
    def gram(self, d: int = 0):
        """
        Compute Gram inner product matrix, storing it in lower
        triangular banded form.

        The (i,j) entry is

        G_ij = integral b_i^(d) b_j^(d)

        where b_i are the basis elements of the BSpline and (d) is the
        d-th derivative.

        If d is a matrix then, it is assumed to specify a differential
        operator as follows: the first row represents the order of derivative
        with the second row the coefficient corresponding to that order.

        For instance:

        [[2, 3],
         [3, 1]]

        represents 3 * f^(2) + 1 * f^(3).

        INPUTS:
           d    -- which derivative to apply to each basis element,
                   if d is a matrix, it is assumed to specify
                   a differential operator as above

        OUTPUTS: gram
           gram -- the matrix of inner products of (derivatives)
                   of the BSpline elements
        """

class SmoothingSpline(BSpline):
    penmax: float
    method: str
    target_df: int
    default_pen: float
    optimize: bool
    weights: Incomplete
    df_total: Incomplete
    N: Incomplete
    btb: Incomplete
    rank: Incomplete
    pen: Incomplete
    coef: Incomplete
    resid: Incomplete
    def fit(self, y, x: Incomplete | None = None, weights: Incomplete | None = None, pen: float = 0.0) -> None:
        '''
        Fit the smoothing spline to a set of (x,y) pairs.

        INPUTS:
           y       -- response variable
           x       -- if None, uses self.x
           weights -- optional array of weights
           pen     -- constant in front of Gram matrix

        OUTPUTS: None
           The smoothing spline is determined by self.coef,
           subsequent calls of __call__ will be the smoothing spline.

        ALGORITHM:
           Formally, this solves a minimization:

           fhat = ARGMIN_f SUM_i=1^n (y_i-f(x_i))^2 + pen * int f^(2)^2

           int is integral. pen is lambda (from Hastie)

           See Chapter 5 of

           Hastie, Tibshirani and Friedman (2001). "The Elements of Statistical
           Learning." Springer-Verlag. 536 pages.

           for more details.

        TODO:
           Should add arbitrary derivative penalty instead of just
           second derivative.
        '''
    def smooth(self, y, x: Incomplete | None = None, weights: Incomplete | None = None) -> None: ...
    def gcv(self):
        '''
        Generalized cross-validation score of current fit.

        Craven, P. and Wahba, G.  "Smoothing noisy data with spline functions.
        Estimating the correct degree of smoothing by
        the method of generalized cross-validation."
        Numerische Mathematik, 31(4), 377-403.
        '''
    def df_resid(self):
        """
        Residual degrees of freedom in the fit.

        self.N - self.trace()

        where self.N is the number of observations of last fit.
        """
    def df_fit(self):
        """
        How many degrees of freedom used in the fit?

        self.trace()
        """
    def trace(self):
        """
        Trace of the smoothing matrix S(pen)

        TODO: addin a reference to Wahba, and whoever else I used.
        """
    def fit_target_df(self, y, x: Incomplete | None = None, df: Incomplete | None = None, weights: Incomplete | None = None, tol: float = 0.001, apen: int = 0, bpen: float = 0.001) -> None:
        """
        Fit smoothing spline with approximately df degrees of freedom
        used in the fit, i.e. so that self.trace() is approximately df.

        Uses binary search strategy.

        In general, df must be greater than the dimension of the null space
        of the Gram inner product. For cubic smoothing splines, this means
        that df > 2.

        INPUTS:
           y       -- response variable
           x       -- if None, uses self.x
           df      -- target degrees of freedom
           weights -- optional array of weights
           tol     -- (relative) tolerance for convergence
           apen    -- lower bound of penalty for binary search
           bpen    -- upper bound of penalty for binary search

        OUTPUTS: None
           The smoothing spline is determined by self.coef,
           subsequent calls of __call__ will be the smoothing spline.
        """
    def fit_optimize_gcv(self, y, x: Incomplete | None = None, weights: Incomplete | None = None, tol: float = 0.001, brack=(-100, 20)):
        """
        Fit smoothing spline trying to optimize GCV.

        Try to find a bracketing interval for scipy.optimize.golden
        based on bracket.

        It is probably best to use target_df instead, as it is
        sometimes difficult to find a bracketing interval.

        INPUTS:
           y       -- response variable
           x       -- if None, uses self.x
           df      -- target degrees of freedom
           weights -- optional array of weights
           tol     -- (relative) tolerance for convergence
           brack   -- an initial guess at the bracketing interval

        OUTPUTS: None
           The smoothing spline is determined by self.coef,
           subsequent calls of __call__ will be the smoothing spline.
        """

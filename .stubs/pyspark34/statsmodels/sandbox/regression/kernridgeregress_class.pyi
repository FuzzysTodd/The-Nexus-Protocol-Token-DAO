from _typeshed import Incomplete

def kernel_rbf(x, y, scale: int = 1, **kwds): ...
def kernel_euclid(x, y, p: int = 2, **kwds): ...

class GaussProcess:
    """class to perform kernel ridge regression (gaussian process)

    Warning: this class is memory intensive, it creates nobs x nobs distance
    matrix and its inverse, where nobs is the number of rows (observations).
    See sparse version for larger number of observations


    Notes
    -----

    Todo:
    * normalize multidimensional x array on demand, either by var or cov
    * add confidence band
    * automatic selection or proposal of smoothing parameters

    Note: this is different from kernel smoothing regression,
       see for example https://en.wikipedia.org/wiki/Kernel_smoother

    In this version of the kernel ridge regression, the training points
    are fitted exactly.
    Needs a fast version for leave-one-out regression, for fitting each
    observation on all the other points.
    This version could be numerically improved for the calculation for many
    different values of the ridge coefficient. see also short summary by
    Isabelle Guyon (ETHZ) in a manuscript KernelRidge.pdf

    Needs verification and possibly additional statistical results or
    summary statistics for interpretation, but this is a problem with
    non-parametric, non-linear methods.

    Reference
    ---------

    Rasmussen, C.E. and C.K.I. Williams, 2006, Gaussian Processes for Machine
    Learning, the MIT Press, www.GaussianProcess.org/gpal, chapter 2

    a short summary of the kernel ridge regression is at
    http://www.ics.uci.edu/~welling/teaching/KernelsICS273B/Kernel-Ridge.pdf
    """
    x: Incomplete
    kernel: Incomplete
    scale: Incomplete
    ridgecoeff: Incomplete
    distxsample: Incomplete
    Kinv: Incomplete
    y: Incomplete
    yest: Incomplete
    def __init__(self, x, y: Incomplete | None = None, kernel=..., scale: float = 0.5, ridgecoeff: float = 1e-10, **kwds) -> None:
        """
        Parameters
        ----------
        x : 2d array (N,K)
           data array of explanatory variables, columns represent variables
           rows represent observations
        y : 2d array (N,1) (optional)
           endogenous variable that should be fitted or predicted
           can alternatively be specified as parameter to fit method
        kernel : function, default: kernel_rbf
           kernel: (x1,x2)->kernel matrix is a function that takes as parameter
           two column arrays and return the kernel or distance matrix
        scale : float (optional)
           smoothing parameter for the rbf kernel
        ridgecoeff : float (optional)
           coefficient that is multiplied with the identity matrix in the
           ridge regression

        Notes
        -----
        After initialization, kernel matrix is calculated and if y is given
        as parameter then also the linear regression parameter and the
        fitted or estimated y values, yest, are calculated. yest is available
        as an attribute in this case.

        Both scale and the ridge coefficient smooth the fitted curve.

        """
    parest: Incomplete
    def fit(self, y):
        """fit the training explanatory variables to a sample ouput variable"""
    xpredict: Incomplete
    ypredict: Incomplete
    def predict(self, x):
        """predict new y values for a given array of explanatory variables"""
    def plot(self, y, plt=...) -> None:
        """some basic plots"""

def example1() -> None: ...
def example2(m: int = 100, scale: float = 0.01, stride: int = 2) -> None: ...

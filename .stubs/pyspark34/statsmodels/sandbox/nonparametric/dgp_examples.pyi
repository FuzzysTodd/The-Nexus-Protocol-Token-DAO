from _typeshed import Incomplete

def fg1(x):
    """Fan and Gijbels example function 1

    """
def fg1eu(x):
    """Eubank similar to Fan and Gijbels example function 1

    """
def fg2(x):
    """Fan and Gijbels example function 2

    """
def func1(x):
    """made up example with sin, square

    """

doc: Incomplete

class _UnivariateFunction:
    __doc__: str
    x: Incomplete
    y_true: Incomplete
    y: Incomplete
    def __init__(self, nobs: int = 200, x: Incomplete | None = None, distr_x: Incomplete | None = None, distr_noise: Incomplete | None = None) -> None: ...
    def plot(self, scatter: bool = True, ax: Incomplete | None = None):
        """plot the mean function and optionally the scatter of the sample

        Parameters
        ----------
        scatter : bool
            If true, then add scatterpoints of sample to plot.
        ax : None or matplotlib axis instance
            If None, then a matplotlib.pyplot figure is created, otherwise
            the given axis, ax, is used.

        Returns
        -------
        Figure
            This is either the created figure instance or the one associated
            with ax if ax is given.

        """

class UnivariateFanGijbels1(_UnivariateFunction):
    __doc__: Incomplete
    s_x: float
    s_noise: float
    func: Incomplete
    def __init__(self, nobs: int = 200, x: Incomplete | None = None, distr_x: Incomplete | None = None, distr_noise: Incomplete | None = None) -> None: ...

class UnivariateFanGijbels2(_UnivariateFunction):
    __doc__: Incomplete
    s_x: float
    s_noise: float
    func: Incomplete
    def __init__(self, nobs: int = 200, x: Incomplete | None = None, distr_x: Incomplete | None = None, distr_noise: Incomplete | None = None) -> None: ...

class UnivariateFanGijbels1EU(_UnivariateFunction):
    """

    Eubank p.179f
    """
    s_noise: float
    func: Incomplete
    def __init__(self, nobs: int = 50, x: Incomplete | None = None, distr_x: Incomplete | None = None, distr_noise: Incomplete | None = None) -> None: ...

class UnivariateFunc1(_UnivariateFunction):
    """

    made up, with sin and quadratic trend
    """
    s_noise: float
    func: Incomplete
    def __init__(self, nobs: int = 200, x: Incomplete | None = None, distr_x: Incomplete | None = None, distr_noise: Incomplete | None = None) -> None: ...
    def het_scale(self, x): ...

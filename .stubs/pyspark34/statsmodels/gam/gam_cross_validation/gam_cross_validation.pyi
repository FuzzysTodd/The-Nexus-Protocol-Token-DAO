import abc
from _typeshed import Incomplete
from statsmodels.compat.python import with_metaclass as with_metaclass
from statsmodels.gam.smooth_basis import GenericSmoothers as GenericSmoothers, UnivariateGenericSmoother as UnivariateGenericSmoother

class BaseCV(Incomplete, metaclass=abc.ABCMeta):
    """
    BaseCV class. It computes the cross validation error of a given model.
    All the cross validation classes can be derived by this one
    (e.g. GamCV, LassoCV,...)
    """
    cv_iterator: Incomplete
    exog: Incomplete
    endog: Incomplete
    train_test_cv_indices: Incomplete
    def __init__(self, cv_iterator, endog, exog) -> None: ...
    def fit(self, **kwargs): ...

class MultivariateGAMCV(BaseCV):
    cost: Incomplete
    gam: Incomplete
    smoother: Incomplete
    exog_linear: Incomplete
    alphas: Incomplete
    cv_iterator: Incomplete
    def __init__(self, smoother, alphas, gam, cost, endog, exog, cv_iterator) -> None: ...

class BasePenaltiesPathCV(Incomplete):
    """
    Base class for cross validation over a grid of parameters.

    The best parameter is saved in alpha_cv

    This class is currently not used
    """
    alphas: Incomplete
    alpha_cv: Incomplete
    cv_error: Incomplete
    cv_std: Incomplete
    def __init__(self, alphas) -> None: ...
    def plot_path(self) -> None: ...

class MultivariateGAMCVPath:
    """k-fold cross-validation for GAM

    Warning: The API of this class is preliminary and will change.

    Parameters
    ----------
    smoother : additive smoother instance
    alphas : list of iteratables
        list of alpha for smooths. The product space will be used as alpha
        grid for cross-validation
    gam : model class
        model class for creating a model with k-fole training data
    cost : function
        cost function for the prediction error
    endog : ndarray
        dependent (response) variable of the model
    cv_iterator : instance of cross-validation iterator
    """
    cost: Incomplete
    smoother: Incomplete
    gam: Incomplete
    alphas: Incomplete
    alphas_grid: Incomplete
    endog: Incomplete
    exog: Incomplete
    cv_iterator: Incomplete
    cv_error: Incomplete
    cv_std: Incomplete
    alpha_cv: Incomplete
    def __init__(self, smoother, alphas, gam, cost, endog, exog, cv_iterator) -> None: ...
    def fit(self, **kwargs): ...

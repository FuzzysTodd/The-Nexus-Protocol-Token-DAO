from ..base import BaseEstimator as BaseEstimator, MetaEstimatorMixin as MetaEstimatorMixin, clone as clone, is_classifier as is_classifier, is_regressor as is_regressor
from ..utils import Bunch as Bunch, check_random_state as check_random_state, deprecated as deprecated
from ..utils.metaestimators import _BaseComposition
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

class BaseEnsemble(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):
    '''Base class for all ensemble classes.

    Warning: This class should not be used directly. Use derived classes
    instead.

    Parameters
    ----------
    estimator : object
        The base estimator from which the ensemble is built.

    n_estimators : int, default=10
        The number of estimators in the ensemble.

    estimator_params : list of str, default=tuple()
        The list of attributes to use as parameters when instantiating a
        new base estimator. If none are given, default parameters are used.

    base_estimator : object, default="deprecated"
        Use `estimator` instead.

        .. deprecated:: 1.2
            `base_estimator` is deprecated and will be removed in 1.4.
            Use `estimator` instead.

    Attributes
    ----------
    estimator_ : estimator
        The base estimator from which the ensemble is grown.

    base_estimator_ : estimator
        The base estimator from which the ensemble is grown.

        .. deprecated:: 1.2
            `base_estimator_` is deprecated and will be removed in 1.4.
            Use `estimator_` instead.

    estimators_ : list of estimators
        The collection of fitted base estimators.
    '''
    estimator: Incomplete
    n_estimators: Incomplete
    estimator_params: Incomplete
    base_estimator: Incomplete
    @abstractmethod
    def __init__(self, estimator: Incomplete | None = None, *, n_estimators: int = 10, estimator_params=..., base_estimator: str = 'deprecated'): ...
    @property
    def base_estimator_(self):
        """Estimator used to grow the ensemble."""
    def __len__(self) -> int:
        """Return the number of estimators in the ensemble."""
    def __getitem__(self, index):
        """Return the index'th estimator in the ensemble."""
    def __iter__(self):
        """Return iterator over estimators in the ensemble."""

class _BaseHeterogeneousEnsemble(MetaEstimatorMixin, _BaseComposition, metaclass=ABCMeta):
    """Base class for heterogeneous ensemble of learners.

    Parameters
    ----------
    estimators : list of (str, estimator) tuples
        The ensemble of estimators to use in the ensemble. Each element of the
        list is defined as a tuple of string (i.e. name of the estimator) and
        an estimator instance. An estimator can be set to `'drop'` using
        `set_params`.

    Attributes
    ----------
    estimators_ : list of estimators
        The elements of the estimators parameter, having been fitted on the
        training data. If an estimator has been set to `'drop'`, it will not
        appear in `estimators_`.
    """
    @property
    def named_estimators(self):
        """Dictionary to access any fitted sub-estimators by name.

        Returns
        -------
        :class:`~sklearn.utils.Bunch`
        """
    estimators: Incomplete
    @abstractmethod
    def __init__(self, estimators): ...
    def set_params(self, **params):
        """
        Set the parameters of an estimator from the ensemble.

        Valid parameter keys can be listed with `get_params()`. Note that you
        can directly set the parameters of the estimators contained in
        `estimators`.

        Parameters
        ----------
        **params : keyword arguments
            Specific parameters using e.g.
            `set_params(parameter_name=new_value)`. In addition, to setting the
            parameters of the estimator, the individual estimator of the
            estimators can also be set, or can be removed by setting them to
            'drop'.

        Returns
        -------
        self : object
            Estimator instance.
        """
    def get_params(self, deep: bool = True):
        """
        Get the parameters of an estimator from the ensemble.

        Returns the parameters given in the constructor as well as the
        estimators contained within the `estimators` parameter.

        Parameters
        ----------
        deep : bool, default=True
            Setting it to True gets the various estimators and the parameters
            of the estimators as well.

        Returns
        -------
        params : dict
            Parameter and estimator names mapped to their values or parameter
            names mapped to their values.
        """

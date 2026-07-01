import numpy
from optuna.distributions import BaseDistribution as BaseDistribution, CategoricalDistribution as CategoricalDistribution, DiscreteUniformDistribution as DiscreteUniformDistribution, IntLogUniformDistribution as IntLogUniformDistribution, IntUniformDistribution as IntUniformDistribution, LogUniformDistribution as LogUniformDistribution, UniformDistribution as UniformDistribution
from typing import Any, Dict, List

class _SearchSpaceTransform:
    """Transform a search space and parameter configurations to continuous space.

    The search space bounds and parameter configurations are represented as ``numpy.ndarray``s and
    transformed into continuous space. Bounds and parameters associated with categorical
    distributions are one-hot encoded. Parameter configurations in this space can additionally be
    untransformed, or mapped back to the original space. This type of
    transformation/untransformation is useful for e.g. implementing samplers without having to
    condition on distribution types before sampling parameter values.

    Args:
        search_space:
            The search space. If any transformations are to be applied, parameter configurations
            are assumed to hold parameter values for all of the distributions defined in this
            search space. Otherwise, assertion failures will be raised.
        transform_log:
            If :obj:`True`, apply log/exp operations to the bounds and parameters with
            corresponding distributions in log space during transformation/untransformation.
            Should always be :obj:`True` if any parameters are going to be sampled from the
            transformed space.
        transform_step:
            If :obj:`True`, offset the lower and higher bounds by a half step each, increasing the
            space by one step. This allows fair sampling for values close to the bounds.
            Should always be :obj:`True` if any parameters are going to be sampled from the
            transformed space.

    Attributes:
        bounds:
            Constructed bounds from the given search space.
        column_to_encoded_columns:
            Constructed mapping from original parameter column index to encoded column indices.
        encoded_column_to_column:
            Constructed mapping from encoded column index to original parameter column index.

    Note:
        Parameter values are not scaled to the unit cube.

    Note:
        ``transform_log`` and ``transform_step`` are useful for constructing bounds and parameters
        without any actual transformations by setting those arguments to :obj:`False`. This is
        needed for e.g. the hyperparameter importance assessments.

    """
    def __init__(self, search_space: Dict[str, BaseDistribution], transform_log: bool = True, transform_step: bool = True) -> None: ...
    @property
    def bounds(self) -> numpy.ndarray: ...
    @property
    def column_to_encoded_columns(self) -> List[numpy.ndarray]: ...
    @property
    def encoded_column_to_column(self) -> numpy.ndarray: ...
    def transform(self, params: Dict[str, Any]) -> numpy.ndarray:
        """Transform a parameter configuration from actual values to continuous space.

        Args:
            params:
                A parameter configuration to transform.

        Returns:
            A 1-dimensional ``numpy.ndarray`` holding the transformed parameters in the
            configuration.

        """
    def untransform(self, trans_params: numpy.ndarray) -> Dict[str, Any]:
        """Untransform a parameter configuration from continuous space to actual values.

        Args:
            trans_params:
                A 1-dimensional ``numpy.ndarray`` in the transformed space corresponding to a
                parameter configuration.

        Returns:
            A dictionary of an untransformed parameter configuration. Keys are parameter names.
            Values are untransformed parameter values.

        """

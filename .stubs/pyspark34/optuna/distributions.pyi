import abc
from _typeshed import Incomplete
from typing import Any, Sequence

CategoricalChoiceType = None | bool | int | float | str

class BaseDistribution(metaclass=abc.ABCMeta):
    """Base class for distributions.

    Note that distribution classes are not supposed to be called by library users.
    They are used by :class:`~optuna.trial.Trial` and :class:`~optuna.samplers` internally.
    """
    def to_external_repr(self, param_value_in_internal_repr: float) -> Any:
        """Convert internal representation of a parameter value into external representation.

        Args:
            param_value_in_internal_repr:
                Optuna's internal representation of a parameter value.

        Returns:
            Optuna's external representation of a parameter value.
        """
    def to_internal_repr(self, param_value_in_external_repr: Any) -> float:
        """Convert external representation of a parameter value into internal representation.

        Args:
            param_value_in_external_repr:
                Optuna's external representation of a parameter value.

        Returns:
            Optuna's internal representation of a parameter value.
        """
    @abc.abstractmethod
    def single(self) -> bool:
        """Test whether the range of this distribution contains just a single value.

        Returns:
            :obj:`True` if the range of this distribution contains just a single value,
            otherwise :obj:`False`.
        """
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class UniformDistribution(BaseDistribution):
    """A uniform distribution in the linear domain.

    This object is instantiated by :func:`~optuna.trial.Trial.suggest_uniform`, and passed to
    :mod:`~optuna.samplers` in general.

    Attributes:
        low:
            Lower endpoint of the range of the distribution. ``low`` is included in the range.
        high:
            Upper endpoint of the range of the distribution. ``high`` is included from the range.

    Raises:
        ValueError:
            If ``low`` value is larger than ``high`` value.
    """
    low: Incomplete
    high: Incomplete
    def __init__(self, low: float, high: float) -> None: ...
    def single(self) -> bool: ...

class LogUniformDistribution(BaseDistribution):
    """A uniform distribution in the log domain.

    This object is instantiated by :func:`~optuna.trial.Trial.suggest_float` with ``log=True``
    and :func:`~optuna.trial.Trial.suggest_loguniform`, and passed to
    :mod:`~optuna.samplers` in general.

    Attributes:
        low:
            Lower endpoint of the range of the distribution. ``low`` is included in the range.
        high:
            Upper endpoint of the range of the distribution. ``high`` is included from the range.

    Raises:
        ValueError:
            If ``low`` value is larger than ``high`` value, or ``low`` value is smaller than or
            equal to 0.
    """
    low: Incomplete
    high: Incomplete
    def __init__(self, low: float, high: float) -> None: ...
    def single(self) -> bool: ...

class DiscreteUniformDistribution(BaseDistribution):
    """A discretized uniform distribution in the linear domain.

    This object is instantiated by :func:`~optuna.trial.Trial.suggest_uniform` with ``step``
    argument and :func:`~optuna.trial.Trial.suggest_discrete_uniform`, and passed
    to :mod:`~optuna.samplers` in general.

    .. note::
        If the range :math:`[\\mathsf{low}, \\mathsf{high}]` is not divisible by :math:`q`,
        :math:`\\mathsf{high}` will be replaced with the maximum of :math:`k q + \\mathsf{low}
        < \\mathsf{high}`, where :math:`k` is an integer.

    Attributes:
        low:
            Lower endpoint of the range of the distribution. ``low`` is included in the range.
        high:
            Upper endpoint of the range of the distribution. ``high`` is included in the range.
        q:
            A discretization step.

    Raises:
        ValueError:
            If ``low`` value is larger than ``high`` value.
    """
    low: Incomplete
    high: Incomplete
    q: Incomplete
    def __init__(self, low: float, high: float, q: float) -> None: ...
    def single(self) -> bool: ...

class IntUniformDistribution(BaseDistribution):
    """A uniform distribution on integers.

    This object is instantiated by :func:`~optuna.trial.Trial.suggest_int`, and passed to
    :mod:`~optuna.samplers` in general.

    .. note::
        If the range :math:`[\\mathsf{low}, \\mathsf{high}]` is not divisible by
        :math:`\\mathsf{step}`, :math:`\\mathsf{high}` will be replaced with the maximum of
        :math:`k \\times \\mathsf{step} + \\mathsf{low} < \\mathsf{high}`, where :math:`k` is
        an integer.

    Attributes:
        low:
            Lower endpoint of the range of the distribution. ``low`` is included in the range.
        high:
            Upper endpoint of the range of the distribution. ``high`` is included in the range.
        step:
            A step for spacing between values.

    Raises:
        ValueError:
            If ``low`` value is larger than ``high`` value, or ``step`` value is smaller or
            equal to 0.
    """
    low: Incomplete
    high: Incomplete
    step: Incomplete
    def __init__(self, low: int, high: int, step: int = 1) -> None: ...
    def to_external_repr(self, param_value_in_internal_repr: float) -> int: ...
    def to_internal_repr(self, param_value_in_external_repr: int) -> float: ...
    def single(self) -> bool: ...

class IntLogUniformDistribution(BaseDistribution):
    """A uniform distribution on integers in the log domain.

    This object is instantiated by :func:`~optuna.trial.Trial.suggest_int`, and passed to
    :mod:`~optuna.samplers` in general.

    Attributes:
        low:
            Lower endpoint of the range of the distribution. ``low`` is included in the range.
        high:
            Upper endpoint of the range of the distribution. ``high`` is included in the range.
        step:
            A step for spacing between values.

            .. warning::
                Deprecated in v2.0.0. ``step`` argument will be removed in the future.
                The removal of this feature is currently scheduled for v4.0.0,
                but this schedule is subject to change.

                Samplers and other components in Optuna relying on this distribution will ignore
                this value and assume that ``step`` is always 1.
                User-defined samplers may continue to use other values besides 1 during the
                deprecation.

    Raises:
        ValueError:
            If ``low`` value is larger than ``high`` value, or ``low`` value is smaller than 1.
    """
    low: Incomplete
    high: Incomplete
    def __init__(self, low: int, high: int, step: int = 1) -> None: ...
    def to_external_repr(self, param_value_in_internal_repr: float) -> int: ...
    def to_internal_repr(self, param_value_in_external_repr: int) -> float: ...
    def single(self) -> bool: ...
    @property
    def step(self) -> int: ...
    @step.setter
    def step(self, value: int) -> None: ...

class CategoricalDistribution(BaseDistribution):
    """A categorical distribution.

    This object is instantiated by :func:`~optuna.trial.Trial.suggest_categorical`, and
    passed to :mod:`~optuna.samplers` in general.

    Args:
        choices:
            Parameter value candidates.

    .. note::

        Not all types are guaranteed to be compatible with all storages. It is recommended to
        restrict the types of the choices to :obj:`None`, :class:`bool`, :class:`int`,
        :class:`float` and :class:`str`.

    Attributes:
        choices:
            Parameter value candidates.

    Raises:
        ValueError:
            If ``choices`` do not contain any elements.
    """
    choices: Incomplete
    def __init__(self, choices: Sequence[CategoricalChoiceType]) -> None: ...
    def to_external_repr(self, param_value_in_internal_repr: float) -> CategoricalChoiceType: ...
    def to_internal_repr(self, param_value_in_external_repr: CategoricalChoiceType) -> float: ...
    def single(self) -> bool: ...

DISTRIBUTION_CLASSES: Incomplete

def json_to_distribution(json_str: str) -> BaseDistribution:
    """Deserialize a distribution in JSON format.

    Args:
        json_str: A JSON-serialized distribution.

    Returns:
        A deserialized distribution.

    Raises:
        ValueError:
            If the unknown class is specified.
    """
def distribution_to_json(dist: BaseDistribution) -> str:
    """Serialize a distribution to JSON format.

    Args:
        dist: A distribution to be serialized.

    Returns:
        A JSON string of a given distribution.

    """
def check_distribution_compatibility(dist_old: BaseDistribution, dist_new: BaseDistribution) -> None:
    """A function to check compatibility of two distributions.

    Note that this method is not supposed to be called by library users.

    Args:
        dist_old: A distribution previously recorded in storage.
        dist_new: A distribution newly added to storage.

    Raises:
        ValueError:
            If different distribution kinds are set to ``dist_old`` and ``dist_new``,
            or ``dist_old.choices`` doesn't match ``dist_new.choices``
            for :class:`~optuna.distributions.CategoricalDistribution`.
    """

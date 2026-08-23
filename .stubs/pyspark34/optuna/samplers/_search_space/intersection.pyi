from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.study import BaseStudy as BaseStudy
from typing import Dict

class IntersectionSearchSpace:
    """A class to calculate the intersection search space of a :class:`~optuna.study.BaseStudy`.

    Intersection search space contains the intersection of parameter distributions that have been
    suggested in the completed trials of the study so far.
    If there are multiple parameters that have the same name but different distributions,
    neither is included in the resulting search space
    (i.e., the parameters with dynamic value ranges are excluded).

    Note that an instance of this class is supposed to be used for only one study.
    If different studies are passed to :func:`~optuna.samplers.IntersectionSearchSpace.calculate`,
    a :obj:`ValueError` is raised.

    Args:
        include_pruned:
            Whether pruned trials should be included in the search space.
    """
    def __init__(self, include_pruned: bool = False) -> None: ...
    def calculate(self, study: BaseStudy, ordered_dict: bool = False) -> Dict[str, BaseDistribution]:
        """Returns the intersection search space of the :class:`~optuna.study.BaseStudy`.

        Args:
            study:
                A study with completed trials.
            ordered_dict:
                A boolean flag determining the return type.
                If :obj:`False`, the returned object will be a :obj:`dict`.
                If :obj:`True`, the returned object will be an :obj:`collections.OrderedDict`
                sorted by keys, i.e. parameter names.

        Returns:
            A dictionary containing the parameter names and parameter's distributions.

        Raises:
            ValueError:
                If different studies are passed into this method.
        """

def intersection_search_space(study: BaseStudy, ordered_dict: bool = False, include_pruned: bool = False) -> Dict[str, BaseDistribution]:
    """Return the intersection search space of the :class:`~optuna.study.BaseStudy`.

    Intersection search space contains the intersection of parameter distributions that have been
    suggested in the completed trials of the study so far.
    If there are multiple parameters that have the same name but different distributions,
    neither is included in the resulting search space
    (i.e., the parameters with dynamic value ranges are excluded).

    .. note::
        :class:`~optuna.samplers.IntersectionSearchSpace` provides the same functionality with
        a much faster way. Please consider using it if you want to reduce execution time
        as much as possible.

    Args:
        study:
            A study with completed trials.
        ordered_dict:
            A boolean flag determining the return type.
            If :obj:`False`, the returned object will be a :obj:`dict`.
            If :obj:`True`, the returned object will be an :obj:`collections.OrderedDict` sorted by
            keys, i.e. parameter names.
        include_pruned:
            Whether pruned trials should be included in the search space.

    Returns:
        A dictionary containing the parameter names and parameter's distributions.
    """

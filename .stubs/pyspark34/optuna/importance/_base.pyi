import abc
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.samplers import intersection_search_space as intersection_search_space
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from typing import Callable, Dict, List

class BaseImportanceEvaluator(metaclass=abc.ABCMeta):
    """Abstract parameter importance evaluator."""
    @abc.abstractmethod
    def evaluate(self, study: Study, params: List[str] | None = None, *, target: Callable[[FrozenTrial], float] | None = None) -> Dict[str, float]:
        """Evaluate parameter importances based on completed trials in the given study.

        .. note::

            This method is not meant to be called by library users.

        .. seealso::

            Please refer to :func:`~optuna.importance.get_param_importances` for how a concrete
            evaluator should implement this method.

        Args:
            study:
                An optimized study.
            params:
                A list of names of parameters to assess.
                If :obj:`None`, all parameters that are present in all of the completed trials are
                assessed.
            target:
                A function to specify the value to evaluate importances.
                If it is :obj:`None` and ``study`` is being used for single-objective optimization,
                the objective values are used. Can also be used for other trial attributes, such as
                the duration, like ``target=lambda t: t.duration.total_seconds()``.

                .. note::
                    Specify this argument if ``study`` is being used for multi-objective
                    optimization. For example, to get the hyperparameter importance of the first
                    objective, use ``target=lambda t: t.values[0]`` for the target parameter.

        Returns:
            An :class:`collections.OrderedDict` where the keys are parameter names and the values
            are assessed importances.

        Raises:
            :exc:`ValueError`:
                If ``target`` is :obj:`None` and ``study`` is being used for multi-objective
                optimization.
        """

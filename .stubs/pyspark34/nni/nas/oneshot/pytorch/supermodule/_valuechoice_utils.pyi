import numpy as np
import torch
from nni.common.hpo_utils import ParameterSpec
from nni.nas.nn.pytorch.choice import ChoiceOf, ValueChoiceX
from typing import Any, Sequence, TypeVar

__all__ = ['dedup_inner_choices', 'evaluate_value_choice_with_dict', 'traverse_all_options', 'weighted_sum', 'evaluate_constant']

Choice = Any
T = TypeVar('T')

def dedup_inner_choices(value_choices: list[ValueChoiceX]) -> dict[str, ParameterSpec]:
    """Find all leaf nodes in ``value_choices``,
    save them into in the format of ``{label: parameter_spec}``.
    """
def evaluate_value_choice_with_dict(value_choice: ChoiceOf[T], chosen: dict[str, Choice]) -> T:
    '''To evaluate a composition of value-choice with a dict,
    with format of ``{label: chosen_value}``.
    The implementation is two-pass. We first get a list of values,
    then feed the values into ``value_choice.evaluate``.
    This can be potentially optimized in terms of speed.

    Examples
    --------
    >>> chosen = {"exp_ratio": 3}
    >>> evaluate_value_choice_with_dict(value_choice_in, chosen)
    48
    >>> evaluate_value_choice_with_dict(value_choice_out, chosen)
    96
    '''
def traverse_all_options(value_choice: ChoiceOf[T], weights: dict[str, list[float]] | dict[str, np.ndarray] | dict[str, torch.Tensor] | None = None) -> list[tuple[T, float]] | list[T]:
    """Traverse all possible computation outcome of a value choice.
    If ``weights`` is not None, it will also compute the probability of each possible outcome.

    Parameters
    ----------
    value_choice : ValueChoiceX
        The value choice to traverse.
    weights : Optional[dict[str, list[float]]], default = None
        If there's a prior on leaf nodes, and we intend to know the (joint) prior on results,
        weights can be provided. The key is label, value are list of float indicating probability.
        Normally, they should sum up to 1, but we will not check them in this function.

    Returns
    -------
    list[Union[tuple[Any, float], Any]]
        Results will be sorted and duplicates will be eliminated.
        If weights is provided, the return value will be a list of tuple, with option and its weight.
        Otherwise, it will be a list of options.
    """
def evaluate_constant(expr: Any) -> Any:
    """Evaluate a value choice expression to a constant. Raise ValueError if it's not a constant."""
def weighted_sum(items: list[T], weights: Sequence[float | None] = ...) -> T:
    """Return a weighted sum of items.

    Items can be list of tensors, numpy arrays, or nested lists / dicts.

    If ``weights`` is None, this is simply an unweighted sum.
    """

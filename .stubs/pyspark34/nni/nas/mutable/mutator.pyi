from _typeshed import Incomplete
from nni.nas.execution import Model
from typing import Any, Iterable, List, Tuple

__all__ = ['Sampler', 'Mutator', 'InvalidMutation']

Choice = Any

class Sampler:
    """
    Handles `Mutator.choice()` calls.
    """
    def choice(self, candidates: List[Choice], mutator: Mutator, model: Model, index: int) -> Choice: ...
    def mutation_start(self, mutator: Mutator, model: Model) -> None: ...
    def mutation_end(self, mutator: Mutator, model: Model) -> None: ...

class Mutator:
    """
    Mutates graphs in model to generate new model.
    `Mutator` class will be used in two places:

    1. Inherit `Mutator` to implement graph mutation logic.
    2. Use `Mutator` subclass to implement NAS strategy.

    In scenario 1, the subclass should implement `Mutator.mutate()` interface with `Mutator.choice()`.
    In scenario 2, strategy should use constructor or `Mutator.bind_sampler()` to initialize subclass,
    and then use `Mutator.apply()` to mutate model.
    For certain mutator subclasses, strategy or sampler can use `Mutator.dry_run()` to predict choice candidates.
    # Method names are open for discussion.

    If mutator has a label, in most cases, it means that this mutator is applied to nodes with this label.
    """
    sampler: Incomplete
    label: Incomplete
    def __init__(self, sampler: Sampler | None = None, label: str = ...) -> None: ...
    def bind_sampler(self, sampler: Sampler) -> Mutator:
        """
        Set the sampler which will handle `Mutator.choice` calls.
        """
    def apply(self, model: Model) -> Model:
        """
        Apply this mutator on a model.
        Returns mutated model.
        The model will be copied before mutation and the original model will not be modified.
        """
    def dry_run(self, model: Model) -> Tuple[List[List[Choice]], Model]:
        """
        Dry run mutator on a model to collect choice candidates.
        If you invoke this method multiple times on same or different models,
        it may or may not return identical results, depending on how the subclass implements `Mutator.mutate()`.
        """
    def mutate(self, model: Model) -> None:
        """
        Abstract method to be implemented by subclass.
        Mutate a model in place.
        """
    def choice(self, candidates: Iterable[Choice]) -> Choice:
        """
        Ask sampler to make a choice.
        """

class _RecorderSampler(Sampler):
    recorded_candidates: Incomplete
    def __init__(self) -> None: ...
    def choice(self, candidates: List[Choice], *args) -> Choice: ...

class InvalidMutation(Exception): ...

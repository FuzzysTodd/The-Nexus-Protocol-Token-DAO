import abc
from typing import Any, Callable

__all__ = ['Evaluator']

class Evaluator(abc.ABC, metaclass=abc.ABCMeta):
    """
    Evaluator of a model. An evaluator should define where the training code is, and the configuration of
    training code. The configuration includes basic runtime information trainer needs to know (such as number of GPUs)
    or tune-able parameters (such as learning rate), depending on the implementation of training code.

    Each config should define how it is interpreted in ``_execute()``, taking only one argument which is the mutated model class.
    For example, functional evaluator might directly import the function and call the function.
    """
    def evaluate(self, model_cls: Callable[[], Any] | Any) -> Any:
        """To run evaluation of a model. The model could be either a concrete model or a callable returning a model.

        The concrete implementation of evaluate depends on the implementation of ``_execute()`` in sub-class.
        """
    @abc.abstractmethod
    def __eq__(self, other) -> bool: ...

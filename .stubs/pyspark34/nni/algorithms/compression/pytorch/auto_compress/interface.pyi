import abc
from abc import ABC, abstractmethod
from torch.nn import Module as Module
from torch.optim import Optimizer
from typing import Callable, Iterable

class BaseAutoCompressionEngine(ABC, metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def trial_execute_compress(cls):
        """
        Execute the compressing trial.
        """

class AbstractAutoCompressionModule(ABC, metaclass=abc.ABCMeta):
    """
    The abstract container that user need to implement.
    """
    @classmethod
    @abstractmethod
    def model(cls) -> Module:
        """
        Returns
        -------
        torch.nn.Module
            Model to be compress.
        """
    @classmethod
    @abstractmethod
    def evaluator(cls) -> Callable[[Module], float]:
        """
        Returns
        -------
        function
            The function used to evaluate the compressed model, return a scalar.
        """
    @classmethod
    @abstractmethod
    def optimizer_factory(cls) -> Callable[[Iterable], Optimizer] | None:
        """
        Returns
        -------
        Optional[Callable[[Iterable], Optimizer]]
            Optimizer factory function. Input is a iterable value, i.e. `model.parameters()`.
            Output is the `torch.optim.Optimizer` instance.
        """
    @classmethod
    @abstractmethod
    def criterion(cls) -> Callable | None:
        """
        Returns
        -------
        Optional[Callable]
            The criterion function used to train the model.
        """
    @classmethod
    @abstractmethod
    def sparsifying_trainer(cls, compress_algorithm_name: str) -> Callable[[Module, Optimizer, Callable, int], None] | None:
        """
        The trainer is used in sparsifying process.

        Parameters
        ----------
        compress_algorithm_name: str
            The name of pruner and quantizer, i.e. 'level', 'l1', 'qat'.

        Returns
        -------
        Optional[Callable[[Module, Optimizer, Callable, int], None]]
            Used to train model in compress stage, include `model, optimizer, criterion, current_epoch` as function arguments.
        """
    @classmethod
    @abstractmethod
    def post_compress_finetuning_trainer(cls, compress_algorithm_name: str) -> Callable[[Module, Optimizer, Callable, int], None] | None:
        """
        The trainer is used in post-compress finetuning process.

        Parameters
        ----------
        compress_algorithm_name: str
            The name of pruner and quantizer, i.e. 'level', 'l1', 'qat'.

        Returns
        -------
        Optional[Callable[[Module, Optimizer, Callable, int], None]]
            Used to train model in finetune stage, include `model, optimizer, criterion, current_epoch` as function arguments.
        """
    @classmethod
    @abstractmethod
    def post_compress_finetuning_epochs(cls, compress_algorithm_name: str) -> int:
        """
        The epochs in post-compress finetuning process.

        Parameters
        ----------
        compress_algorithm_name: str
            The name of pruner and quantizer, i.e. 'level', 'l1', 'qat'.

        Returns
        -------
        int
            The finetuning epoch number.
        """

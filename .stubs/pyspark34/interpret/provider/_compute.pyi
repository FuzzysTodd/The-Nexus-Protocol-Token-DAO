import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod

class ComputeProvider(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def parallel(self, compute_fn, compute_args_iter): ...

class JobLibProvider(ComputeProvider):
    n_jobs: Incomplete
    def __init__(self, n_jobs: int = -1) -> None: ...
    def parallel(self, compute_fn, compute_args_iter): ...

class AzureMLProvider(ComputeProvider):
    def parallel(self, compute_fn, compute_args_iter) -> None: ...

import abc
from nni.nas.execution.common import Model as Model
from nni.nas.mutable import Mutator as Mutator
from typing import Any, List

class BaseStrategy(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, base_model: Model, applied_mutators: List[Mutator]) -> None: ...
    def export_top_models(self, top_k: int) -> List[Any]: ...

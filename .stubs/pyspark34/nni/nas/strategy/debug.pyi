from .base import BaseStrategy as BaseStrategy
from nni.nas import Sampler as Sampler, utils as utils
from nni.nas.execution.common import get_mutation_summary as get_mutation_summary
from nni.nas.execution.pytorch import codegen as codegen
from nni.nas.execution.pytorch.graph import BaseGraphData as BaseGraphData

class ChooseFirstSampler(Sampler):
    def choice(self, candidates, mutator, model, index): ...

class _LocalDebugStrategy(BaseStrategy):
    """
    This class is supposed to be used internally, for debugging trial mutation
    """
    def run_one_model(self, model) -> None: ...
    def run(self, base_model, applied_mutators) -> None: ...

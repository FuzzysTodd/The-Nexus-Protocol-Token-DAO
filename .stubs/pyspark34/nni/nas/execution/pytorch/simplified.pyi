import torch.nn as nn
from .graph import BaseExecutionEngine as BaseExecutionEngine
from _typeshed import Incomplete
from nni.nas.evaluator import Evaluator as Evaluator
from nni.nas.execution.common import Model as Model, get_mutation_dict as get_mutation_dict, mutation_dict_to_summary as mutation_dict_to_summary, receive_trial_parameters as receive_trial_parameters
from nni.nas.utils import ContextStack as ContextStack
from typing import Any, Dict, Type

class PythonGraphData:
    class_: Incomplete
    init_parameters: Incomplete
    mutation: Incomplete
    evaluator: Incomplete
    mutation_summary: Incomplete
    def __init__(self, class_: Type[nn.Module], init_parameters: Dict[str, Any], mutation: Dict[str, Any], evaluator: Evaluator) -> None: ...
    def dump(self) -> dict: ...
    @staticmethod
    def load(data) -> PythonGraphData: ...

class PurePythonExecutionEngine(BaseExecutionEngine):
    """
    This is the execution engine that doesn't rely on Python-IR converter.

    We didn't explicitly state this independency for now. Front-end needs to decide which converter / no converter
    to use depending on the execution type. In the future, that logic may be moved into this execution engine.

    The execution engine needs to store the class path of base model, and init parameters to re-initialize the model
    with the mutation dict in the context, so that the mutable modules are created to be the fixed instance on the fly.
    """
    @classmethod
    def pack_model_data(cls, model: Model) -> Any: ...
    @classmethod
    def trial_execute_graph(cls) -> None: ...

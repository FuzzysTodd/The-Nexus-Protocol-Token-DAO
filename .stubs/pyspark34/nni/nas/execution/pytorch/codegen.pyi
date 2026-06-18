from _typeshed import Incomplete
from nni.nas.execution.common.graph import Model

__all__ = ['model_to_pytorch_script']

def model_to_pytorch_script(model: Model, placement: Incomplete | None = None) -> str: ...

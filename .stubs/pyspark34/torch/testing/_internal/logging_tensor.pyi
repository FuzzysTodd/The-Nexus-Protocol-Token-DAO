import contextlib
import logging
import torch
from _typeshed import Incomplete
from collections.abc import Generator
from torch.utils._python_dispatch import TorchDispatchMode as TorchDispatchMode
from torch.utils._pytree import tree_map as tree_map
from typing import Iterator, List

class LoggingTensor(torch.Tensor):
    elem: torch.Tensor
    context = contextlib.nullcontext
    __torch_function__: Incomplete
    @staticmethod
    def __new__(cls, elem, *args, **kwargs): ...
    @classmethod
    def __torch_dispatch__(cls, func, types, args=(), kwargs: Incomplete | None = None): ...

class LoggingTensorMode(TorchDispatchMode):
    def __torch_dispatch__(self, func, types, args=(), kwargs: Incomplete | None = None): ...

class LoggingTensorReentrant(LoggingTensor):
    context = torch.overrides.enable_reentrant_dispatch

class LoggingTensorHandler(logging.Handler):
    log_list: List[str]
    next_shortid: int
    use_shortid_for_all_tensors: Incomplete
    def __init__(self, log_list: List[str], use_shortid_for_all_tensors: bool) -> None: ...
    def emit(self, record) -> None: ...

def log_input(name: str, var: object): ...
def capture_logs(is_mode: bool = False) -> Iterator[List[str]]: ...
def capture_logs_with_logging_tensor_mode() -> Generator[Incomplete, None, None]: ...

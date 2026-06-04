from _typeshed import Incomplete
from collections.abc import Generator
from torch.backends import ContextProp as ContextProp, PropModule as PropModule

def is_available():
    """Returns whether PyTorch is built with MKL-DNN support."""

VERBOSE_OFF: int
VERBOSE_ON: int
VERBOSE_ON_CREATION: int

class verbose:
    """
    On-demand oneDNN (former MKL-DNN) verbosing functionality
    To make it easier to debug performance issues, oneDNN can dump verbose
    messages containing information like kernel size, input data size and
    execution duration while executing the kernel. The verbosing functionality
    can be invoked via an environment variable named `DNNL_VERBOSE`. However,
    this methodology dumps messages in all steps. Those are a large amount of
    verbose messages. Moreover, for investigating the performance issues,
    generally taking verbose messages for one single iteration is enough.
    This on-demand verbosing functionality makes it possible to control scope
    for verbose message dumping. In the following example, verbose messages
    will be dumped out for the second inference only.

    .. highlight:: python
    .. code-block:: python

        import torch
        model(data)
        with torch.backends.mkldnn.verbose(torch.backends.mkldnn.VERBOSE_ON):
            model(data)

    Args:
        level: Verbose level
            - ``VERBOSE_OFF``: Disable verbosing
            - ``VERBOSE_ON``:  Enable verbosing
            - ``VERBOSE_ON_CREATION``: Enable verbosing, including oneDNN kernel creation
    """
    level: Incomplete
    def __init__(self, level) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...

def set_flags(_enabled): ...
def flags(enabled: bool = False) -> Generator[None, None, None]: ...

class MkldnnModule(PropModule):
    def __init__(self, m, name) -> None: ...
    enabled: Incomplete

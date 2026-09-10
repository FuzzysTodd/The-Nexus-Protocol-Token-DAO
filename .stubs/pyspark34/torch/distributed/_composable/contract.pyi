from _typeshed import Incomplete
from torch.distributed._composable_state import _State
from typing import Type

class _StateKey(str):
    def __new__(cls, string: str = '__composable_api_state_key'): ...

STATE_KEY: Incomplete
REGISTRY_KEY: Incomplete

class RegistryItem: ...

def contract(state_cls: Type[_State] = ...):
    '''
    Decorate a function as a composable distributed API, where the first
    argument of the function must be an :class:`nn.Module` instance. The
    decorator verifies that the wrapped function does not modify parameter,
    buffer or sub-module fully-qualified names (FQN).

    When a function ``func`` is decorated by ``@contract()``, a
    ``.state(module: nn.Module)`` method will be installed to the decorated
    function. Then you can retrieve and modify the state on a module by calling
    ``func.state(module)``.

    Example::
        >>> # xdoctest: +SKIP
        >>> import torch.nn as nn
        >>>
        >>> class MyModel(nn.Module):
        >>>     def __init__(self):
        >>>         super().__init__()
        >>>         self.l1 = nn.Linear(10, 10)
        >>>         self.l2 = nn.Linear(10, 10)
        >>>
        >>>     def forward(self, x):
        >>>         return self.l2(self.l1(x))
        >>>
        >>> @contract()
        >>> def my_feature(module: nn.Module) -> nn.Module:
        >>>     my_feature.state(module).some_state = "any value"
        >>>     return module
        >>>
        >>> model = MyModel()
        >>> my_feature(model.l1)
        >>> assert my_feature.state(model.l1).some_state == "any value"
        >>> my_feature(model.l2)
        >>> model(torch.randn(2, 10)).sum().backward()
    '''

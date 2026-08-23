from _typeshed import Incomplete
from nni.nas.utils import ContextStack as ContextStack
from typing import Type

class FixedFactory:
    '''Make a model space ready to create a fixed model.

    Examples
    --------
    >>> factory = FixedFactory(ModelSpaceClass, {"choice1": 3})
    >>> model = factory(channels=16, classes=10)
    '''
    cls: Incomplete
    arch: Incomplete
    def __init__(self, cls: Type, arch: dict) -> None: ...
    def __call__(self, *init_args, **init_kwargs): ...

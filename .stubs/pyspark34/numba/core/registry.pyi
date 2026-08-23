from _typeshed import Incomplete
from collections.abc import Generator
from functools import cached_property as cached_property
from numba.core import cpu as cpu, dispatcher as dispatcher, typing as typing, utils as utils
from numba.core.descriptors import TargetDescriptor as TargetDescriptor

class _NestedContext:
    def nested(self, typing_context, target_context) -> Generator[None, None, None]: ...

class CPUTarget(TargetDescriptor):
    options: Incomplete
    @property
    def target_context(self):
        """
        The target context for CPU targets.
        """
    @property
    def typing_context(self):
        """
        The typing context for CPU targets.
        """
    def nested_context(self, typing_context, target_context):
        """
        A context manager temporarily replacing the contexts with the
        given ones, for the current thread of execution.
        """

cpu_target: Incomplete

class CPUDispatcher(dispatcher.Dispatcher):
    targetdescr = cpu_target

class DelayedRegistry(utils.UniqueDict):
    """
    A unique dictionary but with deferred initialisation of the values.

    Attributes
    ----------
    ondemand:

        A dictionary of key -> value, where value is executed
        the first time it is is used.  It is used for part of a deferred
        initialization strategy.
    """
    ondemand: Incomplete
    key_type: Incomplete
    value_type: Incomplete
    def __init__(self, *args, **kws) -> None: ...
    def __getitem__(self, item): ...
    def __setitem__(self, key, value) -> None: ...

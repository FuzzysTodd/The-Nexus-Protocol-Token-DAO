import abc
import weakref
from _typeshed import Incomplete
from numba.core import errors as errors

class RetargetCache:
    """Cache for retargeted dispatchers.

    The cache uses the original dispatcher as the key.
    """
    container_type = weakref.WeakKeyDictionary
    def __init__(self) -> None: ...
    def save_cache(self, orig_disp, new_disp) -> None:
        """Save a dispatcher associated with the given key.
        """
    def load_cache(self, orig_disp):
        """Load a dispatcher associated with the given key.
        """
    def items(self):
        """Returns the contents of the cache.
        """
    def stats(self):
        """Returns stats regarding cache hit/miss.
        """

class BaseRetarget(abc.ABC, metaclass=abc.ABCMeta):
    """Abstract base class for retargeting logic.
    """
    @abc.abstractmethod
    def check_compatible(self, orig_disp):
        """Check that the retarget is compatible.

        This method does not return anything meaningful (e.g. None)
        Incompatibility is signalled via raising an exception.
        """
    @abc.abstractmethod
    def retarget(self, orig_disp):
        """Retargets the given dispatcher and returns a new dispatcher-like
        callable. Or, returns the original dispatcher if the the target_backend
        will not change.
        """

class BasicRetarget(BaseRetarget, metaclass=abc.ABCMeta):
    """A basic retargeting implementation for a single output target.

    This class has two abstract methods/properties that subclasses must define.

    - `output_target` must return output target name.
    - `compile_retarget` must define the logic to retarget the given dispatcher.

    By default, this class uses `RetargetCache` as the internal cache. This
    can be modified by overriding the `.cache_type` class attribute.

    """
    cache_type = RetargetCache
    cache: Incomplete
    def __init__(self) -> None: ...
    @property
    @abc.abstractmethod
    def output_target(self) -> str:
        """Returns the output target name.

        See numba/tests/test_retargeting.py for example usage.
        """
    @abc.abstractmethod
    def compile_retarget(self, orig_disp):
        """Returns the retargeted dispatcher.

        See numba/tests/test_retargeting.py for example usage.
        """
    def check_compatible(self, orig_disp) -> None:
        """
        This implementation checks that
        `self.output_target == orig_disp._required_target_backend`
        """
    def retarget(self, orig_disp):
        """Apply retargeting to orig_disp.

        The retargeted dispatchers are cached for future use.
        """

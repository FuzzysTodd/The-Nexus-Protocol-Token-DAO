from .base import BaseDistribution as BaseDistribution, BaseEnvironment as BaseEnvironment, FilesystemWheel as FilesystemWheel, MemoryWheel as MemoryWheel, Wheel as Wheel
from typing import List, Literal, Protocol, Type

__all__ = ['BaseDistribution', 'BaseEnvironment', 'FilesystemWheel', 'MemoryWheel', 'Wheel', 'get_default_environment', 'get_environment', 'get_wheel_distribution', 'select_backend']

class Backend(Protocol):
    NAME: Literal['importlib', 'pkg_resources']
    Distribution: Type[BaseDistribution]
    Environment: Type[BaseEnvironment]

def select_backend() -> Backend: ...
def get_default_environment() -> BaseEnvironment:
    """Get the default representation for the current environment.

    This returns an Environment instance from the chosen backend. The default
    Environment instance should be built from ``sys.path`` and may use caching
    to share instance state accorss calls.
    """
def get_environment(paths: List[str] | None) -> BaseEnvironment:
    """Get a representation of the environment specified by ``paths``.

    This returns an Environment instance from the chosen backend based on the
    given import paths. The backend must build a fresh instance representing
    the state of installed distributions when this function is called.
    """
def get_wheel_distribution(wheel: Wheel, canonical_name: str) -> BaseDistribution:
    """Get the representation of the specified wheel's distribution metadata.

    This returns a Distribution instance from the chosen backend based on
    the given wheel's ``.dist-info`` directory.

    :param canonical_name: Normalized project name of the given wheel.
    """

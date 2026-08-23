from .base import ConfigBase
from .utils import PathLike
from dataclasses import dataclass
from typing import Any, Dict

__all__ = ['AlgorithmConfig', 'CustomAlgorithmConfig']

@dataclass(init=False)
class _AlgorithmConfig(ConfigBase):
    '''
    Common base class for ``AlgorithmConfig`` and ``CustomAlgorithmConfig``.

    It\'s a "union set" of 2 derived classes. So users can use it as either one.
    '''
    name: str | None = ...
    class_name: str | None = ...
    code_directory: PathLike | None = ...
    class_args: Dict[str, Any] | None = ...

@dataclass(init=False)
class AlgorithmConfig(_AlgorithmConfig):
    """
    Configuration for built-in algorithm.
    """
    name: str
    class_args: Dict[str, Any] | None = ...

@dataclass(init=False)
class CustomAlgorithmConfig(_AlgorithmConfig):
    """
    Configuration for custom algorithm.
    """
    class_name: str
    code_directory: PathLike | None = ...
    class_args: Dict[str, Any] | None = ...

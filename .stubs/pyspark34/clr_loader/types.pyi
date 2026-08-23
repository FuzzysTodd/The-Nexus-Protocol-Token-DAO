from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from os import PathLike
from typing import Dict

__all__ = ['StrOrPath']

StrOrPath = str | PathLike

@dataclass
class RuntimeInfo:
    """Information on a Runtime instance

    An informative text can be retrieved from this by converting it to a
    ``str``, in particular the following results in readable debug information:

        >>> ri = RuntimeInfo()
        >>> print(ri)
        6.12.0.122 (tarball)
        Runtime: Mono
        =============
          Version:      6.12.0.122 (tarball)
          Initialized:  True
          Shut down:    False
          Properties:
    """
    kind: str
    version: str
    initialized: bool
    shutdown: bool
    properties: Dict[str, str] = ...
    def __init__(self, kind, version, initialized, shutdown, properties) -> None: ...

class ClrFunction:
    def __init__(self, runtime: Runtime, assembly: StrOrPath, typename: str, func_name: str) -> None: ...
    def __call__(self, buffer: bytes) -> int: ...

class Assembly:
    def __init__(self, runtime: Runtime, path: StrOrPath) -> None: ...
    def get_function(self, name: str, func: str | None = None) -> ClrFunction:
        """Get a wrapped .NET function instance

        The function must be ``static``, and it must have the signature
        ``int Func(IntPtr ptr, int size)``. The returned wrapped instance will
        take a ``binary`` and call the .NET function with a pointer to that
        buffer and the buffer length. The buffer is reflected using CFFI's
        `from_buffer`.

        :param name: If ``func`` is not given, this is the fully qualified name
                     of the function. If ``func`` is given, this is the fully
                     qualified name of the containing class
        :param func: Name of the function
        :return:     A function object that takes a single ``binary`` parameter
                     and returns an ``int``
        """

class Runtime(metaclass=ABCMeta):
    """CLR Runtime

    Encapsulates the lifetime of a CLR (.NET) runtime. If the instance is
    deleted, the runtime will be shut down.
    """
    @abstractmethod
    def info(self) -> RuntimeInfo:
        """Get configuration and version information"""
    def get_assembly(self, assembly_path: StrOrPath) -> Assembly:
        """Get an assembly wrapper

        This function does not guarantee that the respective assembly is or can
        be loaded. Due to the design of the different hosting APIs, loading only
        happens when the first function is referenced, and only then potential
        errors will be raised."""
    @abstractmethod
    def shutdown(self) -> None:
        '''Shut down the runtime as much as possible

        Implementations should still be able to "reinitialize", thus the final
        cleanup will usually happen in an ``atexit`` handler.'''
    def __del__(self) -> None: ...

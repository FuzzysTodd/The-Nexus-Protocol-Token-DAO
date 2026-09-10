import types
from _typeshed import Incomplete
from typing import List

class _QEngineProp:
    def __get__(self, obj, objtype) -> str: ...
    def __set__(self, obj, val: str) -> None: ...

class _SupportedQEnginesProp:
    def __get__(self, obj, objtype) -> List[str]: ...
    def __set__(self, obj, val) -> None: ...

class QuantizedEngine(types.ModuleType):
    m: Incomplete
    def __init__(self, m, name) -> None: ...
    def __getattr__(self, attr): ...
    engine: Incomplete
    supported_engines: Incomplete

engine: str
supported_engines: List[str]

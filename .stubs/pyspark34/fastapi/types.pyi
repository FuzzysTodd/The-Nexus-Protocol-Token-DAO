from _typeshed import Incomplete
from enum import Enum
from pydantic import BaseModel
from typing import Any, Callable, Dict, Set, Type, TypeVar

DecoratedCallable = TypeVar('DecoratedCallable', bound=Callable[..., Any])
UnionType: Incomplete
NoneType: Incomplete
ModelNameMap = Dict[Type[BaseModel] | Type[Enum], str]
IncEx = Set[int] | Set[str] | Dict[int, Any] | Dict[str, Any]

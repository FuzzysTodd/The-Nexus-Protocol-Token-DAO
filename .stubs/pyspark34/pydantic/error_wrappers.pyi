from .types import ModelOrDc
from .typing import ReprArgs
from .utils import Representation
from _typeshed import Incomplete
from typing import Any, Dict, List, Sequence, Tuple
from typing_extensions import TypedDict

__all__ = ['ErrorWrapper', 'ValidationError']

Loc = Tuple[int | str, ...]

class _ErrorDictRequired(TypedDict):
    loc: Loc
    msg: str
    type: str

class ErrorDict(_ErrorDictRequired, total=False):
    ctx: Dict[str, Any]

class ErrorWrapper(Representation):
    exc: Incomplete
    def __init__(self, exc: Exception, loc: str | Loc) -> None: ...
    def loc_tuple(self) -> Loc: ...
    def __repr_args__(self) -> ReprArgs: ...
ErrorList = Sequence[Any] | ErrorWrapper

class ValidationError(Representation, ValueError):
    raw_errors: Incomplete
    model: Incomplete
    def __init__(self, errors: Sequence[ErrorList], model: ModelOrDc) -> None: ...
    def errors(self) -> List['ErrorDict']: ...
    def json(self, *, indent: None | int | str = 2) -> str: ...
    def __repr_args__(self) -> ReprArgs: ...

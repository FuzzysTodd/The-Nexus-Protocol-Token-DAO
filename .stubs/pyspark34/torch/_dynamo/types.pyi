import dataclasses
import types
from typing import Callable, Dict, List, NamedTuple, OrderedDict, Protocol

DynamoFrameType = types.FrameType

class GuardFail(NamedTuple):
    reason: str
    orig_code: types.CodeType

class GuardFn(Protocol):
    closure_vars: OrderedDict[str, object]
    args: List[str]
    code_parts: List[str]
    verbose_code_parts: List[str]
    global_scope: Dict[str, object]
    guard_fail_fn: Callable[[GuardFail], None] | None
    def __call__(self, *maybe_dotzero: object, **f_locals: object) -> bool: ...

@dataclasses.dataclass
class GuardedCode:
    code: types.CodeType
    check_fn: GuardFn
    def __init__(self, code, check_fn) -> None: ...

class DynamoCallbackFn(Protocol):
    def __call__(self, frame: DynamoFrameType, cache_size: int) -> GuardedCode | None: ...
DynamoCallback = DynamoCallbackFn | None | bool

class DynamoGuardHook(Protocol):
    def __call__(self, guard_fn: GuardFn, code: types.CodeType, f_locals: Dict[str, object], last: bool) -> None: ...

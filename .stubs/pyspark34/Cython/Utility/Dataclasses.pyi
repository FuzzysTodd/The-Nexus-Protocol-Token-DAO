from _typeshed import Incomplete
from typing import NamedTuple

class _MISSING_TYPE: ...

MISSING: Incomplete

class _DataclassParams(NamedTuple):
    init: Incomplete
    repr: Incomplete
    eq: Incomplete
    order: Incomplete
    unsafe_hash: Incomplete
    frozen: Incomplete
    match_args: Incomplete
    kw_only: Incomplete
    slots: Incomplete
    weakref_slot: Incomplete

class Field:
    name: Incomplete
    type: Incomplete
    default: Incomplete
    default_factory: Incomplete
    init: Incomplete
    repr: Incomplete
    hash: Incomplete
    compare: Incomplete
    metadata: Incomplete
    kw_only: Incomplete
    def __init__(self, default, default_factory, init, repr, hash, compare, metadata, kw_only) -> None: ...

class _HAS_DEFAULT_FACTORY_CLASS: ...

def dataclass(*args, **kwds) -> None: ...

class _FIELD_BASE:
    name: Incomplete
    def __init__(self, name) -> None: ...

def field(*ignore, **kwds): ...

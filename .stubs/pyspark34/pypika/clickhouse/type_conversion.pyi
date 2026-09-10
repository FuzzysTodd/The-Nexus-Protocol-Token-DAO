from _typeshed import Incomplete
from pypika.terms import Field as Field, Function as Function
from pypika.utils import format_alias_sql as format_alias_sql

class ToString(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToFixedString(Function):
    alias: Incomplete
    name: str
    schema: Incomplete
    args: Incomplete
    def __init__(self, field, length: int, alias: str = None, schema: str = None) -> None: ...
    def get_sql(self, with_alias: bool = False, with_namespace: bool = False, quote_char: Incomplete | None = None, dialect: Incomplete | None = None, **kwargs): ...

class ToInt8(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToInt16(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToInt32(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToInt64(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToUInt8(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToUInt16(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToUInt32(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToUInt64(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToFloat32(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToFloat64(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToDate(Function):
    def __init__(self, name, alias: str = None) -> None: ...

class ToDateTime(Function):
    def __init__(self, name, alias: str = None) -> None: ...

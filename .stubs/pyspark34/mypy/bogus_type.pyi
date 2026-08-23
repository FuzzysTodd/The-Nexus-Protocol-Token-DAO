from mypy_extensions import FlexibleAlias
from typing import Any, TypeVar

T = TypeVar('T')
MYPYC: bool
Bogus = FlexibleAlias[T, Any]
Bogus = FlexibleAlias[T, T]

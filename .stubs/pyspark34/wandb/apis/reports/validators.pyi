import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import TypeVar

LINEPLOT_STYLES: Incomplete
BARPLOT_STYLES: Incomplete
FONT_SIZES: Incomplete
LEGEND_POSITIONS: Incomplete
LEGEND_ORIENTATIONS: Incomplete
AGGFUNCS: Incomplete
RANGEFUNCS: Incomplete
MARKS: Incomplete
TIMESTEPS: Incomplete
SMOOTHING_TYPES: Incomplete
CODE_COMPARE_DIFF: Incomplete
UNDEFINED_TYPE = TypeVar('UNDEFINED_TYPE')

class Validator(ABC, metaclass=abc.ABCMeta):
    how: Incomplete
    def __init__(self, how: Incomplete | None = None) -> None: ...
    @abstractmethod
    def call(self, attr_name, value): ...
    def __call__(self, attr, value) -> None: ...

class TypeValidator(Validator):
    attr_type: Incomplete
    def __init__(self, attr_type, *args, **kwargs) -> None: ...
    def call(self, attr_name, value) -> None: ...

class OneOf(Validator):
    options: Incomplete
    def __init__(self, options, *args, **kwargs) -> None: ...
    def call(self, attr_name, value) -> None: ...

class Length(Validator):
    k: Incomplete
    def __init__(self, k, *args, **kwargs) -> None: ...
    def call(self, attr_name, value) -> None: ...

class Between(Validator):
    lb: Incomplete
    ub: Incomplete
    def __init__(self, lb, ub, *args, **kwargs) -> None: ...
    def call(self, attr_name, value) -> None: ...

class OrderString(TypeValidator):
    def __init__(self) -> None: ...
    def call(self, attr_name, value) -> None: ...

class LayoutDict(Validator):
    def call(self, attr_name, value) -> None: ...

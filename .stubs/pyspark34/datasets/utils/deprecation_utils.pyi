import enum
from .logging import get_logger as get_logger
from _typeshed import Incomplete

logger: Incomplete

def deprecated(help_message: str | None = None):
    """Decorator to mark a class or a function as deprecated.

    Args:
        help_message (:obj:`str`, optional): An optional message to guide the user on how to
            switch to non-deprecated usage of the library.
    """

class OnAccess(enum.EnumMeta):
    """
    Enum metaclass that calls a user-specified function whenever a member is accessed.
    """
    def __getattribute__(cls, name): ...
    def __getitem__(cls, name): ...
    def __call__(cls, value, names: Incomplete | None = None, *, module: Incomplete | None = None, qualname: Incomplete | None = None, type: Incomplete | None = None, start: int = 1): ...

class DeprecatedEnum(enum.Enum, metaclass=OnAccess):
    """
    Enum class that calls `deprecate` method whenever a member is accessed.
    """
    def __new__(cls, value): ...
    @property
    def help_message(self): ...
    def deprecate(self) -> None: ...

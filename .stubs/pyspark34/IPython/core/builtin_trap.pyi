from _typeshed import Incomplete
from traitlets.config.configurable import Configurable

class __BuiltinUndefined: ...

BuiltinUndefined: Incomplete

class __HideBuiltin: ...

HideBuiltin: Incomplete

class BuiltinTrap(Configurable):
    shell: Incomplete
    auto_builtins: Incomplete
    def __init__(self, shell: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None): ...
    def add_builtin(self, key, value) -> None:
        """Add a builtin and save the original."""
    def remove_builtin(self, key, orig) -> None:
        """Remove an added builtin and re-set the original."""
    def activate(self) -> None:
        """Store ipython references in the __builtin__ namespace."""
    def deactivate(self) -> None:
        """Remove any builtins which might have been added by add_builtins, or
        restore overwritten ones to their previous values."""

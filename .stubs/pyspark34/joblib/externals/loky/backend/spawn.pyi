from _typeshed import Incomplete

WINEXE: bool
WINSERVICE: bool

def get_executable(): ...
def get_preparation_data(name, init_main_module: bool = True):
    """Return info about parent needed by child to unpickle process object."""

old_main_modules: Incomplete

def prepare(data, parent_sentinel: Incomplete | None = None) -> None:
    """Try to get current process ready to unpickle process object."""

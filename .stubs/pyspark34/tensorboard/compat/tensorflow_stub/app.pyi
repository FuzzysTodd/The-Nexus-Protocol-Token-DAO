from . import flags as flags
from _typeshed import Incomplete

class _HelpFlag(flags.BooleanFlag):
    """Special boolean flag that displays usage and raises SystemExit."""
    NAME: str
    SHORT_NAME: str
    def __init__(self) -> None: ...
    def parse(self, arg) -> None: ...

class _HelpshortFlag(_HelpFlag):
    """--helpshort is an alias for --help."""
    NAME: str
    SHORT_NAME: Incomplete

class _HelpfullFlag(flags.BooleanFlag):
    """Display help for flags in main module and all dependent modules."""
    def __init__(self) -> None: ...
    def parse(self, arg) -> None: ...

def run(main: Incomplete | None = None, argv: Incomplete | None = None) -> None:
    """Runs the program with an optional 'main' function and 'argv' list."""

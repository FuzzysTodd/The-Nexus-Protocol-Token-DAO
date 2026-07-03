from _typeshed import Incomplete

__all__ = ['Session']

class Session:
    """Represents a virtual environment creation session."""
    def __init__(self, verbosity, app_data, interpreter, creator, seeder, activators) -> None: ...
    @property
    def verbosity(self):
        """The verbosity of the run."""
    @property
    def interpreter(self):
        """Create a virtual environment based on this reference interpreter."""
    @property
    def creator(self):
        """The creator used to build the virtual environment (must be compatible with the interpreter)."""
    @property
    def seeder(self):
        """The mechanism used to provide the seed packages (pip, setuptools, wheel)."""
    @property
    def activators(self):
        """Activators used to generate activations scripts."""
    def run(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class _Debug:
    """lazily populate debug."""
    creator: Incomplete
    def __init__(self, creator) -> None: ...

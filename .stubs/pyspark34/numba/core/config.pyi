from _typeshed import Incomplete

IS_WIN32: Incomplete
IS_OSX: Incomplete
MACHINE_BITS: Incomplete
IS_32BITS: Incomplete
PYVERSION: Incomplete

class _EnvReloader:
    def __init__(self) -> None: ...
    old_environ: Incomplete
    def reset(self) -> None: ...
    def update(self, force: bool = False) -> None: ...
    def validate(self) -> None: ...
    def process_environ(self, environ): ...

def reload_config() -> None:
    """
    Reload the configuration from environment variables, if necessary.
    """

import typing as t
from _typeshed import Incomplete

prefix: Incomplete

class ReloaderLoop:
    name: str
    extra_files: Incomplete
    exclude_patterns: Incomplete
    interval: Incomplete
    def __init__(self, extra_files: t.Iterable[str] | None = None, exclude_patterns: t.Iterable[str] | None = None, interval: int | float = 1) -> None: ...
    def __enter__(self) -> ReloaderLoop:
        """Do any setup, then run one step of the watch to populate the
        initial filesystem state.
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None:
        """Clean up any resources associated with the reloader."""
    def run(self) -> None:
        """Continually run the watch step, sleeping for the configured
        interval after each step.
        """
    def run_step(self) -> None:
        """Run one step for watching the filesystem. Called once to set
        up initial state, then repeatedly to update it.
        """
    def restart_with_reloader(self) -> int:
        """Spawn a new Python interpreter with the same arguments as the
        current one, but running the reloader thread.
        """
    def trigger_reload(self, filename: str) -> None: ...
    def log_reload(self, filename: str) -> None: ...

class StatReloaderLoop(ReloaderLoop):
    name: str
    mtimes: Incomplete
    def __enter__(self) -> ReloaderLoop: ...
    def run_step(self) -> None: ...

class WatchdogReloaderLoop(ReloaderLoop):
    name: Incomplete
    observer: Incomplete
    event_handler: Incomplete
    should_reload: bool
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...
    def trigger_reload(self, filename: str) -> None: ...
    watches: Incomplete
    def __enter__(self) -> ReloaderLoop: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def run(self) -> None: ...
    def run_step(self) -> None: ...

reloader_loops: dict[str, type[ReloaderLoop]]

def ensure_echo_on() -> None:
    """Ensure that echo mode is enabled. Some tools such as PDB disable
    it which causes usability issues after a reload."""
def run_with_reloader(main_func: t.Callable[[], None], extra_files: t.Iterable[str] | None = None, exclude_patterns: t.Iterable[str] | None = None, interval: int | float = 1, reloader_type: str = 'auto') -> None:
    """Run the given function in an independent Python interpreter."""

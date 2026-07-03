import typing as t
from _typeshed import Incomplete
from traitlets.config.configurable import LoggingConfigurable

class KernelRestarter(LoggingConfigurable):
    """Monitor and autorestart a kernel."""
    kernel_manager: Incomplete
    debug: Incomplete
    time_to_dead: Incomplete
    stable_start_time: Incomplete
    restart_limit: Incomplete
    random_ports_until_alive: Incomplete
    callbacks: Incomplete
    def start(self) -> None:
        """Start the polling of the kernel."""
    def stop(self) -> None:
        """Stop the kernel polling."""
    def add_callback(self, f: t.Callable[..., t.Any], event: str = 'restart') -> None:
        """register a callback to fire on a particular event

        Possible values for event:

          'restart' (default): kernel has died, and will be restarted.
          'dead': restart has failed, kernel will be left dead.

        """
    def remove_callback(self, f: t.Callable[..., t.Any], event: str = 'restart') -> None:
        """unregister a callback to fire on a particular event

        Possible values for event:

          'restart' (default): kernel has died, and will be restarted.
          'dead': restart has failed, kernel will be left dead.

        """
    def poll(self) -> None: ...

from . import port_file as port_file
from .service_base import ServiceInterface as ServiceInterface
from .service_sock import ServiceSockInterface as ServiceSockInterface
from wandb import termlog as termlog
from wandb.env import error_reporting_enabled as error_reporting_enabled
from wandb.errors import Error as Error
from wandb.sdk.wandb_settings import Settings as Settings
from wandb.util import get_module as get_module

class ServiceStartProcessError(Error):
    """Raised when a known error occurs when launching wandb service."""
class ServiceStartTimeoutError(Error):
    """Raised when service start times out."""
class ServiceStartPortError(Error):
    """Raised when service start fails to find a port."""

class _Service:
    def __init__(self, settings: Settings) -> None: ...
    def start(self) -> None: ...
    @property
    def sock_port(self) -> int | None: ...
    @property
    def service_interface(self) -> ServiceInterface: ...
    def join(self) -> int: ...

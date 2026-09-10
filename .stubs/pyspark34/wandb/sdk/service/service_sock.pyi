from ..lib.sock_client import SockClient as SockClient
from .service_base import ServiceInterface as ServiceInterface
from wandb.sdk.wandb_settings import Settings as Settings

class ServiceSockInterface(ServiceInterface):
    def __init__(self) -> None: ...
    def get_transport(self) -> str: ...

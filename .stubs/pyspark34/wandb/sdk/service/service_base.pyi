import abc
from abc import abstractmethod
from wandb.sdk.wandb_settings import Settings as Settings

class ServiceInterface(metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    @abstractmethod
    def get_transport(self) -> str: ...

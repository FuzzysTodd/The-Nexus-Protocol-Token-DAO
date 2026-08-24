from abc import ABCMeta, abstractmethod

class TargetDescriptor(metaclass=ABCMeta):
    def __init__(self, target_name) -> None: ...
    @property
    @abstractmethod
    def typing_context(self): ...
    @property
    @abstractmethod
    def target_context(self): ...

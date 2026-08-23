from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.activation.via_template import ViaTemplateActivator

__all__ = ['FishActivator']

class FishActivator(ViaTemplateActivator):
    def templates(self) -> Generator[Incomplete, None, None]: ...

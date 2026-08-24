from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.activation.via_template import ViaTemplateActivator

__all__ = ['BashActivator']

class BashActivator(ViaTemplateActivator):
    def templates(self) -> Generator[Incomplete, None, None]: ...
    def as_name(self, template): ...

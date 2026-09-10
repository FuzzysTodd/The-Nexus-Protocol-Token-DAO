from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.activation.via_template import ViaTemplateActivator

__all__ = ['CShellActivator']

class CShellActivator(ViaTemplateActivator):
    @classmethod
    def supports(cls, interpreter): ...
    def templates(self) -> Generator[Incomplete, None, None]: ...

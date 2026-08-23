from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.activation.via_template import ViaTemplateActivator

__all__ = ['PowerShellActivator']

class PowerShellActivator(ViaTemplateActivator):
    def templates(self) -> Generator[Incomplete, None, None]: ...

from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.activation.via_template import ViaTemplateActivator

__all__ = ['NushellActivator']

class NushellActivator(ViaTemplateActivator):
    def templates(self) -> Generator[Incomplete, None, None]: ...
    def replacements(self, creator, dest_folder): ...

from .buildable import BuildableModule as BuildableModule
from .builder import Builder as Builder
from .exceptions import UserException as UserException
from .installable import Installable as Installable
from _typeshed import Incomplete

class SetuptoolsBuilder(Builder):
    """ The implementation of a setuptools-based project builder. """
    def build_executable(self, buildable, *, fatal: bool = True) -> None:
        """ Build an executable from a BuildableExecutable object and return
        the relative pathname of the executable.
        """
    def build_project(self, target_dir, *, wheel_tag: Incomplete | None = None) -> None:
        """ Build the project. """
    def install_project(self, target_dir, *, wheel_tag: Incomplete | None = None) -> None:
        """ Install the project into a target directory. """

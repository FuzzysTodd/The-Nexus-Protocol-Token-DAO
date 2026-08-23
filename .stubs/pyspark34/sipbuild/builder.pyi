import abc
from .abstract_builder import AbstractBuilder as AbstractBuilder
from .buildable import BuildableFromSources as BuildableFromSources
from .code_generator import set_globals as set_globals
from .distinfo import write_metadata as write_metadata
from .exceptions import UserException as UserException
from .installable import Installable as Installable
from .module import copy_sip_h as copy_sip_h, copy_sip_pyi as copy_sip_pyi
from .py_versions import OLDEST_SUPPORTED_MINOR as OLDEST_SUPPORTED_MINOR
from .version import SIP_VERSION as SIP_VERSION, SIP_VERSION_STR as SIP_VERSION_STR
from _typeshed import Incomplete
from abc import abstractmethod

class Builder(AbstractBuilder, metaclass=abc.ABCMeta):
    """ The default base implementation of a project builder. """
    def build(self) -> None:
        """ Build the project in-situ. """
    @abstractmethod
    def build_executable(self, buildable, *, fatal: bool = True):
        """ Build an executable from a BuildableExecutable object and return
        the relative pathname of the executable.
        """
    @abstractmethod
    def build_project(self, target_dir, *, wheel_tag: Incomplete | None = None):
        """ Build the project. """
    def build_sdist(self, sdist_directory):
        """ Build an sdist for the project and return the name of the sdist
        file.
        """
    def build_wheel(self, wheel_directory):
        """ Build a wheel for the project and return the name of the wheel
        file.
        """
    def install(self) -> None:
        """ Install the project. """
    @abstractmethod
    def install_project(self, target_dir, *, wheel_tag: Incomplete | None = None):
        """ Install the project into a target directory. """

from .exceptions import UserFileException as UserFileException
from .py_versions import OLDEST_SUPPORTED_MINOR as OLDEST_SUPPORTED_MINOR
from .toml import toml_load as toml_load
from _typeshed import Incomplete

class PyProjectException(UserFileException):
    """ An exception related to a pyproject.toml file. """
    def __init__(self, text, *, detail: Incomplete | None = None) -> None:
        """ Initialise the exception. """

class PyProjectOptionException(PyProjectException):
    """ An exception related to a specific option of a pyproject.toml file. """
    def __init__(self, name, text, *, section_name: Incomplete | None = None, detail: Incomplete | None = None) -> None:
        """ Initialise the exception. """

class PyProjectUndefinedOptionException(PyProjectOptionException):
    """ An exception related to an undefined option of a pyproject.toml file.
    """
    def __init__(self, name, *, section_name: Incomplete | None = None) -> None:
        """ Initialise the exception. """

class PyProject:
    """ Encapsulate a parsed pyproject.toml file. """
    toml_error: Incomplete
    def __init__(self) -> None:
        """ Initialise the object. """
    def get_metadata(self):
        """ Return a dict containing the PEP 566 meta-data. """
    def get_section(self, section_name, *, required: bool = False):
        """ Return a sub-section with a dotted name. """

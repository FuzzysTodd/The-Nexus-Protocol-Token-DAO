from .abstract_project import AbstractProject as AbstractProject
from .exceptions import handle_exception as handle_exception
from _typeshed import Incomplete

def build_sdist(sdist_directory, config_settings: Incomplete | None = None):
    """ The PEP 517 hook for building an sdist from pyproject.toml. """
def build_wheel(wheel_directory, config_settings: Incomplete | None = None, metadata_directory: Incomplete | None = None):
    """ The PEP 517 hook for building a wheel from pyproject.toml. """

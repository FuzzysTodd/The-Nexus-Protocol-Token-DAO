from . import expand as _expand
from ..errors import FileError as FileError, OptionError as OptionError
from ..warnings import SetuptoolsWarning as SetuptoolsWarning
from _typeshed import Incomplete
from setuptools.dist import Distribution as Distribution

def load_file(filepath: _Path) -> dict: ...
def validate(config: dict, filepath: _Path) -> bool: ...
def apply_configuration(dist: Distribution, filepath: _Path, ignore_option_errors: bool = False) -> Distribution:
    """Apply the configuration from a ``pyproject.toml`` file into an existing
    distribution object.
    """
def read_configuration(filepath: _Path, expand: bool = True, ignore_option_errors: bool = False, dist: Distribution | None = None):
    """Read given configuration file and returns options from it as a dict.

    :param str|unicode filepath: Path to configuration file in the ``pyproject.toml``
        format.

    :param bool expand: Whether to expand directives and other computed values
        (i.e. post-process the given configuration)

    :param bool ignore_option_errors: Whether to silently ignore
        options, values of which could not be resolved (e.g. due to exceptions
        in directives such as file:, attr:, etc.).
        If False exceptions are propagated as expected.

    :param Distribution|None: Distribution object to which the configuration refers.
        If not given a dummy object will be created and discarded after the
        configuration is read. This is used for auto-discovery of packages and in the
        case a dynamic configuration (e.g. ``attr`` or ``cmdclass``) is expanded.
        When ``expand=False`` this object is simply ignored.

    :rtype: dict
    """
def expand_configuration(config: dict, root_dir: _Path | None = None, ignore_option_errors: bool = False, dist: Distribution | None = None) -> dict:
    """Given a configuration with unresolved fields (e.g. dynamic, cmdclass, ...)
    find their final values.

    :param dict config: Dict containing the configuration for the distribution
    :param str root_dir: Top-level directory for the distribution/project
        (the same directory where ``pyproject.toml`` is place)
    :param bool ignore_option_errors: see :func:`read_configuration`
    :param Distribution|None: Distribution object to which the configuration refers.
        If not given a dummy object will be created and discarded after the
        configuration is read. Used in the case a dynamic configuration
        (e.g. ``attr`` or ``cmdclass``).

    :rtype: dict
    """

class _ConfigExpander:
    config: Incomplete
    root_dir: Incomplete
    project_cfg: Incomplete
    dynamic: Incomplete
    setuptools_cfg: Incomplete
    dynamic_cfg: Incomplete
    ignore_option_errors: Incomplete
    def __init__(self, config: dict, root_dir: _Path | None = None, ignore_option_errors: bool = False, dist: Distribution | None = None) -> None: ...
    def expand(self): ...

class _EnsurePackagesDiscovered(_expand.EnsurePackagesDiscovered):
    def __init__(self, distribution: Distribution, project_cfg: dict, setuptools_cfg: dict) -> None: ...
    def __enter__(self):
        """When entering the context, the values of ``packages``, ``py_modules`` and
        ``package_dir`` that are missing in ``dist`` are copied from ``setuptools_cfg``.
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None):
        """When exiting the context, if values of ``packages``, ``py_modules`` and
        ``package_dir`` are missing in ``setuptools_cfg``, copy from ``dist``.
        """

class _ExperimentalConfiguration(SetuptoolsWarning): ...

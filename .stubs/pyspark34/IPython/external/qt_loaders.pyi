import importlib.abc
from _typeshed import Incomplete

QT_API_PYQT6: str
QT_API_PYSIDE6: str
QT_API_PYQT5: str
QT_API_PYSIDE2: str
QT_API_PYQT: str
QT_API_PYQTv1: str
QT_API_PYSIDE: str
QT_API_PYQT_DEFAULT: str
api_to_module: Incomplete

class ImportDenier(importlib.abc.MetaPathFinder):
    """Import Hook that will guard against bad Qt imports
    once IPython commits to a specific binding
    """
    def __init__(self) -> None: ...
    def forbid(self, module_name) -> None: ...
    def find_spec(self, fullname, path, target: Incomplete | None = None) -> None: ...

ID: Incomplete

def commit_api(api) -> None:
    """Commit to a particular API, and trigger ImportErrors on subsequent
    dangerous imports"""
def loaded_api():
    """Return which API is loaded, if any

    If this returns anything besides None,
    importing any other Qt binding is unsafe.

    Returns
    -------
    None, 'pyside6', 'pyqt6', 'pyside2', 'pyside', 'pyqt', 'pyqt5', 'pyqtv1'
    """
def has_binding(api):
    """Safely check for PyQt4/5, PySide or PySide2, without importing submodules

    Parameters
    ----------
    api : str [ 'pyqtv1' | 'pyqt' | 'pyqt5' | 'pyside' | 'pyside2' | 'pyqtdefault']
        Which module to check for

    Returns
    -------
    True if the relevant module appears to be importable
    """
def qtapi_version():
    """Return which QString API has been set, if any

    Returns
    -------
    The QString API version (1 or 2), or None if not set
    """
def can_import(api):
    """Safely query whether an API is importable, without importing it"""
def import_pyqt4(version: int = 2):
    """
    Import PyQt4

    Parameters
    ----------
    version : 1, 2, or None
        Which QString/QVariant API to use. Set to None to use the system
        default
    ImportErrors raised within this function are non-recoverable
    """
def import_pyqt5():
    """
    Import PyQt5

    ImportErrors raised within this function are non-recoverable
    """
def import_pyqt6():
    """
    Import PyQt6

    ImportErrors raised within this function are non-recoverable
    """
def import_pyside():
    """
    Import PySide

    ImportErrors raised within this function are non-recoverable
    """
def import_pyside2():
    """
    Import PySide2

    ImportErrors raised within this function are non-recoverable
    """
def import_pyside6():
    """
    Import PySide6

    ImportErrors raised within this function are non-recoverable
    """
def load_qt(api_options):
    """
    Attempt to import Qt, given a preference list
    of permissible bindings

    It is safe to call this function multiple times.

    Parameters
    ----------
    api_options : List of strings
        The order of APIs to try. Valid items are 'pyside', 'pyside2',
        'pyqt', 'pyqt5', 'pyqtv1' and 'pyqtdefault'

    Returns
    -------
    A tuple of QtCore, QtGui, QtSvg, QT_API
    The first three are the Qt modules. The last is the
    string indicating which module was loaded.

    Raises
    ------
    ImportError, if it isn't possible to import any requested
    bindings (either because they aren't installed, or because
    an incompatible library has already been installed)
    """
def enum_factory(QT_API, QtCore):
    """Construct an enum helper to account for PyQt5 <-> PyQt6 changes."""

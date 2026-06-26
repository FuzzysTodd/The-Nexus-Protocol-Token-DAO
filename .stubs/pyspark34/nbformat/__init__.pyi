from ._version import __version__ as __version__, version_info as version_info
from .converter import convert as convert
from .notebooknode import NotebookNode as NotebookNode, from_dict as from_dict
from .sentinel import Sentinel as Sentinel
from .v4 import nbformat as current_nbformat, nbformat_minor as current_nbformat_minor
from .validator import ValidationError as ValidationError, validate as validate
from _typeshed import Incomplete

__all__ = ['versions', 'validate', 'ValidationError', 'convert', 'from_dict', 'NotebookNode', 'current_nbformat', 'current_nbformat_minor', 'NBFormatError', 'NO_CONVERT', 'reads', 'read', 'writes', 'write', 'version_info', '__version__', 'Sentinel']

versions: Incomplete

class NBFormatError(ValueError): ...

NO_CONVERT: Incomplete

def reads(s, as_version, capture_validation_error: Incomplete | None = None, **kwargs):
    '''Read a notebook from a string and return the NotebookNode object as the given version.

    The string can contain a notebook of any version.
    The notebook will be returned `as_version`, converting, if necessary.

    Notebook format errors will be logged.

    Parameters
    ----------
    s : unicode
        The raw unicode string to read the notebook from.
    as_version : int
        The version of the notebook format to return.
        The notebook will be converted, if necessary.
        Pass nbformat.NO_CONVERT to prevent conversion.
    capture_validation_error : dict, optional
        If provided, a key of "ValidationError" with a
        value of the ValidationError instance will be added
        to the dictionary.

    Returns
    -------
    nb : NotebookNode
        The notebook that was read.
    '''
def writes(nb, version=..., capture_validation_error: Incomplete | None = None, **kwargs):
    '''Write a notebook to a string in a given format in the given nbformat version.

    Any notebook format errors will be logged.

    Parameters
    ----------
    nb : NotebookNode
        The notebook to write.
    version : int, optional
        The nbformat version to write.
        If unspecified, or specified as nbformat.NO_CONVERT,
        the notebook\'s own version will be used and no conversion performed.
    capture_validation_error : dict, optional
        If provided, a key of "ValidationError" with a
        value of the ValidationError instance will be added
        to the dictionary.

    Returns
    -------
    s : unicode
        The notebook as a JSON string.
    '''
def read(fp, as_version, capture_validation_error: Incomplete | None = None, **kwargs):
    '''Read a notebook from a file as a NotebookNode of the given version.

    The string can contain a notebook of any version.
    The notebook will be returned `as_version`, converting, if necessary.

    Notebook format errors will be logged.

    Parameters
    ----------
    fp : file or str
        A file-like object with a read method that returns unicode (use
        ``io.open()`` in Python 2), or a path to a file.
    as_version : int
        The version of the notebook format to return.
        The notebook will be converted, if necessary.
        Pass nbformat.NO_CONVERT to prevent conversion.
    capture_validation_error : dict, optional
        If provided, a key of "ValidationError" with a
        value of the ValidationError instance will be added
        to the dictionary.

    Returns
    -------
    nb : NotebookNode
        The notebook that was read.
    '''
def write(nb, fp, version=..., capture_validation_error: Incomplete | None = None, **kwargs) -> None:
    '''Write a notebook to a file in a given nbformat version.

    The file-like object must accept unicode input.

    Parameters
    ----------
    nb : NotebookNode
        The notebook to write.
    fp : file or str
        Any file-like object with a write method that accepts unicode, or
        a path to write a file.
    version : int, optional
        The nbformat version to write.
        If nb is not this version, it will be converted.
        If unspecified, or specified as nbformat.NO_CONVERT,
        the notebook\'s own version will be used and no conversion performed.
    capture_validation_error : dict, optional
        If provided, a key of "ValidationError" with a
        value of the ValidationError instance will be added
        to the dictionary.
    '''

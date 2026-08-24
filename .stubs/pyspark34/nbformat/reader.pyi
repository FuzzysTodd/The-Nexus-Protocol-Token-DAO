from .validator import ValidationError as ValidationError

class NotJSONError(ValueError):
    """An error raised when an object is not valid JSON."""

def parse_json(s, **kwargs):
    """Parse a JSON string into a dict."""
def get_version(nb):
    """Get the version of a notebook.

    Parameters
    ----------
    nb : dict
        NotebookNode or dict containing notebook data.

    Returns
    -------
    Tuple containing major (int) and minor (int) version numbers
    """
def reads(s, **kwargs):
    """Read a notebook from a json string and return the
    NotebookNode object.

    This function properly reads notebooks of any version.  No version
    conversion is performed.

    Parameters
    ----------
    s : unicode | bytes
        The raw string or bytes object to read the notebook from.

    Returns
    -------
    nb : NotebookNode
        The notebook that was read.

    Raises
    ------
    ValidationError
        Notebook JSON for a given version is missing an expected key and cannot be read.
    NBFormatError
        Specified major version is invalid or unsupported.
    """
def read(fp, **kwargs):
    """Read a notebook from a file and return the NotebookNode object.

    This function properly reads notebooks of any version.  No version
    conversion is performed.

    Parameters
    ----------
    fp : file
        Any file-like object with a read method.

    Returns
    -------
    nb : NotebookNode
        The notebook that was read.
    """

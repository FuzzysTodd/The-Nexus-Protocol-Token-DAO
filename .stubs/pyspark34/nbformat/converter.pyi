from . import versions as versions
from .reader import get_version as get_version
from .validator import ValidationError as ValidationError

def convert(nb, to_version):
    """Convert a notebook node object to a specific version.  Assumes that
    all the versions starting from 1 to the latest major X are implemented.
    In other words, there should never be a case where v1 v2 v3 v5 exist without
    a v4.  Also assumes that all conversions can be made in one step increments
    between major versions and ignores minor revisions.

    Parameters
    ----------
    nb : NotebookNode
    to_version : int
        Major revision to convert the notebook to.  Can either be an upgrade or
        a downgrade.

    Raises
    ------
    ValueError
        Notebook failed to convert.
    ValueError
        The version specified is invalid or doesn't exist.
    ValidationError
        Conversion failed due to missing expected attributes.
    """

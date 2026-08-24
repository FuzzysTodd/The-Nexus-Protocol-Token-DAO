from _typeshed import Incomplete

def check_version(v, min_v, max_v: Incomplete | None = None):
    """check version string v >= min_v and v < max_v

    Parameters
    ----------
    v : str
        version of the package
    min_v : str
        minimal version supported
    max_v : str
        earliest version not supported
    Note: If dev/prerelease tags result in TypeError for string-number
    comparison, it is assumed that the check passes and the version dependency
    is satisfied. Users on dev branches are responsible for keeping their own
    packages up to date.
    """

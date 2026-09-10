def pkg_commit_hash(pkg_path):
    """Get short form of commit hash given directory `pkg_path`

    We get the commit hash from git if it's a repo.

    If this fail, we return a not-found placeholder tuple

    Parameters
    ----------
    pkg_path : str
        directory containing package
        only used for getting commit from active repo

    Returns
    -------
    hash_from : str
        Where we got the hash from - description
    hash_str : str
        short form of hash
    """
def pkg_info(pkg_path):
    """Return dict describing the context of this package

    Parameters
    ----------
    pkg_path : str
        path containing __init__.py for package

    Returns
    -------
    context : dict
        with named parameters of interest
    """
def get_sys_info():
    """Return useful information about the system as a dict."""

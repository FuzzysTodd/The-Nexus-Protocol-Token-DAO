from _typeshed import Incomplete

ALGORITHMS_AVAILABLE: Incomplete

def file_hash(fname, alg: str = 'sha256'):
    '''
    Calculate the hash of a given file.

    Useful for checking if a file has changed or been corrupted.

    Parameters
    ----------
    fname : str
        The name of the file.
    alg : str
        The type of the hashing algorithm

    Returns
    -------
    hash : str
        The hash of the file.

    Examples
    --------

    >>> fname = "test-file-for-hash.txt"
    >>> with open(fname, "w") as f:
    ...     __ = f.write("content of the file")
    >>> print(file_hash(fname))
    0fc74468e6a9a829f103d069aeb2bb4f8646bad58bf146bb0e3379b759ec4a00
    >>> import os
    >>> os.remove(fname)

    '''
def hash_algorithm(hash_string):
    '''
    Parse the name of the hash method from the hash string.

    The hash string should have the following form ``algorithm:hash``, where
    algorithm can be the name of any algorithm known to :mod:`hashlib`.

    If the algorithm is omitted or the hash string is None, will default to
    ``"sha256"``.

    Parameters
    ----------
    hash_string : str
        The hash string with optional algorithm prepended.

    Returns
    -------
    hash_algorithm : str
        The name of the algorithm.

    Examples
    --------

    >>> print(hash_algorithm("qouuwhwd2j192y1lb1iwgowdj2898wd2d9"))
    sha256
    >>> print(hash_algorithm("md5:qouuwhwd2j192y1lb1iwgowdj2898wd2d9"))
    md5
    >>> print(hash_algorithm("sha256:qouuwhwd2j192y1lb1iwgowdj2898wd2d9"))
    sha256
    >>> print(hash_algorithm("SHA256:qouuwhwd2j192y1lb1iwgowdj2898wd2d9"))
    sha256
    >>> print(hash_algorithm("xxh3_64:qouuwhwd2j192y1lb1iwgowdj2898wd2d9"))
    xxh3_64
    >>> print(hash_algorithm(None))
    sha256

    '''
def hash_matches(fname, known_hash, strict: bool = False, source: Incomplete | None = None):
    """
    Check if the hash of a file matches a known hash.

    If the *known_hash* is None, will always return True.

    Coverts hashes to lowercase before comparison to avoid system specific
    mismatches between hashes in the registry and computed hashes.

    Parameters
    ----------
    fname : str or PathLike
        The path to the file.
    known_hash : str
        The known hash. Optionally, prepend ``alg:`` to the hash to specify the
        hashing algorithm. Default is SHA256.
    strict : bool
        If True, will raise a :class:`ValueError` if the hash does not match
        informing the user that the file may be corrupted.
    source : str
        The source of the downloaded file (name or URL, for example). Will be
        used in the error message if *strict* is True. Has no other use other
        than reporting to the user where the file came from in case of hash
        mismatch. If None, will default to *fname*.

    Returns
    -------
    is_same : bool
        True if the hash matches, False otherwise.

    """
def make_registry(directory, output, recursive: bool = True) -> None:
    """
    Make a registry of files and hashes for the given directory.

    This is helpful if you have many files in your test dataset as it keeps you
    from needing to manually update the registry.

    Parameters
    ----------
    directory : str
        Directory of the test data to put in the registry. All file names in
        the registry will be relative to this directory.
    output : str
        Name of the output registry file.
    recursive : bool
        If True, will recursively look for files in subdirectories of
        *directory*.

    """

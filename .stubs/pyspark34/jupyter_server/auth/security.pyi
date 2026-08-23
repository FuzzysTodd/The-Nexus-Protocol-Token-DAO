from _typeshed import Incomplete
from collections.abc import Generator

salt_len: int

def passwd(passphrase: Incomplete | None = None, algorithm: str = 'argon2'):
    """Generate hashed password and salt for use in server configuration.

    In the server configuration, set `c.ServerApp.password` to
    the generated string.

    Parameters
    ----------
    passphrase : str
        Password to hash.  If unspecified, the user is asked to input
        and verify a password.
    algorithm : str
        Hashing algorithm to use (e.g, 'sha1' or any argument supported
        by :func:`hashlib.new`, or 'argon2').

    Returns
    -------
    hashed_passphrase : str
        Hashed password, in the format 'hash_algorithm:salt:passphrase_hash'.

    Examples
    --------
    >>> passwd('mypassword')  # doctest: +ELLIPSIS
    'argon2:...'

    """
def passwd_check(hashed_passphrase, passphrase):
    """Verify that a given passphrase matches its hashed version.

    Parameters
    ----------
    hashed_passphrase : str
        Hashed password, in the format returned by `passwd`.
    passphrase : str
        Passphrase to validate.

    Returns
    -------
    valid : bool
        True if the passphrase matches the hash.

    Examples
    --------
    >>> myhash = passwd('mypassword')
    >>> passwd_check(myhash, 'mypassword')
    True

    >>> passwd_check(myhash, 'otherpassword')
    False

    >>> passwd_check('sha1:0e112c3ddfce:a68df677475c2b47b6e86d0467eec97ac5f4b85a',
    ...              'mypassword')
    True
    """
def persist_config(config_file: Incomplete | None = None, mode: int = 384) -> Generator[Incomplete, None, None]:
    """Context manager that can be used to modify a config object

    On exit of the context manager, the config will be written back to disk,
    by default with user-only (600) permissions.
    """
def set_password(password: Incomplete | None = None, config_file: Incomplete | None = None):
    """Ask user for password, store it in JSON configuration file"""

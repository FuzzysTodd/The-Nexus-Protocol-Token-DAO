import ctypes as _ctypes
from _typeshed import Incomplete

OS_RESULT = _ctypes.c_int32

class KeychainError(OSError):
    """The RuntimeError that will be run when a function interacting with Keychain fails."""
    ACCESS_DENIED: int
    NO_SUCH_KEYCHAIN: int
    NO_DEFAULT: int
    ITEM_NOT_FOUND: int
    exit_status: Incomplete
    message: Incomplete
    def __init__(self, exit_status) -> None: ...

class Keychain:
    """Encapsulates the interactions with a particular MacOS Keychain."""
    def __init__(self, filename: str = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def get_generic_password(self, service: str, account_name: str) -> str:
        """Fetch the password associated with a particular service and account.

        :param service: The service that this password is associated with.
        :param account_name: The account that this password is associated with.
        :return: The value of the password associated with the specified service and account.
        """
    def set_generic_password(self, service: str, account_name: str, value: str) -> None:
        """Associate a password with a given service and account.

        :param service: The service to associate this password with.
        :param account_name: The account to associate this password with.
        :param value: The string that should be used as the password.
        """
    def get_internet_password(self, service: str, username: str) -> str:
        """ Fetches a password associated with a domain and username.
        NOTE: THIS IS NOT YET IMPLEMENTED
        :param service: The website/service that this password is associated with.
        :param username: The account that this password is associated with.
        :return: The password that was associated with the given service and username.
        """
    def set_internet_password(self, service: str, username: str, value: str) -> None:
        """Sets a password associated with a domain and a username.
        NOTE: THIS IS NOT YET IMPLEMENTED
        :param service: The website/service that this password is associated with.
        :param username: The account that this password is associated with.
        :param value: The password that should be associated with the given service and username.
        """

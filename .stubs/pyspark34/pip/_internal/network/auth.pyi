import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from pip._internal.utils.logging import getLogger as getLogger
from pip._internal.utils.misc import ask as ask, ask_input as ask_input, ask_password as ask_password, remove_auth_from_url as remove_auth_from_url, split_auth_netloc_from_url as split_auth_netloc_from_url
from pip._internal.vcs.versioncontrol import AuthInfo as AuthInfo
from pip._vendor.requests.auth import AuthBase as AuthBase, HTTPBasicAuth as HTTPBasicAuth
from pip._vendor.requests.models import Request as Request, Response as Response
from pip._vendor.requests.utils import get_netrc_auth as get_netrc_auth
from typing import Any, List, NamedTuple

logger: Incomplete
KEYRING_DISABLED: bool

class Credentials(NamedTuple):
    url: str
    username: str
    password: str

class KeyRingBaseProvider(ABC, metaclass=abc.ABCMeta):
    """Keyring base provider interface"""
    has_keyring: bool
    @abstractmethod
    def get_auth_info(self, url: str, username: str | None) -> AuthInfo | None: ...
    @abstractmethod
    def save_auth_info(self, url: str, username: str, password: str) -> None: ...

class KeyRingNullProvider(KeyRingBaseProvider):
    """Keyring null provider"""
    has_keyring: bool
    def get_auth_info(self, url: str, username: str | None) -> AuthInfo | None: ...
    def save_auth_info(self, url: str, username: str, password: str) -> None: ...

class KeyRingPythonProvider(KeyRingBaseProvider):
    """Keyring interface which uses locally imported `keyring`"""
    has_keyring: bool
    keyring: Incomplete
    def __init__(self) -> None: ...
    def get_auth_info(self, url: str, username: str | None) -> AuthInfo | None: ...
    def save_auth_info(self, url: str, username: str, password: str) -> None: ...

class KeyRingCliProvider(KeyRingBaseProvider):
    """Provider which uses `keyring` cli

    Instead of calling the keyring package installed alongside pip
    we call keyring on the command line which will enable pip to
    use which ever installation of keyring is available first in
    PATH.
    """
    has_keyring: bool
    keyring: Incomplete
    def __init__(self, cmd: str) -> None: ...
    def get_auth_info(self, url: str, username: str | None) -> AuthInfo | None: ...
    def save_auth_info(self, url: str, username: str, password: str) -> None: ...

def get_keyring_provider(provider: str) -> KeyRingBaseProvider: ...

class MultiDomainBasicAuth(AuthBase):
    prompting: Incomplete
    index_urls: Incomplete
    passwords: Incomplete
    def __init__(self, prompting: bool = True, index_urls: List[str] | None = None, keyring_provider: str = 'auto') -> None: ...
    @property
    def keyring_provider(self) -> KeyRingBaseProvider: ...
    @keyring_provider.setter
    def keyring_provider(self, provider: str) -> None: ...
    @property
    def use_keyring(self) -> bool: ...
    def __call__(self, req: Request) -> Request: ...
    def handle_401(self, resp: Response, **kwargs: Any) -> Response: ...
    def warn_on_401(self, resp: Response, **kwargs: Any) -> None:
        """Response callback to warn about incorrect credentials."""
    def save_credentials(self, resp: Response, **kwargs: Any) -> None:
        """Response callback to save credentials on success."""

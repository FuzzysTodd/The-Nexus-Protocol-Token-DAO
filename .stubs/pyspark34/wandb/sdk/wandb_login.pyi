import enum
from ..apis import InternalApi as InternalApi
from .internal.internal_api import Api as Api
from .lib import apikey as apikey
from .wandb_settings import Settings as Settings, Source as Source
from _typeshed import Incomplete
from typing import Literal
from wandb.errors import UsageError as UsageError

def login(anonymous: Literal['must', 'allow', 'never'] | None = None, key: str | None = None, relogin: bool | None = None, host: str | None = None, force: bool | None = None, timeout: int | None = None) -> bool:
    '''Log in to W&B.

    Arguments:
        anonymous: (string, optional) Can be "must", "allow", or "never".
            If set to "must" we\'ll always log in anonymously, if set to
            "allow" we\'ll only create an anonymous user if the user
            isn\'t already logged in.
        key: (string, optional) authentication key.
        relogin: (bool, optional) If true, will re-prompt for API key.
        host: (string, optional) The host to connect to.
        force: (bool, optional) If true, will force a relogin.
        timeout: (int, optional) Number of seconds to wait for user input.

    Returns:
        bool: if key is configured

    Raises:
        UsageError - if api_key cannot be configured and no tty
    '''

class ApiKeyStatus(enum.Enum):
    VALID: int
    NOTTY: int
    OFFLINE: int
    DISABLED: int

class _WandbLogin:
    kwargs: Incomplete
    def __init__(self) -> None: ...
    def setup(self, kwargs) -> None: ...
    def is_apikey_configured(self): ...
    def set_backend(self, backend) -> None: ...
    def set_silent(self, silent: bool): ...
    def set_entity(self, entity: str): ...
    def login(self): ...
    def login_display(self) -> None: ...
    def configure_api_key(self, key) -> None: ...
    def update_session(self, key: str | None, status: ApiKeyStatus = ...) -> None: ...
    def prompt_api_key(self) -> None: ...
    def propogate_login(self) -> None: ...

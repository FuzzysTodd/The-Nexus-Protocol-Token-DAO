from .token_utils import TokenUtils as TokenUtils
from _typeshed import Incomplete
from typing import Any, NamedTuple

class AccessToken(NamedTuple):
    """Represents an OAuth access token."""
    token: str
    expires_on: int

class FabricCredential:
    token_utils: Incomplete
    def __init__(self) -> None: ...
    def get_token(self, *scopes: str, **kwargs: Any): ...

class OnelakeTokenCrendential:
    pbienv: Incomplete
    def __init__(self, pbienv: str, **kwargs) -> None: ...
    def get_token(self, *scopes, **kwargs) -> AccessToken: ...

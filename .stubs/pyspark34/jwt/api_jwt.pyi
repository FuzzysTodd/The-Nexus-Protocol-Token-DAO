import json
from . import api_jws as api_jws
from .algorithms import AllowedPrivateKeys as AllowedPrivateKeys, AllowedPublicKeys as AllowedPublicKeys
from .exceptions import DecodeError as DecodeError, ExpiredSignatureError as ExpiredSignatureError, ImmatureSignatureError as ImmatureSignatureError, InvalidAudienceError as InvalidAudienceError, InvalidIssuedAtError as InvalidIssuedAtError, InvalidIssuerError as InvalidIssuerError, MissingRequiredClaimError as MissingRequiredClaimError
from .warnings import RemovedInPyjwt3Warning as RemovedInPyjwt3Warning
from _typeshed import Incomplete
from collections.abc import Iterable
from datetime import timedelta
from typing import Any

class PyJWT:
    options: Incomplete
    def __init__(self, options: dict[str, Any] | None = None) -> None: ...
    def encode(self, payload: dict[str, Any], key: AllowedPrivateKeys | str | bytes, algorithm: str | None = 'HS256', headers: dict[str, Any] | None = None, json_encoder: type[json.JSONEncoder] | None = None, sort_headers: bool = True) -> str: ...
    def decode_complete(self, jwt: str | bytes, key: AllowedPublicKeys | str | bytes = '', algorithms: list[str] | None = None, options: dict[str, Any] | None = None, verify: bool | None = None, detached_payload: bytes | None = None, audience: str | Iterable[str] | None = None, issuer: str | None = None, leeway: float | timedelta = 0, **kwargs: Any) -> dict[str, Any]: ...
    def decode(self, jwt: str | bytes, key: AllowedPublicKeys | str | bytes = '', algorithms: list[str] | None = None, options: dict[str, Any] | None = None, verify: bool | None = None, detached_payload: bytes | None = None, audience: str | Iterable[str] | None = None, issuer: str | None = None, leeway: float | timedelta = 0, **kwargs: Any) -> Any: ...

encode: Incomplete
decode_complete: Incomplete
decode: Incomplete

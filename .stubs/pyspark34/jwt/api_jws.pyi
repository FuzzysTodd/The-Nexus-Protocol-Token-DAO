import json
from .algorithms import Algorithm as Algorithm, AllowedPrivateKeys as AllowedPrivateKeys, AllowedPublicKeys as AllowedPublicKeys, get_default_algorithms as get_default_algorithms, has_crypto as has_crypto, requires_cryptography as requires_cryptography
from .exceptions import DecodeError as DecodeError, InvalidAlgorithmError as InvalidAlgorithmError, InvalidSignatureError as InvalidSignatureError, InvalidTokenError as InvalidTokenError
from .utils import base64url_decode as base64url_decode, base64url_encode as base64url_encode
from .warnings import RemovedInPyjwt3Warning as RemovedInPyjwt3Warning
from _typeshed import Incomplete
from typing import Any

class PyJWS:
    header_typ: str
    options: Incomplete
    def __init__(self, algorithms: list[str] | None = None, options: dict[str, Any] | None = None) -> None: ...
    def register_algorithm(self, alg_id: str, alg_obj: Algorithm) -> None:
        """
        Registers a new Algorithm for use when creating and verifying tokens.
        """
    def unregister_algorithm(self, alg_id: str) -> None:
        """
        Unregisters an Algorithm for use when creating and verifying tokens
        Throws KeyError if algorithm is not registered.
        """
    def get_algorithms(self) -> list[str]:
        """
        Returns a list of supported values for the 'alg' parameter.
        """
    def get_algorithm_by_name(self, alg_name: str) -> Algorithm:
        '''
        For a given string name, return the matching Algorithm object.

        Example usage:

        >>> jws_obj.get_algorithm_by_name("RS256")
        '''
    def encode(self, payload: bytes, key: AllowedPrivateKeys | str | bytes, algorithm: str | None = 'HS256', headers: dict[str, Any] | None = None, json_encoder: type[json.JSONEncoder] | None = None, is_payload_detached: bool = False, sort_headers: bool = True) -> str: ...
    def decode_complete(self, jwt: str | bytes, key: AllowedPublicKeys | str | bytes = '', algorithms: list[str] | None = None, options: dict[str, Any] | None = None, detached_payload: bytes | None = None, **kwargs) -> dict[str, Any]: ...
    def decode(self, jwt: str | bytes, key: AllowedPublicKeys | str | bytes = '', algorithms: list[str] | None = None, options: dict[str, Any] | None = None, detached_payload: bytes | None = None, **kwargs) -> Any: ...
    def get_unverified_header(self, jwt: str | bytes) -> dict[str, Any]:
        """Returns back the JWT header parameters as a dict()

        Note: The signature is not verified so the header parameters
        should not be fully trusted until signature verification is complete
        """

encode: Incomplete
decode_complete: Incomplete
decode: Incomplete
register_algorithm: Incomplete
unregister_algorithm: Incomplete
get_algorithm_by_name: Incomplete
get_unverified_header: Incomplete

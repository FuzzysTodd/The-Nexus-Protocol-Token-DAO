import typing
from _typeshed import Incomplete
from cryptography.exceptions import InternalError as InternalError
from cryptography.hazmat.bindings._rust import openssl as openssl
from cryptography.hazmat.bindings.openssl._conditional import CONDITIONAL_NAMES as CONDITIONAL_NAMES

def build_conditional_library(lib: typing.Any, conditional_names: typing.Dict[str, typing.Callable[[], typing.List[str]]]) -> typing.Any: ...

class Binding:
    """
    OpenSSL API wrapper.
    """
    lib: typing.ClassVar
    ffi: Incomplete
    def __init__(self) -> None: ...
    @classmethod
    def init_static_locks(cls) -> None: ...

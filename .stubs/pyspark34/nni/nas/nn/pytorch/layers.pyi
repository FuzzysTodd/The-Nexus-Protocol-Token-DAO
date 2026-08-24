from ._layers import *
from _typeshed import Incomplete

nn_cache_file_path: Incomplete
cache_version: int

def validate_cache() -> bool: ...
def generate_stub_file() -> str: ...
def write_cache(code: str) -> None: ...

code: Incomplete

from _typeshed import Incomplete
from collections.abc import Generator
from jedi.inference.helpers import is_big_annoying_library as is_big_annoying_library
from jedi.inference.names import ParamNameWrapper as ParamNameWrapper
from jedi.inference.utils import to_list as to_list

def process_params(param_names, star_count: int = 3) -> Generator[Incomplete, Incomplete, None]: ...

class ParamNameFixedKind(ParamNameWrapper):
    def __init__(self, param_name, new_kind) -> None: ...
    def get_kind(self): ...

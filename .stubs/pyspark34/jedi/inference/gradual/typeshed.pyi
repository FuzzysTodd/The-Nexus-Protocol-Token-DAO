from _typeshed import Incomplete
from jedi import settings as settings
from jedi.file_io import FileIO as FileIO
from jedi.inference.base_value import NO_VALUES as NO_VALUES, ValueSet as ValueSet
from jedi.inference.gradual.stub_value import StubModuleValue as StubModuleValue, TypingModuleWrapper as TypingModuleWrapper
from jedi.inference.value import ModuleValue as ModuleValue
from jedi.parser_utils import get_cached_code_lines as get_cached_code_lines
from typing import NamedTuple

TYPESHED_PATH: Incomplete
DJANGO_INIT_PATH: Incomplete

class PathInfo(NamedTuple):
    path: Incomplete
    is_third_party: Incomplete

def import_module_decorator(func): ...
def try_to_load_stub_cached(inference_state, import_names, *args, **kwargs): ...
def parse_stub_module(inference_state, file_io): ...
def create_stub_module(inference_state, grammar, python_value_set, stub_module_node, file_io, import_names): ...

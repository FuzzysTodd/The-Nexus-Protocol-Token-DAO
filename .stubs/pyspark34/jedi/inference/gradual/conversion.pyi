from jedi import debug as debug
from jedi.inference.base_value import NO_VALUES as NO_VALUES, ValueSet as ValueSet
from jedi.inference.gradual.stub_value import StubModuleValue as StubModuleValue
from jedi.inference.gradual.typeshed import try_to_load_stub_cached as try_to_load_stub_cached
from jedi.inference.utils import to_list as to_list
from jedi.inference.value.decorator import Decoratee as Decoratee

def convert_names(names, only_stubs: bool = False, prefer_stubs: bool = False, prefer_stub_to_compiled: bool = True): ...
def convert_values(values, only_stubs: bool = False, prefer_stubs: bool = False, ignore_compiled: bool = True): ...
def to_stub(value): ...

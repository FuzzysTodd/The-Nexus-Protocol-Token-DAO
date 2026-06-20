from .. import skipfiles as skipfiles, variables as variables
from ..allowed_functions import is_allowed as is_allowed
from ..exc import RestartAnalysis as RestartAnalysis, unimplemented as unimplemented
from ..guards import GuardBuilder as GuardBuilder
from ..mutation_guard import GenerationTracker as GenerationTracker
from ..source import AttrSource as AttrSource, GetItemSource as GetItemSource, NNModuleSource as NNModuleSource, NotNNModuleSource as NotNNModuleSource
from ..utils import is_lazy_module as is_lazy_module, is_safe_constant as is_safe_constant, istensor as istensor, istype as istype, proxy_args_kwargs as proxy_args_kwargs
from .base import MutableLocal as MutableLocal, VariableTracker as VariableTracker, typestr as typestr
from .functions import invoke_and_store_as_constant as invoke_and_store_as_constant
from .lists import SliceVariable as SliceVariable
from .user_defined import UserDefinedObjectVariable as UserDefinedObjectVariable
from _typeshed import Incomplete
from typing import Dict, List

class NNModuleVariable(VariableTracker):
    module_type: Incomplete
    module_key: Incomplete
    def __init__(self, module_type: type, module_key: str, **kwargs) -> None: ...
    def python_type(self): ...
    def unpack_var_sequence(self, tx): ...
    def call_hasattr(self, tx, name: str) -> VariableTracker: ...
    def is_training(self, tx): ...
    def convert_to_unspecialized(self, tx) -> None:
        """Restart analysis treating this module as an UnspecializedNNModuleVariable"""
    def var_getattr(self, tx, name): ...
    def call_function(self, tx, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker], constant: bool = False) -> VariableTracker: ...

class UnspecializedNNModuleVariable(UserDefinedObjectVariable):
    """
    The above class will specialize on the id() of a module and place
    parameters on the torch.fx.GraphModule.  Giving one graph per
    module instance.  This version treats nn.Modules() like other user
    defined objects and will pass parameters into the FX graph as inputs.
    Giving one graph per module class.
    """
    source: Incomplete
    def __init__(self, value, **kwargs) -> None: ...
    def unpack_var_sequence(self, tx): ...
    def call_function(self, tx, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

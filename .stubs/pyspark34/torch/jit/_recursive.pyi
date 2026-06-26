import torch
from _typeshed import Incomplete
from torch._sources import fake_range as fake_range
from torch.jit._check import AttributeTypeIsSupportedChecker as AttributeTypeIsSupportedChecker
from torch.jit.frontend import get_class_properties as get_class_properties, get_default_args as get_default_args, get_jit_class_def as get_jit_class_def, get_jit_def as get_jit_def
from torch.nn import Module as Module
from typing import Dict, List, NamedTuple, Set, Type

class ScriptMethodStub(NamedTuple):
    resolution_callback: Incomplete
    def_: Incomplete
    original_method: Incomplete

class PropertyStub(NamedTuple):
    resolution_callback: Incomplete
    def_: Incomplete

ignored_attributes: Incomplete

def make_stub(func, name): ...
def make_stub_from_method(nn_module, method_name): ...
def make_stubs_from_exported_methods(mod): ...
def jit_ignored_properties(module): ...

class SourceContext(torch._C._jit_tree_views.SourceRangeFactory):
    def __init__(self, source, filename, file_lineno, leading_whitespace_len) -> None: ...

def infer_concrete_type_builder(nn_module, share_types: bool = True):
    """
    Build a ConcreteModuleTypeBuilder from an nn.Module. This
    ConcreteModuleType doesn't have a JIT type associated with it yet, it
    must be filled in by the caller.
    """

class ConcreteTypeStore:
    type_store: Dict[Type[Module], List[torch._C.ConcreteModuleType]]
    methods_compiled: Set[torch._C.ConcreteModuleType]
    def __init__(self) -> None: ...
    def get_or_create_concrete_type(self, nn_module):
        """
        Infer a ConcreteType from this `nn.Module` instance. Underlying JIT
        types are re-used if possible.
        """

concrete_type_store: Incomplete

def create_methods_and_properties_from_stubs(concrete_type, method_stubs, property_stubs) -> None: ...
def create_hooks_from_stubs(concrete_type, hook_stubs, pre_hook_stubs) -> None: ...
def get_module_concrete_type(nn_module, share_types: bool = True):
    """
    Gets a concrete type for nn_modules. If share_types is True, the concrete
    type is fetched from concrete_type_store. If it is False, a new concrete type
    is created without first searching concrete_type_store.

    Args:
        nn_module:  The original Python nn.Module that we are creating a ScriptModule for.
        share_types = Whether to share underlying JIT types between modules (if possible).

    Returns:
        A concrete type for nn_module.
    """
def create_script_class(obj):
    """
    Create and return a RecursiveScriptClass instance from a Python object.

    Arguments:
        obj: A Python object.
    """
def create_script_module(nn_module, stubs_fn, share_types: bool = True, is_tracing: bool = False):
    """
    Creates a new ScriptModule from an nn.Module

    Args:
        nn_module:  The original Python nn.Module that we are creating a ScriptModule for.
        stubs_fn:  Lambda that takes an nn.Module and generates a list of ScriptMethodStubs to compile.
        share_types:  Whether to share underlying JIT types between modules (if possible).
            NOTE: Only set to False this when we cannot guarantee type sharing will work
                correctly. This only happens today for traced modules, where the same
                module can produce different traced methods depending on the inputs.
        is_tracing: Whether this function is called during tracing or scripting. If tracing,
                we don't need to do AttributeTypeIsSupportedChecker because all the unsupported
                attributes will be baked as constant in the tracing graph. In addition,
                this check significantly slows down the traced modules when the module size is big.
    """
def create_script_module_impl(nn_module, concrete_type, stubs_fn):
    """
    Convert an nn.Module to a RecursiveScriptModule.

    Args:
        nn_module:  The original Python nn.Module that we are creating a ScriptModule for.
        concrete_type:  The fully initialized ConcreteType of the module.
        stubs_fn:  Lambda that takes an nn.Module and generates a list of ScriptMethodStubs to compile.
    """
def script_model_defines_attr(script_model, attr): ...
def add_python_attr_to_scripted_model(script_model, orig, attr) -> None: ...
def get_overload_annotations(mod, jit_ignored_properties): ...
def get_overload_name_mapping(overload_info): ...
def make_stubs_for_overloads(overload_info): ...
def check_module_initialized(mod) -> None: ...
def infer_methods_to_compile(nn_module):
    """
    Implements the default rules for which methods should act as starting
    points for compilation (TODO add a link when the rules are published).
    """
def get_hook_stubs(nn_module):
    """
    Returns forward hook and pre_hook ScriptModuleStubs
    """
def get_property_stubs(nn_module):
    """
    Create property stubs for the properties of the module by creating method
    stubs for the getter and setter.
    """
def interface_script(mod_interface, nn_module):
    """
    Makes a ScriptModule from an nn.Module, using the interface methods rule for
    determining which methods to compile.

    Args:
        mod_interface: the interface type that the module have
        nn_module:  The original Python nn.Module that we are creating a ScriptModule for.
    """
def try_compile_fn(fn, loc): ...
def wrap_cpp_class(cpp_class):
    """
    Wrap this torch._C.Object in a Python RecursiveScriptClass.
    """
def wrap_cpp_module(cpp_module):
    """
    Wrap this torch._C.ScriptModule in a Python ScriptModule, recursively for all submodules
    """
def compile_unbound_method(concrete_type, fn): ...
def lazy_bind(concrete_type, unbound_method):
    """
    Returns a function that lazily binds `unbound_method` to a provided
    Module IValue, then invokes the method. We do this so that any Python
    shenanigans that will poison type sharing are impossible at compile
    time.
    """

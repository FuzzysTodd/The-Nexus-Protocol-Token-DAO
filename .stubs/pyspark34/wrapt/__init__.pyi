from .arguments import formatargspec as formatargspec
from .decorators import AdapterFactory as AdapterFactory, adapter_factory as adapter_factory, decorator as decorator, synchronized as synchronized
from .importer import discover_post_import_hooks as discover_post_import_hooks, notify_module_loaded as notify_module_loaded, register_post_import_hook as register_post_import_hook, when_imported as when_imported
from .wrappers import BoundFunctionWrapper as BoundFunctionWrapper, CallableObjectProxy as CallableObjectProxy, FunctionWrapper as FunctionWrapper, ObjectProxy as ObjectProxy, PartialCallableObjectProxy as PartialCallableObjectProxy, WeakFunctionProxy as WeakFunctionProxy, apply_patch as apply_patch, function_wrapper as function_wrapper, patch_function_wrapper as patch_function_wrapper, resolve_path as resolve_path, transient_function_wrapper as transient_function_wrapper, wrap_function_wrapper as wrap_function_wrapper, wrap_object as wrap_object, wrap_object_attribute as wrap_object_attribute
from _typeshed import Incomplete
from inspect import getcallargs as getcallargs

__version_info__: Incomplete
__version__: Incomplete

import contextlib
from _typeshed import Incomplete
from types import ModuleType

CONFIG_TYPES: Incomplete

def install_config_module(module) -> None:
    """
    Converts a module-level config into a `ConfigModule()`
    """

class ConfigModule(ModuleType):
    def __init__(self) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __getattr__(self, name): ...
    def __delattr__(self, name) -> None: ...
    def save_config(self):
        """Convert config to a pickled blob"""
    def load_config(self, data) -> None:
        """Restore from a prior call to save_config()"""
    def to_dict(self): ...
    def patch(self, arg1: Incomplete | None = None, arg2: Incomplete | None = None, **kwargs):
        '''
        Decorator and/or context manager to make temporary changes to a config.

        As a decorator:

            @config.patch("name", val)
            @config.patch(name1=val1, name2=val2):
            @config.patch({"name1": val1, "name2", val2})
            def foo(...):
                ...

        As a context manager:

            with config.patch("name", val):
                ...
        '''

class ContextDecorator(contextlib.ContextDecorator):
    """
    Same as contextlib.ContextDecorator, but with support for
    `unittest.TestCase`
    """
    def __call__(self, func): ...

class SubConfigProxy:
    '''
    Shim to redirect to main config.
    `config.triton.cudagraphs` maps to _config["triton.cudagraphs"]
    '''
    def __init__(self, config, prefix) -> None: ...
    def __setattr__(self, name, value): ...
    def __getattr__(self, name): ...
    def __delattr__(self, name): ...

def patch_object(obj, name, value):
    """
    Workaround `mock.patch.object` issue with ConfigModule
    """

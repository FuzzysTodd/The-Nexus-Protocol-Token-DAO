from _typeshed import Incomplete
from tensorflow.python.eager import monitoring as monitoring
from tensorflow.python.util import fast_module_type as fast_module_type, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.tools.compatibility import all_renames_v2 as all_renames_v2

FastModuleType: Incomplete
compat_v1_usage_gauge: Incomplete

def get_rename_v2(name): ...
def contains_deprecation_decorator(decorators): ...
def has_deprecation_decorator(symbol):
    """Checks if given object has a deprecation decorator.

  We check if deprecation decorator is in decorators as well as
  whether symbol is a class whose __init__ method has a deprecation
  decorator.
  Args:
    symbol: Python object.

  Returns:
    True if symbol has deprecation decorator.
  """

class TFModuleWrapper(FastModuleType):
    """Wrapper for TF modules to support deprecation messages and lazyloading."""
    compat_v1_usage_recorded: bool
    def __init__(self, wrapped, module_name, public_apis: Incomplete | None = None, deprecation: bool = True, has_lite: bool = False) -> None: ...
    def __setattr__(self, arg, val) -> None: ...
    def __dir__(self): ...
    def __delattr__(self, name) -> None: ...
    def __reduce__(self): ...

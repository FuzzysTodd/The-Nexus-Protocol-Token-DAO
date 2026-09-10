from _typeshed import Incomplete
from tensorflow.python.util import tf_decorator as tf_decorator, tf_inspect as tf_inspect
from typing import NamedTuple

ESTIMATOR_API_NAME: str
KERAS_API_NAME: str
TENSORFLOW_API_NAME: str
SUBPACKAGE_NAMESPACES: Incomplete

class _Attributes(NamedTuple):
    names: Incomplete
    constants: Incomplete

API_ATTRS: Incomplete
API_ATTRS_V1: Incomplete

class SymbolAlreadyExposedError(Exception):
    """Raised when adding API names to symbol that already has API names."""
class InvalidSymbolNameError(Exception):
    """Raised when trying to export symbol as an invalid or unallowed name."""

def get_symbol_from_name(name): ...
def get_canonical_name_for_symbol(symbol, api_name=..., add_prefix_to_v1_names: bool = False):
    """Get canonical name for the API symbol.

  Example:
  ```python
  from tensorflow.python.util import tf_export
  cls = tf_export.get_symbol_from_name('keras.optimizers.Adam')

  # Gives `<class 'keras.optimizer_v2.adam.Adam'>`
  print(cls)

  # Gives `keras.optimizers.Adam`
  print(tf_export.get_canonical_name_for_symbol(cls, api_name='keras'))
  ```

  Args:
    symbol: API function or class.
    api_name: API name (tensorflow or estimator).
    add_prefix_to_v1_names: Specifies whether a name available only in V1
      should be prefixed with compat.v1.

  Returns:
    Canonical name for the API symbol (for e.g. initializers.zeros) if
    canonical name could be determined. Otherwise, returns None.
  """
def get_canonical_name(api_names, deprecated_api_names):
    """Get preferred endpoint name.

  Args:
    api_names: API names iterable.
    deprecated_api_names: Deprecated API names iterable.
  Returns:
    Returns one of the following in decreasing preference:
    - first non-deprecated endpoint
    - first endpoint
    - None
  """
def get_v1_names(symbol):
    """Get a list of TF 1.* names for this symbol.

  Args:
    symbol: symbol to get API names for.

  Returns:
    List of all API names for this symbol including TensorFlow and
    Estimator names.
  """
def get_v2_names(symbol):
    """Get a list of TF 2.0 names for this symbol.

  Args:
    symbol: symbol to get API names for.

  Returns:
    List of all API names for this symbol including TensorFlow and
    Estimator names.
  """
def get_v1_constants(module):
    """Get a list of TF 1.* constants in this module.

  Args:
    module: TensorFlow module.

  Returns:
    List of all API constants under the given module including TensorFlow and
    Estimator constants.
  """
def get_v2_constants(module):
    """Get a list of TF 2.0 constants in this module.

  Args:
    module: TensorFlow module.

  Returns:
    List of all API constants under the given module including TensorFlow and
    Estimator constants.
  """

class api_export:
    """Provides ways to export symbols to the TensorFlow API."""
    def __init__(self, *args, **kwargs) -> None:
        """Export under the names *args (first one is considered canonical).

    Args:
      *args: API names in dot delimited format.
      **kwargs: Optional keyed arguments.
        v1: Names for the TensorFlow V1 API. If not set, we will use V2 API
          names both for TensorFlow V1 and V2 APIs.
        overrides: List of symbols that this is overriding
          (those overrided api exports will be removed). Note: passing overrides
          has no effect on exporting a constant.
        api_name: Name of the API you want to generate (e.g. `tensorflow` or
          `estimator`). Default is `tensorflow`.
        allow_multiple_exports: Allow symbol to be exported multiple time under
          different names.
    """
    def __call__(self, func):
        """Calls this decorator.

    Args:
      func: decorated symbol (function or class).

    Returns:
      The input function with _tf_api_names attribute set.

    Raises:
      SymbolAlreadyExposedError: Raised when a symbol already has API names
        and kwarg `allow_multiple_exports` not set.
    """
    def set_attr(self, func, api_names_attr, names) -> None: ...
    def export_constant(self, module_name, name) -> None:
        '''Store export information for constants/string literals.

    Export information is stored in the module where constants/string literals
    are defined.

    e.g.
    ```python
    foo = 1
    bar = 2
    tf_export("consts.foo").export_constant(__name__, \'foo\')
    tf_export("consts.bar").export_constant(__name__, \'bar\')
    ```

    Args:
      module_name: (string) Name of the module to store constant at.
      name: (string) Current constant name.
    '''

def kwarg_only(f):
    """A wrapper that throws away all non-kwarg arguments."""

tf_export: Incomplete
keras_export: Incomplete

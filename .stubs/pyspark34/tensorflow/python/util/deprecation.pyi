from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.util import decorator_utils as decorator_utils, is_in_graph_mode as is_in_graph_mode, tf_contextlib as tf_contextlib, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import NamedTuple

class DeprecatedNamesAlreadySet(Exception):
    """Raised when setting deprecated names multiple times for the same symbol."""

def deprecated_alias(deprecated_name, name, func_or_class, warn_once: bool = True):
    """Deprecate a symbol in favor of a new name with identical semantics.

  This function is meant to be used when defining a backwards-compatibility
  alias for a symbol which has been moved. For example:

  module1.py:
  ```python
  class NewNameForClass: pass
  ```

  module2.py:
  ```python
  import module1

  DeprecatedNameForClass = deprecated_alias(
    deprecated_name='module2.DeprecatedNameForClass',
    name='module1.NewNameForClass',
    func_or_class=module1.NewNameForClass)
  ```

  This function works for classes and functions.

  For classes, it creates a new class which is functionally identical (it
  inherits from the original, and overrides its constructor), but which prints
  a deprecation warning when an instance is created. It also adds a deprecation
  notice to the class' docstring.

  For functions, it returns a function wrapped by `tf_decorator.make_decorator`.
  That function prints a warning when used, and has a deprecation notice in its
  docstring. This is more or less equivalent (the deprecation warning has
  slightly different text) to writing:

  ```python
  @deprecated
  def deprecated_alias(original_args):
    real_function(original_args)
  ```

  Args:
    deprecated_name: The name of the symbol that is being deprecated, to be used
      in the warning message. This should be its fully qualified name to avoid
      confusion.
    name: The name of the symbol that is to be used instead of the deprecated
      name. This should be a fully qualified name to avoid confusion.
    func_or_class: The (non-deprecated) class or function for which a deprecated
      alias should be created.
    warn_once: If True (the default), only print a deprecation warning the first
      time this function is used, or the class is instantiated.

  Returns:
    A wrapped version of `func_or_class` which prints a deprecation warning on
    use and has a modified docstring.
  """
def deprecated_endpoints(*args):
    """Decorator for marking endpoints deprecated.

  This decorator does not print deprecation messages.
  TODO(annarev): eventually start printing deprecation warnings when
  @deprecation_endpoints decorator is added.

  Args:
    *args: Deprecated endpoint names.

  Returns:
    A function that takes symbol as an argument and adds
    _tf_deprecated_api_names to that symbol.
    _tf_deprecated_api_names would be set to a list of deprecated
    endpoint names for the symbol.
  """
def deprecated(date, instructions, warn_once: bool = True):
    """Decorator for marking functions or methods deprecated.

  This decorator logs a deprecation warning whenever the decorated function is
  called. It has the following format:

    <function> (from <module>) is deprecated and will be removed after <date>.
    Instructions for updating:
    <instructions>

  If `date` is None, 'after <date>' is replaced with 'in a future version'.
  <function> will include the class name if it is a method.

  It also edits the docstring of the function: ' (deprecated)' is appended
  to the first line of the docstring and a deprecation notice is prepended
  to the rest of the docstring.

  Args:
    date: String or None. The date the function is scheduled to be removed. Must
      be ISO 8601 (YYYY-MM-DD), or None.
    instructions: String. Instructions on how to update code using the
      deprecated function.
    warn_once: Boolean. Set to `True` to warn only the first time the decorated
      function is called. Otherwise, every call will log a warning.

  Returns:
    Decorated function or method.

  Raises:
    ValueError: If date is not None or in ISO 8601 format, or instructions are
      empty.
  """

class DeprecatedArgSpec(NamedTuple):
    position: Incomplete
    has_ok_value: Incomplete
    ok_value: Incomplete

def deprecated_args(date, instructions, *deprecated_arg_names_or_tuples, **kwargs):
    """Decorator for marking specific function arguments as deprecated.

  This decorator logs a deprecation warning whenever the decorated function is
  called with the deprecated argument. It has the following format:

    Calling <function> (from <module>) with <arg> is deprecated and will be
    removed after <date>. Instructions for updating:
      <instructions>

  If `date` is None, 'after <date>' is replaced with 'in a future version'.
  <function> includes the class name if it is a method.

  It also edits the docstring of the function: ' (deprecated arguments)' is
  appended to the first line of the docstring and a deprecation notice is
  prepended to the rest of the docstring.

  Args:
    date: String or None. The date the function is scheduled to be removed. Must
      be ISO 8601 (YYYY-MM-DD), or None.
    instructions: String. Instructions on how to update code using the
      deprecated function.
    *deprecated_arg_names_or_tuples: String or 2-Tuple (String, ok_val).  The
      string is the deprecated argument name. Optionally, an ok-value may be
      provided.  If the user provided argument equals this value, the warning is
      suppressed.
    **kwargs: If `warn_once=False` is passed, every call with a deprecated
      argument will log a warning. The default behavior is to only warn the
      first time the function is called with any given deprecated argument. All
      other kwargs raise `ValueError`.

  Returns:
    Decorated function or method.

  Raises:
    ValueError: If date is not None or in ISO 8601 format, instructions are
      empty, the deprecated arguments are not present in the function
      signature, the second element of a deprecated_tuple is not a
      list, or if a kwarg other than `warn_once` is passed.
  """
def deprecated_arg_values(date, instructions, warn_once: bool = True, **deprecated_kwargs):
    """Decorator for marking specific function argument values as deprecated.

  This decorator logs a deprecation warning whenever the decorated function is
  called with the deprecated argument values. It has the following format:

    Calling <function> (from <module>) with <arg>=<value> is deprecated and
    will be removed after <date>. Instructions for updating:
      <instructions>

  If `date` is None, 'after <date>' is replaced with 'in a future version'.
  <function> will include the class name if it is a method.

  It also edits the docstring of the function: ' (deprecated arguments)' is
  appended to the first line of the docstring and a deprecation notice is
  prepended to the rest of the docstring.

  Args:
    date: String or None. The date the function is scheduled to be removed. Must
      be ISO 8601 (YYYY-MM-DD), or None
    instructions: String. Instructions on how to update code using the
      deprecated function.
    warn_once: If `True`, warn only the first time this function is called with
      deprecated argument values. Otherwise, every call (with a deprecated
      argument value) will log a warning.
    **deprecated_kwargs: The deprecated argument values.

  Returns:
    Decorated function or method.

  Raises:
    ValueError: If date is not None or in ISO 8601 format, or instructions are
      empty.
  """
def deprecated_argument_lookup(new_name, new_value, old_name, old_value):
    """Looks up deprecated argument name and ensures both are not used.

  Args:
    new_name: new name of argument
    new_value: value of new argument (or None if not used)
    old_name: old name of argument
    old_value: value of old argument (or None if not used)

  Returns:
    The effective argument that should be used.
  Raises:
    ValueError: if new_value and old_value are both non-null
  """
def rewrite_argument_docstring(old_doc, old_argument, new_argument): ...
def silence() -> Generator[None, None, None]:
    """Temporarily silence deprecation warnings."""
def deprecate_moved_module(deprecated_name, new_module, deletion_version):
    '''Logs a warning when a module that has been moved to a new location is used.

  Copy the following code into the old module:

  ```
  import deprecation
  import new_module

  __getattr__ = deprecation.deprecate_moved_module(
      __name__, new_module, "2.9")  # adjust version number.
  ```

  Args:
    deprecated_name: Name of old module.
    new_module: Module to replace the old module.
    deletion_version: Version of TensorFlow in which the old module will be
      removed.

  Returns:
    A function that logs a warning and returns the symbol from the new module.
    Set this function as the module\'s `__getattr__`.
  '''

class HiddenTfApiAttribute(property):
    """Hides a class attribute from the public API.

  Attributes in public classes can be hidden from the API by having an '_' in
  front of the name (e.g. ClassName._variables). This doesn't work when
  attributes or methods are inherited from a parent class. To hide inherited
  attributes, set their values to be `deprecation.hide_attribute_from_api`.
  For example, this is used in V2 Estimator to hide the deprecated
  export_savedmodel method:
    class EstimatorV2(Estimator):
       export_savedmodel = deprecation.hide_attribute_from_api('...')
  """
    def __init__(self, deprecation_message) -> None: ...
hide_attribute_from_api = HiddenTfApiAttribute
HIDDEN_ATTRIBUTE: Incomplete

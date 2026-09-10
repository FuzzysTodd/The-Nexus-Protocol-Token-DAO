class OptionsBase:
    """Base class for representing a set of tf.data options.

  Attributes:
    _options: Stores the option values.
  """
    def __init__(self) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __setattr__(self, name, value) -> None: ...

def graph_rewrites(): ...
def create_option(name, ty, docstring, default_factory=...):
    """Creates a type-checked property.

  Args:
    name: The name to use.
    ty: The type to use. The type of the property will be validated when it
      is set.
    docstring: The docstring to use.
    default_factory: A callable that takes no arguments and returns a default
      value to use if not set.

  Returns:
    A type-checked property.
  """
def merge_options(*options_list):
    """Merges the given options, returning the result as a new options object.

  The input arguments are expected to have a matching type that derives from
  `tf.data.OptionsBase` (and thus each represent a set of options). The method
  outputs an object of the same type created by merging the sets of options
  represented by the input arguments.

  If an option is set to different values by different options objects, the
  result will match the setting of the options object that appears in the input
  list last.

  If an option is an instance of `tf.data.OptionsBase` itself, then this method
  is applied recursively to the set of options represented by this option.

  Args:
    *options_list: options to merge

  Raises:
    TypeError: if the input arguments are incompatible or not derived from
      `tf.data.OptionsBase`

  Returns:
    A new options object which is the result of merging the given options.
  """

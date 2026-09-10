from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.framework import ops as ops
from tensorflow.python.platform import tf_logging as tf_logging

def collect(val, collections, default_collections) -> None:
    """Adds keys to a collection.

  Args:
    val: The value to add per each key.
    collections: A collection of keys to add.
    default_collections: Used if collections is None.
  """
def clean_tag(name):
    """Cleans a tag. Removes illegal characters for instance.

  Args:
    name: The original tag name to be processed.

  Returns:
    The cleaned tag name.
  """
def summary_scope(name, family: Incomplete | None = None, default_name: Incomplete | None = None, values: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Enters a scope used for the summary and yields both the name and tag.

  To ensure that the summary tag name is always unique, we create a name scope
  based on `name` and use the full scope name in the tag.

  If `family` is set, then the tag name will be '<family>/<scope_name>', where
  `scope_name` is `<outer_scope>/<family>/<name>`. This ensures that `family`
  is always the prefix of the tag (and unmodified), while ensuring the scope
  respects the outer scope from this summary was created.

  Args:
    name: A name for the generated summary node.
    family: Optional; if provided, used as the prefix of the summary tag name.
    default_name: Optional; if provided, used as default name of the summary.
    values: Optional; passed as `values` parameter to name_scope.

  Yields:
    A tuple `(tag, scope)`, both of which are unique and should be used for the
    tag and the scope for the summary to output.
  """

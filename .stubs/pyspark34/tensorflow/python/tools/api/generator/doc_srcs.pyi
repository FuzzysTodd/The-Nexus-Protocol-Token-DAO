from _typeshed import Incomplete
from tensorflow.python.util import tf_export as tf_export

class DocSource:
    """Specifies docstring source for a module.

  Only one of docstring or docstring_module_name should be set.
  * If docstring is set, then we will use this docstring when
    for the module.
  * If docstring_module_name is set, then we will copy the docstring
    from docstring source module.
  """
    docstring: Incomplete
    docstring_module_name: Incomplete
    def __init__(self, docstring: Incomplete | None = None, docstring_module_name: Incomplete | None = None) -> None: ...

def get_doc_sources(api_name):
    """Get a map from module to a DocSource object.

  Args:
    api_name: API you want to generate (e.g. `tensorflow` or `estimator`).

  Returns:
    Map from module name to DocSource object.
  """

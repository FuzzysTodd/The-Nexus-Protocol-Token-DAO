from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.framework import api_def_pb2 as api_def_pb2, op_def_pb2 as op_def_pb2
from tensorflow.python.util import compat as compat, tf_contextlib as tf_contextlib

class AlreadyGarbageCollectedError(Exception):
    def __init__(self, name, obj_type) -> None: ...

class UniquePtr:
    """Wrapper around single-ownership C-API objects that handles deletion."""
    name: Incomplete
    deleter: Incomplete
    type_name: Incomplete
    def __init__(self, name, obj, deleter) -> None: ...
    def get(self) -> Generator[Incomplete, None, None]:
        """Yields the managed C-API Object, guaranteeing aliveness.

    This is a context manager. Inside the context the C-API object is
    guaranteed to be alive.

    Raises:
      AlreadyGarbageCollectedError: if the object is already deleted.
    """
    def __del__(self) -> None: ...

class ScopedTFStatus:
    """Wrapper around TF_Status that handles deletion."""
    status: Incomplete
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...

class ScopedTFGraph(UniquePtr):
    """Wrapper around TF_Graph that handles deletion."""
    def __init__(self, name) -> None: ...

class ScopedTFImportGraphDefOptions:
    """Wrapper around TF_ImportGraphDefOptions that handles deletion."""
    options: Incomplete
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...

class ScopedTFImportGraphDefResults:
    """Wrapper around TF_ImportGraphDefOptions that handles deletion."""
    results: Incomplete
    def __init__(self, results) -> None: ...
    def __del__(self) -> None: ...

class ScopedTFFunction(UniquePtr):
    """Wrapper around TF_Function that handles deletion."""
    def __init__(self, func, name) -> None: ...

class ScopedTFBuffer:
    """An internal class to help manage the TF_Buffer lifetime."""
    buffer: Incomplete
    def __init__(self, buf_string) -> None: ...
    def __del__(self) -> None: ...

class ApiDefMap:
    """Wrapper around Tf_ApiDefMap that handles querying and deletion.

  The OpDef protos are also stored in this class so that they could
  be queried by op name.
  """
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...
    def put_api_def(self, text) -> None: ...
    def get_api_def(self, op_name): ...
    def get_op_def(self, op_name): ...
    def op_names(self): ...

def tf_buffer(data: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Context manager that creates and deletes TF_Buffer.

  Example usage:
    with tf_buffer() as buf:
      # get serialized graph def into buf
      ...
      proto_data = c_api.TF_GetBuffer(buf)
      graph_def.ParseFromString(compat.as_bytes(proto_data))
    # buf has been deleted

    with tf_buffer(some_string) as buf:
      c_api.TF_SomeFunction(buf)
    # buf has been deleted

  Args:
    data: An optional `bytes`, `str`, or `unicode` object. If not None, the
      yielded buffer will contain this data.

  Yields:
    Created TF_Buffer
  """
def tf_output(c_op, index):
    """Returns a wrapped TF_Output with specified operation and index.

  Args:
    c_op: wrapped TF_Operation
    index: integer

  Returns:
    Wrapped TF_Output
  """
def tf_operations(graph) -> Generator[Incomplete, None, None]:
    """Generator that yields every TF_Operation in `graph`.

  Args:
    graph: Graph

  Yields:
    wrapped TF_Operation
  """
def new_tf_operations(graph) -> Generator[Incomplete, None, None]:
    """Generator that yields newly-added TF_Operations in `graph`.

  Specifically, yields TF_Operations that don't have associated Operations in
  `graph`. This is useful for processing nodes added by the C API.

  Args:
    graph: Graph

  Yields:
    wrapped TF_Operation
  """

from _typeshed import Incomplete

PY2: Incomplete
PY26: Incomplete
PY27: Incomplete
PY275: Incomplete
PY3: Incomplete
PY34: Incomplete
string_types: Incomplete
binary_types: Incomplete
range_func = range
memoryview_type = memoryview
struct_bool_decl: str

def import_numpy():
    """
    Returns the numpy module if it exists on the system,
    otherwise returns None.
    """

class NumpyRequiredForThisFeature(RuntimeError):
    """
    Error raised when user tries to use a feature that
    requires numpy without having numpy installed.
    """

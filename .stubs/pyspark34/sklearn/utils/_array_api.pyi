from .._config import get_config as get_config
from .fixes import parse_version as parse_version
from _typeshed import Incomplete

def device(x):
    '''Hardware device the array data resides on.

    Parameters
    ----------
    x : array
        Array instance from NumPy or an array API compatible library.

    Returns
    -------
    out : device
        `device` object (see the "Device Support" section of the array API spec).
    '''
def size(x):
    """Return the total number of elements of x.

    Parameters
    ----------
    x : array
        Array instance from NumPy or an array API compatible library.

    Returns
    -------
    out : int
        Total number of elements.
    """
def isdtype(dtype, kind, *, xp):
    '''Returns a boolean indicating whether a provided dtype is of type "kind".

    Included in the v2022.12 of the Array API spec.
    https://data-apis.org/array-api/latest/API_specification/generated/array_api.isdtype.html
    '''

class _ArrayAPIWrapper:
    """sklearn specific Array API compatibility wrapper

    This wrapper makes it possible for scikit-learn maintainers to
    deal with discrepancies between different implementations of the
    Python array API standard and its evolution over time.

    The Python array API standard specification:
    https://data-apis.org/array-api/latest/

    Documentation of the NumPy implementation:
    https://numpy.org/neps/nep-0047-array-api-standard.html
    """
    def __init__(self, array_namespace) -> None: ...
    def __getattr__(self, name): ...
    def take(self, X, indices, *, axis: int = 0): ...
    def isdtype(self, dtype, kind): ...

class _NumPyAPIWrapper:
    """Array API compat wrapper for any numpy version

    NumPy < 1.22 does not expose the numpy.array_api namespace. This
    wrapper makes it possible to write code that uses the standard
    Array API while working with any version of NumPy supported by
    scikit-learn.

    See the `get_namespace()` public function for more details.
    """
    def __getattr__(self, name): ...
    @property
    def bool(self): ...
    def astype(self, x, dtype, *, copy: bool = True, casting: str = 'unsafe'): ...
    def asarray(self, x, *, dtype: Incomplete | None = None, device: Incomplete | None = None, copy: Incomplete | None = None): ...
    def unique_inverse(self, x): ...
    def unique_counts(self, x): ...
    def unique_values(self, x): ...
    def concat(self, arrays, *, axis: Incomplete | None = None): ...
    def reshape(self, x, shape, *, copy: Incomplete | None = None):
        """Gives a new shape to an array without changing its data.

        The Array API specification requires shape to be a tuple.
        https://data-apis.org/array-api/latest/API_specification/generated/array_api.reshape.html
        """
    def isdtype(self, dtype, kind): ...

def get_namespace(*arrays):
    """Get namespace of arrays.

    Introspect `arrays` arguments and return their common Array API
    compatible namespace object, if any. NumPy 1.22 and later can
    construct such containers using the `numpy.array_api` namespace
    for instance.

    See: https://numpy.org/neps/nep-0047-array-api-standard.html

    If `arrays` are regular numpy arrays, an instance of the
    `_NumPyAPIWrapper` compatibility wrapper is returned instead.

    Namespace support is not enabled by default. To enabled it
    call:

      sklearn.set_config(array_api_dispatch=True)

    or:

      with sklearn.config_context(array_api_dispatch=True):
          # your code here

    Otherwise an instance of the `_NumPyAPIWrapper`
    compatibility wrapper is always returned irrespective of
    the fact that arrays implement the `__array_namespace__`
    protocol or not.

    Parameters
    ----------
    *arrays : array objects
        Array objects.

    Returns
    -------
    namespace : module
        Namespace shared by array objects. If any of the `arrays` are not arrays,
        the namespace defaults to NumPy.

    is_array_api_compliant : bool
        True if the arrays are containers that implement the Array API spec.
        Always False when array_api_dispatch=False.
    """

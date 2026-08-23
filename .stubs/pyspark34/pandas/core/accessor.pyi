from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Callable

class DirNamesMixin:
    def __dir__(self) -> list[str]:
        """
        Provide method name lookup and completion.

        Notes
        -----
        Only provide 'public' methods.
        """

class PandasDelegate:
    """
    Abstract base class for delegating methods/properties.
    """

def delegate_names(delegate, accessors: list[str], typ: str, overwrite: bool = False, accessor_mapping: Callable[[str], str] = ..., raise_on_missing: bool = True):
    '''
    Add delegated names to a class using a class decorator.  This provides
    an alternative usage to directly calling `_add_delegate_accessors`
    below a class definition.

    Parameters
    ----------
    delegate : object
        The class to get methods/properties & doc-strings.
    accessors : Sequence[str]
        List of accessor to add.
    typ : {\'property\', \'method\'}
    overwrite : bool, default False
       Overwrite the method/property in the target class if it exists.
    accessor_mapping: Callable, default lambda x: x
        Callable to map the delegate\'s function to the cls\' function.
    raise_on_missing: bool, default True
        Raise if an accessor does not exist on delegate.
        False skips the missing accessor.

    Returns
    -------
    callable
        A class decorator.

    Examples
    --------
    @delegate_names(Categorical, ["categories", "ordered"], "property")
    class CategoricalAccessor(PandasDelegate):
        [...]
    '''

class CachedAccessor:
    """
    Custom property-like object.

    A descriptor for caching accessors.

    Parameters
    ----------
    name : str
        Namespace that will be accessed under, e.g. ``df.foo``.
    accessor : cls
        Class with the extension methods.

    Notes
    -----
    For accessor, The class's __init__ method assumes that one of
    ``Series``, ``DataFrame`` or ``Index`` as the
    single argument ``data``.
    """
    def __init__(self, name: str, accessor) -> None: ...
    def __get__(self, obj, cls): ...

def register_dataframe_accessor(name): ...
def register_series_accessor(name): ...
def register_index_accessor(name): ...

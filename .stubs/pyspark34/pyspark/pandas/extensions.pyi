from pyspark.pandas._typing import T as T
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.indexes import Index as Index
from pyspark.pandas.series import Series as Series
from typing import Callable, Generic, Type

class CachedAccessor(Generic[T]):
    '''
    Custom property-like object.

    A descriptor for caching accessors:

    Parameters
    ----------
    name : str
        Namespace that accessor methods, properties, etc will be accessed under, e.g. "foo" for a
        dataframe accessor yields the accessor ``df.foo``
    accessor: cls
        Class with the extension methods.

    Notes
    -----
    For accessor, the class\'s __init__ method assumes that you are registering an accessor for one
    of ``Series``, ``DataFrame``, or ``Index``.

    This object is not meant to be instantiated directly. Instead, use register_dataframe_accessor,
    register_series_accessor, or register_index_accessor.

    The pandas-on-Spark accessor is modified based on pandas.core.accessor.
    '''
    def __init__(self, name: str, accessor: Type[T]) -> None: ...
    def __get__(self, obj: DataFrame | Series | Index | None, cls: Type[T]) -> T | Type[T]: ...

def register_dataframe_accessor(name: str) -> Callable[[Type[T]], Type[T]]:
    '''
    Register a custom accessor with a DataFrame

    Parameters
    ----------
    name : str
        name used when calling the accessor after its registered

    Returns
    -------
    callable
        A class decorator.

    See Also
    --------
    register_series_accessor: Register a custom accessor on Series objects
    register_index_accessor: Register a custom accessor on Index objects

    Notes
    -----
    When accessed, your accessor will be initialized with the pandas-on-Spark object the user
    is interacting with. The accessor\'s init method should always ingest the object being accessed.
    See the examples for the init signature.

    In the pandas API, if data passed to your accessor has an incorrect dtype, it\'s recommended to
    raise an ``AttributeError`` for consistency purposes. In pandas-on-Spark, ``ValueError`` is more
    frequently used to annotate when a value\'s datatype is unexpected for a given method/function.

    Ultimately, you can structure this however you like, but pandas-on-Spark would likely do
    something like this:

    >>> ps.Series([\'a\', \'b\']).dt
    ...
    Traceback (most recent call last):
        ...
    ValueError: Cannot call DatetimeMethods on type StringType()

    Examples
    --------
    In your library code::

        from pyspark.pandas.extensions import register_dataframe_accessor

        @register_dataframe_accessor("geo")
        class GeoAccessor:

            def __init__(self, pandas_on_spark_obj):
                self._obj = pandas_on_spark_obj
                # other constructor logic

            @property
            def center(self):
                # return the geographic center point of this DataFrame
                lat = self._obj.latitude
                lon = self._obj.longitude
                return (float(lon.mean()), float(lat.mean()))

            def plot(self):
                # plot this array\'s data on a map
                pass

    Then, in an ipython session::

        >>> ## Import if the accessor is in the other file.
        >>> # from my_ext_lib import GeoAccessor
        >>> psdf = ps.DataFrame({"longitude": np.linspace(0,10),
        ...                     "latitude": np.linspace(0, 20)})
        >>> psdf.geo.center  # doctest: +SKIP
        (5.0, 10.0)

        >>> psdf.geo.plot()  # doctest: +SKIP
    '''
def register_series_accessor(name: str) -> Callable[[Type[T]], Type[T]]:
    '''
    Register a custom accessor with a Series object

    Parameters
    ----------
    name : str
        name used when calling the accessor after its registered

    Returns
    -------
    callable
        A class decorator.

    See Also
    --------
    register_dataframe_accessor: Register a custom accessor on DataFrame objects
    register_index_accessor: Register a custom accessor on Index objects

    Notes
    -----
    When accessed, your accessor will be initialized with the pandas-on-Spark object the user is
    interacting with. The code signature must be::

        def __init__(self, pandas_on_spark_obj):
            # constructor logic
        ...

    In the pandas API, if data passed to your accessor has an incorrect dtype, it\'s recommended to
    raise an ``AttributeError`` for consistency purposes. In pandas-on-Spark, ``ValueError`` is more
    frequently used to annotate when a value\'s datatype is unexpected for a given method/function.

    Ultimately, you can structure this however you like, but pandas-on-Spark would likely do
    something like this:

    >>> ps.Series([\'a\', \'b\']).dt
    ...
    Traceback (most recent call last):
        ...
    ValueError: Cannot call DatetimeMethods on type StringType()

    Examples
    --------
    In your library code::

        from pyspark.pandas.extensions import register_series_accessor

        @register_series_accessor("geo")
        class GeoAccessor:

            def __init__(self, pandas_on_spark_obj):
                self._obj = pandas_on_spark_obj

            @property
            def is_valid(self):
                # boolean check to see if series contains valid geometry
                return True

    Then, in an ipython session::

        >>> ## Import if the accessor is in the other file.
        >>> # from my_ext_lib import GeoAccessor
        >>> psdf = ps.DataFrame({"longitude": np.linspace(0,10),
        ...                     "latitude": np.linspace(0, 20)})
        >>> psdf.longitude.geo.is_valid  # doctest: +SKIP
        True
    '''
def register_index_accessor(name: str) -> Callable[[Type[T]], Type[T]]:
    '''
    Register a custom accessor with an Index

    Parameters
    ----------
    name : str
        name used when calling the accessor after its registered

    Returns
    -------
    callable
        A class decorator.

    See Also
    --------
    register_dataframe_accessor: Register a custom accessor on DataFrame objects
    register_series_accessor: Register a custom accessor on Series objects

    Notes
    -----
    When accessed, your accessor will be initialized with the pandas-on-Spark object the user is
    interacting with. The code signature must be::

        def __init__(self, pandas_on_spark_obj):
            # constructor logic
        ...

    In the pandas API, if data passed to your accessor has an incorrect dtype, it\'s recommended to
    raise an ``AttributeError`` for consistency purposes. In pandas-on-Spark, ``ValueError`` is more
    frequently used to annotate when a value\'s datatype is unexpected for a given method/function.

    Ultimately, you can structure this however you like, but pandas-on-Spark would likely do
    something like this:

    >>> ps.Series([\'a\', \'b\']).dt
    ...
    Traceback (most recent call last):
        ...
    ValueError: Cannot call DatetimeMethods on type StringType()

    Examples
    --------
    In your library code::

        from pyspark.pandas.extensions import register_index_accessor

        @register_index_accessor("foo")
        class CustomAccessor:

            def __init__(self, pandas_on_spark_obj):
                self._obj = pandas_on_spark_obj
                self.item = "baz"

            @property
            def bar(self):
                # return item value
                return self.item

    Then, in an ipython session::

        >>> ## Import if the accessor is in the other file.
        >>> # from my_ext_lib import CustomAccessor
        >>> psdf = ps.DataFrame({"longitude": np.linspace(0,10),
        ...                     "latitude": np.linspace(0, 20)})
        >>> psdf.index.foo.bar  # doctest: +SKIP
        \'baz\'
    '''

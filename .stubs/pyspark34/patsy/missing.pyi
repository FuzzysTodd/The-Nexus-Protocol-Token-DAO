from _typeshed import Incomplete

__all__ = ['NAAction']

class NAAction:
    '''An :class:`NAAction` object defines a strategy for handling missing
    data.

    "NA" is short for "Not Available", and is used to refer to any value which
    is somehow unmeasured or unavailable. In the long run, it is devoutly
    hoped that numpy will gain first-class missing value support. Until then,
    we work around this lack as best we\'re able.

    There are two parts to this: First, we have to determine what counts as
    missing data. For numerical data, the default is to treat NaN values
    (e.g., ``numpy.nan``) as missing. For categorical data, the default is to
    treat NaN values, and also the Python object None, as missing. (This is
    consistent with how pandas does things, so if you\'re already using
    None/NaN to mark missing data in your pandas DataFrames, you\'re good to
    go.)

    Second, we have to decide what to do with any missing data when we
    encounter it. One option is to simply discard any rows which contain
    missing data from our design matrices (``drop``). Another option is to
    raise an error (``raise``). A third option would be to simply let the
    missing values pass through into the returned design matrices. However,
    this last option is not yet implemented, because of the lack of any
    standard way to represent missing values in arbitrary numpy matrices;
    we\'re hoping numpy will get this sorted out before we standardize on
    anything ourselves.

    You can control how patsy handles missing data through the ``NA_action=``
    argument to functions like :func:`build_design_matrices` and
    :func:`dmatrix`. If all you want to do is to choose between ``drop`` and
    ``raise`` behaviour, you can pass one of those strings as the
    ``NA_action=`` argument directly. If you want more fine-grained control
    over how missing values are detected and handled, then you can create an
    instance of this class, or your own object that implements the same
    interface, and pass that as the ``NA_action=`` argument instead.
    '''
    on_NA: Incomplete
    NA_types: Incomplete
    def __init__(self, on_NA: str = 'drop', NA_types=['None', 'NaN']) -> None:
        '''The :class:`NAAction` constructor takes the following arguments:

        :arg on_NA: How to handle missing values. The default is ``"drop"``,
          which removes all rows from all matrices which contain any missing
          values. Also available is ``"raise"``, which raises an exception
          when any missing values are encountered.
        :arg NA_types: Which rules are used to identify missing values, as a
          list of strings. Allowed values are:

          * ``"None"``: treat the ``None`` object as missing in categorical
            data.
          * ``"NaN"``: treat floating point NaN values as missing in
            categorical and numerical data.

        .. versionadded:: 0.2.0
        '''
    def is_categorical_NA(self, obj):
        """Return True if `obj` is a categorical NA value.

        Note that here `obj` is a single scalar value."""
    def is_numerical_NA(self, arr):
        """Returns a 1-d mask array indicating which rows in an array of
        numerical values contain at least one NA value.

        Note that here `arr` is a numpy array or pandas DataFrame."""
    def handle_NA(self, values, is_NAs, origins):
        """Takes a set of factor values that may have NAs, and handles them
        appropriately.

        :arg values: A list of `ndarray` objects representing the data.
          These may be 1- or 2-dimensional, and may be of varying dtype. All
          will have the same number of rows (or entries, for 1-d arrays).
        :arg is_NAs: A list with the same number of entries as `values`,
          containing boolean `ndarray` objects that indicate which rows
          contain NAs in the corresponding entry in `values`.
        :arg origins: A list with the same number of entries as
          `values`, containing information on the origin of each
          value. If we encounter a problem with some particular value, we use
          the corresponding entry in `origins` as the origin argument when
          raising a :class:`PatsyError`.
        :returns: A list of new values (which may have a differing number of
          rows.)
        """

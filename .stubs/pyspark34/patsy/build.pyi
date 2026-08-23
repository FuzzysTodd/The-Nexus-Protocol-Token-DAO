from _typeshed import Incomplete

__all__ = ['design_matrix_builders', 'build_design_matrices']

class _MockFactor:
    def __init__(self, name: str = 'MOCKMOCK') -> None: ...
    def eval(self, state, env): ...
    def name(self): ...

def design_matrix_builders(termlists, data_iter_maker, eval_env, NA_action: str = 'drop'):
    """Construct several :class:`DesignInfo` objects from termlists.

    This is one of Patsy's fundamental functions. This function and
    :func:`build_design_matrices` together form the API to the core formula
    interpretation machinery.

    :arg termlists: A list of termlists, where each termlist is a list of
      :class:`Term` objects which together specify a design matrix.
    :arg data_iter_maker: A zero-argument callable which returns an iterator
      over dict-like data objects. This must be a callable rather than a
      simple iterator because sufficiently complex formulas may require
      multiple passes over the data (e.g. if there are nested stateful
      transforms).
    :arg eval_env: Either a :class:`EvalEnvironment` which will be used to
      look up any variables referenced in `termlists` that cannot be
      found in `data_iter_maker`, or else a depth represented as an
      integer which will be passed to :meth:`EvalEnvironment.capture`.
      ``eval_env=0`` means to use the context of the function calling
      :func:`design_matrix_builders` for lookups. If calling this function
      from a library, you probably want ``eval_env=1``, which means that
      variables should be resolved in *your* caller's namespace.
    :arg NA_action: An :class:`NAAction` object or string, used to determine
      what values count as 'missing' for purposes of determining the levels of
      categorical factors.
    :returns: A list of :class:`DesignInfo` objects, one for each
      termlist passed in.

    This function performs zero or more iterations over the data in order to
    sniff out any necessary information about factor types, set up stateful
    transforms, pick column names, etc.

    See :ref:`formulas` for details.

    .. versionadded:: 0.2.0
       The ``NA_action`` argument.
    .. versionadded:: 0.4.0
       The ``eval_env`` argument.
    """

class _CheckMatch:
    value: Incomplete
    def __init__(self, name, eq_fn) -> None: ...
    def check(self, seen_value, desc, origin) -> None: ...

def build_design_matrices(design_infos, data, NA_action: str = 'drop', return_type: str = 'matrix', dtype=...):
    '''Construct several design matrices from :class:`DesignMatrixBuilder`
    objects.

    This is one of Patsy\'s fundamental functions. This function and
    :func:`design_matrix_builders` together form the API to the core formula
    interpretation machinery.

    :arg design_infos: A list of :class:`DesignInfo` objects describing the
      design matrices to be built.
    :arg data: A dict-like object which will be used to look up data.
    :arg NA_action: What to do with rows that contain missing values. You can
      ``"drop"`` them, ``"raise"`` an error, or for customization, pass an
      :class:`NAAction` object. See :class:`NAAction` for details on what
      values count as \'missing\' (and how to alter this).
    :arg return_type: Either ``"matrix"`` or ``"dataframe"``. See below.
    :arg dtype: The dtype of the returned matrix. Useful if you want to use
      single-precision or extended-precision.

    This function returns either a list of :class:`DesignMatrix` objects (for
    ``return_type="matrix"``) or a list of :class:`pandas.DataFrame` objects
    (for ``return_type="dataframe"``). In both cases, all returned design
    matrices will have ``.design_info`` attributes containing the appropriate
    :class:`DesignInfo` objects.

    Note that unlike :func:`design_matrix_builders`, this function takes only
    a simple data argument, not any kind of iterator. That\'s because this
    function doesn\'t need a global view of the data -- everything that depends
    on the whole data set is already encapsulated in the ``design_infos``. If
    you are incrementally processing a large data set, simply call this
    function for each chunk.

    Index handling: This function always checks for indexes in the following
    places:

    * If ``data`` is a :class:`pandas.DataFrame`, its ``.index`` attribute.
    * If any factors evaluate to a :class:`pandas.Series` or
      :class:`pandas.DataFrame`, then their ``.index`` attributes.

    If multiple indexes are found, they must be identical (same values in the
    same order). If no indexes are found, then a default index is generated
    using ``np.arange(num_rows)``. One way or another, we end up with a single
    index for all the data. If ``return_type="dataframe"``, then this index is
    used as the index of the returned DataFrame objects. Examining this index
    makes it possible to determine which rows were removed due to NAs.

    Determining the number of rows in design matrices: This is not as obvious
    as it might seem, because it\'s possible to have a formula like "~ 1" that
    doesn\'t depend on the data (it has no factors). For this formula, it\'s
    obvious what every row in the design matrix should look like (just the
    value ``1``); but, how many rows like this should there be? To determine
    the number of rows in a design matrix, this function always checks in the
    following places:

    * If ``data`` is a :class:`pandas.DataFrame`, then its number of rows.
    * The number of entries in any factors present in any of the design
    * matrices being built.

    All these values much match. In particular, if this function is called to
    generate multiple design matrices at once, then they must all have the
    same number of rows.

    .. versionadded:: 0.2.0
       The ``NA_action`` argument.

    '''

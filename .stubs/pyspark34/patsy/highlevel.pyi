__all__ = ['dmatrix', 'dmatrices', 'incr_dbuilder', 'incr_dbuilders']

def incr_dbuilder(formula_like, data_iter_maker, eval_env: int = 0, NA_action: str = 'drop'):
    """Construct a design matrix builder incrementally from a large data set.

    :arg formula_like: Similar to :func:`dmatrix`, except that explicit
      matrices are not allowed. Must be a formula string, a
      :class:`ModelDesc`, a :class:`DesignInfo`, or an object with a
      ``__patsy_get_model_desc__`` method.
    :arg data_iter_maker: A zero-argument callable which returns an iterator
      over dict-like data objects. This must be a callable rather than a
      simple iterator because sufficiently complex formulas may require
      multiple passes over the data (e.g. if there are nested stateful
      transforms).
    :arg eval_env: Either a :class:`EvalEnvironment` which will be used to
      look up any variables referenced in `formula_like` that cannot be
      found in `data`, or else a depth represented as an
      integer which will be passed to :meth:`EvalEnvironment.capture`.
      ``eval_env=0`` means to use the context of the function calling
      :func:`incr_dbuilder` for lookups. If calling this function from a
      library, you probably want ``eval_env=1``, which means that variables
      should be resolved in *your* caller's namespace.
    :arg NA_action: An :class:`NAAction` object or string, used to determine
      what values count as 'missing' for purposes of determining the levels of
      categorical factors.
    :returns: A :class:`DesignInfo`

    Tip: for `data_iter_maker`, write a generator like::

      def iter_maker():
          for data_chunk in my_data_store:
              yield data_chunk

    and pass `iter_maker` (*not* `iter_maker()`).

    .. versionadded:: 0.2.0
       The ``NA_action`` argument.
    """
def incr_dbuilders(formula_like, data_iter_maker, eval_env: int = 0, NA_action: str = 'drop'):
    """Construct two design matrix builders incrementally from a large data
    set.

    :func:`incr_dbuilders` is to :func:`incr_dbuilder` as :func:`dmatrices` is
    to :func:`dmatrix`. See :func:`incr_dbuilder` for details.
    """
def dmatrix(formula_like, data={}, eval_env: int = 0, NA_action: str = 'drop', return_type: str = 'matrix'):
    '''Construct a single design matrix given a formula_like and data.

    :arg formula_like: An object that can be used to construct a design
      matrix. See below.
    :arg data: A dict-like object that can be used to look up variables
      referenced in `formula_like`.
    :arg eval_env: Either a :class:`EvalEnvironment` which will be used to
      look up any variables referenced in `formula_like` that cannot be
      found in `data`, or else a depth represented as an
      integer which will be passed to :meth:`EvalEnvironment.capture`.
      ``eval_env=0`` means to use the context of the function calling
      :func:`dmatrix` for lookups. If calling this function from a library,
      you probably want ``eval_env=1``, which means that variables should be
      resolved in *your* caller\'s namespace.
    :arg NA_action: What to do with rows that contain missing values. You can
      ``"drop"`` them, ``"raise"`` an error, or for customization, pass an
      :class:`NAAction` object. See :class:`NAAction` for details on what
      values count as \'missing\' (and how to alter this).
    :arg return_type: Either ``"matrix"`` or ``"dataframe"``. See below.

    The `formula_like` can take a variety of forms. You can use any of the
    following:

    * (The most common option) A formula string like ``"x1 + x2"`` (for
      :func:`dmatrix`) or ``"y ~ x1 + x2"`` (for :func:`dmatrices`). For
      details see :ref:`formulas`.
    * A :class:`ModelDesc`, which is a Python object representation of a
      formula. See :ref:`formulas` and :ref:`expert-model-specification` for
      details.
    * A :class:`DesignInfo`.
    * An object that has a method called :meth:`__patsy_get_model_desc__`.
      For details see :ref:`expert-model-specification`.
    * A numpy array_like (for :func:`dmatrix`) or a tuple
      (array_like, array_like) (for :func:`dmatrices`). These will have
      metadata added, representation normalized, and then be returned
      directly. In this case `data` and `eval_env` are
      ignored. There is special handling for two cases:

      * :class:`DesignMatrix` objects will have their :class:`DesignInfo`
        preserved. This allows you to set up custom column names and term
        information even if you aren\'t using the rest of the patsy
        machinery.
      * :class:`pandas.DataFrame` or :class:`pandas.Series` objects will have
        their (row) indexes checked. If two are passed in, their indexes must
        be aligned. If ``return_type="dataframe"``, then their indexes will be
        preserved on the output.

    Regardless of the input, the return type is always either:

    * A :class:`DesignMatrix`, if ``return_type="matrix"`` (the default)
    * A :class:`pandas.DataFrame`, if ``return_type="dataframe"``.

    The actual contents of the design matrix is identical in both cases, and
    in both cases a :class:`DesignInfo` object will be available in a
    ``.design_info`` attribute on the return value. However, for
    ``return_type="dataframe"``, any pandas indexes on the input (either in
    `data` or directly passed through `formula_like`) will be preserved, which
    may be useful for e.g. time-series models.

    .. versionadded:: 0.2.0
       The ``NA_action`` argument.
    '''
def dmatrices(formula_like, data={}, eval_env: int = 0, NA_action: str = 'drop', return_type: str = 'matrix'):
    '''Construct two design matrices given a formula_like and data.

    This function is identical to :func:`dmatrix`, except that it requires
    (and returns) two matrices instead of one. By convention, the first matrix
    is the "outcome" or "y" data, and the second is the "predictor" or "x"
    data.

    See :func:`dmatrix` for details.
    '''

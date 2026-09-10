from _typeshed import Incomplete

__all__ = ['register_jax_array_methods']

class _IndexUpdateHelper:
    '''Helper property for index update functionality.

  The ``at`` property provides a functionally pure equivalent of in-place
  array modifications.

  In particular:

  ==============================  ================================
  Alternate syntax                Equivalent In-place expression
  ==============================  ================================
  ``x = x.at[idx].set(y)``        ``x[idx] = y``
  ``x = x.at[idx].add(y)``        ``x[idx] += y``
  ``x = x.at[idx].multiply(y)``   ``x[idx] *= y``
  ``x = x.at[idx].divide(y)``     ``x[idx] /= y``
  ``x = x.at[idx].power(y)``      ``x[idx] **= y``
  ``x = x.at[idx].min(y)``        ``x[idx] = minimum(x[idx], y)``
  ``x = x.at[idx].max(y)``        ``x[idx] = maximum(x[idx], y)``
  ``x = x.at[idx].apply(ufunc)``  ``ufunc.at(x, idx)``
  ``x = x.at[idx].get()``         ``x = x[idx]``
  ==============================  ================================

  None of the ``x.at`` expressions modify the original ``x``; instead they return
  a modified copy of ``x``. However, inside a :py:func:`~jax.jit` compiled function,
  expressions like :code:`x = x.at[idx].set(y)` are guaranteed to be applied in-place.

  Unlike NumPy in-place operations such as :code:`x[idx] += y`, if multiple
  indices refer to the same location, all updates will be applied (NumPy would
  only apply the last update, rather than applying all updates.) The order
  in which conflicting updates are applied is implementation-defined and may be
  nondeterministic (e.g., due to concurrency on some hardware platforms).

  By default, JAX assumes that all indices are in-bounds. Alternative out-of-bound
  index semantics can be specified via the ``mode`` parameter (see below).

  Arguments
  ---------
  mode : str
      Specify out-of-bound indexing mode. Options are:

      - ``"promise_in_bounds"``: (default) The user promises that indices are in bounds.
        No additional checking will be performed. In practice, this means that
        out-of-bounds indices in ``get()`` will be clipped, and out-of-bounds indices
        in ``set()``, ``add()``, etc. will be dropped.
      - ``"clip"``: clamp out of bounds indices into valid range.
      - ``"drop"``: ignore out-of-bound indices.
      - ``"fill"``: alias for ``"drop"``.  For `get()`, the optional ``fill_value``
        argument specifies the value that will be returned.

        See :class:`jax.lax.GatherScatterMode` for more details.

  indices_are_sorted : bool
      If True, the implementation will assume that the indices passed to ``at[]``
      are sorted in ascending order, which can lead to more efficient execution
      on some backends.
  unique_indices : bool
      If True, the implementation will assume that the indices passed to ``at[]``
      are unique, which can result in more efficient execution on some backends.
  fill_value : Any
      Only applies to the ``get()`` method: the fill value to return for out-of-bounds
      slices when `mode` is ``\'fill\'``. Ignored otherwise. Defaults to ``NaN`` for
      inexact types, the largest negative value for signed types, the largest positive
      value for unsigned types, and ``True`` for booleans.

  Examples
  --------
  >>> x = jnp.arange(5.0)
  >>> x
  Array([0., 1., 2., 3., 4.], dtype=float32)
  >>> x.at[2].add(10)
  Array([ 0.,  1., 12.,  3.,  4.], dtype=float32)
  >>> x.at[10].add(10)  # out-of-bounds indices are ignored
  Array([0., 1., 2., 3., 4.], dtype=float32)
  >>> x.at[20].add(10, mode=\'clip\')
  Array([ 0.,  1.,  2.,  3., 14.], dtype=float32)
  >>> x.at[2].get()
  Array(2., dtype=float32)
  >>> x.at[20].get()  # out-of-bounds indices clipped
  Array(4., dtype=float32)
  >>> x.at[20].get(mode=\'fill\')  # out-of-bounds indices filled with NaN
  Array(nan, dtype=float32)
  >>> x.at[20].get(mode=\'fill\', fill_value=-1)  # custom fill value
  Array(-1., dtype=float32)
  '''
    array: Incomplete
    def __init__(self, array) -> None: ...
    def __getitem__(self, index): ...

class _IndexUpdateRef:
    """Helper object to call indexed update functions for an (advanced) index.

  This object references a source array and a specific indexer into that array.
  Methods on this object return copies of the source array that have been
  modified at the positions specified by the indexer.
  """
    array: Incomplete
    index: Incomplete
    def __init__(self, array, index) -> None: ...
    def get(self, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: Incomplete | None = None, fill_value: Incomplete | None = None):
        """Equivalent to ``x[idx]``.

    Returns the value of ``x`` that would result from the NumPy-style
    :mod:indexing <numpy.doc.indexing>` ``x[idx]``. This function differs from
    the usual array indexing syntax in that it allows additional keyword
    arguments ``indices_are_sorted`` and ``unique_indices`` to be passed.

    See :mod:`jax.ops` for details.
    """
    def set(self, values, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: Incomplete | None = None):
        """Pure equivalent of ``x[idx] = y``.

    Returns the value of ``x`` that would result from the NumPy-style
    :mod:`indexed assignment <numpy.doc.indexing>` ``x[idx] = y``.

    See :mod:`jax.ops` for details.
    """
    def apply(self, func, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: Incomplete | None = None):
        """Pure equivalent of ``func.at(x, idx)`` for a unary ufunc ``func``.

    Returns the value of ``x`` that would result from applying the unary
    function ``func`` to ``x`` at the given indices. This is similar to
    ``x.at[idx].set(func(x[idx]))``, but differs in the case of repeated indices:
    in ``x.at[idx].apply(func)``, repeated indices result in the function being
    applied multiple times.

    Note that in the current implementation, ``scatter_apply`` is not compatible
    with automatic differentiation.

    See :mod:`jax.ops` for details.
    """
    def add(self, values, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: Incomplete | None = None):
        """Pure equivalent of ``x[idx] += y``.

    Returns the value of ``x`` that would result from the NumPy-style
    :mod:indexed assignment <numpy.doc.indexing>` ``x[idx] += y``.

    See :mod:`jax.ops` for details.
    """
    def multiply(self, values, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: Incomplete | None = None):
        """Pure equivalent of ``x[idx] *= y``.

    Returns the value of ``x`` that would result from the NumPy-style
    :mod:indexed assignment <numpy.doc.indexing>` ``x[idx] *= y``.

    See :mod:`jax.ops` for details.
    """
    mul = multiply
    def divide(self, values, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: Incomplete | None = None):
        """Pure equivalent of ``x[idx] /= y``.

    Returns the value of ``x`` that would result from the NumPy-style
    :mod:indexed assignment <numpy.doc.indexing>` ``x[idx] /= y``.

    See :mod:`jax.ops` for details.
    """
    def power(self, values, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: Incomplete | None = None):
        """Pure equivalent of ``x[idx] **= y``.

    Returns the value of ``x`` that would result from the NumPy-style
    :mod:indexed assignment <numpy.doc.indexing>` ``x[idx] **= y``.

    See :mod:`jax.ops` for details.
    """
    def min(self, values, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: Incomplete | None = None):
        """Pure equivalent of ``x[idx] = minimum(x[idx], y)``.

    Returns the value of ``x`` that would result from the NumPy-style
    :mod:indexed assignment <numpy.doc.indexing>`
    ``x[idx] = minimum(x[idx], y)``.

    See :mod:`jax.ops` for details.
    """
    def max(self, values, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: Incomplete | None = None):
        """Pure equivalent of ``x[idx] = maximum(x[idx], y)``.

    Returns the value of ``x`` that would result from the NumPy-style
    :mod:indexed assignment <numpy.doc.indexing>`
    ``x[idx] = maximum(x[idx], y)``.

    See :mod:`jax.ops` for details.
    """

def register_jax_array_methods() -> None:
    """Call this function once to register methods of JAX arrays"""

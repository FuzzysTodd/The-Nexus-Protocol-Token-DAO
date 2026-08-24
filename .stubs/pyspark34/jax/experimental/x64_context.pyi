from collections.abc import Generator

def enable_x64(new_val: bool = True):
    """Experimental context manager to temporarily enable X64 mode.

  Usage::

    >>> x = np.arange(5, dtype='float64')
    >>> with enable_x64():
    ...   print(jnp.asarray(x).dtype)
    ...
    float64

  See Also
  --------
  jax.experimental.enable_x64 : temporarily enable X64 mode.
  """
def disable_x64() -> Generator[None, None, None]:
    """Experimental context manager to temporarily disable X64 mode.

  Usage::

    >>> x = np.arange(5, dtype='float64')
    >>> with disable_x64():
    ...   print(jnp.asarray(x).dtype)
    ...
    float32

  See Also
  --------
  jax.experimental.enable_x64 : temporarily enable X64 mode.
  """

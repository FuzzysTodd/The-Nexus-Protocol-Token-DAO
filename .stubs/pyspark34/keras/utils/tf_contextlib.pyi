def contextmanager(target):
    """A tf_decorator-aware wrapper for `contextlib.contextmanager`.

    Usage is identical to `contextlib.contextmanager`.

    Args:
      target: A callable to be wrapped in a contextmanager.
    Returns:
      A callable that can be used inside of a `with` statement.
    """

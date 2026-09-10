def lazy_load(name):
    """Decorator to define a function that lazily loads the module 'name'.

    This can be used to defer importing troublesome dependencies - e.g. ones that
    are large and infrequently used, or that cause a dependency cycle -
    until they are actually used.

    Args:
      name: the fully-qualified name of the module; typically the last segment
        of 'name' matches the name of the decorated function

    Returns:
      Decorator function that produces a lazy-loading module 'name' backed by the
      underlying decorated function.
    """

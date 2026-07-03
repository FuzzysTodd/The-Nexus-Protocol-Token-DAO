from tensorflow.python.util import decorator_utils as decorator_utils

def keyword_args_only(func):
    """Decorator for marking specific function accepting keyword args only.

  This decorator raises a `ValueError` if the input `func` is called with any
  non-keyword args. This prevents the caller from providing the arguments in
  wrong order.

  Args:
    func: The function or method needed to be decorated.

  Returns:
    Decorated function or method.

  Raises:
    ValueError: If `func` is not callable.
  """

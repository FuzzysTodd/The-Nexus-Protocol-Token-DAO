from tensorflow.python.util import tf_export

class estimator_export(tf_export.api_export):
    """Provides ways to export symbols to the TensorFlow Estimator API."""
    def __init__(self, *args, **kwargs) -> None:
        """Export under the names *args (first one is considered canonical).

    All symbols exported by this decorator are exported under the `estimator`
    API name.

    Args:
      *args: API names in dot delimited format.
      **kwargs: Optional keyed arguments.
        v1: Names for the TensorFlow V1 API. If not set, we will use V2 API
          names both for TensorFlow V1 and V2 APIs.
        overrides: List of symbols that this is overriding
          (those overrided api exports will be removed). Note: passing overrides
          has no effect on exporting a constant.
        allow_multiple_exports: Allow symbol to be exported multiple time under
          different names.
    """
    def __call__(self, func):
        """Calls this decorator.

    Args:
      func: decorated symbol (function or class).

    Returns:
      The input function with _tf_api_names attribute set and marked as
      deprecated.

    Raises:
      SymbolAlreadyExposedError: Raised when a symbol already has API names
        and kwarg `allow_multiple_exports` not set.
    """

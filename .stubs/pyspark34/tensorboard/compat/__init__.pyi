def tf():
    """Provide the root module of a TF-like API for use within TensorBoard.

    By default this is equivalent to `import tensorflow as tf`, but it can be used
    in combination with //tensorboard/compat:tensorflow (to fall back to a stub TF
    API implementation if the real one is not available) or with
    //tensorboard/compat:no_tensorflow (to force unconditional use of the stub).

    Returns:
      The root module of a TF-like API, if available.

    Raises:
      ImportError: if a TF-like API is not available.
    """
def tf2():
    """Provide the root module of a TF-2.0 API for use within TensorBoard.

    Returns:
      The root module of a TF-2.0 API, if available.

    Raises:
      ImportError: if a TF-2.0 API is not available.
    """

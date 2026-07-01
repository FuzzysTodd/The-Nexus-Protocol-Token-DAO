from tensorflow.python.ops.distributions import bijector

__all__ = ['Identity']

class Identity(bijector.Bijector):
    """Compute Y = g(X) = X.

    Example Use:

    ```python
    # Create the Y=g(X)=X transform which is intended for Tensors with 1 batch
    # ndim and 1 event ndim (i.e., vector of vectors).
    identity = Identity()
    x = [[1., 2],
         [3, 4]]
    x == identity.forward(x) == identity.inverse(x)
    ```

  """
    def __init__(self, validate_args: bool = False, name: str = 'identity') -> None: ...

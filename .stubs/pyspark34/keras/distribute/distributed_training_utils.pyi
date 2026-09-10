from _typeshed import Incomplete
from keras import backend as backend

FLAGS: Incomplete

def global_batch_size_supported(distribution_strategy): ...
def call_replica_local_fn(fn, *args, **kwargs):
    """Call a function that uses replica-local variables.

    This function correctly handles calling `fn` in a cross-replica
    context.

    Args:
      fn: The function to call.
      *args: Positional arguments to the `fn`.
      **kwargs: Keyword argument to `fn`.

    Returns:
      The result of calling `fn`.
    """
def is_distributed_variable(v):
    """Returns whether `v` is a distributed variable."""
def get_strategy():
    """Creates a `tf.distribute.Strategy` object from flags.

    Example usage:

    ```python
    strategy = utils.get_strategy()
    with strategy.scope():
      model = tf.keras.Sequential([tf.keras.layers.Dense(10)])

    model.compile(...)
    train_ds, test_ds = ...
    model.fit(train_ds, validation_data=test_ds, epochs=10)
    ```

    Returns:
      `tf.distribute.Strategy` instance.
    """
def maybe_preemption_handler_scope(model): ...

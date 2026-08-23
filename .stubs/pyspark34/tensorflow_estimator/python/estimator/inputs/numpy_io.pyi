from _typeshed import Incomplete
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.inputs.queues import feeding_functions as feeding_functions

def numpy_input_fn(x, y: Incomplete | None = None, batch_size: int = 128, num_epochs: int = 1, shuffle: Incomplete | None = None, queue_capacity: int = 1000, num_threads: int = 1):
    """Returns input function that would feed dict of numpy arrays into the model.

  This returns a function outputting `features` and `targets` based on the dict
  of numpy arrays. The dict `features` has the same keys as the `x`. The dict
  `targets` has the same keys as the `y` if `y` is a dict.

  Example:

  ```python
  age = np.arange(4) * 1.0
  height = np.arange(32, 36)
  x = {'age': age, 'height': height}
  y = np.arange(-32, -28)

  with tf.Session() as session:
    input_fn = numpy_io.numpy_input_fn(
        x, y, batch_size=2, shuffle=False, num_epochs=1)
  ```

  Args:
    x: numpy array object or dict of numpy array objects. If an array, the array
      will be treated as a single feature.
    y: numpy array object or dict of numpy array object. `None` if absent.
    batch_size: Integer, size of batches to return.
    num_epochs: Integer, number of epochs to iterate over data. If `None` will
      run forever.
    shuffle: Boolean, if True shuffles the queue. Avoid shuffle at prediction
      time.
    queue_capacity: Integer, size of queue to accumulate.
    num_threads: Integer, number of threads used for reading and enqueueing. In
      order to have predicted and repeatable order of reading and enqueueing,
      such as in prediction and evaluation mode, `num_threads` should be 1.

  Returns:
    Function, that has signature of ()->(dict of `features`, `targets`)

  Raises:
    ValueError: if the shape of `y` mismatches the shape of values in `x` (i.e.,
      values in `x` have same shape).
    ValueError: if duplicate keys are in both `x` and `y` when `y` is a dict.
    ValueError: if x or y is an empty dict.
    TypeError: `x` is not a dict or array.
    ValueError: if 'shuffle' is not provided or a bool.
  """

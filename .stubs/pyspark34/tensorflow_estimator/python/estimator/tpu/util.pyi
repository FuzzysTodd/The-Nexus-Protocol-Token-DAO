import tensorflow as tf
from _typeshed import Incomplete
from typing import NamedTuple

class IterationsPerLoopCounter(NamedTuple):
    value: Incomplete
    unit: Incomplete

def check_positive_integer(value, name) -> None:
    """Checks whether `value` is a positive integer."""
def parse_iterations_per_loop(iterations_per_loop):
    '''Parses the `iterations_per_loop` value.

  The parser expects the value of the `iterations_per_loop` value to be a
  positive integer value with unit:`count` or time-based value `<N><s|m|h>`
  where <N> is any positive integer and `s`, `m`, `h` are unit of time in
  seconds, minutes, hours respectively. Examples of valid values: `3600s`, `60m`
  , `1h`.

  Args:
    iterations_per_loop: Number of iterations or time alloted to spend on per
      device loop.

  Returns:
    A dictionary of `value` and `unit`. The `unit` value can be either a raw
    `count`, or time in `seconds`.
    {
      "value": <positive-integer>,
      "unit": <unit: `count` | `seconds`>
    }
  '''

class MultiHostDatasetInitializerHook(tf.compat.v1.train.SessionRunHook):
    """Creates a SessionRunHook that initializes all passed iterators."""
    def __init__(self, dataset_initializers) -> None: ...
    def after_create_session(self, session, coord) -> None: ...

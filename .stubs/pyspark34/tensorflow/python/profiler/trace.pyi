from tensorflow.python.util.tf_export import tf_export as tf_export

enabled: bool

class Trace:
    '''Context manager that generates a trace event in the profiler.

  A trace event will start when entering the context, and stop and save the
  result to the profiler when exiting the context. Open TensorBoard Profile tab
  and choose trace viewer to view the trace event in the timeline.

  Trace events are created only when the profiler is enabled. More information
  on how to use the profiler can be found at
  https://tensorflow.org/guide/profiler

  Example usage:
  ```python
  tf.profiler.experimental.start(\'logdir\')
  for step in range(num_steps):
    # Creates a trace event for each training step with the step number.
    with tf.profiler.experimental.Trace("Train", step_num=step, _r=1):
      train_fn()
  tf.profiler.experimental.stop()
  ```
  '''
    def __init__(self, name, **kwargs) -> None:
        '''Creates a trace event in the profiler.

    Args:
      name: The name of the trace event.
      **kwargs: Keyword arguments added to the trace event.
                Both the key and value are of types that
                can be converted to strings, which will be
                interpreted by the profiler according to the
                traceme name.

      Example usage:

      ```python

        tf.profiler.experimental.start(\'logdir\')
        for step in range(num_steps):
          # Creates a trace event for each training step with the
          # step number.
          with tf.profiler.experimental.Trace("Train", step_num=step):
            train_fn()
        tf.profiler.experimental.stop()

      ```
      The example above uses the keyword argument "step_num" to specify the
      training step being traced.
    '''
    def __enter__(self): ...
    def set_metadata(self, **kwargs) -> None:
        '''Sets metadata in this trace event.

    Args:
      **kwargs: metadata in key-value pairs.

    This method enables setting metadata in a trace event after it is
    created.

    Example usage:

    ```python

      def call(function):
        with tf.profiler.experimental.Trace("call",
             function_name=function.name) as tm:
          binary, in_cache = jit_compile(function)
          tm.set_metadata(in_cache=in_cache)
          execute(binary)

    ```
    In this example, we want to trace how much time spent on
    calling a function, which includes compilation and execution.
    The compilation can be either getting a cached copy of the
    binary or actually generating the binary, which is indicated
    by the boolean "in_cache" returned by jit_compile(). We need
    to use set_metadata() to pass in_cache because we did not know
    the in_cache value when the trace was created (and we cannot
    create the trace after jit_compile(), because we want
    to measure the entire duration of call()).
    '''
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

def trace_wrapper(trace_name, **trace_kwargs):
    """Decorator alternative to `with Trace(): ...`.  It's faster.

  Args:
    trace_name: The name of the trace event, or a callable to be traced, in
      which case the name is inferred from qualname or name of the callable.
    **trace_kwargs: Keyword arguments added to the trace event. Both the key and
      value are of types that can be converted to strings, which will be
      interpreted by the profiler according to the traceme name.

  Returns:
    A decorator that can wrap a function and apply `Trace` scope if needed,
    or a decorated function if used as a decorator directly.

  Example usage:
    ```python

    @trace_wrapper('trace_name')
    def func(x, y, z):
      pass  # code to execute and apply `Trace` if needed.

    # Equivalent to
    # with Trace('trace_name'):
    #   func(1, 2, 3)
    func(1, 2, 3)
    ```

  or
    ```python

    @trace_wrapper
    def func(x, y, z):
      pass  # code to execute and apply `Trace` if needed.

    # Equivalent to
    # with Trace(func.__qualname__):
    #   func(1, 2, 3)
    func(1, 2, 3)
    ```

  """

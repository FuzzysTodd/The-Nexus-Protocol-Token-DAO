from _typeshed import Incomplete

KERAS_VARIABLE_NAMES: Incomplete

def allow_initializer_layout(init_method):
    '''A decorator for injecting layout information to layer.__init__.

    Layout will be a new param for any of the weights for all the keras layers.
    Adding the param to all the __init__ method will be a big/duplicated work.

    This decorator is design to reduce and code duplication and make it easy to
    add/remove the dtensor feature if needed.

    Sample usage:
    ```python
    class Dense(tf.keras.layer.Layer):

      @allow_initializer_layout
      def __init__(self, units,
                   kernel_initializer=\'zeros\',
                   bias_initializer=\'zeros\',
                   **kwargs):
         super().__init__(**kwargs)

    d = Dense(units=8, kernel_layout=layout1, bias_layout=layout2)
    d.kernel_layout == layout1
    d.bias_layout == layout2
    ```

    By adding this annotation, it will:

    1. Filter out the kwargs based on some keywords, eg if the
      \'kernel_initialzer\' appears in method signature, then it will try to pop
      the \'kernel_layout\' if it presents. Same for "bias" and
      "recurrent_kernel", etc. This will make sure the layout related param is
      not passed to `BaseLayer.__init__`, which will raise error about unexpect
      keyword args.
    2. Set the self.kernel/bias_layout attribute after the `__init__` method is
       called. Keras framework will use those fields to create weights down the
       stream.

    Args:
      init_method: the `__init__` method of the Keras layer to annotate.

    Returns:
      the annotated __init__ method.
    '''
def inject_mesh(init_method):
    """Inject DTensor mesh information to an object.

    This is useful for keras object like `Metric` and `Optimizer` which need
    DTensor mesh to create the weights, but doesn't want to change the current
    public API interface.

    This is for temporary usage and eventually the mesh/layout information will
    be public arguments in the `__init__` method.

    Sample usage:
    ```python
    class Accuracy(tf.keras.metrics.Metric):

      @inject_mesh
      def __init__(self, name='accuracy', dtype=None):
         super().__init__(**kwargs)

      acc = Accuracy(mesh=mesh)
      assert acc._mesh == mesh
    ```

    Args:
      init_method: the `__init__` method of the Keras class to annotate.

    Returns:
      the annotated __init__ method.
    """
def call_with_layout(fn, layout, *args, **kwargs):
    """Invoke the function with inputs and relayout the result.

    Args:
      fn: the function to invoke.
      layout: if not None, the output of the fn will be relayout with this.
      *args: positional arguments to be called with fn.
      **kwargs: keyword arguments to be called with fn.

    Returns:
      The output of fn, with potential relayout with the layout specified.
    """

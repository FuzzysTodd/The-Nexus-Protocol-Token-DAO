import enum
from _typeshed import Incomplete
from tflite_runtime import metrics_portable as metrics

class Delegate:
    """Python wrapper class to manage TfLiteDelegate objects.

  The shared library is expected to have two functions,
  tflite_plugin_create_delegate and tflite_plugin_destroy_delegate,
  which should implement the API specified in
  tensorflow/lite/delegates/external/external_delegate_interface.h.
  """
    message: str
    def __init__(self, library, options: Incomplete | None = None) -> None:
        """Loads delegate from the shared library.

    Args:
      library: Shared library name.
      options: Dictionary of options that are required to load the delegate. All
        keys and values in the dictionary should be serializable. Consult the
        documentation of the specific delegate for required and legal options.
        (default None)

    Raises:
      RuntimeError: This is raised if the Python implementation is not CPython.
    """
    def __del__(self) -> None: ...

def load_delegate(library, options: Incomplete | None = None):
    """Returns loaded Delegate object.

  Example usage:

  ```
  import tensorflow as tf

  try:
    delegate = tf.lite.experimental.load_delegate('delegate.so')
  except ValueError:
    // Fallback to CPU

  if delegate:
    interpreter = tf.lite.Interpreter(
        model_path='model.tflite',
        experimental_delegates=[delegate])
  else:
    interpreter = tf.lite.Interpreter(model_path='model.tflite')
  ```

  This is typically used to leverage EdgeTPU for running TensorFlow Lite models.
  For more information see: https://coral.ai/docs/edgetpu/tflite-python/

  Args:
    library: Name of shared library containing the
      [TfLiteDelegate](https://www.tensorflow.org/lite/performance/delegates).
    options: Dictionary of options that are required to load the delegate. All
      keys and values in the dictionary should be convertible to str. Consult
      the documentation of the specific delegate for required and legal options.
      (default None)

  Returns:
    Delegate object.

  Raises:
    ValueError: Delegate failed to load.
    RuntimeError: If delegate loading is used on unsupported platform.
  """

class SignatureRunner:
    '''SignatureRunner class for running TFLite models using SignatureDef.

  This class should be instantiated through TFLite Interpreter only using
  get_signature_runner method on Interpreter.
  Example,
  signature = interpreter.get_signature_runner("my_signature")
  result = signature(input_1=my_input_1, input_2=my_input_2)
  print(result["my_output"])
  print(result["my_second_output"])
  All names used are this specific SignatureDef names.

  Notes:
    No other function on this object or on the interpreter provided should be
    called while this object call has not finished.
  '''
    def __init__(self, interpreter: Incomplete | None = None, signature_key: Incomplete | None = None) -> None:
        """Constructor.

    Args:
      interpreter: Interpreter object that is already initialized with the
        requested model.
      signature_key: SignatureDef key to be used.
    """
    def __call__(self, **kwargs):
        """Runs the SignatureDef given the provided inputs in arguments.

    Args:
      **kwargs: key,value for inputs to the model. Key is the SignatureDef input
        name. Value is numpy array with the value.

    Returns:
      dictionary of the results from the model invoke.
      Key in the dictionary is SignatureDef output name.
      Value is the result Tensor.
    """
    def get_input_details(self):
        """Gets input tensor details.

    Returns:
      A dictionary from input name to tensor details where each item is a
      dictionary with details about an input tensor. Each dictionary contains
      the following fields that describe the tensor:

      + `name`: The tensor name.
      + `index`: The tensor index in the interpreter.
      + `shape`: The shape of the tensor.
      + `shape_signature`: Same as `shape` for models with known/fixed shapes.
        If any dimension sizes are unknown, they are indicated with `-1`.
      + `dtype`: The numpy data type (such as `np.int32` or `np.uint8`).
      + `quantization`: Deprecated, use `quantization_parameters`. This field
        only works for per-tensor quantization, whereas
        `quantization_parameters` works in all cases.
      + `quantization_parameters`: A dictionary of parameters used to quantize
        the tensor:
        ~ `scales`: List of scales (one if per-tensor quantization).
        ~ `zero_points`: List of zero_points (one if per-tensor quantization).
        ~ `quantized_dimension`: Specifies the dimension of per-axis
        quantization, in the case of multiple scales/zero_points.
      + `sparsity_parameters`: A dictionary of parameters used to encode a
        sparse tensor. This is empty if the tensor is dense.
    """
    def get_output_details(self):
        """Gets output tensor details.

    Returns:
      A dictionary from input name to tensor details where each item is a
      dictionary with details about an output tensor. The dictionary contains
      the same fields as described for `get_input_details()`.
    """

class OpResolverType(enum.Enum):
    '''Different types of op resolvers for Tensorflow Lite.

  * `AUTO`: Indicates the op resolver that is chosen by default in TfLite
     Python, which is the "BUILTIN" as described below.
  * `BUILTIN`: Indicates the op resolver for built-in ops with optimized kernel
    implementation.
  * `BUILTIN_REF`: Indicates the op resolver for built-in ops with reference
    kernel implementation. It\'s generally used for testing and debugging.
  * `BUILTIN_WITHOUT_DEFAULT_DELEGATES`: Indicates the op resolver for
    built-in ops with optimized kernel implementation, but it will disable
    the application of default TfLite delegates (like the XNNPACK delegate) to
    the model graph. Generally this should not be used unless there are issues
    with the default configuration.
  '''
    AUTO: int
    BUILTIN: int
    BUILTIN_REF: int
    BUILTIN_WITHOUT_DEFAULT_DELEGATES: int

class Interpreter:
    """Interpreter interface for running TensorFlow Lite models.

  Models obtained from `TfLiteConverter` can be run in Python with
  `Interpreter`.

  As an example, lets generate a simple Keras model and convert it to TFLite
  (`TfLiteConverter` also supports other input formats with `from_saved_model`
  and `from_concrete_function`)

  >>> x = np.array([[1.], [2.]])
  >>> y = np.array([[2.], [4.]])
  >>> model = tf.keras.models.Sequential([
  ...           tf.keras.layers.Dropout(0.2),
  ...           tf.keras.layers.Dense(units=1, input_shape=[1])
  ...         ])
  >>> model.compile(optimizer='sgd', loss='mean_squared_error')
  >>> model.fit(x, y, epochs=1)
  >>> converter = tf.lite.TFLiteConverter.from_keras_model(model)
  >>> tflite_model = converter.convert()

  `tflite_model` can be saved to a file and loaded later, or directly into the
  `Interpreter`. Since TensorFlow Lite pre-plans tensor allocations to optimize
  inference, the user needs to call `allocate_tensors()` before any inference.

  >>> interpreter = tf.lite.Interpreter(model_content=tflite_model)
  >>> interpreter.allocate_tensors()  # Needed before execution!

  Sample execution:

  >>> output = interpreter.get_output_details()[0]  # Model has single output.
  >>> input = interpreter.get_input_details()[0]  # Model has single input.
  >>> input_data = tf.constant(1., shape=[1, 1])
  >>> interpreter.set_tensor(input['index'], input_data)
  >>> interpreter.invoke()
  >>> interpreter.get_tensor(output['index']).shape
  (1, 1)

  Use `get_signature_runner()` for a more user-friendly inference API.
  """
    def __init__(self, model_path: Incomplete | None = None, model_content: Incomplete | None = None, experimental_delegates: Incomplete | None = None, num_threads: Incomplete | None = None, experimental_op_resolver_type=..., experimental_preserve_all_tensors: bool = False) -> None:
        """Constructor.

    Args:
      model_path: Path to TF-Lite Flatbuffer file.
      model_content: Content of model.
      experimental_delegates: Experimental. Subject to change. List of
        [TfLiteDelegate](https://www.tensorflow.org/lite/performance/delegates)
          objects returned by lite.load_delegate().
      num_threads: Sets the number of threads used by the interpreter and
        available to CPU kernels. If not set, the interpreter will use an
        implementation-dependent default number of threads. Currently, only a
        subset of kernels, such as conv, support multi-threading. num_threads
        should be >= -1. Setting num_threads to 0 has the effect to disable
        multithreading, which is equivalent to setting num_threads to 1. If set
        to the value -1, the number of threads used will be
        implementation-defined and platform-dependent.
      experimental_op_resolver_type: The op resolver used by the interpreter. It
        must be an instance of OpResolverType. By default, we use the built-in
        op resolver which corresponds to tflite::ops::builtin::BuiltinOpResolver
        in C++.
      experimental_preserve_all_tensors: If true, then intermediate tensors used
        during computation are preserved for inspection, and if the passed op
        resolver type is AUTO or BUILTIN, the type will be changed to
        BUILTIN_WITHOUT_DEFAULT_DELEGATES so that no Tensorflow Lite default
        delegates are applied. If false, getting intermediate tensors could
        result in undefined values or None, especially when the graph is
        successfully modified by the Tensorflow Lite default delegate.

    Raises:
      ValueError: If the interpreter was unable to create.
    """
    def __del__(self) -> None: ...
    def allocate_tensors(self): ...
    def get_tensor_details(self):
        """Gets tensor details for every tensor with valid tensor details.

    Tensors where required information about the tensor is not found are not
    added to the list. This includes temporary tensors without a name.

    Returns:
      A list of dictionaries containing tensor information.
    """
    def get_input_details(self):
        """Gets model input tensor details.

    Returns:
      A list in which each item is a dictionary with details about
      an input tensor. Each dictionary contains the following fields
      that describe the tensor:

      + `name`: The tensor name.
      + `index`: The tensor index in the interpreter.
      + `shape`: The shape of the tensor.
      + `shape_signature`: Same as `shape` for models with known/fixed shapes.
        If any dimension sizes are unknown, they are indicated with `-1`.
      + `dtype`: The numpy data type (such as `np.int32` or `np.uint8`).
      + `quantization`: Deprecated, use `quantization_parameters`. This field
        only works for per-tensor quantization, whereas
        `quantization_parameters` works in all cases.
      + `quantization_parameters`: A dictionary of parameters used to quantize
        the tensor:
        ~ `scales`: List of scales (one if per-tensor quantization).
        ~ `zero_points`: List of zero_points (one if per-tensor quantization).
        ~ `quantized_dimension`: Specifies the dimension of per-axis
        quantization, in the case of multiple scales/zero_points.
      + `sparsity_parameters`: A dictionary of parameters used to encode a
        sparse tensor. This is empty if the tensor is dense.
    """
    def set_tensor(self, tensor_index, value) -> None:
        """Sets the value of the input tensor.

    Note this copies data in `value`.

    If you want to avoid copying, you can use the `tensor()` function to get a
    numpy buffer pointing to the input buffer in the tflite interpreter.

    Args:
      tensor_index: Tensor index of tensor to set. This value can be gotten from
        the 'index' field in get_input_details.
      value: Value of tensor to set.

    Raises:
      ValueError: If the interpreter could not set the tensor.
    """
    def resize_tensor_input(self, input_index, tensor_size, strict: bool = False) -> None:
        """Resizes an input tensor.

    Args:
      input_index: Tensor index of input to set. This value can be gotten from
        the 'index' field in get_input_details.
      tensor_size: The tensor_shape to resize the input to.
      strict: Only unknown dimensions can be resized when `strict` is True.
        Unknown dimensions are indicated as `-1` in the `shape_signature`
        attribute of a given tensor. (default False)

    Raises:
      ValueError: If the interpreter could not resize the input tensor.

    Usage:
    ```
    interpreter = Interpreter(model_content=tflite_model)
    interpreter.resize_tensor_input(0, [num_test_images, 224, 224, 3])
    interpreter.allocate_tensors()
    interpreter.set_tensor(0, test_images)
    interpreter.invoke()
    ```
    """
    def get_output_details(self):
        """Gets model output tensor details.

    Returns:
      A list in which each item is a dictionary with details about
      an output tensor. The dictionary contains the same fields as
      described for `get_input_details()`.
    """
    def get_signature_list(self):
        """Gets list of SignatureDefs in the model.

    Example,
    ```
    signatures = interpreter.get_signature_list()
    print(signatures)

    # {
    #   'add': {'inputs': ['x', 'y'], 'outputs': ['output_0']}
    # }

    Then using the names in the signature list you can get a callable from
    get_signature_runner().
    ```

    Returns:
      A list of SignatureDef details in a dictionary structure.
      It is keyed on the SignatureDef method name, and the value holds
      dictionary of inputs and outputs.
    """
    def get_signature_runner(self, signature_key: Incomplete | None = None):
        """Gets callable for inference of specific SignatureDef.

    Example usage,
    ```
    interpreter = tf.lite.Interpreter(model_content=tflite_model)
    interpreter.allocate_tensors()
    fn = interpreter.get_signature_runner('div_with_remainder')
    output = fn(x=np.array([3]), y=np.array([2]))
    print(output)
    # {
    #   'quotient': array([1.], dtype=float32)
    #   'remainder': array([1.], dtype=float32)
    # }
    ```

    None can be passed for signature_key if the model has a single Signature
    only.

    All names used are this specific SignatureDef names.


    Args:
      signature_key: Signature key for the SignatureDef, it can be None if and
        only if the model has a single SignatureDef. Default value is None.

    Returns:
      This returns a callable that can run inference for SignatureDef defined
      by argument 'signature_key'.
      The callable will take key arguments corresponding to the arguments of the
      SignatureDef, that should have numpy values.
      The callable will returns dictionary that maps from output names to numpy
      values of the computed results.

    Raises:
      ValueError: If passed signature_key is invalid.
    """
    def get_tensor(self, tensor_index, subgraph_index: int = 0):
        """Gets the value of the output tensor (get a copy).

    If you wish to avoid the copy, use `tensor()`. This function cannot be used
    to read intermediate results.

    Args:
      tensor_index: Tensor index of tensor to get. This value can be gotten from
        the 'index' field in get_output_details.
      subgraph_index: Index of the subgraph to fetch the tensor. Default value
        is 0, which means to fetch from the primary subgraph.

    Returns:
      a numpy array.
    """
    def tensor(self, tensor_index):
        '''Returns function that gives a numpy view of the current tensor buffer.

    This allows reading and writing to this tensors w/o copies. This more
    closely mirrors the C++ Interpreter class interface\'s tensor() member, hence
    the name. Be careful to not hold these output references through calls
    to `allocate_tensors()` and `invoke()`. This function cannot be used to read
    intermediate results.

    Usage:

    ```
    interpreter.allocate_tensors()
    input = interpreter.tensor(interpreter.get_input_details()[0]["index"])
    output = interpreter.tensor(interpreter.get_output_details()[0]["index"])
    for i in range(10):
      input().fill(3.)
      interpreter.invoke()
      print("inference %s" % output())
    ```

    Notice how this function avoids making a numpy array directly. This is
    because it is important to not hold actual numpy views to the data longer
    than necessary. If you do, then the interpreter can no longer be invoked,
    because it is possible the interpreter would resize and invalidate the
    referenced tensors. The NumPy API doesn\'t allow any mutability of the
    the underlying buffers.

    WRONG:

    ```
    input = interpreter.tensor(interpreter.get_input_details()[0]["index"])()
    output = interpreter.tensor(interpreter.get_output_details()[0]["index"])()
    interpreter.allocate_tensors()  # This will throw RuntimeError
    for i in range(10):
      input.fill(3.)
      interpreter.invoke()  # this will throw RuntimeError since input,output
    ```

    Args:
      tensor_index: Tensor index of tensor to get. This value can be gotten from
        the \'index\' field in get_output_details.

    Returns:
      A function that can return a new numpy array pointing to the internal
      TFLite tensor state at any point. It is safe to hold the function forever,
      but it is not safe to hold the numpy array forever.
    '''
    def invoke(self) -> None:
        """Invoke the interpreter.

    Be sure to set the input sizes, allocate tensors and fill values before
    calling this. Also, note that this function releases the GIL so heavy
    computation can be done in the background while the Python interpreter
    continues. No other function on this object should be called while the
    invoke() call has not finished.

    Raises:
      ValueError: When the underlying interpreter fails raise ValueError.
    """
    def reset_all_variables(self): ...

class InterpreterWithCustomOps(Interpreter):
    """Interpreter interface for TensorFlow Lite Models that accepts custom ops.

  The interface provided by this class is experimental and therefore not exposed
  as part of the public API.

  Wraps the tf.lite.Interpreter class and adds the ability to load custom ops
  by providing the names of functions that take a pointer to a BuiltinOpResolver
  and add a custom op.
  """
    def __init__(self, custom_op_registerers: Incomplete | None = None, **kwargs) -> None:
        """Constructor.

    Args:
      custom_op_registerers: List of str (symbol names) or functions that take a
        pointer to a MutableOpResolver and register a custom op. When passing
        functions, use a pybind function that takes a uintptr_t that can be
        recast as a pointer to a MutableOpResolver.
      **kwargs: Additional arguments passed to Interpreter.

    Raises:
      ValueError: If the interpreter was unable to create.
    """

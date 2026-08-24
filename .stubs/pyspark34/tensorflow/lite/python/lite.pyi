import enum
from _typeshed import Incomplete
from tensorflow.lite.experimental.microfrontend.python.ops import audio_microfrontend_op as audio_microfrontend_op
from tensorflow.lite.python.convert import ConverterError as ConverterError, OpsSet as OpsSet, toco_convert as toco_convert
from tensorflow.lite.python.convert_phase import Component as Component, SubComponent as SubComponent, convert_phase as convert_phase
from tensorflow.lite.python.interpreter import Interpreter as Interpreter, OpResolverType as OpResolverType, load_delegate as load_delegate
from tensorflow.lite.python.metrics import metrics as metrics
from tensorflow.lite.python.op_hint import OpHint as OpHint, convert_op_hints_to_stubs as convert_op_hints_to_stubs
from tensorflow.lite.tools import flatbuffer_utils as flatbuffer_utils
from tensorflow.lite.tools.optimize.debugging.python.debugger import QuantizationDebugOptions as QuantizationDebugOptions, QuantizationDebugger as QuantizationDebugger
from tensorflow.python.eager import context as context
from tensorflow.python.framework import versions as versions
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util import keras_deps as keras_deps

class Optimize(enum.Enum):
    """Enum defining the optimizations to apply when generating a tflite model.

  DEFAULT
      The default optimization strategy that enables post-training quantization.
      The type of post-training quantization that will be used is dependent on
      the other converter options supplied. Refer to the
      [documentation](/lite/performance/post_training_quantization) for further
      information on the types available and how to use them.

  OPTIMIZE_FOR_SIZE
      Deprecated. Does the same as DEFAULT.

  OPTIMIZE_FOR_LATENCY
      Deprecated. Does the same as DEFAULT.

  EXPERIMENTAL_SPARSITY
      Experimental flag, subject to change.

      Enable optimization by taking advantage of the sparse model weights
      trained with pruning.

      The converter will inspect the sparsity pattern of the model weights and
      do its best to improve size and latency.
      The flag can be used alone to optimize float32 models with sparse weights.
      It can also be used together with the DEFAULT optimization mode to
      optimize quantized models with sparse weights.
  """
    DEFAULT: str
    OPTIMIZE_FOR_SIZE: str
    OPTIMIZE_FOR_LATENCY: str
    EXPERIMENTAL_SPARSITY: str

class RepresentativeDataset:
    """Representative dataset used to optimize the model.

  This is a generator function that provides a small dataset to calibrate or
  estimate the range, i.e, (min, max) of all floating-point arrays in the model
  (such as model input, activation outputs of intermediate layers, and model
  output) for quantization. Usually, this is a small subset of a few hundred
  samples randomly chosen, in no particular order, from the training or
  evaluation dataset.
  """
    input_gen: Incomplete
    def __init__(self, input_gen) -> None:
        """Creates a representative dataset.

    Args:
      input_gen: A generator function that generates input samples for the
        model and has the same order, type and shape as the inputs to the model.
        Usually, this is a small subset of a few hundred samples randomly
        chosen, in no particular order, from the training or evaluation dataset.
    """

class TargetSpec:
    '''Specification of target device used to optimize the model.

  Attributes:
    supported_ops: Experimental flag, subject to change. Set of `tf.lite.OpsSet`
      options, where each option represents a set of operators supported by the
      target device. (default {tf.lite.OpsSet.TFLITE_BUILTINS}))
    supported_types: Set of `tf.dtypes.DType` data types supported on the target
      device. If initialized, optimization might be driven by the smallest type
      in this set. (default set())
    experimental_select_user_tf_ops: Experimental flag, subject to change. Set
      of user\'s TensorFlow operators\' names that are required in the TensorFlow
      Lite runtime. These ops will be exported as select TensorFlow ops in the
      model (in conjunction with the tf.lite.OpsSet.SELECT_TF_OPS flag). This is
      an advanced feature that should only be used if the client is using TF ops
      that may not be linked in by default with the TF ops that are provided
      when using the SELECT_TF_OPS path. The client is responsible for linking
      these ops into the target runtime.
    experimental_supported_backends: Experimental flag, subject to change.
      Set containing names of supported backends. Currently only "GPU" is
      supported, more options will be available later.
  '''
    supported_ops: Incomplete
    supported_types: Incomplete
    experimental_select_user_tf_ops: Incomplete
    experimental_supported_backends: Incomplete
    def __init__(self, supported_ops: Incomplete | None = None, supported_types: Incomplete | None = None, experimental_select_user_tf_ops: Incomplete | None = None, experimental_supported_backends: Incomplete | None = None) -> None: ...

class QuantizationMode:
    """QuantizationMode determines the quantization type from user options."""
    enable_mlir_variable_quantization: Incomplete
    def __init__(self, optimizations, target_spec, representative_dataset, graph_def, disable_per_channel: bool = False, experimental_new_dynamic_range_quantizer: bool = False, experimental_low_bit_qat: bool = False, full_integer_quantization_bias_type: Incomplete | None = None, experimental_mlir_variable_quantization: bool = False) -> None: ...
    def is_post_training_int8_only_quantization(self): ...
    def is_post_training_int8_quantization_with_float_fallback(self): ...
    def is_post_training_int8_quantization(self): ...
    def is_post_training_int16x8_only_quantization(self): ...
    def is_post_training_int16x8_quantization_with_float_fallback(self): ...
    def is_post_training_int16x8_quantization(self): ...
    def is_post_training_integer_quantization(self): ...
    def is_low_bit_quantize_aware_training(self): ...
    def is_quantization_aware_training(self): ...
    def is_integer_quantization(self): ...
    def is_post_training_dynamic_range_quantization(self): ...
    def is_post_training_float16_quantization(self): ...
    def is_bfloat16_quantization(self): ...
    def activations_type(self): ...
    def bias_type(self): ...
    def converter_flags(self, inference_ty: Incomplete | None = None, inference_input_ty: Incomplete | None = None):
        """Flags to the converter."""
    def is_allow_float(self): ...
    def is_any_optimization_enabled(self): ...
    def is_quantization_aware_trained_model(self):
        """Checks if the graph contains any training-time quantization ops."""

class TFLiteConverterBase:
    """Converter subclass to share functionality between V1 and V2 converters."""
    optimizations: Incomplete
    representative_dataset: Incomplete
    target_spec: Incomplete
    allow_custom_ops: bool
    experimental_new_converter: bool
    experimental_new_quantizer: bool
    experimental_enable_resource_variables: bool
    saved_model_dir: Incomplete
    exclude_conversion_metadata: bool
    experimental_new_dynamic_range_quantizer: bool
    def __init__(self) -> None: ...

class TFLiteConverterBaseV2(TFLiteConverterBase):
    """Converter subclass to share functionality between V2 converters."""
    inference_input_type: Incomplete
    inference_output_type: Incomplete
    def __init__(self) -> None:
        """Constructor for TFLiteConverter."""
    def convert(self, graph_def, input_tensors, output_tensors):
        """Converts a TensorFlow GraphDef based on instance variables.

    Args:
      graph_def: Frozen TensorFlow GraphDef.
      input_tensors: List of input tensors.
      output_tensors: List of output tensors.

    Returns:
      The converted data in serialized format.

    Raises:
      ValueError:
        No concrete functions is specified.
        Multiple concrete functions are specified.
        Input shape is not specified.
        Invalid quantization parameters.
    """

class TFLiteSavedModelConverterV2(TFLiteConverterBaseV2):
    """Converts the given SavedModel into TensorFlow Lite model.

  Attributes:
      saved_model_dir: Directory of the SavedModel.
  """
    saved_model_dir: Incomplete
    def __init__(self, saved_model_dir, saved_model_tags: Incomplete | None = None, saved_model_exported_names: Incomplete | None = None, trackable_obj: Incomplete | None = None) -> None:
        """Constructor for TFLiteConverter.

    Args:
      saved_model_dir: Directory of the SavedModel.
      saved_model_tags: Set of tags identifying the MetaGraphDef within the
        SavedModel to analyze. All tags in the tag set must be present. (default
        {tf.saved_model.SERVING}).
      saved_model_exported_names: Names to be exported when the saved model
        import path is on.
      trackable_obj: tf.AutoTrackable object associated with `funcs`. A
        reference to this object needs to be maintained so that Variables do not
        get garbage collected since functions have a weak reference to
        Variables. This is only required when the tf.AutoTrackable object is not
        maintained by the user (e.g. `from_saved_model`).
    """
    def convert(self):
        """Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format.

    Raises:
      ValueError:
        No concrete functions is specified.
        Multiple concrete functions are specified.
        Input shape is not specified.
        Invalid quantization parameters.
    """

class TFLiteKerasModelConverterV2(TFLiteConverterBaseV2):
    """Converts the given Keras model into TensorFlow Lite model."""
    experimental_lower_to_saved_model: bool
    def __init__(self, keras_model, trackable_obj: Incomplete | None = None) -> None:
        """Constructor for TFLiteConverter.

    Args:
      keras_model: tf.Keras.Model.
      trackable_obj: tf.AutoTrackable object associated with `funcs`. A
        reference to this object needs to be maintained so that Variables do not
        get garbage collected since functions have a weak reference to
        Variables. This is only required when the tf.AutoTrackable object is not
        maintained by the user (e.g. `from_saved_model`).
    """
    def convert(self):
        """Converts a keras model based on instance variables.

    Returns:
      The converted data in serialized format.

    Raises:
      ValueError:
        Multiple concrete functions are specified.
        Input shape is not specified.
        Invalid quantization parameters.
    """

class TFLiteFrozenGraphConverterV2(TFLiteConverterBaseV2):
    """Converts the given frozen graph into TensorFlow Lite model."""
    experimental_lower_to_saved_model: bool
    def __init__(self, funcs, trackable_obj: Incomplete | None = None) -> None:
        """Constructor for TFLiteConverter.

    Args:
      funcs: List of TensorFlow ConcreteFunctions. The list should not contain
        duplicate elements.
      trackable_obj: tf.AutoTrackable object associated with `funcs`. A
        reference to this object needs to be maintained so that Variables do not
        get garbage collected since functions have a weak reference to
        Variables. This is only required when the tf.AutoTrackable object is not
        maintained by the user (e.g. `from_saved_model`).
    """
    def convert(self):
        """Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format.

    Raises:
      ValueError:
        No concrete functions is specified.
        Multiple concrete functions are specified.
        Input shape is not specified.
        Invalid quantization parameters.
    """

class TFLiteJaxConverterV2(TFLiteConverterBaseV2):
    """Converts the given jax model into TensorFlow Lite model."""
    def __init__(self, serving_funcs, inputs) -> None:
        '''Constructor for TFLiteConverter.

    Args:
      serving_funcs: A list functions of the serving func of the jax module, the
        model params should already be inlined. (e.g., `serving_func =
        functools.partial(model, params=params)`)
      inputs: Array of input tensor placeholders tuple,s like `jnp.zeros`. For
        example, wrapped in an array like
        "[(\'input1\', input1), (\'input2\', input2)]]".
    Jax function is polymorphic, for example:
    ```python
    def add(a, b):
      return a + b
    ```
    Will yield different computations if different input signatures are passed
    in: Pass `add(10.0, 20.0)` will yield a scalar `add` while pass
      `add(np.random((100, 1)), np.random(100, 100))` will yield a broadcasting
      add.  We will need the input information to do tracing for the converter
      to properly convert the model. So it\'s important to pass in the desired
      `input placeholders` with the correct input shape/type.

    In the converted tflite model:
    Currently: the function name will be default to main, the output names will
    be the traced outputs. The output ordering shall match the serving function.
    '''
    def convert(self):
        """Converts a Jax serving func based on instance variables.

    Returns:
      The converted data in serialized format.

    Raises:
      ImportError:
        If cannot import the xla_computation from jax.
      ValueError:
        No serving function is specified.
        Input tensors are not specified.
        The truth value of an array with more than one element is ambiguous.
        Failed to convert the given Jax function to hlo.

    """

class TFLiteConverterV2(TFLiteFrozenGraphConverterV2):
    """Converts a TensorFlow model into TensorFlow Lite model.

  Attributes:
    optimizations: Experimental flag, subject to change. Set of optimizations to
      apply. e.g {tf.lite.Optimize.DEFAULT}. (default None, must be None or a
      set of values of type `tf.lite.Optimize`)
    representative_dataset: A generator function used for integer quantization
      where each generated sample has the same order, type and shape as the
      inputs to the model. Usually, this is a small subset of a few hundred
      samples randomly chosen, in no particular order, from the training or
      evaluation dataset. This is an optional attribute, but required for full
      integer quantization, i.e, if `tf.int8` is the only supported type in
      `target_spec.supported_types`. Refer to `tf.lite.RepresentativeDataset`.
      (default None)
    target_spec: Experimental flag, subject to change. Specifications of target
      device, including supported ops set, supported types and a set of user's
      defined TensorFlow operators required in the TensorFlow Lite runtime.
      Refer to `tf.lite.TargetSpec`.
    inference_input_type: Data type of the input layer. Note that integer types
      (tf.int8 and tf.uint8) are currently only supported for post training
      integer quantization and quantization aware training. (default tf.float32,
      must be in {tf.float32, tf.int8, tf.uint8})
    inference_output_type: Data type of the output layer. Note that integer
      types (tf.int8 and tf.uint8) are currently only supported for post
      training integer quantization and quantization aware training. (default
      tf.float32, must be in {tf.float32, tf.int8, tf.uint8})
    allow_custom_ops: Boolean indicating whether to allow custom operations.
      When False, any unknown operation is an error. When True, custom ops are
      created for any op that is unknown. The developer needs to provide these
      to the TensorFlow Lite runtime with a custom resolver. (default False)
    exclude_conversion_metadata: Whether not to embed the conversion metadata
      into the converted model. (default False)
    experimental_new_converter: Experimental flag, subject to change. Enables
      MLIR-based conversion. (default True)
    experimental_new_quantizer: Experimental flag, subject to change. Enables
      MLIR-based quantization conversion instead of Flatbuffer-based conversion.
      (default True)
    experimental_enable_resource_variables: Experimental flag, subject to
      change. Enables
      [resource variables](https://tensorflow.org/guide/migrate/tf1_vs_tf2#resourcevariables_instead_of_referencevariables)
      to be converted by this converter. This is only allowed if the
      from_saved_model interface is used. (default True)

  Example usage:

  ```python
  # Converting a SavedModel to a TensorFlow Lite model.
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
    tflite_model = converter.convert()

  # Converting a tf.Keras model to a TensorFlow Lite model.
  converter = tf.lite.TFLiteConverter.from_keras_model(model)
  tflite_model = converter.convert()

  # Converting ConcreteFunctions to a TensorFlow Lite model.
  converter = tf.lite.TFLiteConverter.from_concrete_functions([func], model)
  tflite_model = converter.convert()

  # Converting a Jax model to a TensorFlow Lite model.
  converter = tf.lite.TFLiteConverter.experimental_from_jax([func], [[
      ('input1', input1), ('input2', input2)]])
  tflite_model = converter.convert()
  ```
  """
    def __init__(self, funcs, trackable_obj: Incomplete | None = None) -> None:
        """Constructor for TFLiteConverter.

    Args:
      funcs: List of TensorFlow ConcreteFunctions. The list should not contain
        duplicate elements.
      trackable_obj: tf.AutoTrackable object associated with `funcs`. A
        reference to this object needs to be maintained so that Variables do not
        get garbage collected since functions have a weak reference to
        Variables. This is only required when the tf.AutoTrackable object is not
        maintained by the user (e.g. `from_saved_model`).
    """
    @classmethod
    def from_concrete_functions(cls, funcs, trackable_obj: Incomplete | None = None):
        """Creates a TFLiteConverter object from ConcreteFunctions.

    Args:
      funcs: List of TensorFlow ConcreteFunctions. The list should not contain
        duplicate elements. Currently converter can only convert a single
        ConcreteFunction. Converting multiple functions is under development.
      trackable_obj:   An `AutoTrackable` object (typically `tf.module`)
        associated with `funcs`. A reference to this object needs to be
        maintained so that Variables do not get garbage collected since
        functions have a weak reference to Variables.

    Returns:
      TFLiteConverter object.

    Raises:
      Invalid input type.
    """
    @classmethod
    def from_saved_model(cls, saved_model_dir, signature_keys: Incomplete | None = None, tags: Incomplete | None = None):
        """Creates a TFLiteConverter object from a SavedModel directory.

    Args:
      saved_model_dir: SavedModel directory to convert.
      signature_keys: List of keys identifying SignatureDef containing inputs
        and outputs. Elements should not be duplicated. By default the
        `signatures` attribute of the MetaGraphdef is used. (default
        saved_model.signatures)
      tags: Set of tags identifying the MetaGraphDef within the SavedModel to
        analyze. All tags in the tag set must be present. (default
        {tf.saved_model.SERVING} or {'serve'})

    Returns:
      TFLiteConverter object.

    Raises:
      Invalid signature keys.
    """
    @classmethod
    def from_keras_model(cls, model):
        """Creates a TFLiteConverter object from a Keras model.

    Args:
      model: tf.Keras.Model

    Returns:
      TFLiteConverter object.
    """
    @classmethod
    def experimental_from_jax(cls, serving_funcs, inputs):
        """Creates a TFLiteConverter object from a Jax model with its inputs.

    Args:
      serving_funcs: A array of Jax functions with all the weights applied
        already.
      inputs: A array of Jax input placeholders tuples list, e.g.,
        jnp.zeros(INPUT_SHAPE). Each tuple list should correspond with the
        serving function.

    Returns:
      TFLiteConverter object.
    """
    def convert(self):
        """Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format.

    Raises:
      ValueError:
        No concrete functions is specified.
        Multiple concrete functions are specified.
        Input shape is not specified.
        Invalid quantization parameters.
    """

class TFLiteConverterBaseV1(TFLiteConverterBase):
    """Converter subclass to share functionality between V1 converters."""
    inference_type: Incomplete
    inference_input_type: Incomplete
    inference_output_type: Incomplete
    output_format: Incomplete
    quantized_input_stats: Incomplete
    default_ranges_stats: Incomplete
    drop_control_dependency: bool
    reorder_across_fake_quant: bool
    change_concat_input_ranges: bool
    dump_graphviz_dir: Incomplete
    dump_graphviz_video: bool
    conversion_summary_dir: Incomplete
    def __init__(self, experimental_debug_info_func) -> None:
        """Constructor for TFLiteConverter.

    Args:
      experimental_debug_info_func: An experimental function to retrieve the
        graph debug info for a set of nodes from the `graph_def`.
    """
    optimizations: Incomplete
    def __setattr__(self, name, value) -> None: ...
    def __getattribute__(self, name): ...
    def convert(self):
        """Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format. Either a TFLite Flatbuffer or a
      Graphviz graph depending on value in `output_format`.

    Raises:
      ValueError:
        Input shape is not specified.
        None value for dimension in input_tensor.
    """
    def get_input_arrays(self):
        """Returns a list of the names of the input tensors.

    Returns:
      List of strings.
    """

class TFLiteSavedModelConverter(TFLiteConverterBaseV1):
    """Converts the given SavedModel into TensorFlow Lite model.

  Attributes:
      saved_model_dir: Directory of the SavedModel.
  """
    saved_model_dir: Incomplete
    def __init__(self, saved_model_dir, saved_model_tags, saved_model_exported_names, experimental_debug_info_func: Incomplete | None = None) -> None:
        """Constructor for TFLiteConverter.

    Args:
      saved_model_dir: Directory of the SavedModel.
      saved_model_tags: Set of tags identifying the MetaGraphDef within the
        SavedModel to analyze. All tags in the tag set must be present. (default
        {tf.saved_model.SERVING}).
      saved_model_exported_names: Names to be exported when the saved model
        import path is on.
      experimental_debug_info_func: An experimental function to retrieve the
        graph debug info for a set of nodes from the `graph_def`.

    Raises:
      ValueError: Invalid arguments.
    """
    def convert(self):
        """Converts a TensorFlow GraphDef based on instance variables.

    Note that in the converted TensorFlow Lite model, the input tensor's order
    might be changed each time `convert` is called. To access input tensor
    information, please consider using the `SignatureRunner` API
    (`interpreter.get_signature_runner`).

    Returns:
      The converted data in serialized format. Either a TFLite Flatbuffer or a
      Graphviz graph depending on value in `output_format`.

    Raises:
      ValueError:
        Input shape is not specified.
        None value for dimension in input_tensor.
    """

class TFLiteKerasModelConverter(TFLiteConverterBaseV1):
    """Converts the given SavedModel into TensorFlow Lite model."""
    def __init__(self, model_file, input_arrays: Incomplete | None = None, input_shapes: Incomplete | None = None, output_arrays: Incomplete | None = None, custom_objects: Incomplete | None = None) -> None:
        '''Constructor for TFLiteConverter.

    Args:
      model_file: Full filepath of HDF5 file containing the tf.keras model.
      input_arrays: List of input tensors to freeze graph with. Uses input
        arrays from SignatureDef when none are provided. (default None)
      input_shapes: Dict of strings representing input tensor names to list of
        integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
        Automatically determined when input shapes is None (e.g., {"foo" :
          None}). (default None)
      output_arrays: List of output tensors to freeze graph with. Uses output
        arrays from SignatureDef when none are provided. (default None)
      custom_objects: Dict mapping names (strings) to custom classes or
        functions to be considered during model deserialization. (default None)

    Raises:
      ValueError: Invalid arguments.
    '''
    def convert(self):
        """Converts a Keras model based on instance variables.

    Returns:
      The converted data in serialized format. Either a TFLite Flatbuffer or a
      Graphviz graph depending on value in `output_format`.

    Raises:
      ValueError:
        Input shape is not specified.
        None value for dimension in input_tensor.
    """

class TFLiteFrozenGraphConverter(TFLiteConverterBaseV1):
    """Converts the given frozen graph def into TensorFlow Lite model."""
    def __init__(self, graph_def, input_tensors, output_tensors, input_arrays_with_shape: Incomplete | None = None, output_arrays: Incomplete | None = None, experimental_debug_info_func: Incomplete | None = None) -> None:
        '''Constructor for TFLiteConverter.

    Args:
      graph_def: Frozen TensorFlow GraphDef.
      input_tensors: List of input tensors. Type and shape are computed using
        `foo.shape` and `foo.dtype`.
      output_tensors: List of output tensors (only .name is used from this).
      input_arrays_with_shape: Tuple of strings representing input tensor names
        and list of integers representing input shapes
        (e.g., [("foo", [1, 16, 16, 3])]). Use only when graph cannot be loaded
          into TensorFlow and when `input_tensors` and `output_tensors` are
          None. (default None)
      output_arrays: List of output tensors to freeze graph with. Use only when
        graph cannot be loaded into TensorFlow and when `input_tensors` and
        `output_tensors` are None. (default None)
      experimental_debug_info_func: An experimental function to retrieve the
        graph debug info for a set of nodes from the `graph_def`.

    Raises:
      ValueError: Invalid arguments.
    '''
    def convert(self):
        """Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format. Either a TFLite Flatbuffer or a
      Graphviz graph depending on value in `output_format`.

    Raises:
      ValueError:
        Input shape is not specified.
        None value for dimension in input_tensor.
    """

class TFLiteConverter(TFLiteFrozenGraphConverter):
    '''Convert a TensorFlow model into `output_format`.

  This is used to convert from a TensorFlow GraphDef, SavedModel or tf.keras
  model into either a TFLite FlatBuffer or graph visualization.

  Attributes:
    optimizations: Experimental flag, subject to change. Set of optimizations to
      apply. e.g {tf.lite.Optimize.DEFAULT}. (default None, must be None or a
      set of values of type `tf.lite.Optimize`)
    representative_dataset: A generator function used for integer quantization
      where each generated sample has the same order, type and shape as the
      inputs to the model. Usually, this is a small subset of a few hundred
      samples randomly chosen, in no particular order, from the training or
      evaluation dataset. This is an optional attribute, but required for full
      integer quantization, i.e, if `tf.int8` is the only supported type in
      `target_spec.supported_types`. Refer to `tf.lite.RepresentativeDataset`.
      (default None)
    target_spec: Experimental flag, subject to change. Specifications of target
      device, including supported ops set, supported types and a set of user\'s
      defined TensorFlow operators required in the TensorFlow Lite runtime.
      Refer to `tf.lite.TargetSpec`.
    inference_type: Data type of numeric arrays, excluding the input layer.
      (default tf.float32, must be in {tf.float32, tf.int8, tf.uint8})
    inference_input_type: Data type of the numeric arrays in the input layer. If
      `inference_input_type` is in {tf.int8, tf.uint8}, then
      `quantized_input_stats` must be provided. (default is the value assigned
      to `inference_type`, must be in {tf.float32, tf.int8, tf.uint8})
    inference_output_type: Data type of the numeric arrays in the output layer.
      (default is the value assigned to `inference_type`, must be in
      {tf.float32, tf.int8, tf.uint8})
    quantized_input_stats: Map of input tensor names to a tuple of floats
      representing the mean and standard deviation of the training data.
      (e.g., {"foo" : (0., 1.)}). Required if `inference_input_type` is tf.int8
        or tf.uint8. (default None)
    default_ranges_stats: Tuple of integers (min, max) representing range values
      for all numeric arrays without a specified range. Intended for
      experimenting with quantization via "dummy quantization". (default None)
    allow_custom_ops: Boolean indicating whether to allow custom operations.
      When False any unknown operation is an error. When True, custom ops are
      created for any op that is unknown. The developer will need to provide
      these to the TensorFlow Lite runtime with a custom resolver. (default
      False)
    drop_control_dependency: Boolean indicating whether to drop control
      dependencies silently. This is due to TFLite not supporting control
      dependencies. (default True)
    reorder_across_fake_quant: Boolean indicating whether to reorder FakeQuant
      nodes in unexpected locations. Used when the location of the FakeQuant
      nodes is preventing graph transformations necessary to convert the graph.
      Results in a graph that differs from the quantized training graph,
      potentially causing differing arithmetic behavior. (default False)
    change_concat_input_ranges: Boolean to change behavior of min/max ranges for
      inputs and outputs of the concat operator for quantized models. Changes
      the ranges of concat operator overlap when true. (default False)
    output_format: Output file format. (default
      tf.compat.v1.lite.constants.TFLITE, must be in
      {tf.compat.v1.lite.constants.TFLITE,
      tf.compat.v1.lite.constants.GRAPHVIZ_DOT})
    dump_graphviz_dir: Full filepath of folder to dump the graphs at various
      stages of processing GraphViz .dot files. Preferred over
      `output_format=tf.compat.v1.lite.constants.GRAPHVIZ_DOT` in order to keep
      the requirements of the output file. (default None)
    dump_graphviz_video: Boolean indicating whether to dump the GraphViz .dot
      files after every graph transformation. Requires the `dump_graphviz_dir`
      flag to be specified. (default False)
    conversion_summary_dir: Full path of the directory to store conversion logs.
      (default None)
    exclude_conversion_metadata: Whether not to embed the conversion metadata
      into the converted model. (default False)
    target_ops: Deprecated. Please use `target_spec.supported_ops` instead.
    post_training_quantize: Deprecated. Please use `optimizations` instead and
      set it to `{tf.lite.Optimize.DEFAULT}`. (default False)
    experimental_new_converter: Experimental flag, subject to change. Enables
      MLIR-based conversion. (default True)
    experimental_new_quantizer: Experimental flag, subject to change. Enables
      MLIR-based quantization conversion instead of Flatbuffer-based conversion.
      (default True)

  Example usage:

    ```python
    # Converting a GraphDef from session.
    converter = tf.compat.v1.lite.TFLiteConverter.from_session(
      sess, in_tensors, out_tensors)
    tflite_model = converter.convert()
    open("converted_model.tflite", "wb").write(tflite_model)

    # Converting a GraphDef from file.
    converter = tf.compat.v1.lite.TFLiteConverter.from_frozen_graph(
      graph_def_file, input_arrays, output_arrays)
    tflite_model = converter.convert()
    open("converted_model.tflite", "wb").write(tflite_model)

    # Converting a SavedModel.
    converter = tf.compat.v1.lite.TFLiteConverter.from_saved_model(
        saved_model_dir)
    tflite_model = converter.convert()
    open("converted_model.tflite", "wb").write(tflite_model)

    # Converting a tf.keras model.
    converter = tf.compat.v1.lite.TFLiteConverter.from_keras_model_file(
        keras_model)
    tflite_model = converter.convert()
    open("converted_model.tflite", "wb").write(tflite_model)
    ```
  '''
    def __init__(self, graph_def, input_tensors, output_tensors, input_arrays_with_shape: Incomplete | None = None, output_arrays: Incomplete | None = None, experimental_debug_info_func: Incomplete | None = None) -> None:
        '''Constructor for TFLiteConverter.

    Args:
      graph_def: Frozen TensorFlow GraphDef.
      input_tensors: List of input tensors. Type and shape are computed using
        `foo.shape` and `foo.dtype`.
      output_tensors: List of output tensors (only .name is used from this).
      input_arrays_with_shape: Tuple of strings representing input tensor names
        and list of integers representing input shapes
        (e.g., [("foo" : [1, 16, 16, 3])]). Use only when graph cannot be loaded
          into TensorFlow and when `input_tensors` and `output_tensors` are
          None. (default None)
      output_arrays: List of output tensors to freeze graph with. Use only when
        graph cannot be loaded into TensorFlow and when `input_tensors` and
        `output_tensors` are None. (default None)
      experimental_debug_info_func: An experimental function to retrieve the
        graph debug info for a set of nodes from the `graph_def`.

    Raises:
      ValueError: Invalid arguments.
    '''
    @classmethod
    def from_session(cls, sess, input_tensors, output_tensors):
        """Creates a TFLiteConverter class from a TensorFlow Session.

    Args:
      sess: TensorFlow Session.
      input_tensors: List of input tensors. Type and shape are computed using
        `foo.shape` and `foo.dtype`.
      output_tensors: List of output tensors (only .name is used from this).

    Returns:
      TFLiteConverter class.
    """
    @classmethod
    def from_frozen_graph(cls, graph_def_file, input_arrays, output_arrays, input_shapes: Incomplete | None = None):
        '''Creates a TFLiteConverter class from a file containing a frozen GraphDef.

    Args:
      graph_def_file: Full filepath of file containing frozen GraphDef.
      input_arrays: List of input tensors to freeze graph with.
      output_arrays: List of output tensors to freeze graph with.
      input_shapes: Dict of strings representing input tensor names to list of
        integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
        Automatically determined when input shapes is None (e.g., {"foo" :
          None}). (default None)

    Returns:
      TFLiteConverter class.

    Raises:
      IOError:
        File not found.
        Unable to parse input file.
      ValueError:
        The graph is not frozen.
        input_arrays or output_arrays contains an invalid tensor name.
        input_shapes is not correctly defined when required
    '''
    @classmethod
    def from_saved_model(cls, saved_model_dir, input_arrays: Incomplete | None = None, input_shapes: Incomplete | None = None, output_arrays: Incomplete | None = None, tag_set: Incomplete | None = None, signature_key: Incomplete | None = None):
        '''Creates a TFLiteConverter class from a SavedModel.

    Args:
      saved_model_dir: SavedModel directory to convert.
      input_arrays: List of input tensors to freeze graph with. Uses input
        arrays from SignatureDef when none are provided. (default None)
      input_shapes: Dict of strings representing input tensor names to list of
        integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
        Automatically determined when input shapes is None (e.g., {"foo" :
          None}). (default None)
      output_arrays: List of output tensors to freeze graph with. Uses output
        arrays from SignatureDef when none are provided. (default None)
      tag_set: Set of tags identifying the MetaGraphDef within the SavedModel to
        analyze. All tags in the tag set must be present. (default
        {tf.saved_model.SERVING})
      signature_key: Key identifying SignatureDef containing inputs and outputs.
        (default tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY)

    Returns:
      TFLiteConverter class.
    '''
    @classmethod
    def from_keras_model_file(cls, model_file, input_arrays: Incomplete | None = None, input_shapes: Incomplete | None = None, output_arrays: Incomplete | None = None, custom_objects: Incomplete | None = None):
        '''Creates a TFLiteConverter class from a tf.keras model file.

    Args:
      model_file: Full filepath of HDF5 file containing the tf.keras model.
      input_arrays: List of input tensors to freeze graph with. Uses input
        arrays from SignatureDef when none are provided. (default None)
      input_shapes: Dict of strings representing input tensor names to list of
        integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
        Automatically determined when input shapes is None (e.g., {"foo" :
          None}). (default None)
      output_arrays: List of output tensors to freeze graph with. Uses output
        arrays from SignatureDef when none are provided. (default None)
      custom_objects: Dict mapping names (strings) to custom classes or
        functions to be considered during model deserialization. (default None)

    Returns:
      TFLiteConverter class.
    '''
    def convert(self):
        """Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format. Either a TFLite Flatbuffer or a
      Graphviz graph depending on value in `output_format`.

    Raises:
      ValueError:
        Input shape is not specified.
        None value for dimension in input_tensor.
    """

class TocoConverter:
    """Convert a TensorFlow model into `output_format`.

  This class has been deprecated. Please use `lite.TFLiteConverter` instead.
  """
    @classmethod
    def from_session(cls, sess, input_tensors, output_tensors):
        """Creates a TocoConverter class from a TensorFlow Session."""
    @classmethod
    def from_frozen_graph(cls, graph_def_file, input_arrays, output_arrays, input_shapes: Incomplete | None = None):
        """Creates a TocoConverter class from a file containing a frozen graph."""
    @classmethod
    def from_saved_model(cls, saved_model_dir, input_arrays: Incomplete | None = None, input_shapes: Incomplete | None = None, output_arrays: Incomplete | None = None, tag_set: Incomplete | None = None, signature_key: Incomplete | None = None):
        """Creates a TocoConverter class from a SavedModel."""
    @classmethod
    def from_keras_model_file(cls, model_file, input_arrays: Incomplete | None = None, input_shapes: Incomplete | None = None, output_arrays: Incomplete | None = None):
        """Creates a TocoConverter class from a tf.keras model file."""

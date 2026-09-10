from _typeshed import Incomplete
from tensorflow.core.framework import variable_pb2 as variable_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2, meta_graph_pb2 as meta_graph_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python.client import session as session
from tensorflow.python.eager import context as context, wrap_function as wrap_function
from tensorflow.python.framework import convert_to_constants as convert_to_constants, dtypes as dtypes, errors as errors, graph_util as graph_util, importer as importer, ops as ops
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from tensorflow.python.ops import array_ops as array_ops, gen_resource_variable_ops as gen_resource_variable_ops
from tensorflow.python.saved_model import builder as builder, load as load, loader as loader, save as save, signature_constants as signature_constants, tag_constants as tag_constants
from tensorflow.python.trackable import asset as asset, autotrackable as autotrackable, resource as resource
from tensorflow.python.training import saver as saver
from tensorflow.python.util import deprecation as deprecation, nest as nest
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

gen_trt_ops: Incomplete

class TrtPrecisionMode:
    FP32: str
    FP16: str
    INT8: str
    @staticmethod
    def supported_precision_modes(): ...

DEFAULT_TRT_MAX_WORKSPACE_SIZE_BYTES: Incomplete
PROFILE_STRATEGY_RANGE: str
PROFILE_STRATEGY_OPTIMAL: str
PROFILE_STRATEGY_RANGE_OPTIMAL: str
PROFILE_STRATEGY_IMPLICIT_BATCH_MODE_COMPATIBLE: str

def supported_profile_strategies(): ...

class TrtConversionParams(NamedTuple('TrtConversionParams', [('max_workspace_size_bytes', Incomplete), ('precision_mode', Incomplete), ('minimum_segment_size', Incomplete), ('maximum_cached_engines', Incomplete), ('use_calibration', Incomplete), ('allow_build_at_runtime', Incomplete)])):
    """Parameters that are used for TF-TRT conversion.

  Fields:
    max_workspace_size_bytes: the maximum GPU temporary memory that the TRT
      engine can use at execution time. This corresponds to the
      'workspaceSize' parameter of nvinfer1::IBuilder::setMaxWorkspaceSize().
    precision_mode: one of the strings in
      TrtPrecisionMode.supported_precision_modes().
    minimum_segment_size: the minimum number of nodes required for a subgraph
      to be replaced by TRTEngineOp.
    maximum_cached_engines: max number of cached TRT engines for dynamic TRT
      ops. Created TRT engines for a dynamic dimension are cached. If the
      number of cached engines is already at max but none of them supports the
      input shapes, the TRTEngineOp will fall back to run the original TF
      subgraph that corresponds to the TRTEngineOp.
    use_calibration: this argument is ignored if precision_mode is not INT8.
      If set to True, a calibration graph will be created to calibrate the
      missing ranges. The calibration graph must be converted to an inference
      graph by running calibration with calibrate(). If set to False,
      quantization nodes will be expected for every tensor in the graph
      (excluding those which will be fused). If a range is missing, an error
      will occur. Please note that accuracy may be negatively affected if
      there is a mismatch between which tensors TRT quantizes and which
      tensors were trained with fake quantization.
    allow_build_at_runtime: whether to allow building TensorRT engines during
      runtime if no prebuilt TensorRT engine can be found that can handle the
      given inputs during runtime, then a new TensorRT engine is built at
      runtime if allow_build_at_runtime=True, and otherwise native TF is used.
  """
    def __new__(cls, max_workspace_size_bytes=..., precision_mode=..., minimum_segment_size: int = 3, maximum_cached_engines: int = 1, use_calibration: bool = True, allow_build_at_runtime: bool = True): ...

DEFAULT_TRT_CONVERSION_PARAMS: Incomplete

def get_tensorrt_rewriter_config(conversion_params, is_dynamic_op: Incomplete | None = None, max_batch_size: Incomplete | None = None, is_v2: bool = False, disable_non_trt_optimizers: bool = False): ...

class TrtGraphConverter:
    '''A converter for TF-TRT transformation for TF 1.x GraphDef/SavedModels.

  To run the conversion without quantization calibration (e.g. for FP32/FP16
  precision modes):

  ```python
  converter = TrtGraphConverter(
      input_saved_model_dir="my_dir",
      precision_mode=TrtPrecisionMode.FP16)
  converted_graph_def = converter.convert()
  converter.save(output_saved_model_dir)
  ```

  To run the conversion with quantization calibration:

  ```python
  converter = TrtGraphConverter(
      input_saved_model_dir="my_dir",
      precision_mode=TrtPrecisionMode.INT8)
  converter.convert()

  # Run calibration 10 times.
  converted_graph_def = converter.calibrate(
      fetch_names=[\'output:0\'],
      num_runs=10,
      feed_dict_fn=lambda: {\'input:0\': my_next_data()})

  converter.save(output_saved_model_dir)
  ```
  '''
    def __init__(self, input_saved_model_dir: Incomplete | None = None, input_saved_model_tags: Incomplete | None = None, input_saved_model_signature_key: Incomplete | None = None, input_graph_def: Incomplete | None = None, nodes_denylist: Incomplete | None = None, max_batch_size: int = 1, max_workspace_size_bytes=..., precision_mode=..., minimum_segment_size: int = 3, is_dynamic_op: bool = False, maximum_cached_engines: int = 1, use_calibration: bool = True) -> None:
        """Initializes the converter.

    Args:
      input_saved_model_dir: the directory to load the SavedModel which contains
        the input graph to transforms. Used only when input_graph_def is None.
      input_saved_model_tags: list of tags to load the SavedModel.
      input_saved_model_signature_key: the key of the signature to optimize the
        graph for.
      input_graph_def: a GraphDef object containing a model to be transformed.
        If set to None, the graph will be read from the SavedModel loaded from
        input_saved_model_dir.
      nodes_denylist: list of node names to prevent the converter from touching.
      max_batch_size: max size for the input batch.
      max_workspace_size_bytes: the maximum GPU temporary memory which the TRT
        engine can use at execution time. This corresponds to the
        'workspaceSize' parameter of nvinfer1::IBuilder::setMaxWorkspaceSize().
      precision_mode: one of TrtPrecisionMode.supported_precision_modes().
      minimum_segment_size: the minimum number of nodes required for a subgraph
        to be replaced by TRTEngineOp.
      is_dynamic_op: whether to generate dynamic TRT ops which will build the
        TRT network and engine at run time.
      maximum_cached_engines: max number of cached TRT engines in dynamic TRT
        ops. If the number of cached engines is already at max but none of them
        can serve the input, the TRTEngineOp will fall back to run the TF
        function based on which the TRTEngineOp is created.
      use_calibration: this argument is ignored if precision_mode is not INT8.
        If set to True, a calibration graph will be created to calibrate the
        missing ranges. The calibration graph must be converted to an inference
        graph by running calibration with calibrate(). If set to False,
        quantization nodes will be expected for every tensor in the graph
        (excluding those which will be fused). If a range is missing, an error
        will occur. Please note that accuracy may be negatively affected if
        there is a mismatch between which tensors TRT quantizes and which
        tensors were trained with fake quantization.

    Raises:
      ValueError: if the combination of the parameters is invalid.
      RuntimeError: if this class is used in TF 2.0.
    """
    def convert(self):
        """Run the TF-TRT conversion.

    Returns:
      The converted GraphDef for TF 1.x.
    """
    def calibrate(self, fetch_names, num_runs, feed_dict_fn: Incomplete | None = None, input_map_fn: Incomplete | None = None):
        """Run the calibration and return the calibrated GraphDef.

    Args:
      fetch_names: a list of output tensor name to fetch during calibration.
      num_runs: number of runs of the graph during calibration.
      feed_dict_fn: a function that returns a dictionary mapping input names (as
        strings) in the GraphDef to be calibrated to values (e.g. Python list,
        numpy arrays, etc). One and only one of `feed_dict_fn` and
        `input_map_fn` should be specified.
      input_map_fn: a function that returns a dictionary mapping input names (as
        strings) in the GraphDef to be calibrated to Tensor objects. The values
        of the named input tensors in the GraphDef to be calibrated will be
        re-mapped to the respective `Tensor` values during calibration. One and
        only one of `feed_dict_fn` and `input_map_fn` should be specified.

    Raises:
      ValueError: if the input combination is invalid.
      RuntimeError: if this method is called in eager mode.

    Returns:
      The GraphDef after the calibration.
    """
    def save(self, output_saved_model_dir) -> None:
        """Save the converted graph as a SavedModel.

    Args:
      output_saved_model_dir: construct a SavedModel using the converted
        GraphDef and save it to the specified directory. This option only works
        when the input graph is loaded from a SavedModel, i.e. when
        input_saved_model_dir is specified and input_graph_def is None in
        __init__().

    Raises:
      ValueError: if the input to the converter is a GraphDef instead of a
      SavedModel.
    """

class _TRTEngineResource(resource.TrackableResource):
    """Class to track the serialized engines resource."""
    def __init__(self, resource_name, filename, maximum_cached_engines, device: str = 'GPU') -> None: ...

class TrtGraphConverterV2:
    '''An offline converter for TF-TRT transformation for TF 2.0 SavedModels.

  Windows support is provided experimentally. No guarantee is made regarding
  functionality or engineering support. Use at your own risk.

  There are several ways to run the conversion:

  1. FP32/FP16 precision

     ```python
     params = tf.experimental.tensorrt.ConversionParams(
         precision_mode=\'FP16\')
     converter = tf.experimental.tensorrt.Converter(
         input_saved_model_dir="my_dir", conversion_params=params)
     converter.convert()
     converter.save(output_saved_model_dir)
     ```

     In this case, no TRT engines will be built or saved in the converted
     SavedModel. But if input data is available during conversion, we can still
     build and save the TRT engines to reduce the cost during inference (see
     option 2 below).

  2. FP32/FP16 precision with pre-built engines

     ```python
     params = tf.experimental.tensorrt.ConversionParams(
         precision_mode=\'FP16\',
         # Set this to a large enough number so it can cache all the engines.
         maximum_cached_engines=16)
     converter = tf.experimental.tensorrt.Converter(
         input_saved_model_dir="my_dir", conversion_params=params)
     converter.convert()

     # Define a generator function that yields input data, and use it to execute
     # the graph to build TRT engines.
     def my_input_fn():
       for _ in range(num_runs):
         inp1, inp2 = ...
         yield inp1, inp2

     converter.build(input_fn=my_input_fn)  # Generate corresponding TRT engines
     converter.save(output_saved_model_dir)  # Generated engines will be saved.
     ```

     In this way, one engine will be built/saved for each unique input shapes of
     the TRTEngineOp. This is good for applications that cannot afford building
     engines during inference but have access to input data that is similar to
     the one used in production (for example, that has the same input shapes).
     Also, the generated TRT engines is platform dependent, so we need to run
     `build()` in an environment that is similar to production (e.g. with
     same type of GPU).

  3. INT8 precision and calibration with pre-built engines

     ```python
     params = tf.experimental.tensorrt.ConversionParams(
         precision_mode=\'INT8\',
         # Currently only one INT8 engine is supported in this mode.
         maximum_cached_engines=1,
         use_calibration=True)
     converter = tf.experimental.tensorrt.Converter(
         input_saved_model_dir="my_dir", conversion_params=params)

     # Define a generator function that yields input data, and run INT8
     # calibration with the data. All input data should have the same shape.
     # At the end of convert(), the calibration stats (e.g. range information)
     # will be saved and can be used to generate more TRT engines with different
     # shapes. Also, one TRT engine will be generated (with the same shape as
     # the calibration data) for save later.
     def my_calibration_input_fn():
       for _ in range(num_runs):
         inp1, inp2 = ...
         yield inp1, inp2

     converter.convert(calibration_input_fn=my_calibration_input_fn)

     # (Optional) Generate more TRT engines offline (same as the previous
     # option), to avoid the cost of generating them during inference.
     def my_input_fn():
       for _ in range(num_runs):
         inp1, inp2 = ...
         yield inp1, inp2
     converter.build(input_fn=my_input_fn)

     # Save the TRT engine and the engines.
     converter.save(output_saved_model_dir)
     ```
  4. To use dynamic shape, we need to call the build method with an input
     function to generate profiles. This step is similar to the INT8 calibration
     step described above. The converter also needs to be created with
     use_dynamic_shape=True and one of the following profile_strategies for
     creating profiles based on the inputs produced by the input function:
     * `Range`: create one profile that works for inputs with dimension values
       in the range of [min_dims, max_dims] where min_dims and max_dims are
       derived from the provided inputs.
     * `Optimal`: create one profile for each input. The profile only works for
       inputs with the same dimensions as the input it is created for. The GPU
       engine will be run with optimal performance with such inputs.
     * `Range+Optimal`: create the profiles for both `Range` and `Optimal`.
  '''
    freeze: Incomplete
    def __init__(self, input_saved_model_dir: Incomplete | None = None, input_saved_model_tags: Incomplete | None = None, input_saved_model_signature_key: Incomplete | None = None, use_dynamic_shape: Incomplete | None = None, dynamic_shape_profile_strategy: Incomplete | None = None, max_workspace_size_bytes=..., precision_mode=..., minimum_segment_size: int = 3, maximum_cached_engines: int = 1, use_calibration: bool = True, allow_build_at_runtime: bool = True, conversion_params: Incomplete | None = None) -> None:
        """Initialize the converter.

    Args:
      input_saved_model_dir: the directory to load the SavedModel which contains
        the input graph to transforms. Required.
      input_saved_model_tags: list of tags to load the SavedModel.
      input_saved_model_signature_key: the key of the signature to optimize the
        graph for.
      use_dynamic_shape: whether to enable dynamic shape support. None is
        equivalent to False in the current implementation.
      dynamic_shape_profile_strategy: one of the strings in
        supported_profile_strategies(). None is equivalent to Range in the
        current implementation.
      max_workspace_size_bytes: the maximum GPU temporary memory that the TRT
        engine can use at execution time. This corresponds to the
        'workspaceSize' parameter of nvinfer1::IBuilder::setMaxWorkspaceSize().
      precision_mode: one of the strings in
        TrtPrecisionMode.supported_precision_modes().
      minimum_segment_size: the minimum number of nodes required for a subgraph
        to be replaced by TRTEngineOp.
      maximum_cached_engines: max number of cached TRT engines for dynamic TRT
        ops. Created TRT engines for a dynamic dimension are cached. If the
        number of cached engines is already at max but none of them supports the
        input shapes, the TRTEngineOp will fall back to run the original TF
        subgraph that corresponds to the TRTEngineOp.
      use_calibration: this argument is ignored if precision_mode is not INT8.
        If set to True, a calibration graph will be created to calibrate the
        missing ranges. The calibration graph must be converted to an inference
        graph by running calibration with calibrate(). If set to False,
        quantization nodes will be expected for every tensor in the graph
        (excluding those which will be fused). If a range is missing, an error
        will occur. Please note that accuracy may be negatively affected if
        there is a mismatch between which tensors TRT quantizes and which
        tensors were trained with fake quantization.
      allow_build_at_runtime: whether to allow building TensorRT engines during
        runtime if no prebuilt TensorRT engine can be found that can handle the
        given inputs during runtime, then a new TensorRT engine is built at
        runtime if allow_build_at_runtime=True, and otherwise native TF is used.
      conversion_params: a TrtConversionParams instance (deprecated).

    Raises:
      ValueError: if the combination of the parameters is invalid.
    """
    def convert(self, calibration_input_fn: Incomplete | None = None):
        """Convert the input SavedModel in 2.0 format.

    Args:
      calibration_input_fn: a generator function that yields input data as a
        list or tuple or dict, which will be used to execute the converted
        signature for calibration. All the returned input data should have the
        same shape. Example: `def input_fn(): yield input1, input2, input3`

        If dynamic_shape_mode==False, (or if the graph has static input shapes)
        then we run calibration and build the calibrated engine during
        conversion.

        If dynamic_shape_mode==True (and the graph has any unknown input
        shape), then the reference to calibration_input_fn is stored, and the
        calibration is actually performed when we build the engine (see
        build()).

    Raises:
      ValueError: if the input combination is invalid.

    Returns:
      The TF-TRT converted Function.
    """
    def build(self, input_fn) -> None:
        """Run inference with converted graph in order to build TensorRT engines.

    If the conversion requires INT8 calibration, then a reference to the
    calibration function was stored during the call to convert(). Calibration
    will be performed while we build the TensorRT engines.

    Args:
      input_fn: a generator function that provides the input data as a single
        array, OR a list or tuple of the arrays OR a dict, which will be used
        to execute the converted signature to generate TRT engines.
        Example 1:
        `def input_fn():
             # Let's assume a network with 1 input tensor.
             # We generate 2 sets of dummy input data:
             input_shapes = [(1, 16),    # 1st shape
                             (2, 32)]    # 2nd shape
             for shapes in input_shapes:
                 # return an input tensor
                 yield np.zeros(shape).astype(np.float32)'

        Example 2:
        `def input_fn():
             # Let's assume a network with 2 input tensors.
             # We generate 3 sets of dummy input data:
             input_shapes = [[(1, 16), (2, 16)], # 1st input list
                             [(2, 32), (4, 32)], # 2nd list of two tensors
                             [(4, 32), (8, 32)]] # 3rd input list
             for shapes in input_shapes:
                 # return a list of input tensors
                 yield [np.zeros(x).astype(np.float32) for x in shapes]`

    Raises:
      NotImplementedError: build() is already called.
      RuntimeError: the input_fx is None.
    """
    def save(self, output_saved_model_dir, save_gpu_specific_engines: bool = True, options: Incomplete | None = None) -> None:
        """Save the converted SavedModel.

    Args:
      output_saved_model_dir: directory to saved the converted SavedModel.
      save_gpu_specific_engines: whether to save TRT engines that have been
        built. When True, all engines are saved and when False, the engines
        are not saved and will be rebuilt at inference time. By using
        save_gpu_specific_engines=False after doing INT8 calibration, inference
        can be done on different GPUs than the GPU that the model was calibrated
        and saved on.
      options: `tf.saved_model.SaveOptions` object for configuring save options.
    Raises:
      RuntimeError: if the needed calibration hasn't been done.
    """
    def summary(self, line_length: int = 160, detailed: bool = True, print_fn: Incomplete | None = None) -> None:
        """This method describes the results of the conversion by TF-TRT.

    It includes information such as the name of the engine, the number of nodes
    per engine, the input and output dtype, along with the input shape of each
    TRTEngineOp.

    Args:
      line_length: Default line length when printing on the console. Minimum 160
        characters long.
      detailed: Whether or not to show the nodes inside each TRTEngineOp.
      print_fn: Print function to use. Defaults to `print`. It will be called on
        each line of the summary. You can set it to a custom function in order
        to capture the string summary.

    Raises:
      RuntimeError: if the graph is not converted.
    """

def create_inference_graph(input_graph_def, outputs, max_batch_size: int = 1, max_workspace_size_bytes=..., precision_mode=..., minimum_segment_size: int = 3, is_dynamic_op: bool = False, maximum_cached_engines: int = 1, input_saved_model_dir: Incomplete | None = None, input_saved_model_tags: Incomplete | None = None, input_saved_model_signature_key: Incomplete | None = None, output_saved_model_dir: Incomplete | None = None):
    """Python wrapper for the TRT transformation.

  Args:
    input_graph_def: a GraphDef object containing a model to be transformed. If
      set to None, the graph will be read from the SavedModel loaded from
      input_saved_model_dir.
    outputs: list of tensors or node names for the model outputs. Only used when
      input_graph_def is not None.
    max_batch_size: max size for the input batch.
    max_workspace_size_bytes: the maximum GPU temporary memory which the TRT
      engine can use at execution time. This corresponds to the 'workspaceSize'
      parameter of nvinfer1::IBuilder::setMaxWorkspaceSize().
    precision_mode: one of TrtPrecisionMode.supported_precision_modes().
    minimum_segment_size: the minimum number of nodes required for a subgraph to
      be replaced by TRTEngineOp.
    is_dynamic_op: whether to generate dynamic TRT ops which will build the TRT
      network and engine at run time.
    maximum_cached_engines: max number of cached TRT engines in dynamic TRT ops.
      If the number of cached engines is already at max but none of them can
      serve the input, the TRTEngineOp will fall back to run the TF function
      based on which the TRTEngineOp is created.
    input_saved_model_dir: the directory to load the SavedModel which contains
      the input graph to transforms. Used only when input_graph_def is None.
    input_saved_model_tags: list of tags to load the SavedModel.
    input_saved_model_signature_key: the key of the signature to optimize the
      graph for.
    output_saved_model_dir: if not None, construct a SavedModel using the
      returned GraphDef and save it to the specified directory. This option only
      works when the input graph is loaded from a SavedModel, i.e. when
      input_saved_model_dir is specified and input_graph_def is None.

  Returns:
    A GraphDef transformed from input_graph_def (or the SavedModel graph def
    loaded from input_saved_model_dir, if input_graph_def is not present), where
    all TRT compatible subgraphs are replaced with TRTEngineOps, and a TF
    function is added for each of the subgraphs.

    If is_dynamic_op is True, each TRTEngineOp will contain a serialized
    subgraph GraphDef, which will be converted to a TRT engine at execution time
    and the TRT engine will be cached for future usage. A new TRT engine will be
    created each time when none of the cached engines match the input shapes. If
    it fails to execute the TRT engine or the number of cached engines reaches
    maximum_cached_engines, the op will fall back to call the corresponding TF
    function.

    If is_dynamic_op is False, each TRTEngineOp will contain a serialized TRT
    engine created from the corresponding subgraph. No more engines will be
    created on the fly, and the op will fall back to call the corresponding TF
    function when it fails to execute the engine.

  Raises:
    ValueError: if the combination of the parameters is invalid.
  """

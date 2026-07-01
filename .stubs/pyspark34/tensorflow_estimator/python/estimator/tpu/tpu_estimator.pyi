import enum
import tensorflow as tf
from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.ops import control_flow_ops
from tensorflow_estimator.python.estimator import estimator as estimator_lib, model_fn as model_fn_lib
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.tpu import error_handling as error_handling, iteration_count_estimator as iteration_count_estimator, tpu_config as tpu_config, tpu_context as tpu_context
from tensorflow_estimator.python.estimator.tpu._tpu_estimator_embedding import AdagradParameters as AdagradParameters, AdamParameters as AdamParameters, EmbeddingConfigSpec as EmbeddingConfigSpec, StochasticGradientDescentParameters as StochasticGradientDescentParameters
from typing import NamedTuple

class CatchInvalidHostcallFunctions(control_flow_ops.XLAControlFlowContext):
    def AddOp(self, op) -> None: ...

class PeriodicLogger:
    def __init__(self, seconds) -> None: ...
    def log(self, msg, *args, **kw) -> None: ...

class _SIGNAL:
    """Signal used to control the thread of infeed/outfeed.

  All preserved signals must be negative numbers. Positive numbers are used to
  indicate the number of iterations for next training/evaluation loop.
  """
    NEXT_BATCH: int
    STOP: int

class TPUEstimatorSpec(model_fn_lib._TPUEstimatorSpec):
    """Ops and objects returned from a `model_fn` and passed to `TPUEstimator`.

  See `EstimatorSpec` for `mode`, `predictions`, `loss`, `train_op`, and
  `export_outputs`.

  For evaluation, `eval_metrics `is a tuple of `metric_fn` and `tensors`, where
  `metric_fn` runs on CPU to generate metrics and `tensors` represents the
  `Tensor`s transferred from TPU system to CPU host and passed to `metric_fn`.
  To be precise, TPU evaluation expects a slightly different signature from the
  `tf.estimator.Estimator`. While `EstimatorSpec.eval_metric_ops` expects a
  dict, `TPUEstimatorSpec.eval_metrics` is a tuple of `metric_fn` and `tensors`.
  The `tensors` could be a list of `Tensor`s or dict of names to `Tensor`s. The
  `tensors` usually specify the model logits, which are transferred back from
  TPU system to CPU host. All tensors must have be batch-major, i.e., the batch
  size is the first dimension. Once all tensors are available at CPU host from
  all shards, they are concatenated (on CPU) and passed as positional arguments
  to the `metric_fn` if `tensors` is list or keyword arguments if `tensors` is
  a dict. `metric_fn` takes the `tensors` and returns a dict from metric string
  name to the result of calling a metric function, namely a `(metric_tensor,
  update_op)` tuple. See `TPUEstimator` for MNIST example how to specify the
  `eval_metrics`.

  `scaffold_fn` is a function running on CPU to generate the `Scaffold`. This
  function should not capture any Tensors in `model_fn`.

  `host_call` is a tuple of a `function` and a list or dictionary of `tensors`
  to pass to that function and returns a list of Tensors. `host_call` currently
  works for train() and evaluate(). The Tensors returned by the function is
  executed on the CPU on every step, so there is communication overhead when
  sending tensors from TPU to CPU. To reduce the overhead, try reducing the
  size of the tensors. The `tensors` are concatenated along their major (batch)
  dimension, and so must be >= rank 1. The `host_call` is useful for writing
  summaries with `tf.contrib.summary.create_file_writer`.

  @compatibility(TF2)
  TPU Estimator manages its own TensorFlow graph and session, so it is not
  compatible with TF2 behaviors. We recommend that you migrate to the newer
  `tf.distribute.TPUStrategy`. See the
  [TPU guide](https://www.tensorflow.org/guide/tpu) for details.
  @end_compatibility
  """
    def __new__(cls, mode, predictions: Incomplete | None = None, loss: Incomplete | None = None, train_op: Incomplete | None = None, eval_metrics: Incomplete | None = None, export_outputs: Incomplete | None = None, scaffold_fn: Incomplete | None = None, host_call: Incomplete | None = None, training_hooks: Incomplete | None = None, evaluation_hooks: Incomplete | None = None, prediction_hooks: Incomplete | None = None):
        """Creates a validated `TPUEstimatorSpec` instance."""
    def as_estimator_spec(self):
        """Creates an equivalent `EstimatorSpec` used by CPU train/eval."""

class _OpQueueContext:
    """Manages work queue and thread for a infeed/outfeed thread."""
    def __init__(self, name, target, args) -> None: ...
    def stop(self) -> None: ...
    def send_next_batch_signal(self, iterations) -> None: ...
    def read_iteration_counts(self) -> Generator[Incomplete, None, None]: ...
    def join(self) -> None: ...

class _OpSignalOnceQueueContext(_OpQueueContext):
    """Manages work queue and thread for a infeed/outfeed thread.

  This subclass only signals once.
  """
    def __init__(self, name, target, args) -> None: ...
    def send_next_batch_signal(self, iterations) -> None: ...

class TPUInfeedOutfeedSessionHook(tf.compat.v1.train.SessionRunHook):
    """A Session hook setting up the TPU initialization, infeed, and outfeed.

  This hook does two major things:
  1. initialize and shutdown TPU system.
  2. launch and join the threads for infeed enqueue and (optional) outfeed
     dequeue.
  """
    def __init__(self, ctx, enqueue_ops, dequeue_ops, tpu_compile_op, run_infeed_loop_on_coordinator: bool = True, rendezvous: Incomplete | None = None, master: Incomplete | None = None, session_config: Incomplete | None = None, tpu_init_ops: Incomplete | None = None, outfeed_every_n_steps: int = 1) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def before_run(self, run_context) -> None: ...
    def end(self, session) -> None: ...

class TPUInfeedOutfeedSessionHookForPrediction(TPUInfeedOutfeedSessionHook):
    def __init__(self, ctx, enqueue_ops, dequeue_ops, tpu_compile_op, rendezvous: Incomplete | None = None, master: Incomplete | None = None, session_config: Incomplete | None = None) -> None: ...

class _TPUStopAtStepHook(tf.compat.v1.train.SessionRunHook):
    """Hook that requests stop at a specified step.

  This hook is similar to the `session_run_hook._StopAfterNEvalsHook` with
  following differences for TPU training:

  1. This hook sets the variable for `iterations_per_loop`, which is used by
     `TPUInfeedOutfeedSessionHook` to control the iterations for infeed/outfeed.
     If the `iterations_per_loop` value is specified as time in seconds, the
     number of iterations per `Session.run` will be estimated automatically
     based on per iteration runtime.

     As the hook execution order is not guaranteed, the variable update is
     handled in `after_create_session` and `after_run` as
     `TPUInfeedOutfeedSessionHook` reads the variable value in `before_run`.

  2. For each training loop (session.run), the global step could be increased
     multiple times on TPU. The global step tensor value will be explicitly read
     again in `after_run` to ensure the latest value is retrieved to avoid race
     condition.
  """
    def __init__(self, iterations_per_loop_counter, num_steps: Incomplete | None = None, final_step: Incomplete | None = None) -> None:
        """Initializes a `TPUStopAtStepHook`.

    Args:
      iterations_per_loop_counter: A namedtuple of [`value',`unit`] that
        represents the number of 'iterations count' or 'time in seconds' to run
        optimizer per loop, based on the `unit` specified, `count` or `seconds`
        respectively.
      num_steps: Number of steps to execute.
      final_step: Step after which to stop.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
    def begin(self) -> None:
        """Initializes variables.

    Initializes the global step and iterations per loop variables.

    Raises:
      RuntimeError: An error occurred if global step variable does not exist.
    """
    def after_create_session(self, session, coord) -> None:
        """Computes and updates the first time iterations count.

    The iterations are computed by choosing the smaller of the (`final step` -
    `global step`), and the initial estimated iterations returned by the
    estimator (by default is 1).

    Args:
      session: A TensorFlow Session that has been created.
      coord: A Coordinator object which keeps track of all threads.
    """
    def before_run(self, run_context) -> None:
        """Reset the timer."""
    def after_run(self, run_context, run_values) -> None:
        """Computes the next iterations per loop value or terminates.

    Computes the elapsed time to run the last optimizer loop and if the
    `IterationCountEstimator` is used, records the elapsed time and iterations
    count. If the final step count has been reached, terminates. Otherwise,
    computes and updates the number of iterations to run the optimizer per loop.

    Args:
      run_context: A `SessionRunContext` object.
      run_values: A SessionRunValues object.
    """

class _SetEvalIterationsHook(tf.compat.v1.train.SessionRunHook):
    """Hook that requests stop at a specified step."""
    def __init__(self, num_steps) -> None:
        """Initializes a `_SetEvalIterationsHook`.

    Args:
      num_steps: Number of steps to execute.
    """
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...

class _StoppingPredictHook(tf.compat.v1.train.SessionRunHook):
    """Hook that requests stop according to the stopping signal in prediction."""
    def __init__(self, scalar_stopping_signal) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

def generate_per_core_enqueue_ops_fn_for_host(ctx, input_fn, inputs_structure_recorder, host_device, host_id):
    """Generates infeed enqueue ops for per-core input_fn on a single host."""
def generate_per_host_enqueue_ops_fn_for_host(ctx, input_fn, inputs_structure_recorder, batch_axis, device, host_id):
    """Generates infeed enqueue ops for per-host input_fn on a single host."""
def generate_per_host_v2_enqueue_ops_fn_for_host(ctx, input_fn, inputs_structure_recorder, device, host_id, invocation_index):
    """Generates infeed enqueue ops for per-host input_fn on a single host."""
def generate_broadcast_enqueue_ops_fn(ctx, input_fn, inputs_structure_recorder, num_hosts):
    """Generates infeed enqueue ops for one input_fn on all the hosts."""

class TensorPacker:
    """Pack and unpack small tensors into a big one for efficiency."""
    def __init__(self, small_feature_dim_size, minimum_num_small_features_to_group) -> None: ...
    def maybe_concatenate_features(self, features) -> None:
        """If there are enough small tensors, concat them for performance."""
    def maybe_split_features(self, maybe_concatenated_features) -> None: ...

class _InputPipeline:
    """`_InputPipeline` handles invoking `input_fn` and piping to infeed queue.

  `_InputPipeline` abstracts the per-core/per-host `input_fn` invocation from
  call site.  To be precise, based on the configuration in
  `_InternalTPUContext`,  it invokes `input_fn` for all cores (usually
  multi-host TPU training) or for one host (usually for single-host TPU
  evaluation), and sends all `features` and `labels` returned by `input_fn` to
  TPU infeed. For per-core invocation, `features` and `labels` are piped to
  infeed directly, one tuple for each core. For per-host invocation,  `features`
  and `labels` are split at host (with respect to `batch_axis`) and piped to all
  cores accordingly.

  In addition, flatten/unflatten are handled by `_InputPipeline` also.  Model
  inputs returned by the `input_fn` can have one of the following forms:
  1. features
  2. (features, labels)
  3. ((arbitrarily nested structure of features), labels)

  Internally, form 1 is reformed to `(features, None)` as features and labels
  are passed separately to underlying methods. For TPU training, TPUEstimator
  may expect multiple `features` and `labels` tuples one for each core.

  TPUEstimator allows various different structures for inputs (namely `features`
  and `labels`).  Both `features` and `labels` can be any nested sturcture
  supported by TF nest (namely, dict, tuples, namedtuples or any nested
  structure of such of Tensors).  `labels` could be `None` as well.

  These are flattened before they are passed to the infeed/outfeed library
  as that expectes flattend lists.
  """
    class InputsStructureRecorder:
        """The recorder to record inputs structure."""
        def __init__(self, input_partition_dims: Incomplete | None = None) -> None: ...
        @property
        def flattened_input_dims(self): ...
        def has_labels(self): ...
        def validate_and_record_structure(self, features, labels) -> None:
            """Validates and records the structure of `features` and `labels`."""
        tensor_packer: Incomplete
        def flatten_features_and_labels(self, features, labels, signals: Incomplete | None = None):
            """Flattens the `features` and `labels` to a single tensor list."""
        def unflatten_features_and_labels(self, flattened_inputs):
            """Restores the flattened inputs to original features and labels form.

      Args:
        flattened_inputs: Flattened inputs for each shard.

      Returns:
        A tuple of (`features`, `labels`), where `labels` could be None.
        Each one, if present, should have identical structure (single tensor vs
        dict) as the one returned by input_fn.

      Raises:
        ValueError: If the number of expected tensors from `flattened_inputs`
          mismatches the recorded structure.
      """
    def __init__(self, input_fn, batch_axis, ctx) -> None:
        """Constructor.

    Args:
      input_fn: input fn for train or eval.
      batch_axis: A python tuple of int values describing how each tensor
        produced by the Estimator `input_fn` should be split across the TPU
        compute shards.
      ctx: A `_InternalTPUContext` instance with mode.

    Raises:
      ValueError: If both `sharded_features` and `num_cores` are `None`.
    """
    def generate_infeed_enqueue_ops_and_dequeue_fn(self):
        """Generates infeed enqueue ops and dequeue_fn."""

def call_computation(computation_inputs, computation, batch_config: Incomplete | None = None):
    """Call computation.

  Args:
    computation_inputs: A tensor or dict of tensors, the inputs to the
      computation.
    computation: A Python function that takes no inputs and builds computation
      graph. If `computation` returns m outputs, this function will return a
      list of m Tensors.
    batch_config: A BatchConfig named tuple specifying the batching
      configuration to use for inference batching.

  Returns:
    A list of output tensors.
  """

class _ModelFnWrapper:
    """A `model_fn` wrapper.

  This makes calling model_fn on CPU and TPU easier and more consistent and
  performs necessary check and mutation required by TPU training and evaluation.

  In addition, this wrapper manages converting the `model_fn` to a single TPU
  train and eval step.
  """
    def __init__(self, model_fn, config, params, ctx) -> None: ...
    def call_without_tpu(self, features, labels, is_export_mode): ...
    def convert_to_single_tpu_train_step(self, dequeue_fn):
        """Converts user provided model_fn` as a single train step on TPU.

    The user provided `model_fn` takes input tuple
    (features, labels) and produces the EstimatorSpec with train_op and loss for
    train `mode`. This usually represents a single train computation on CPU.

    For TPU training, a train (computation) step is first wrapped in a
    tf.while_loop control flow to repeat for many times and then replicated to
    all TPU shards. Besides the input should be taken from TPU infeed rather
    than input pipeline (input_fn) directly. To fit TPU loop and replicate
    pattern, the original train computation should be reformed, which is the
    returned `train_step`.

    Args:
      dequeue_fn: The function to retrieve inputs, features and labels, from TPU
        infeed dequeue channel.

    Returns:
      A tuple of train_fn, host_calls, and captured scaffold_fn. The train_fn
      representing the train step for TPU.
    """
    def convert_to_single_tpu_eval_step(self, dequeue_fn):
        """Converts user provided model_fn` as a single eval step on TPU.

    Similar to training, the user provided `model_fn` takes input tuple
    (features, labels) and produces the TPUEstimatorSpec with eval_metrics for
    eval `mode`. This usually represents a single evaluation computation on CPU.

    For TPU evaluation, a eval (computation) step is first wrapped in a
    tf.while_loop control flow to repeat for many times and then replicated to
    all TPU shards. Besides the input and output are slightly different. Input,
    features and labels, should be taken from TPU infeed rather than input
    pipeline (input_fn) directly. Output is managed in two stages.  First, the
    model outputs as the result of evaluation computation, usually model logits,
    should be transferred from TPU system to CPU. Then, all model outputs are
    concatenated first on CPU and sent to the metric_fn for metrics computation.
    To fit TPU evaluation pattern, the original eval computation should be
    reformed, which is the returned `eval_step`.

    Args:
      dequeue_fn: The function to retrieve inputs, features and labels, from TPU
        infeed dequeue channel.

    Returns:
      A tuple of eval_fn, host_calls, and captured scaffold_fn. The eval_fn
      representing the eval step for TPU.
    """
    def convert_to_single_tpu_predict_step(self, dequeue_fn):
        """Converts user provided model_fn` as a single predict step on TPU.

    Args:
      dequeue_fn: The function to retrieve inputs, features and labels, from TPU
        infeed dequeue channel.

    Returns:
      A tuple of predict_fn, host_calls, and captured scaffold_fn. The
      predict_fn representing the predict step for TPU.
    """

class _OutfeedHostCall:
    """Support for `eval_metrics` and `host_call` in TPUEstimatorSpec."""
    def __init__(self, ctx, outfeed_every_n_steps: int = 1) -> None: ...
    @staticmethod
    def validate(host_calls) -> None:
        """Validates the `eval_metrics` and `host_call` in `TPUEstimatorSpec`."""
    @staticmethod
    def create_cpu_hostcall(host_calls):
        """Runs on the host_call on CPU instead of TPU when use_tpu=False."""
    def record(self, host_calls) -> None:
        """Records the host_call structure."""
    def create_enqueue_op(self, step: Incomplete | None = None):
        """Create the op to enqueue the recorded host_calls.

    Returns:
      A list of enqueue ops, which is empty if there are no host calls.
    """
    def create_tpu_hostcall(self):
        """Sends the tensors through outfeed and runs the host_fn on CPU.

    The tensors are concatenated along dimension 0 to form a global tensor
    across all shards. The concatenated function is passed to the host_fn and
    executed on the first host.

    Returns:
      A dictionary mapping name to the return type of the host_call by that
      name.

    Raises:
      RuntimeError: If outfeed tensor is scalar.
    """

class _OutfeedHostCallHook(tf.compat.v1.train.SessionRunHook):
    """Hook to run host calls when use_tpu=False."""
    def __init__(self, tensors) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def before_run(self, run_context): ...
    def end(self, session) -> None: ...

class _NotSaver:
    """What to pass instead of a saver object if you don't want saving."""
    def __init__(self, message) -> None: ...
    def save(self, *args, **kwargs) -> None: ...

class ExamplesPerSecondHook(tf.compat.v1.train.StepCounterHook):
    """Calculate and report global_step/sec and examples/sec during runtime."""
    def __init__(self, batch_size, every_n_steps: int = 100, every_n_secs: Incomplete | None = None, output_dir: Incomplete | None = None, summary_writer: Incomplete | None = None) -> None: ...

class InstallSignalHandlerHook(tf.compat.v1.train.SessionRunHook):
    """Change SIGINT (CTRL^C) handler to force quit the process.

  The default behavior often results in hanging processes.
  The original handler is restored after training/evaluation.
  """
    def __init__(self) -> None: ...
    def before_run(self, run_context) -> None: ...
    def end(self, session) -> None: ...

class ExportSavedModelApiVersion(enum.Enum):
    V1: int
    V2: int

class BatchConfig(NamedTuple('BatchConfig', [('num_batch_threads', Incomplete), ('max_batch_size', Incomplete), ('batch_timeout_micros', Incomplete), ('allowed_batch_sizes', Incomplete), ('max_enqueued_batches', Incomplete)])):
    """Class to handle config inputs into the batching function."""
    def __new__(cls, num_batch_threads, max_batch_size, batch_timeout_micros, allowed_batch_sizes, max_enqueued_batches: int = 100):
        """Creates an BatchConfig instance.

    Args:
     num_batch_threads: Number of scheduling threads for processing batches of
       work. Determines the number of batches processed in parallel.
      max_batch_size: Batch sizes will never be bigger than this.
      batch_timeout_micros: Maximum number of microseconds to wait before
        outputting an incomplete batch.
      allowed_batch_sizes: Optional list of allowed batch sizes. If left empty,
        does nothing. Otherwise, supplies a list of batch sizes, causing the op
        to pad batches up to one of those sizes. The entries must increase
        monotonically, and the final entry must equal max_batch_size.
      max_enqueued_batches: The maximum depth of the batch queue. Defaults to
        100.

    Returns:
      An BatchConfig instance.
    """

class TPUEstimator(estimator_lib.Estimator):
    """Estimator with TPU support.

  TPUEstimator also supports training on CPU and GPU. You don't need to define
  a separate `tf.estimator.Estimator`.

  TPUEstimator handles many of the details of running on TPU devices, such as
  replicating inputs and models for each core, and returning to host
  periodically to run hooks.

  TPUEstimator transforms a global batch size in params to a per-shard batch
  size when calling the `input_fn` and `model_fn`. Users should specify
  global batch size in constructor, and then get the batch size for each shard
  in `input_fn` and `model_fn` by `params['batch_size']`.

  - For training, `model_fn` gets per-core batch size; `input_fn` may get
    per-core or per-host batch size depending on `per_host_input_for_training`
    in `TPUConfig` (See docstring for TPUConfig for details).

  - For evaluation and prediction, `model_fn` gets per-core batch size and
    `input_fn` get per-host batch size.

  Evaluation
  ==========

  `model_fn` should return `TPUEstimatorSpec`, which expects the `eval_metrics`
  for TPU evaluation. If eval_on_tpu is False, the evaluation will execute on
  CPU or GPU; in this case the following discussion on TPU evaluation does not
  apply.

  `TPUEstimatorSpec.eval_metrics` is a tuple of `metric_fn` and `tensors`, where
  `tensors` could be a list of any nested structure of `Tensor`s (See
  `TPUEstimatorSpec` for details).  `metric_fn` takes the `tensors` and returns
  a dict from metric string name to the result of calling a metric function,
  namely a `(metric_tensor, update_op)` tuple.

  One can set `use_tpu` to `False` for testing. All training, evaluation, and
  predict will be executed on CPU. `input_fn` and `model_fn` will receive
  `train_batch_size` or `eval_batch_size` unmodified as `params['batch_size']`.

  Current limitations:
  --------------------

  1. TPU evaluation only works on a single host (one TPU worker) except
     BROADCAST mode.

  2. `input_fn` for evaluation should **NOT** raise an end-of-input exception
     (`OutOfRangeError` or `StopIteration`). And all evaluation steps and all
     batches should have the same size.

  Example (MNIST):
  ----------------

  ```
  # The metric Fn which runs on CPU.
  def metric_fn(labels, logits):
    predictions = tf.argmax(logits, 1)
    return {
      'accuracy': tf.compat.v1.metrics.precision(
          labels=labels, predictions=predictions),
    }

  # Your model Fn which runs on TPU (eval_metrics is list in this example)
  def model_fn(features, labels, mode, config, params):
    ...
    logits = ...

    if mode = tf.estimator.ModeKeys.EVAL:
      return tpu_estimator.TPUEstimatorSpec(
          mode=mode,
          loss=loss,
          eval_metrics=(metric_fn, [labels, logits]))

  # or specify the eval_metrics tensors as dict.
  def model_fn(features, labels, mode, config, params):
    ...
    final_layer_output = ...

    if mode = tf.estimator.ModeKeys.EVAL:
      return tpu_estimator.TPUEstimatorSpec(
          mode=mode,
          loss=loss,
          eval_metrics=(metric_fn, {
              'labels': labels,
              'logits': final_layer_output,
          }))
  ```

  Prediction
  ==========

  Prediction on TPU is an experimental feature to support large batch inference.
  It is not designed for latency-critical system. In addition, due to some
  usability issues, for prediction with small dataset, CPU `.predict`, i.e.,
  creating a new `TPUEstimator` instance with `use_tpu=False`, might be more
  convenient.

  Note: In contrast to TPU training/evaluation, the `input_fn` for prediction
  *should* raise an end-of-input exception (`OutOfRangeError` or
  `StopIteration`), which serves as the stopping signal to `TPUEstimator`. To be
  precise, the ops created by `input_fn` produce one batch of the data.
  The `predict()` API processes one batch at a time. When reaching the end of
  the data source, an end-of-input exception should be raised by one of these
  operations. The user usually does not need to do this manually. As long as the
  dataset is not repeated forever, the `tf.data` API will raise an end-of-input
  exception automatically after the last batch has been produced.

  Note: Estimator.predict returns a Python generator. Please consume all the
  data from the generator so that TPUEstimator can shutdown the TPU system
  properly for user.

  Current limitations:
  --------------------
  1. TPU prediction only works on a single host (one TPU worker).

  2. `input_fn` must return a `Dataset` instance rather than `features`. In
  fact, .train() and .evaluate() also support Dataset as return value.

  Example (MNIST):
  ----------------
  ```
  height = 32
  width = 32
  total_examples = 100

  def predict_input_fn(params):
    batch_size = params['batch_size']

    images = tf.random.uniform(
        [total_examples, height, width, 3], minval=-1, maxval=1)

    dataset = tf.data.Dataset.from_tensor_slices(images)
    dataset = dataset.map(lambda images: {'image': images})

    dataset = dataset.batch(batch_size)
    return dataset

  def model_fn(features, labels, params, mode):
     # Generate predictions, called 'output', from features['image']

    if mode == tf.estimator.ModeKeys.PREDICT:
      return tf.contrib.tpu.TPUEstimatorSpec(
          mode=mode,
          predictions={
              'predictions': output,
              'is_padding': features['is_padding']
          })

  tpu_est = TPUEstimator(
      model_fn=model_fn,
      ...,
      predict_batch_size=16)

  # Fully consume the generator so that TPUEstimator can shutdown the TPU
  # system.
  for item in tpu_est.predict(input_fn=input_fn):
    # Filter out item if the `is_padding` is 1.
    # Process the 'predictions'
  ```

  Exporting
  =========

  `export_saved_model` exports 2 metagraphs, one with `saved_model.SERVING`, and
  another with `saved_model.SERVING` and `saved_model.TPU` tags. At serving
  time, these tags are used to select the appropriate metagraph to load.

  Before running the graph on TPU, the TPU system needs to be initialized. If
  TensorFlow Serving model-server is used, this is done automatically. If not,
  please use `session.run(tpu.initialize_system())`.

  There are two versions of the API: 1 or 2.

  In V1, the exported CPU graph is `model_fn` as it is. The exported TPU graph
  wraps `tpu.rewrite()` and `TPUPartitionedCallOp` around `model_fn` so
  `model_fn` is on TPU by default. To place ops on CPU,
  `tpu_replication.outside_compilation(host_call, logits)` can be used.

  Example:
  ----------------

  ```
  def model_fn(features, labels, mode, config, params):
    ...
    logits = ...
    export_outputs = {
      'logits': export_output_lib.PredictOutput(
        {'logits': logits})
    }

    def host_call(logits):
      class_ids = math_ops.argmax(logits)
      classes = string_ops.as_string(class_ids)
      export_outputs['classes'] =
        export_output_lib.ClassificationOutput(classes=classes)

    tpu_replication.outside_compilation(host_call, logits)

    ...
  ```

  In V2, `export_saved_model()` sets up `params['use_tpu']` flag to let the user
  know if the code is exporting to TPU (or not). When `params['use_tpu']` is
  `True`, users need to call `tpu.rewrite()`, `TPUPartitionedCallOp` and/or
  `batch_function()`.

  TIP: V2 is recommended as it is more flexible (eg: batching, etc).

  @compatibility(TF2)
  TPU Estimator manages its own TensorFlow graph and session, so it is not
  compatible with TF2 behaviors. We recommend that you migrate to the newer
  `tf.distribute.TPUStrategy`. See the
  [TPU guide](https://www.tensorflow.org/guide/tpu) for details.
  @end_compatibility
  """
    def __init__(self, model_fn: Incomplete | None = None, model_dir: Incomplete | None = None, config: Incomplete | None = None, params: Incomplete | None = None, use_tpu: bool = True, train_batch_size: Incomplete | None = None, eval_batch_size: Incomplete | None = None, predict_batch_size: Incomplete | None = None, batch_axis: Incomplete | None = None, eval_on_tpu: bool = True, export_to_tpu: bool = True, export_to_cpu: bool = True, warm_start_from: Incomplete | None = None, embedding_config_spec: Incomplete | None = None, export_saved_model_api_version=...) -> None:
        """Constructs an `TPUEstimator` instance.

    Args:
      model_fn: Model function as required by `Estimator` which returns
        EstimatorSpec or TPUEstimatorSpec. `training_hooks`, 'evaluation_hooks',
        and `prediction_hooks` must not capure any TPU Tensor inside the
        model_fn.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model. If `None`, the model_dir in
        `config` will be used if set. If both are set, they must be same. If
        both are `None`, a temporary directory will be used.
      config: An `tpu_config.RunConfig` configuration object. Cannot be `None`.
      params: An optional `dict` of hyper parameters that will be passed into
        `input_fn` and `model_fn`.  Keys are names of parameters, values are
        basic python types. There are reserved keys for `TPUEstimator`,
        including 'batch_size'.
      use_tpu: A bool indicating whether TPU support is enabled. Currently, -
        TPU training and evaluation respect this bit, but eval_on_tpu can
        override execution of eval. See below.
      train_batch_size: An int representing the global training batch size.
        TPUEstimator transforms this global batch size to a per-shard batch
        size, as params['batch_size'], when calling `input_fn` and `model_fn`.
        Cannot be `None` if `use_tpu` is `True`. Must be divisible by total
        number of replicas.
      eval_batch_size: An int representing evaluation batch size. Must be
        divisible by total number of replicas.
      predict_batch_size: An int representing the prediction batch size. Must be
        divisible by total number of replicas.
      batch_axis: A python tuple of int values describing how each tensor
        produced by the Estimator `input_fn` should be split across the TPU
        compute shards. For example, if your input_fn produced (images, labels)
        where the images tensor is in `HWCN` format, your shard dimensions would
        be [3, 0], where 3 corresponds to the `N` dimension of your images
        Tensor, and 0 corresponds to the dimension along which to split the
        labels to match up with the corresponding images. If None is supplied,
        and per_host_input_for_training is True, batches will be sharded based
        on the major dimension. If tpu_config.per_host_input_for_training is
        False or `PER_HOST_V2`, batch_axis is ignored.
      eval_on_tpu: If False, evaluation runs on CPU or GPU. In this case, the
        model_fn must return `EstimatorSpec` when called with `mode` as `EVAL`.
      export_to_tpu: If True, `export_saved_model()` exports a metagraph for
        serving on TPU. Note that unsupported export modes such as EVAL will be
        ignored. For those modes, only a CPU model will be exported. Currently,
        export_to_tpu only supports PREDICT.
      export_to_cpu: If True, `export_saved_model()` exports a metagraph for
        serving on CPU.
      warm_start_from: Optional string filepath to a checkpoint or SavedModel to
        warm-start from, or a `tf.estimator.WarmStartSettings` object to fully
        configure warm-starting.  If the string filepath is provided instead of
        a `WarmStartSettings`, then all variables are warm-started, and it is
        assumed that vocabularies and Tensor names are unchanged.
      embedding_config_spec: Optional EmbeddingConfigSpec instance to support
        using TPU embedding.
      export_saved_model_api_version: an integer: 1 or 2. 1 corresponds to V1,
        2 corresponds to V2. (Defaults to V1). With
        V1, `export_saved_model()` adds rewrite() and TPUPartitionedCallOp() for
        user; while in v2, user is expected to add rewrite(),
        TPUPartitionedCallOp() etc in their model_fn.

    Raises:
      ValueError: `params` has reserved keys already.
    """
    def train(self, input_fn, hooks: Incomplete | None = None, steps: Incomplete | None = None, max_steps: Incomplete | None = None, saving_listeners: Incomplete | None = None): ...
    def evaluate(self, input_fn, steps: Incomplete | None = None, hooks: Incomplete | None = None, checkpoint_path: Incomplete | None = None, name: Incomplete | None = None): ...
    def predict(self, input_fn, predict_keys: Incomplete | None = None, hooks: Incomplete | None = None, checkpoint_path: Incomplete | None = None, yield_single_examples: bool = True) -> Generator[Incomplete, None, None]: ...

class _CapturedObject:
    """A placeholder to capture an object.

  This is useful when we need to capture a Python object in the Tensorflow
  control flow body function and use it outside the control flow.
  """
    def __init__(self) -> None: ...
    def capture(self, o) -> None: ...
    def get(self): ...

class _CapturingContext(control_flow_ops.ControlFlowContext):
    """Tracks references to Tensors defined in TPU replication."""
    def __init__(self, message) -> None: ...
    def to_control_flow_context_def(self, context_def, export_scope: Incomplete | None = None) -> None: ...
    def AddOp(self, op) -> None: ...
    def AddValue(self, value): ...
    def __enter__(self) -> None: ...
    def __exit__(self, _: type[BaseException] | None, __: BaseException | None, ___: types.TracebackType | None) -> None: ...

class _Inputs:
    """A data structure representing the input_fn returned values.

  This also supports the returned value from input_fn as `Dataset`.
  """
    def __init__(self, features: Incomplete | None = None, labels: Incomplete | None = None, dataset: Incomplete | None = None, signals: Incomplete | None = None) -> None: ...
    @staticmethod
    def from_input_fn(return_values):
        """Returns an `_Inputs` instance according to `input_fn` return value."""
    @property
    def is_dataset(self):
        """Returns True if the return value from input_fn is Dataset."""
    def dataset_initializer(self):
        """Returns the dataset's initializer.

    The initializer must be run before calling `features_and_labels`.
    """
    def features_and_labels(self):
        """Gets `features` and `labels`."""
    def signals(self): ...
    @property
    def dataset(self): ...

class _InputsWithStoppingSignals(_Inputs):
    """Inputs with `_StopSignals` inserted into the dataset."""
    def __init__(self, dataset, batch_size, add_padding: bool = False, num_invocations_per_step: int = 1) -> None: ...
    def features_and_labels(self): ...
    def signals(self):
        """Returns the `Signals` from `_Inputs`."""
    @staticmethod
    def insert_stopping_signal(stop, batch_size, add_padding: bool = False):
        """Inserts stopping_signal into dataset via _map_fn.

    Here we change the data structure in the dataset, such that the return value
    is a dictionary now and `features`, `labels`, and `signals` are three
    distinguished keys in that dict. This provides a better structure, which
    eases the process to decompose the inputs (see `features_and_labels`).

    Args:
      stop: bool, state of current stopping signals.
      batch_size: int, batch size.
      add_padding: bool, whether to pad the tensor to full batch size.

    Returns:
      A map_fn passed to dataset.map API.
    """

class _StopSignals:
    """Signals class holding all logic to handle TPU stopping condition."""
    NON_STOPPING_SIGNAL: bool
    STOPPING_SIGNAL: bool
    def __init__(self, stop, batch_size, padding_mask: Incomplete | None = None) -> None: ...
    def as_dict(self):
        """Returns the signals as Python dict."""
    @staticmethod
    def as_scalar_stopping_signal(signals): ...
    @staticmethod
    def should_stop(scalar_stopping_signal):
        """Detects whether scalar_stopping_signal indicates stopping."""

class _PaddingSignals:
    """Signals class holding all logic to handle padding."""
    @staticmethod
    def pad_features_and_labels(features, labels, batch_size):
        """Pads out the batch dimension of features and labels."""
    @staticmethod
    def slice_tensor_or_dict(tensor_or_dict, signals):
        """Slice the real Tensors according to padding mask in signals."""

def export_estimator_savedmodel(estimator, export_dir_base, serving_input_receiver_fn, assets_extra: Incomplete | None = None, as_text: bool = False, checkpoint_path: Incomplete | None = None):
    """Export `Estimator` trained model for TPU inference.

  Args:
    estimator: `Estimator` with which model has been trained.
    export_dir_base: A string containing a directory in which to create
      timestamped subdirectories containing exported SavedModels.
    serving_input_receiver_fn: A function that takes no argument and returns a
      `ServingInputReceiver` or `TensorServingInputReceiver`.
    assets_extra: A dict specifying how to populate the assets.extra directory
      within the exported SavedModel, or `None` if no extra assets are needed.
    as_text: whether to write the SavedModel proto in text format.
    checkpoint_path: The checkpoint path to export.  If `None` (the default),
      the most recent checkpoint found within the model directory is chosen.

  Returns:
    The string path to the exported directory.
  """
def model_fn_inference_on_tpu(model_fn, features, labels: Incomplete | None = None, config: Incomplete | None = None, params: Incomplete | None = None, batch_config: Incomplete | None = None):
    '''Convenience wrapper for export_saved_model API v2 for a model_fn.
  WARNING:THIS METHOD IS DEPRECATED AND NOT PART OF THE APIS.

  Make sure to set
  `export_saved_model_api_version=tpu_estimator.ExportSavedModelApiVersion.V2`
  when initializing TPUEstimator (default API version is V1). This is because
  1) `tpu.rewrite` (or `tpu.compile`) shouldn\'t be called in a nested way
      (otherwise validation will throw error like
      "NotImplementedError: tpu_shard_context cannot be nested.")
  2) When using V1 API, Estimator calls `tpu.rewrite` so
     using `model_fn_inference_on_tpu` will trigger a nested call.
     When using V2 API, users of Estimator needs to call `tpu.rewrite` (which
     the wrapper does).

  It attempts to execute the entire model function on the TPU for prediction.
  Note that this does not support features which are SparseTensors. If you have
  SparseTensor features, consider partitioning your model function further and
  use inference_on_tpu.

  Args:
    model_fn: the model_fn for which we want to inference on TPU.
    features: a tensor or dict of tensors, serves as the feature inputs to the
      model.
    labels: a tensor or dict of tensors, serves as the labels inputs to the
      model.
    config: auxiliary config to the Estimator.
    params: hparams that we want to pass to the model_fn.
    batch_config: a named tuple to wrap the inference batching configuration
      inputs.

  Returns:
    An EstimatorSpec containing the outputs in export_outputs and predictions.
  '''
def inference_on_tpu(computation, inputs_to_tpu, num_batch_threads, max_batch_size, batch_timeout_micros, allowed_batch_sizes: Incomplete | None = None, max_enqueued_batches: int = 100):
    '''Convenient wrapper for export_saved_model API v2 to wrap TPU computation.

  WARNING: THIS METHOD IS DEPRECATED AND NOT PART OF THE APIS.

  Make sure to set
  `export_saved_model_api_version=tpu_estimator.ExportSavedModelApiVersion.V2`
  when initializing TPUEstimator (default API version is V1). This is because
  1) `tpu.rewrite` (or `tpu.compile`) shouldn\'t be called in a nested way
      (otherwise validation will throw error like
      "NotImplementedError: tpu_shard_context cannot be nested.")
  2) When using V1 API, Estimator calls `tpu.rewrite` so
     using `model_fn_inference_on_tpu` will trigger a nested call.
     When using V2 API, users of Estimator needs to call `tpu.rewrite` (which
     the wrapper does).

  It puts computation on TPU, add batching around it and round robin computation
  between TPU cores.

  See tpu_estimator_test.py for an example.

  Args:
    computation: computation to be put on TPU, which takes inputs_to_tpu as
      arguments.
    inputs_to_tpu: a list of tensors as input to computation.
    num_batch_threads: Number of scheduling threads for processing batches of
      work. Determines the number of batches processed in parallel.
    max_batch_size: Batch sizes will never be bigger than this. If None or 0,
      no batching will done.
    batch_timeout_micros: Maximum number of microseconds to wait before
      outputting an incomplete batch.
    allowed_batch_sizes: Optional list of allowed batch sizes. If left empty,
      does nothing. Otherwise, supplies a list of batch sizes, causing the op to
      pad batches up to one of those sizes. The entries must increase
      monotonically, and the final entry must equal max_batch_size.
    max_enqueued_batches: The maximum depth of the batch queue. Defaults to 100.

  Returns:
    The unbatched computation output Tensors.
  '''

import tensorflow as tf
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from typing import NamedTuple

class TrainSpec(NamedTuple('TrainSpec', [('input_fn', Incomplete), ('max_steps', Incomplete), ('hooks', Incomplete), ('saving_listeners', Incomplete)])):
    '''Configuration for the "train" part for the `train_and_evaluate` call.

  `TrainSpec` determines the input data for the training, as well as the
  duration. Optional hooks run at various stages of training.

  Usage:

  >>> train_spec = tf.estimator.TrainSpec(
  ...    input_fn=lambda: 1,
  ...    max_steps=100,
  ...    hooks=[_StopAtSecsHook(stop_after_secs=10)],
  ...    saving_listeners=[_NewCheckpointListenerForEvaluate(None, 20, None)])
  >>> train_spec.saving_listeners[0]._eval_throttle_secs
  20
  >>> train_spec.hooks[0]._stop_after_secs
  10
  >>> train_spec.max_steps
  100
  '''
    def __new__(cls, input_fn, max_steps: Incomplete | None = None, hooks: Incomplete | None = None, saving_listeners: Incomplete | None = None):
        """Creates a validated `TrainSpec` instance.

    Args:
      input_fn: A function that provides input data for training as minibatches.
        See [Premade Estimators](
        https://tensorflow.org/guide/premade_estimators#create_input_functions)
          for more information. The function should construct and return one of
        the following:
          * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
            tuple (features, labels) with same constraints as below.
          * A tuple (features, labels): Where features is a `Tensor` or a
            dictionary of string feature name to `Tensor` and labels is a
            `Tensor` or a dictionary of string label name to `Tensor`.
      max_steps: Int. Positive number of total steps for which to train model.
        If `None`, train forever. The training `input_fn` is not expected to
        generate `OutOfRangeError` or `StopIteration` exceptions. See the
        `train_and_evaluate` stop condition section for details.
      hooks: Iterable of `tf.train.SessionRunHook` objects to run on all workers
        (including chief) during training.
      saving_listeners: Iterable of `tf.estimator.CheckpointSaverListener`
        objects to run on chief during training.

    Returns:
      A validated `TrainSpec` object.

    Raises:
      ValueError: If any of the input arguments is invalid.
      TypeError: If any of the arguments is not of the expected type.
    """

class EvalSpec(NamedTuple('EvalSpec', [('input_fn', Incomplete), ('steps', Incomplete), ('name', Incomplete), ('hooks', Incomplete), ('exporters', Incomplete), ('start_delay_secs', Incomplete), ('throttle_secs', Incomplete)])):
    '''Configuration for the "eval" part for the `train_and_evaluate` call.

  `EvalSpec` combines details of evaluation of the trained model as well as its
  export. Evaluation consists of computing metrics to judge the performance of
  the trained model.  Export writes out the trained model on to external
  storage.
  '''
    def __new__(cls, input_fn, steps: int = 100, name: Incomplete | None = None, hooks: Incomplete | None = None, exporters: Incomplete | None = None, start_delay_secs: int = 120, throttle_secs: int = 600):
        """Creates a validated `EvalSpec` instance.

    Args:
      input_fn: A function that constructs the input data for evaluation. See
        [Premade Estimators](
        https://tensorflow.org/guide/premade_estimators#create_input_functions)
          for more information. The function should construct and return one of
        the following:
          * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
            tuple (features, labels) with same constraints as below.
          * A tuple (features, labels): Where features is a `Tensor` or a
            dictionary of string feature name to `Tensor` and labels is a
            `Tensor` or a dictionary of string label name to `Tensor`.
      steps: Int. Positive number of steps for which to evaluate model. If
        `None`, evaluates until `input_fn` raises an end-of-input exception. See
        `Estimator.evaluate` for details.
      name: String. Name of the evaluation if user needs to run multiple
        evaluations on different data sets. Metrics for different evaluations
        are saved in separate folders, and appear separately in tensorboard.
      hooks: Iterable of `tf.train.SessionRunHook` objects to run during
        evaluation.
      exporters: Iterable of `Exporter`s, or a single one, or `None`.
        `exporters` will be invoked after each evaluation.
      start_delay_secs: Int. Start evaluating after waiting for this many
        seconds.
      throttle_secs: Int. Do not re-evaluate unless the last evaluation was
        started at least this many seconds ago. Of course, evaluation does not
        occur if no new checkpoints are available, hence, this is the minimum.

    Returns:
      A validated `EvalSpec` object.

    Raises:
      ValueError: If any of the input arguments is invalid.
      TypeError: If any of the arguments is not of the expected type.
    """

def train_and_evaluate(estimator, train_spec, eval_spec):
    '''Train and evaluate the `estimator`.

  This utility function trains, evaluates, and (optionally) exports the model by
  using the given `estimator`. All training related specification is held in
  `train_spec`, including training `input_fn` and training max steps, etc. All
  evaluation and export related specification is held in `eval_spec`, including
  evaluation `input_fn`, steps, etc.

  This utility function provides consistent behavior for both local
  (non-distributed) and distributed configurations. The default distribution
  configuration is parameter server-based between-graph replication. For other
  types of distribution configurations such as all-reduce training, please use
  [DistributionStrategies](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/distribute).

  Overfitting: In order to avoid overfitting, it is recommended to set up the
  training `input_fn` to shuffle the training data properly.

  Stop condition: In order to support both distributed and non-distributed
  configuration reliably, the only supported stop condition for model
  training is `train_spec.max_steps`. If `train_spec.max_steps` is `None`, the
  model is trained forever. *Use with care* if model stop condition is
  different. For example, assume that the model is expected to be trained with
  one epoch of training data, and the training `input_fn` is configured to throw
  `OutOfRangeError` after going through one epoch, which stops the
  `Estimator.train`. For a three-training-worker distributed configuration, each
  training worker is likely to go through the whole epoch independently. So, the
  model will be trained with three epochs of training data instead of one epoch.

  Example of local (non-distributed) training:

  ```python
  # Set up feature columns.
  categorial_feature_a = categorial_column_with_hash_bucket(...)
  categorial_feature_a_emb = embedding_column(
      categorical_column=categorial_feature_a, ...)
  ...  # other feature columns

  estimator = DNNClassifier(
      feature_columns=[categorial_feature_a_emb, ...],
      hidden_units=[1024, 512, 256])

  # Or set up the model directory
  #   estimator = DNNClassifier(
  #       config=tf.estimator.RunConfig(
  #           model_dir=\'/my_model\', save_summary_steps=100),
  #       feature_columns=[categorial_feature_a_emb, ...],
  #       hidden_units=[1024, 512, 256])

  # Input pipeline for train and evaluate.
  def train_input_fn(): # returns x, y
    # please shuffle the data.
    pass
  def eval_input_fn(): # returns x, y
    pass

  train_spec = tf.estimator.TrainSpec(input_fn=train_input_fn, max_steps=1000)
  eval_spec = tf.estimator.EvalSpec(input_fn=eval_input_fn)

  tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)
  ```
  Note that in current implementation `estimator.evaluate` will be called
  multiple times. This means that evaluation graph (including eval_input_fn)
  will be re-created for each `evaluate` call. `estimator.train` will be called
  only once.

  Example of distributed training:

  Regarding the example of distributed training, the code above can be used
  without a change (Please do make sure that the `RunConfig.model_dir` for all
  workers is set to the same directory, i.e., a shared file system all workers
  can read and write). The only extra work to do is setting the environment
  variable `TF_CONFIG` properly for each worker correspondingly.

  Also see
  [Distributed TensorFlow](https://www.tensorflow.org/deploy/distributed).

  Setting environment variable depends on the platform. For example, on Linux,
  it can be done as follows (`$` is the shell prompt):

  ```
  $ TF_CONFIG=\'<replace_with_real_content>\' python train_model.py
  ```

  For the content in `TF_CONFIG`, assume that the training cluster spec looks
  like:

  ```
  cluster = {"chief": ["host0:2222"],
             "worker": ["host1:2222", "host2:2222", "host3:2222"],
             "ps": ["host4:2222", "host5:2222"]}
  ```

  Example of `TF_CONFIG` for chief training worker (must have one and only one):

  ```
  # This should be a JSON string, which is set as environment variable. Usually
  # the cluster manager handles that.
  TF_CONFIG=\'{
      "cluster": {
          "chief": ["host0:2222"],
          "worker": ["host1:2222", "host2:2222", "host3:2222"],
          "ps": ["host4:2222", "host5:2222"]
      },
      "task": {"type": "chief", "index": 0}
  }\'
  ```
  Note that the chief worker also does the model training job, similar to other
  non-chief training workers (see next paragraph). In addition to the model
  training, it manages some extra work, e.g., checkpoint saving and restoring,
  writing summaries, etc.

  Example of `TF_CONFIG` for non-chief training worker (optional, could be
  multiple):

  ```
  # This should be a JSON string, which is set as environment variable. Usually
  # the cluster manager handles that.
  TF_CONFIG=\'{
      "cluster": {
          "chief": ["host0:2222"],
          "worker": ["host1:2222", "host2:2222", "host3:2222"],
          "ps": ["host4:2222", "host5:2222"]
      },
      "task": {"type": "worker", "index": 0}
  }\'
  ```
  where the `task.index` should be set as 0, 1, 2, in this example, respectively
  for non-chief training workers.

  Example of `TF_CONFIG` for parameter server, aka ps (could be multiple):

  ```
  # This should be a JSON string, which is set as environment variable. Usually
  # the cluster manager handles that.
  TF_CONFIG=\'{
      "cluster": {
          "chief": ["host0:2222"],
          "worker": ["host1:2222", "host2:2222", "host3:2222"],
          "ps": ["host4:2222", "host5:2222"]
      },
      "task": {"type": "ps", "index": 0}
  }\'
  ```
  where the `task.index` should be set as 0 and 1, in this example, respectively
  for parameter servers.

  Example of `TF_CONFIG` for evaluator task. Evaluator is a special task that is
  not part of the training cluster. There could be only one. It is used for
  model evaluation.

  ```
  # This should be a JSON string, which is set as environment variable. Usually
  # the cluster manager handles that.
  TF_CONFIG=\'{
      "cluster": {
          "chief": ["host0:2222"],
          "worker": ["host1:2222", "host2:2222", "host3:2222"],
          "ps": ["host4:2222", "host5:2222"]
      },
      "task": {"type": "evaluator", "index": 0}
  }\'
  ```

  When `distribute` or `experimental_distribute.train_distribute` and
  `experimental_distribute.remote_cluster` is set, this method will start a
  client running on the current host which connects to the `remote_cluster` for
  training and evaluation.

  Args:
    estimator: An `Estimator` instance to train and evaluate.
    train_spec: A `TrainSpec` instance to specify the training specification.
    eval_spec: A `EvalSpec` instance to specify the evaluation and export
      specification.

  Returns:
    A tuple of the result of the `evaluate` call to the `Estimator` and the
    export results using the specified `Exporter`s.
    Currently, the return value is undefined for distributed training mode.

  Raises:
    ValueError: if environment variable `TF_CONFIG` is incorrectly set.
  '''

class _StopAtSecsHook(tf.compat.v1.train.SessionRunHook):
    """Stops given secs after begin is called."""
    def __init__(self, stop_after_secs) -> None: ...
    def begin(self) -> None: ...
    def after_run(self, run_context, run_values) -> None: ...

class _NewCheckpointListenerForEvaluate(tf.compat.v1.train.CheckpointSaverListener):
    """A saver listener to run evaluate with every checkpoint."""
    def __init__(self, evaluator, eval_throttle_secs, continuous_eval_listener) -> None: ...
    def begin(self) -> None: ...
    def after_save(self, session, global_step_value): ...
    def end(self, session, global_step_value) -> None: ...

class _TrainingExecutor:
    """The executor to run `Estimator` training and evaluation.

  This implementation supports both distributed and non-distributed (aka local)
  training and evaluation based on the setting in `tf.estimator.RunConfig`.
  """
    def __init__(self, estimator, train_spec, eval_spec, train_hooks: Incomplete | None = None, continuous_eval_listener: Incomplete | None = None) -> None: ...
    @property
    def estimator(self): ...
    def run(self):
        """Executes the run_foo for task type `foo`.

    `_TrainingExecutor` predefines the procedure for task type 'chief',
    'worker', 'ps', and 'evaluator'. For task type `foo`, the corresponding
    procedure is `run_foo'. This `run` method invoke the procedure base on the
    `RunConfig.task_type`.

    Returns:
      A tuple of the result of the `evaluate` call to the `Estimator` and the
      export results using the specified `ExportStrategy`.
      Currently undefined for distributed training mode.

    Raises:
      ValueError: if the estimator.config is mis-configured.
    """
    def run_chief(self):
        """Runs task chief."""
    def run_worker(self):
        """Runs task (training) worker."""
    def run_master(self) -> None:
        """Runs task master."""
    def run_evaluator(self):
        """Runs task evaluator."""
    def run_ps(self) -> None:
        """Runs task parameter server (in training cluster spec)."""
    def run_local(self):
        """Runs training and evaluation locally (non-distributed)."""
    class _Evaluator:
        """A helper class to call `Estimator.evaluate` and export model."""
        def __init__(self, estimator, eval_spec, max_training_steps) -> None: ...
        @property
        def is_final_export_triggered(self): ...
        def evaluate_and_export(self):
            """Evaluate and (maybe) export the current model.

      Returns:
        A tuple of `EvalResult` instance and the export results.

      Raises:
        RuntimeError: for any unexpected internal error.
        TypeError: if evaluation result has wrong type.
      """

class _EvalStatus:
    """The status of an evaluation event.

  For local training and evaluation, the status can only be `EVALUATED` as
  `Estimator.train` always generates a new checkpoint.

  For distributed training and evaluation, a separated evaluator keeps looking
  for new checkpoint. So, multiple situations might occur:

  - EVALUATED: A new checkpoint is found since last evaluation.
      `Estimator.evaluate` will be invoked.
  - MISSING_CHECKPOINT: No checkpoint can be found. Typically, this means
      the trainer has not yet produced any checkpoint.
  - NO_NEW_CHECKPOINT: No new checkpoint can be found since last evaluation.
      Typically, this means the trainer has not yet produced any new checkpoint.
  """
    EVALUATED: str
    MISSING_CHECKPOINT: str
    NO_NEW_CHECKPOINT: str

class _EvalResult(NamedTuple('EvalResult', [('status', Incomplete), ('metrics', Incomplete), ('checkpoint_path', Incomplete)])):
    """_EvalResult holds the result of an evaluation event."""
    def __new__(cls, status, metrics: Incomplete | None = None, checkpoint_path: Incomplete | None = None):
        """Creates a validated `_EvalResult`.

    Args:
      status: See `_EvalStatus`.
      metrics: The evaluation results returned by `Estimator.evaluate`. Only set
        if status is `EVALUATED`.
      checkpoint_path: The corresponding checkpoint path for the `metrics`. Only
        set if status is `EVALUATED`.

    Returns:
      A validated `_EvalResult` object.

    Raises:
      ValueError: If validation fails.
      TypeError: If any of the arguments is not the expected type.
    """

class _ContinuousEvalListener:
    """Interface for listeners that take action before or after evaluation."""
    def before_eval(self):
        """Called before evaluation.

    Returns:
      `False` if you want to skip the current evaluation and early stop the
      continuous evaluation; `True` otherwise.
    """
    def after_eval(self, eval_result):
        """Called after the evaluation is executed.

    Args:
      eval_result: An `_EvalResult` instance.

    Returns:
      False if you want to early stop continuous evaluation; `True` otherwise.
    """

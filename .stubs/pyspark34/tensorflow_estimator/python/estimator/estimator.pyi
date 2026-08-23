from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow_estimator.python.estimator import run_config as run_config
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.export import export_lib as export_lib
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys
from typing import NamedTuple

class Estimator:
    '''Estimator class to train and evaluate TensorFlow models.

  The `Estimator` object wraps a model which is specified by a `model_fn`,
  which, given inputs and a number of other parameters, returns the ops
  necessary to perform training, evaluation, or predictions.

  All outputs (checkpoints, event files, etc.) are written to `model_dir`, or a
  subdirectory thereof. If `model_dir` is not set, a temporary directory is
  used.

  The `config` argument can be passed `tf.estimator.RunConfig` object containing
  information about the execution environment. It is passed on to the
  `model_fn`, if the `model_fn` has a parameter named "config" (and input
  functions in the same manner). If the `config` parameter is not passed, it is
  instantiated by the `Estimator`. Not passing config means that defaults useful
  for local execution are used. `Estimator` makes config available to the model
  (for instance, to allow specialization based on the number of workers
  available), and also uses some of its fields to control internals, especially
  regarding checkpointing.

  The `params` argument contains hyperparameters. It is passed to the
  `model_fn`, if the `model_fn` has a parameter named "params", and to the input
  functions in the same manner. `Estimator` only passes params along, it does
  not inspect it. The structure of `params` is therefore entirely up to the
  developer.

  None of `Estimator`\'s methods can be overridden in subclasses (its
  constructor enforces this). Subclasses should use `model_fn` to configure
  the base class, and may add methods implementing specialized functionality.

  See [estimators](https://tensorflow.org/guide/estimator) for more
  information.

  To warm-start an `Estimator`:

  ```python
  estimator = tf.estimator.DNNClassifier(
      feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
      hidden_units=[1024, 512, 256],
      warm_start_from="/path/to/checkpoint/dir")
  ```

  For more details on warm-start configuration, see
  `tf.estimator.WarmStartSettings`.

  @compatibility(eager)
  Calling methods of `Estimator` will work while eager execution is enabled.
  However, the `model_fn` and `input_fn` is not executed eagerly, `Estimator`
  will switch to graph mode before calling all user-provided functions (incl.
  hooks), so their code has to be compatible with graph mode execution. Note
  that `input_fn` code using `tf.data` generally works in both graph and eager
  modes.
  @end_compatibility
  '''
    def __init__(self, model_fn, model_dir: Incomplete | None = None, config: Incomplete | None = None, params: Incomplete | None = None, warm_start_from: Incomplete | None = None) -> None:
        """Constructs an `Estimator` instance.



    Args:
      model_fn: Model function. Follows the signature:
        * `features` -- This is the first item returned from the `input_fn`
        passed to `train`, `evaluate`, and `predict`. This should be a
        single `tf.Tensor` or `dict` of same.
        * `labels` -- This is the second item returned from the `input_fn`
        passed to `train`, `evaluate`, and `predict`. This should be a
        single `tf.Tensor` or `dict` of same (for multi-head models). If
        mode is `tf.estimator.ModeKeys.PREDICT`, `labels=None` will be
        passed. If the `model_fn`'s signature does not accept `mode`, the
        `model_fn` must still be able to handle `labels=None`.
        * `mode` -- Optional. Specifies if this is training, evaluation or
        prediction. See `tf.estimator.ModeKeys`.
        `params` -- Optional `dict` of hyperparameters.  Will receive what is
        passed to Estimator in `params` parameter. This allows to configure
        Estimators from hyper parameter tuning.
        * `config` -- Optional `estimator.RunConfig` object. Will receive what
        is passed to Estimator as its `config` parameter, or a default
        value. Allows setting up things in your `model_fn` based on
        configuration such as `num_ps_replicas`, or `model_dir`.
        * Returns -- `tf.estimator.EstimatorSpec`
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into an estimator to
        continue training a previously saved model. If `PathLike` object, the
        path will be resolved. If `None`, the model_dir in `config` will be used
        if set. If both are set, they must be same. If both are `None`, a
        temporary directory will be used.
      config: `estimator.RunConfig` configuration object.
      params: `dict` of hyper parameters that will be passed into `model_fn`.
        Keys are names of parameters, values are basic python types.
      warm_start_from: Optional string filepath to a checkpoint or SavedModel to
        warm-start from, or a `tf.estimator.WarmStartSettings` object to fully
        configure warm-starting.  If None, only TRAINABLE variables are
        warm-started.  If the string filepath is provided instead of a
        `tf.estimator.WarmStartSettings`, then all variables are warm-started,
        and it is assumed that vocabularies and `tf.Tensor` names are unchanged.

    Raises:
      ValueError: parameters of `model_fn` don't match `params`.
      ValueError: if this is called via a subclass and if that class overrides
        a member of `Estimator`.
    """
    @property
    def model_dir(self): ...
    @property
    def config(self): ...
    @property
    def params(self): ...
    @property
    def model_fn(self):
        """Returns the `model_fn` which is bound to `self.params`.

    Returns:
      The `model_fn` with following signature:
        `def model_fn(features, labels, mode, config)`
    """
    def get_variable_value(self, name):
        """Returns value of the variable given by name.

    Args:
      name: string or a list of string, name of the tensor.

    Returns:
      Numpy array - value of the tensor.

    Raises:
      ValueError: If the `Estimator` has not produced a checkpoint yet.
    """
    def get_variable_names(self):
        """Returns list of all variable names in this model.

    Returns:
      List of names.

    Raises:
      ValueError: If the `Estimator` has not produced a checkpoint yet.
    """
    def latest_checkpoint(self):
        """Finds the filename of the latest saved checkpoint file in `model_dir`.

    Returns:
      The full path to the latest checkpoint or `None` if no checkpoint was
      found.
    """
    def train(self, input_fn, hooks: Incomplete | None = None, steps: Incomplete | None = None, max_steps: Incomplete | None = None, saving_listeners: Incomplete | None = None):
        """Trains a model given training data `input_fn`.

    Args:
      input_fn: A function that provides input data for training as minibatches.
        See [Premade Estimators](
        https://tensorflow.org/guide/premade_estimators#create_input_functions)
          for more information. The function should construct and return one of
        the following:
          * A `tf.data.Dataset` object: Outputs of `Dataset` object must be a
            tuple `(features, labels)` with same constraints as below.
          * A tuple `(features, labels)`: Where `features` is a `tf.Tensor` or a
            dictionary of string feature name to `Tensor` and `labels` is a
            `Tensor` or a dictionary of string label name to `Tensor`. Both
            `features` and `labels` are consumed by `model_fn`. They should
            satisfy the expectation of `model_fn` from inputs.
      hooks: List of `tf.train.SessionRunHook` subclass instances. Used for
        callbacks inside the training loop.
      steps: Number of steps for which to train the model. If `None`, train
        forever or train until `input_fn` generates the `tf.errors.OutOfRange`
        error or `StopIteration` exception. `steps` works incrementally. If you
        call two times `train(steps=10)` then training occurs in total 20 steps.
        If `OutOfRange` or `StopIteration` occurs in the middle, training stops
        before 20 steps. If you don't want to have incremental behavior please
        set `max_steps` instead. If set, `max_steps` must be `None`.
      max_steps: Number of total steps for which to train model. If `None`,
        train forever or train until `input_fn` generates the
        `tf.errors.OutOfRange` error or `StopIteration` exception. If set,
        `steps` must be `None`. If `OutOfRange` or `StopIteration` occurs in the
        middle, training stops before `max_steps` steps. Two calls to
        `train(steps=100)` means 200 training iterations. On the other hand, two
        calls to `train(max_steps=100)` means that the second call will not do
        any iteration since first call did all 100 steps.
      saving_listeners: list of `CheckpointSaverListener` objects. Used for
        callbacks that run immediately before or after checkpoint savings.

    Returns:
      `self`, for chaining.

    Raises:
      ValueError: If both `steps` and `max_steps` are not `None`.
      ValueError: If either `steps` or `max_steps <= 0`.
    """
    def eval_dir(self, name: Incomplete | None = None):
        """Shows the directory name where evaluation metrics are dumped.

    Args:
      name: Name of the evaluation if user needs to run multiple evaluations on
        different data sets, such as on training data vs test data. Metrics for
        different evaluations are saved in separate folders, and appear
        separately in tensorboard.

    Returns:
      A string which is the path of directory contains evaluation metrics.
    """
    def evaluate(self, input_fn, steps: Incomplete | None = None, hooks: Incomplete | None = None, checkpoint_path: Incomplete | None = None, name: Incomplete | None = None):
        """Evaluates the model given evaluation data `input_fn`.

    For each step, calls `input_fn`, which returns one batch of data.
    Evaluates until:
    - `steps` batches are processed, or
    - `input_fn` raises an end-of-input exception (`tf.errors.OutOfRangeError`
    or `StopIteration`).

    Args:
      input_fn: A function that constructs the input data for evaluation. See
        [Premade Estimators](
        https://tensorflow.org/guide/premade_estimators#create_input_functions)
        for more information. The function should construct and return one of
        the following:
        * A `tf.data.Dataset` object: Outputs of `Dataset` object must be a
          tuple `(features, labels)` with same constraints as below.
        * A tuple `(features, labels)`: Where `features` is a `tf.Tensor` or a
          dictionary of string feature name to `Tensor` and `labels` is a
          `Tensor` or a dictionary of string label name to `Tensor`. Both
          `features` and `labels` are consumed by `model_fn`. They should
          satisfy the expectation of `model_fn` from inputs.
      steps: Number of steps for which to evaluate model. If `None`, evaluates
        until `input_fn` raises an end-of-input exception.
      hooks: List of `tf.train.SessionRunHook` subclass instances. Used for
        callbacks inside the evaluation call.
      checkpoint_path: Path of a specific checkpoint to evaluate. If `None`, the
        latest checkpoint in `model_dir` is used.  If there are no checkpoints
        in `model_dir`, evaluation is run with newly initialized `Variables`
        instead of ones restored from checkpoint.
      name: Name of the evaluation if user needs to run multiple evaluations on
        different data sets, such as on training data vs test data. Metrics for
        different evaluations are saved in separate folders, and appear
        separately in tensorboard.

    Returns:
      A dict containing the evaluation metrics specified in `model_fn` keyed by
      name, as well as an entry `global_step` which contains the value of the
      global step for which this evaluation was performed. For canned
      estimators, the dict contains the `loss` (mean loss per mini-batch) and
      the `average_loss` (mean loss per sample). Canned classifiers also return
      the `accuracy`. Canned regressors also return the `label/mean` and the
      `prediction/mean`.

    Raises:
      ValueError: If `steps <= 0`.
    """
    def predict(self, input_fn, predict_keys: Incomplete | None = None, hooks: Incomplete | None = None, checkpoint_path: Incomplete | None = None, yield_single_examples: bool = True) -> Generator[Incomplete, None, None]:
        """Yields predictions for given features.

    Please note that interleaving two predict outputs does not work. See:
    [issue/20506](
    https://github.com/tensorflow/tensorflow/issues/20506#issuecomment-422208517)

    Args:
      input_fn: A function that constructs the features. Prediction continues
        until `input_fn` raises an end-of-input exception
        (`tf.errors.OutOfRangeError` or `StopIteration`). See [Premade
        Estimators](
        https://tensorflow.org/guide/premade_estimators#create_input_functions)
        for more information. The function should construct and return one of
        the following:
        * `tf.data.Dataset` object -- Outputs of `Dataset` object must have
          same constraints as below.
        * features -- A `tf.Tensor` or a dictionary of string feature name to
          `Tensor`. features are consumed by `model_fn`. They should satisfy
          the expectation of `model_fn` from inputs.
        * A tuple, in which case
          the first item is extracted as features.
      predict_keys: list of `str`, name of the keys to predict. It is used if
        the `tf.estimator.EstimatorSpec.predictions` is a `dict`. If
        `predict_keys` is used then rest of the predictions will be filtered
        from the dictionary. If `None`, returns all.
      hooks: List of `tf.train.SessionRunHook` subclass instances. Used for
        callbacks inside the prediction call.
      checkpoint_path: Path of a specific checkpoint to predict. If `None`, the
        latest checkpoint in `model_dir` is used.  If there are no checkpoints
        in `model_dir`, prediction is run with newly initialized `Variables`
        instead of ones restored from checkpoint.
      yield_single_examples: If `False`, yields the whole batch as returned by
        the `model_fn` instead of decomposing the batch into individual
        elements. This is useful if `model_fn` returns some tensors whose first
        dimension is not equal to the batch size.

    Yields:
      Evaluated values of `predictions` tensors.

    Raises:
      ValueError: If batch length of predictions is not the same and
        `yield_single_examples` is `True`.
      ValueError: If there is a conflict between `predict_keys` and
        `predictions`. For example if `predict_keys` is not `None` but
        `tf.estimator.EstimatorSpec.predictions` is not a `dict`.
    """
    def export_saved_model(self, export_dir_base, serving_input_receiver_fn, assets_extra: Incomplete | None = None, as_text: bool = False, checkpoint_path: Incomplete | None = None, experimental_mode=...):
        """Exports inference graph as a `SavedModel` into the given dir.

    For a detailed guide on SavedModel, see
    [Using the SavedModel format]
    (https://tensorflow.org/guide/saved_model#savedmodels_from_estimators).

    This method builds a new graph by first calling the
    `serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
    this `Estimator`'s `model_fn` to generate the model graph based on those
    features. It restores the given checkpoint (or, lacking that, the most
    recent checkpoint) into this graph in a fresh session.  Finally it creates
    a timestamped export directory below the given `export_dir_base`, and writes
    a `SavedModel` into it containing a single `tf.MetaGraphDef` saved from this
    session.

    The exported `MetaGraphDef` will provide one `SignatureDef` for each
    element of the `export_outputs` dict returned from the `model_fn`, named
    using the same keys.  One of these keys is always
    `tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`,
    indicating which signature will be served when a serving request does not
    specify one. For each signature, the outputs are provided by the
    corresponding `tf.estimator.export.ExportOutput`s, and the inputs are always
    the input receivers provided by the `serving_input_receiver_fn`.

    Extra assets may be written into the `SavedModel` via the `assets_extra`
    argument.  This should be a dict, where each key gives a destination path
    (including the filename) relative to the assets.extra directory.  The
    corresponding value gives the full path of the source file to be copied.
    For example, the simple case of copying a single file without renaming it
    is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

    The experimental_mode parameter can be used to export a single
    train/eval/predict graph as a `SavedModel`.
    See `experimental_export_all_saved_models` for full docs.

    Args:
      export_dir_base: A string containing a directory in which to create
        timestamped subdirectories containing exported `SavedModel`s.
      serving_input_receiver_fn: A function that takes no argument and returns a
        `tf.estimator.export.ServingInputReceiver` or
        `tf.estimator.export.TensorServingInputReceiver`.
      assets_extra: A dict specifying how to populate the assets.extra directory
        within the exported `SavedModel`, or `None` if no extra assets are
        needed.
      as_text: whether to write the `SavedModel` proto in text format.
      checkpoint_path: The checkpoint path to export.  If `None` (the default),
        the most recent checkpoint found within the model directory is chosen.
      experimental_mode: `tf.estimator.ModeKeys` value indicating with mode will
        be exported. Note that this feature is experimental.

    Returns:
      The path to the exported directory as a bytes object.

    Raises:
      ValueError: if no `serving_input_receiver_fn` is provided, no
      `export_outputs` are provided, or no checkpoint can be found.
    """
    def experimental_export_all_saved_models(self, export_dir_base, input_receiver_fn_map, assets_extra: Incomplete | None = None, as_text: bool = False, checkpoint_path: Incomplete | None = None):
        """Exports a `SavedModel` with `tf.MetaGraphDefs` for each requested mode.

    For each mode passed in via the `input_receiver_fn_map`,
    this method builds a new graph by calling the `input_receiver_fn` to obtain
    feature and label `Tensor`s. Next, this method calls the `Estimator`'s
    `model_fn` in the passed mode to generate the model graph based on
    those features and labels, and restores the given checkpoint
    (or, lacking that, the most recent checkpoint) into the graph.
    Only one of the modes is used for saving variables to the `SavedModel`
    (order of preference: `tf.estimator.ModeKeys.TRAIN`,
    `tf.estimator.ModeKeys.EVAL`, then
    `tf.estimator.ModeKeys.PREDICT`), such that up to three
    `tf.MetaGraphDefs` are saved with a single set of variables in a single
    `SavedModel` directory.

    For the variables and `tf.MetaGraphDefs`, a timestamped export directory
    below `export_dir_base`, and writes a `SavedModel` into it containing the
    `tf.MetaGraphDef` for the given mode and its associated signatures.

    For prediction, the exported `MetaGraphDef` will provide one `SignatureDef`
    for each element of the `export_outputs` dict returned from the `model_fn`,
    named using the same keys.  One of these keys is always
    `tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`,
    indicating which signature will be served when a serving request does not
    specify one. For each signature, the outputs are provided by the
    corresponding `tf.estimator.export.ExportOutput`s, and the inputs are always
    the input receivers provided by the `serving_input_receiver_fn`.

    For training and evaluation, the `train_op` is stored in an extra
    collection, and loss, metrics, and predictions are included in a
    `SignatureDef` for the mode in question.

    Extra assets may be written into the `SavedModel` via the `assets_extra`
    argument.  This should be a dict, where each key gives a destination path
    (including the filename) relative to the assets.extra directory.  The
    corresponding value gives the full path of the source file to be copied.
    For example, the simple case of copying a single file without renaming it
    is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

    Args:
      export_dir_base: A string containing a directory in which to create
        timestamped subdirectories containing exported `SavedModel`s.
      input_receiver_fn_map: dict of `tf.estimator.ModeKeys` to
        `input_receiver_fn` mappings, where the `input_receiver_fn` is a
        function that takes no arguments and returns the appropriate subclass of
        `InputReceiver`.
      assets_extra: A dict specifying how to populate the assets.extra directory
        within the exported `SavedModel`, or `None` if no extra assets are
        needed.
      as_text: whether to write the `SavedModel` proto in text format.
      checkpoint_path: The checkpoint path to export.  If `None` (the default),
        the most recent checkpoint found within the model directory is chosen.

    Returns:
      The path to the exported directory as a bytes object.

    Raises:
      ValueError: if any `input_receiver_fn` is `None`, no `export_outputs`
        are provided, or no checkpoint can be found.
    """
    def export_savedmodel(self, export_dir_base, serving_input_receiver_fn, assets_extra: Incomplete | None = None, as_text: bool = False, checkpoint_path: Incomplete | None = None, strip_default_attrs: bool = False):
        """Exports inference graph as a `SavedModel` into the given dir.

    For a detailed guide, see
    [SavedModel from
    Estimators.](https://www.tensorflow.org/guide/estimator#savedmodels_from_estimators).

    This method builds a new graph by first calling the
    `serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
    this `Estimator`'s `model_fn` to generate the model graph based on those
    features. It restores the given checkpoint (or, lacking that, the most
    recent checkpoint) into this graph in a fresh session.  Finally it creates
    a timestamped export directory below the given `export_dir_base`, and writes
    a `SavedModel` into it containing a single `tf.MetaGraphDef` saved from this
    session.

    The exported `MetaGraphDef` will provide one `SignatureDef` for each
    element of the `export_outputs` dict returned from the `model_fn`, named
    using the same keys.  One of these keys is always
    `tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`,
    indicating which signature will be served when a serving request does not
    specify one. For each signature, the outputs are provided by the
    corresponding `tf.estimator.export.ExportOutput`s, and the inputs are always
    the input receivers provided by the `serving_input_receiver_fn`.

    Extra assets may be written into the `SavedModel` via the `assets_extra`
    argument.  This should be a dict, where each key gives a destination path
    (including the filename) relative to the assets.extra directory.  The
    corresponding value gives the full path of the source file to be copied.
    For example, the simple case of copying a single file without renaming it
    is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

    Args:
      export_dir_base: A string containing a directory in which to create
        timestamped subdirectories containing exported `SavedModel`s.
      serving_input_receiver_fn: A function that takes no argument and returns a
        `tf.estimator.export.ServingInputReceiver` or
        `tf.estimator.export.TensorServingInputReceiver`.
      assets_extra: A dict specifying how to populate the assets.extra directory
        within the exported `SavedModel`, or `None` if no extra assets are
        needed.
      as_text: whether to write the `SavedModel` proto in text format.
      checkpoint_path: The checkpoint path to export.  If `None` (the default),
        the most recent checkpoint found within the model directory is chosen.
      strip_default_attrs: Boolean. If `True`, default-valued attributes will be
        removed from the `NodeDef`s. For a detailed guide, see [Stripping
        Default-Valued Attributes](
        https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).

    Returns:
      The path to the exported directory as a bytes object.

    Raises:
      ValueError: if no `serving_input_receiver_fn` is provided, no
      `export_outputs` are provided, or no checkpoint can be found.
    """

class EstimatorV2(Estimator):
    __doc__: Incomplete
    export_savedmodel: Incomplete

def maybe_overwrite_model_dir_and_session_config(config, model_dir):
    """Overwrite estimator config by `model_dir` and `session_config` if needed.

  Args:
    config: Original estimator config.
    model_dir: Estimator model checkpoint directory.

  Returns:
    Overwritten estimator config.

  Raises:
    ValueError: Model directory inconsistent between `model_dir` and `config`.
  """
def create_per_replica_ready_for_local_init_op(scaffold):
    """Create a `tf.train.Scaffold.ready_for_local_init_op` inside a replica."""

VocabInfo: Incomplete

class WarmStartSettings(NamedTuple('WarmStartSettings', [('ckpt_to_initialize_from', Incomplete), ('vars_to_warm_start', Incomplete), ('var_name_to_vocab_info', Incomplete), ('var_name_to_prev_var_name', Incomplete)])):
    '''Settings for warm-starting in `tf.estimator.Estimators`.

  Example Use with canned `tf.estimator.DNNEstimator`:

  ```
  emb_vocab_file = tf.feature_column.embedding_column(
      tf.feature_column.categorical_column_with_vocabulary_file(
          "sc_vocab_file", "new_vocab.txt", vocab_size=100),
      dimension=8)
  emb_vocab_list = tf.feature_column.embedding_column(
      tf.feature_column.categorical_column_with_vocabulary_list(
          "sc_vocab_list", vocabulary_list=["a", "b"]),
      dimension=8)
  estimator = tf.estimator.DNNClassifier(
    hidden_units=[128, 64], feature_columns=[emb_vocab_file, emb_vocab_list],
    warm_start_from=ws)
  ```

  where `ws` could be defined as:

  Warm-start all weights in the model (input layer and hidden weights).
  Either the directory or a specific checkpoint can be provided (in the case
  of the former, the latest checkpoint will be used):

  ```
  ws = WarmStartSettings(ckpt_to_initialize_from="/tmp")
  ws = WarmStartSettings(ckpt_to_initialize_from="/tmp/model-1000")
  ```

  Warm-start only the embeddings (input layer):

  ```
  ws = WarmStartSettings(ckpt_to_initialize_from="/tmp",
                         vars_to_warm_start=".*input_layer.*")
  ```

  Warm-start all weights but the embedding parameters corresponding to
  `sc_vocab_file` have a different vocab from the one used in the current
  model:

  ```
  vocab_info = tf.estimator.VocabInfo(
      new_vocab=sc_vocab_file.vocabulary_file,
      new_vocab_size=sc_vocab_file.vocabulary_size,
      num_oov_buckets=sc_vocab_file.num_oov_buckets,
      old_vocab="old_vocab.txt"
  )
  ws = WarmStartSettings(
      ckpt_to_initialize_from="/tmp",
      var_name_to_vocab_info={
          "input_layer/sc_vocab_file_embedding/embedding_weights": vocab_info
      })
  ```

  Warm-start only `sc_vocab_file` embeddings (and no other variables), which
  have a different vocab from the one used in the current model:

  ```
  vocab_info = tf.estimator.VocabInfo(
      new_vocab=sc_vocab_file.vocabulary_file,
      new_vocab_size=sc_vocab_file.vocabulary_size,
      num_oov_buckets=sc_vocab_file.num_oov_buckets,
      old_vocab="old_vocab.txt"
  )
  ws = WarmStartSettings(
      ckpt_to_initialize_from="/tmp",
      vars_to_warm_start=None,
      var_name_to_vocab_info={
          "input_layer/sc_vocab_file_embedding/embedding_weights": vocab_info
      })
  ```

  Warm-start all weights but the parameters corresponding to `sc_vocab_file`
  have a different vocab from the one used in current checkpoint, and only
  100 of those entries were used:

  ```
  vocab_info = tf.estimator.VocabInfo(
      new_vocab=sc_vocab_file.vocabulary_file,
      new_vocab_size=sc_vocab_file.vocabulary_size,
      num_oov_buckets=sc_vocab_file.num_oov_buckets,
      old_vocab="old_vocab.txt",
      old_vocab_size=100
  )
  ws = WarmStartSettings(
      ckpt_to_initialize_from="/tmp",
      var_name_to_vocab_info={
          "input_layer/sc_vocab_file_embedding/embedding_weights": vocab_info
      })
  ```

  Warm-start all weights but the parameters corresponding to `sc_vocab_file`
  have a different vocab from the one used in current checkpoint and the
  parameters corresponding to `sc_vocab_list` have a different name from the
  current checkpoint:

  ```
  vocab_info = tf.estimator.VocabInfo(
      new_vocab=sc_vocab_file.vocabulary_file,
      new_vocab_size=sc_vocab_file.vocabulary_size,
      num_oov_buckets=sc_vocab_file.num_oov_buckets,
      old_vocab="old_vocab.txt",
      old_vocab_size=100
  )
  ws = WarmStartSettings(
      ckpt_to_initialize_from="/tmp",
      var_name_to_vocab_info={
          "input_layer/sc_vocab_file_embedding/embedding_weights": vocab_info
      },
      var_name_to_prev_var_name={
          "input_layer/sc_vocab_list_embedding/embedding_weights":
              "old_tensor_name"
      })
  ```

  Warm-start all TRAINABLE variables:

  ```
  ws = WarmStartSettings(ckpt_to_initialize_from="/tmp",
                         vars_to_warm_start=".*")
  ```

  Warm-start all variables (including non-TRAINABLE):

  ```
  ws = WarmStartSettings(ckpt_to_initialize_from="/tmp",
                         vars_to_warm_start=[".*"])
  ```

  Warm-start non-TRAINABLE variables "v1", "v1/Momentum", and "v2" but not
  "v2/momentum":

  ```
  ws = WarmStartSettings(ckpt_to_initialize_from="/tmp",
                         vars_to_warm_start=["v1", "v2[^/]"])
  ```

  Attributes:
    ckpt_to_initialize_from: [Required] A string specifying the directory with
      checkpoint file(s) or path to checkpoint from which to warm-start the
      model parameters.
    vars_to_warm_start: [Optional] One of the following:

      * A regular expression (string) that captures which variables to
        warm-start (see tf.compat.v1.get_collection).  This expression will only
        consider variables in the TRAINABLE_VARIABLES collection -- if you need
        to warm-start non_TRAINABLE vars (such as optimizer accumulators or
        batch norm statistics), please use the below option.
      * A list of strings, each a regex scope provided to
        tf.compat.v1.get_collection with GLOBAL_VARIABLES (please see
        tf.compat.v1.get_collection).  For backwards compatibility reasons, this
        is separate from the single-string argument type.
      * A list of Variables to warm-start.  If you do not have access to the
        `Variable` objects at the call site, please use the above option.
      * `None`, in which case only TRAINABLE variables specified in
        `var_name_to_vocab_info` will be warm-started.

      Defaults to `\'.*\'`, which warm-starts all variables in the
      TRAINABLE_VARIABLES collection. Note that this excludes variables such as
      accumulators and moving statistics from batch norm.
    var_name_to_vocab_info: [Optional] Dict of variable names (strings) to
      `tf.estimator.VocabInfo`. The variable names should be "full" variables,
      not the names of the partitions.  If not explicitly provided, the variable
      is assumed to have no (changes to) vocabulary.
    var_name_to_prev_var_name: [Optional] Dict of variable names (strings) to
      name of the previously-trained variable in `ckpt_to_initialize_from`. If
      not explicitly provided, the name of the variable is assumed to be same
      between previous checkpoint and current model.  Note that this has no
      effect on the set of variables that is warm-started, and only controls
      name mapping (use `vars_to_warm_start` for controlling what variables to
      warm-start).
  '''
    def __new__(cls, ckpt_to_initialize_from, vars_to_warm_start: str = '.*', var_name_to_vocab_info: Incomplete | None = None, var_name_to_prev_var_name: Incomplete | None = None): ...

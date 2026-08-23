from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, errors as errors
from tensorflow.python.keras import callbacks as callbacks
from tensorflow.python.ops import array_ops as array_ops, state_ops as state_ops, summary_ops_v2 as summary_ops_v2, variables as variables
from tensorflow.python.training import saver as saver
from tensorflow.python.util.tf_export import keras_export as keras_export

class TensorBoard(callbacks.TensorBoard):
    """Enable visualizations for TensorBoard.

  TensorBoard is a visualization tool provided with TensorFlow.

  This callback logs events for TensorBoard, including:
  * Metrics summary plots
  * Training graph visualization
  * Activation histograms
  * Sampled profiling

  If you have installed TensorFlow with pip, you should be able
  to launch TensorBoard from the command line:

  ```sh
  tensorboard --logdir=path_to_your_logs
  ```

  You can find more information about TensorBoard
  [here](https://www.tensorflow.org/get_started/summaries_and_tensorboard).

  Args:
      log_dir: the path of the directory where to save the log files to be
        parsed by TensorBoard.
      histogram_freq: frequency (in epochs) at which to compute activation and
        weight histograms for the layers of the model. If set to 0, histograms
        won't be computed. Validation data (or split) must be specified for
        histogram visualizations.
      write_graph: whether to visualize the graph in TensorBoard. The log file
        can become quite large when write_graph is set to True.
      write_grads: whether to visualize gradient histograms in TensorBoard.
        `histogram_freq` must be greater than 0.
      batch_size: size of batch of inputs to feed to the network for histograms
        computation.
      write_images: whether to write model weights to visualize as image in
        TensorBoard.
      embeddings_freq: frequency (in epochs) at which selected embedding layers
        will be saved. If set to 0, embeddings won't be computed. Data to be
        visualized in TensorBoard's Embedding tab must be passed as
        `embeddings_data`.
      embeddings_layer_names: a list of names of layers to keep eye on. If None
        or empty list all the embedding layer will be watched.
      embeddings_metadata: a dictionary which maps layer name to a file name in
        which metadata for this embedding layer is saved.
          [Here are details](
            https://www.tensorflow.org/how_tos/embedding_viz/#metadata_optional)
            about metadata files format. In case if the same metadata file is
            used for all embedding layers, string can be passed.
      embeddings_data: data to be embedded at layers specified in
        `embeddings_layer_names`. Numpy array (if the model has a single input)
        or list of Numpy arrays (if the model has multiple inputs). Learn more
        about embeddings [in this guide](
          https://www.tensorflow.org/programmers_guide/embedding).
      update_freq: `'batch'` or `'epoch'` or integer. When using `'batch'`,
        writes the losses and metrics to TensorBoard after each batch. The same
        applies for `'epoch'`. If using an integer, let's say `1000`, the
        callback will write the metrics and losses to TensorBoard every 1000
        samples. Note that writing too frequently to TensorBoard can slow down
        your training.
      profile_batch: Profile the batch to sample compute characteristics. By
        default, it will profile the second batch. Set profile_batch=0 to
        disable profiling.

  Raises:
      ValueError: If histogram_freq is set and no validation data is provided.

  @compatibility(eager)
  Using the `TensorBoard` callback will work when eager execution is enabled,
  with the restriction that outputting histogram summaries of weights and
  gradients is not supported. Consequently, `histogram_freq` will be ignored.
  @end_compatibility
  """
    log_dir: Incomplete
    histogram_freq: Incomplete
    merged: Incomplete
    write_graph: Incomplete
    write_grads: Incomplete
    write_images: Incomplete
    batch_size: Incomplete
    embeddings_freq: Incomplete
    embeddings_layer_names: Incomplete
    embeddings_metadata: Incomplete
    embeddings_data: Incomplete
    update_freq: int
    def __init__(self, log_dir: str = './logs', histogram_freq: int = 0, batch_size: int = 32, write_graph: bool = True, write_grads: bool = False, write_images: bool = False, embeddings_freq: int = 0, embeddings_layer_names: Incomplete | None = None, embeddings_metadata: Incomplete | None = None, embeddings_data: Incomplete | None = None, update_freq: str = 'epoch', profile_batch: int = 2) -> None: ...
    model: Incomplete
    assign_embeddings: Incomplete
    batch_id: Incomplete
    step: Incomplete
    saver: Incomplete
    def set_model(self, model) -> None:
        """Sets Keras model and creates summary ops."""
    def on_train_batch_begin(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_train_batch_end(self, batch, logs: Incomplete | None = None): ...
    def on_test_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_test_end(self, logs: Incomplete | None = None) -> None: ...
    def on_batch_end(self, batch, logs: Incomplete | None = None) -> None:
        """Writes scalar summaries for metrics on every training batch.

    Performs profiling if current batch is in profiler_batches.
    """
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_epoch_begin(self, epoch, logs: Incomplete | None = None) -> None:
        """Add histogram op to Model eval_function callbacks, reset batch count."""
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None:
        """Checks if summary ops should run next epoch, logs scalar summaries."""
    def on_train_end(self, logs: Incomplete | None = None) -> None: ...

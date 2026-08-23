from _typeshed import Incomplete

__all__ = ['hparams', 'scalar', 'histogram_raw', 'histogram', 'make_histogram', 'image', 'image_boxes', 'draw_boxes', 'make_image', 'video', 'make_video', 'audio', 'custom_scalars', 'text', 'pr_curve_raw', 'pr_curve', 'compute_curve', 'mesh']

def hparams(hparam_dict: Incomplete | None = None, metric_dict: Incomplete | None = None, hparam_domain_discrete: Incomplete | None = None):
    """Outputs three `Summary` protocol buffers needed by hparams plugin.
    `Experiment` keeps the metadata of an experiment, such as the name of the
      hyperparameters and the name of the metrics.
    `SessionStartInfo` keeps key-value pairs of the hyperparameters
    `SessionEndInfo` describes status of the experiment e.g. STATUS_SUCCESS

    Args:
      hparam_dict: A dictionary that contains names of the hyperparameters
        and their values.
      metric_dict: A dictionary that contains names of the metrics
        and their values.
      hparam_domain_discrete: (Optional[Dict[str, List[Any]]]) A dictionary that
        contains names of the hyperparameters and all discrete values they can hold

    Returns:
      The `Summary` protobufs for Experiment, SessionStartInfo and
        SessionEndInfo
    """
def scalar(name, tensor, collections: Incomplete | None = None, new_style: bool = False, double_precision: bool = False):
    """Outputs a `Summary` protocol buffer containing a single scalar value.
    The generated Summary has a Tensor.proto containing the input Tensor.
    Args:
      name: A name for the generated node. Will also serve as the series name in
        TensorBoard.
      tensor: A real numeric Tensor containing a single value.
      collections: Optional list of graph collections keys. The new summary op is
        added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
      new_style: Whether to use new style (tensor field) or old style (simple_value
        field). New style could lead to faster data loading.
    Returns:
      A scalar `Tensor` of type `string`. Which contains a `Summary` protobuf.
    Raises:
      ValueError: If tensor has the wrong shape or type.
    """
def histogram_raw(name, min, max, num, sum, sum_squares, bucket_limits, bucket_counts):
    """Outputs a `Summary` protocol buffer with a histogram.
    The generated
    [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
    has one summary value containing a histogram for `values`.
    Args:
      name: A name for the generated node. Will also serve as a series name in
        TensorBoard.
      min: A float or int min value
      max: A float or int max value
      num: Int number of values
      sum: Float or int sum of all values
      sum_squares: Float or int sum of squares for all values
      bucket_limits: A numeric `Tensor` with upper value per bucket
      bucket_counts: A numeric `Tensor` with number of values per bucket
    Returns:
      A scalar `Tensor` of type `string`. The serialized `Summary` protocol
      buffer.
    """
def histogram(name, values, bins, max_bins: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with a histogram.
    The generated
    [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
    has one summary value containing a histogram for `values`.
    This op reports an `InvalidArgument` error if any value is not finite.
    Args:
      name: A name for the generated node. Will also serve as a series name in
        TensorBoard.
      values: A real numeric `Tensor`. Any shape. Values to use to
        build the histogram.
    Returns:
      A scalar `Tensor` of type `string`. The serialized `Summary` protocol
      buffer.
    """
def make_histogram(values, bins, max_bins: Incomplete | None = None):
    """Convert values into a histogram proto using logic from histogram.cc."""
def image(tag, tensor, rescale: int = 1, dataformats: str = 'NCHW'):
    """Outputs a `Summary` protocol buffer with images.
    The summary has up to `max_images` summary values containing images. The
    images are built from `tensor` which must be 3-D with shape `[height, width,
    channels]` and where `channels` can be:
    *  1: `tensor` is interpreted as Grayscale.
    *  3: `tensor` is interpreted as RGB.
    *  4: `tensor` is interpreted as RGBA.
    The `name` in the outputted Summary.Value protobufs is generated based on the
    name, with a suffix depending on the max_outputs setting:
    *  If `max_outputs` is 1, the summary value tag is '*name*/image'.
    *  If `max_outputs` is greater than 1, the summary value tags are
       generated sequentially as '*name*/image/0', '*name*/image/1', etc.
    Args:
      tag: A name for the generated node. Will also serve as a series name in
        TensorBoard.
      tensor: A 3-D `uint8` or `float32` `Tensor` of shape `[height, width,
        channels]` where `channels` is 1, 3, or 4.
        'tensor' can either have values in [0, 1] (float32) or [0, 255] (uint8).
        The image() function will scale the image values to [0, 255] by applying
        a scale factor of either 1 (uint8) or 255 (float32). Out-of-range values
        will be clipped.
    Returns:
      A scalar `Tensor` of type `string`. The serialized `Summary` protocol
      buffer.
    """
def image_boxes(tag, tensor_image, tensor_boxes, rescale: int = 1, dataformats: str = 'CHW', labels: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with images."""
def draw_boxes(disp_image, boxes, labels: Incomplete | None = None): ...
def make_image(tensor, rescale: int = 1, rois: Incomplete | None = None, labels: Incomplete | None = None):
    """Convert a numpy representation of an image to Image protobuf"""
def video(tag, tensor, fps: int = 4): ...
def make_video(tensor, fps): ...
def audio(tag, tensor, sample_rate: int = 44100): ...
def custom_scalars(layout): ...
def text(tag, text): ...
def pr_curve_raw(tag, tp, fp, tn, fn, precision, recall, num_thresholds: int = 127, weights: Incomplete | None = None): ...
def pr_curve(tag, labels, predictions, num_thresholds: int = 127, weights: Incomplete | None = None): ...
def compute_curve(labels, predictions, num_thresholds: Incomplete | None = None, weights: Incomplete | None = None): ...
def mesh(tag, vertices, colors, faces, config_dict, display_name: Incomplete | None = None, description: Incomplete | None = None):
    """Outputs a merged `Summary` protocol buffer with a mesh/point cloud.

    Args:
      tag: A name for this summary operation.
      vertices: Tensor of shape `[dim_1, ..., dim_n, 3]` representing the 3D
        coordinates of vertices.
      faces: Tensor of shape `[dim_1, ..., dim_n, 3]` containing indices of
        vertices within each triangle.
      colors: Tensor of shape `[dim_1, ..., dim_n, 3]` containing colors for each
        vertex.
      display_name: If set, will be used as the display name in TensorBoard.
        Defaults to `name`.
      description: A longform readable description of the summary data. Markdown
        is supported.
      config_dict: Dictionary with ThreeJS classes names and configuration.

    Returns:
      Merged summary for mesh/point cloud representation.
    """

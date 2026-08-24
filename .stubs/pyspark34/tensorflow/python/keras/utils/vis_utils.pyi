from tensorflow.python.keras.utils.io_utils import path_to_string as path_to_string
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export

def check_pydot():
    """Returns True if PyDot and Graphviz are available."""
def is_wrapped_model(layer): ...
def add_edge(dot, src, dst) -> None: ...
def model_to_dot(model, show_shapes: bool = False, show_dtype: bool = False, show_layer_names: bool = True, rankdir: str = 'TB', expand_nested: bool = False, dpi: int = 96, subgraph: bool = False):
    """Convert a Keras model to dot format.

  Args:
    model: A Keras model instance.
    show_shapes: whether to display shape information.
    show_dtype: whether to display layer dtypes.
    show_layer_names: whether to display layer names.
    rankdir: `rankdir` argument passed to PyDot,
        a string specifying the format of the plot:
        'TB' creates a vertical plot;
        'LR' creates a horizontal plot.
    expand_nested: whether to expand nested models into clusters.
    dpi: Dots per inch.
    subgraph: whether to return a `pydot.Cluster` instance.

  Returns:
    A `pydot.Dot` instance representing the Keras model or
    a `pydot.Cluster` instance representing nested model if
    `subgraph=True`.

  Raises:
    ImportError: if graphviz or pydot are not available.
  """
def plot_model(model, to_file: str = 'model.png', show_shapes: bool = False, show_dtype: bool = False, show_layer_names: bool = True, rankdir: str = 'TB', expand_nested: bool = False, dpi: int = 96):
    """Converts a Keras model to dot format and save to a file.

  Example:

  ```python
  input = tf.keras.Input(shape=(100,), dtype='int32', name='input')
  x = tf.keras.layers.Embedding(
      output_dim=512, input_dim=10000, input_length=100)(input)
  x = tf.keras.layers.LSTM(32)(x)
  x = tf.keras.layers.Dense(64, activation='relu')(x)
  x = tf.keras.layers.Dense(64, activation='relu')(x)
  x = tf.keras.layers.Dense(64, activation='relu')(x)
  output = tf.keras.layers.Dense(1, activation='sigmoid', name='output')(x)
  model = tf.keras.Model(inputs=[input], outputs=[output])
  dot_img_file = '/tmp/model_1.png'
  tf.keras.utils.plot_model(model, to_file=dot_img_file, show_shapes=True)
  ```

  Args:
    model: A Keras model instance
    to_file: File name of the plot image.
    show_shapes: whether to display shape information.
    show_dtype: whether to display layer dtypes.
    show_layer_names: whether to display layer names.
    rankdir: `rankdir` argument passed to PyDot,
        a string specifying the format of the plot:
        'TB' creates a vertical plot;
        'LR' creates a horizontal plot.
    expand_nested: Whether to expand nested models into clusters.
    dpi: Dots per inch.

  Returns:
    A Jupyter notebook Image object if Jupyter is installed.
    This enables in-line display of the model plots in notebooks.
  """

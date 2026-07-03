from _typeshed import Incomplete
from keras.utils import io_utils as io_utils, layer_utils as layer_utils

def check_pydot():
    """Returns True if PyDot is available."""
def check_graphviz():
    """Returns True if both PyDot and Graphviz are available."""
def is_wrapped_model(layer): ...
def add_edge(dot, src, dst) -> None: ...
def model_to_dot(model, show_shapes: bool = False, show_dtype: bool = False, show_layer_names: bool = True, rankdir: str = 'TB', expand_nested: bool = False, dpi: int = 96, subgraph: bool = False, layer_range: Incomplete | None = None, show_layer_activations: bool = False, show_trainable: bool = False):
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
      layer_range: input of `list` containing two `str` items, which is the
          starting layer name and ending layer name (both inclusive) indicating
          the range of layers for which the `pydot.Dot` will be generated. It
          also accepts regex patterns instead of exact name. In such case, start
          predicate will be the first element it matches to `layer_range[0]`
          and the end predicate will be the last element it matches to
          `layer_range[1]`. By default `None` which considers all layers of
          model. Note that you must pass range such that the resultant subgraph
          must be complete.
      show_layer_activations: Display layer activations (only for layers that
          have an `activation` property).
      show_trainable: whether to display if a layer is trainable. Displays 'T'
          when the layer is trainable and 'NT' when it is not trainable.

    Returns:
      A `pydot.Dot` instance representing the Keras model or
      a `pydot.Cluster` instance representing nested model if
      `subgraph=True`.

    Raises:
      ValueError: if `model_to_dot` is called before the model is built.
      ImportError: if pydot is not available.
    """
def plot_model(model, to_file: str = 'model.png', show_shapes: bool = False, show_dtype: bool = False, show_layer_names: bool = True, rankdir: str = 'TB', expand_nested: bool = False, dpi: int = 96, layer_range: Incomplete | None = None, show_layer_activations: bool = False, show_trainable: bool = False):
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
          a string specifying the format of the plot: 'TB' creates a vertical
            plot; 'LR' creates a horizontal plot.
      expand_nested: Whether to expand nested models into clusters.
      dpi: Dots per inch.
      layer_range: input of `list` containing two `str` items, which is the
        starting layer name and ending layer name (both inclusive) indicating
        the range of layers for which the plot will be generated. It also
        accepts regex patterns instead of exact name. In such case, start
        predicate will be the first element it matches to `layer_range[0]` and
        the end predicate will be the last element it matches to
        `layer_range[1]`. By default `None` which considers all layers of model.
        Note that you must pass range such that the resultant subgraph must be
        complete.
      show_layer_activations: Display layer activations (only for layers that
        have an `activation` property).
      show_trainable: whether to display if a layer is trainable. Displays 'T'
        when the layer is trainable and 'NT' when it is not trainable.

    Raises:
      ImportError: if graphviz or pydot are not available.
      ValueError: if `plot_model` is called before the model is built.

    Returns:
      A Jupyter notebook Image object if Jupyter is installed.
      This enables in-line display of the model plots in notebooks.
    """

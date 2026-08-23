from _typeshed import Incomplete
from collections.abc import Generator
from keras import initializers as initializers
from keras.utils import io_utils as io_utils

def get_source_inputs(tensor, layer: Incomplete | None = None, node_index: Incomplete | None = None):
    """Returns the list of input tensors necessary to compute `tensor`.

    Output will always be a list of tensors
    (potentially with 1 element).

    Args:
        tensor: The tensor to start from.
        layer: Origin layer of the tensor. Will be
            determined via tensor._keras_history if not provided.
        node_index: Origin node index of the tensor.

    Returns:
        List of input tensors.
    """
def validate_string_arg(input_data, allowable_strings, layer_name, arg_name, allow_none: bool = False, allow_callables: bool = False) -> None:
    """Validates the correctness of a string-based arg."""
def count_params(weights):
    """Count the total number of scalars composing the weights.

    Args:
        weights: An iterable containing the weights on which to compute params

    Returns:
        The total number of scalars composing the weights
    """
def get_layer_index_bound_by_layer_name(model, layer_range: Incomplete | None = None):
    """Get the layer indexes from the model based on layer names.

    The layer indexes can be used to slice the model into sub models for
    display.

    Args:
        model: `tf.keras.Model` instance.
        layer_names: a list or tuple of 2 strings, the starting layer name and
            ending layer name (both inclusive) for the result. All layers will
            be included when `None` is provided.

    Returns:
        The index value of layer based on its unique name (layer_names).
        Output will be [first_layer_index, last_layer_index + 1].
    """
def print_summary(model, line_length: Incomplete | None = None, positions: Incomplete | None = None, print_fn: Incomplete | None = None, expand_nested: bool = False, show_trainable: bool = False, layer_range: Incomplete | None = None) -> None:
    """Prints a summary of a model.

    Args:
        model: Keras model instance.
        line_length: Total length of printed lines
            (e.g. set this to adapt the display to different
            terminal window sizes).
        positions: Relative or absolute positions of log elements in each line.
            If not provided, defaults to `[.33, .55, .67, 1.]`.
        print_fn: Print function to use.
            It will be called on each line of the summary.
            You can set it to a custom function
            in order to capture the string summary.
            It defaults to `print` (prints to stdout).
        expand_nested: Whether to expand the nested models.
            If not provided, defaults to `False`.
        show_trainable: Whether to show if a layer is trainable.
            If not provided, defaults to `False`.
        layer_range: List or tuple containing two strings,
            the starting layer name and ending layer name (both inclusive),
            indicating the range of layers to be printed in the summary. The
            strings could also be regexes instead of an exact name. In this
             case, the starting layer will be the first layer that matches
            `layer_range[0]` and the ending layer will be the last element that
            matches `layer_range[1]`. By default (`None`) all
            layers in the model are included in the summary.
    """
def convert_dense_weights_data_format(dense, previous_feature_map_shape, target_data_format: str = 'channels_first') -> None:
    '''Utility useful when changing a convnet\'s `data_format`.

    When porting the weights of a convnet from one data format to the other,
    if the convnet includes a `Flatten` layer
    (applied to the last convolutional feature map)
    followed by a `Dense` layer, the weights of that `Dense` layer
    should be updated to reflect the new dimension ordering.

    Args:
        dense: The target `Dense` layer.
        previous_feature_map_shape: A shape tuple of 3 integers,
            e.g. `(512, 7, 7)`. The shape of the convolutional
            feature map right before the `Flatten` layer that
            came before the target `Dense` layer.
        target_data_format: One of "channels_last", "channels_first".
            Set it "channels_last"
            if converting a "channels_first" model to "channels_last",
            or reciprocally.
    '''
def is_builtin_layer(layer): ...
def cached_per_instance(f):
    """Lightweight decorator for caching lazily constructed properties.

    When to use:
    This decorator provides simple caching with minimal overhead. It is designed
    for properties which are expensive to compute and static over the life of a
    class instance, and provides no mechanism for cache invalidation. Thus it is
    best suited for lazily exposing derived properties of other static data.

    For classes with custom getattr / setattr behavior (such as trackable
    objects), storing cache results as object attributes is not performant.
    Instead, a specialized cache can significantly reduce property lookup
    overhead. (While still allowing the decorated property to be lazily
    computed.) Consider the following class:

    ```
    class MyClass:
      def __setattr__(self, key, value):
        # Some expensive class specific code
        # ...
        # ...

        super(MyClass, self).__setattr__(key, value)

      @property
      def thing(self):
        # `thing` is expensive to compute (and may not even be requested), so we
        # want to lazily compute it and then cache it.
        output = getattr(self, '_thing', None)
        if output is None:
          self._thing = output = compute_thing(self)
        return output
    ```

    It's also worth noting that ANY overriding of __setattr__, even something as
    simple as:
    ```
      def __setattr__(self, key, value):
        super(MyClass, self).__setattr__(key, value)
    ```

    Slows down attribute assignment by nearly 10x.

    By contrast, replacing the definition of `thing` with the following
    sidesteps the expensive __setattr__ altogether:

    '''
    @property
    @tracking.cached_per_instance
    def thing(self):
      # `thing` is expensive to compute (and may not even be requested), so we
      # want to lazily compute it and then cache it.
      return compute_thing(self)
    '''

    Performance:
    The overhead for this decorator is ~0.4 us / call. A much lower overhead
    implementation (~0.085 us / call) can be achieved by using a custom dict
    type:

    ```
    def dict_based_cache(f):
      class Cache(dict):
        __slots__ = ()
        def __missing__(self, key):
          self[key] = output = f(key)
          return output

      return property(Cache().__getitem__)
    ```

    However, that implementation holds class instances as keys, and as a result
    blocks garbage collection. (And modifying it to use weakref's as keys raises
    the lookup overhead to ~0.4 us) As a result, the WeakKeyDictionary
    implementation below turns out to be more prudent.

    Args:
      f: The function to cache.

    Returns:
      f decorated with simple caching behavior.
    """
def filter_empty_layer_containers(layer_list) -> Generator[Incomplete, None, None]:
    """Filter out empty Layer-like containers and uniquify."""

class CallFunctionSpec:
    """Caches the spec and provides utilities for handling call function
    args."""
    def __init__(self, full_argspec) -> None:
        """Initialies a `CallFunctionSpec`.

        Args:
          full_argspec: the FullArgSpec of a call function of a layer.
        """
    @property
    def full_argspec(self):
        """Returns the FullArgSpec of the call function."""
    @property
    def arg_names(self):
        """List of names of args and kwonlyargs."""
    @arg_names.setter
    def arg_names(self, value) -> None: ...
    @property
    def arg_positions(self):
        """Returns a dict mapping arg names to their index positions."""
    @property
    def expects_training_arg(self):
        """Whether the call function uses 'training' as a parameter."""
    @expects_training_arg.setter
    def expects_training_arg(self, value) -> None: ...
    @property
    def expects_mask_arg(self):
        """Whether the call function uses `mask` as a parameter."""
    @expects_mask_arg.setter
    def expects_mask_arg(self, value) -> None: ...
    @property
    def default_training_arg(self):
        '''The default value given to the "training" argument.'''
    def arg_was_passed(self, arg_name, args, kwargs, inputs_in_args: bool = False):
        """Returns true if argument is present in `args` or `kwargs`.

        Args:
          arg_name: String name of the argument to find.
          args: Tuple of args passed to the call function.
          kwargs: Dictionary of kwargs  passed to the call function.
          inputs_in_args: Whether the input argument (the first argument in the
            call function) is included in `args`. Defaults to `False`.

        Returns:
          True if argument with `arg_name` is present in `args` or `kwargs`.
        """
    def get_arg_value(self, arg_name, args, kwargs, inputs_in_args: bool = False):
        """Retrieves the value for the argument with name `arg_name`.

        Args:
          arg_name: String name of the argument to find.
          args: Tuple of args passed to the call function.
          kwargs: Dictionary of kwargs  passed to the call function.
          inputs_in_args: Whether the input argument (the first argument in the
            call function) is included in `args`. Defaults to `False`.

        Returns:
          The value of the argument with name `arg_name`, extracted from `args`
          or `kwargs`.

        Raises:
          KeyError if the value of `arg_name` cannot be found.
        """
    def set_arg_value(self, arg_name, new_value, args, kwargs, inputs_in_args: bool = False, pop_kwarg_if_none: bool = False):
        """Sets the value of an argument into the given args/kwargs.

        Args:
          arg_name: String name of the argument to find.
          new_value: New value to give to the argument.
          args: Tuple of args passed to the call function.
          kwargs: Dictionary of kwargs  passed to the call function.
          inputs_in_args: Whether the input argument (the first argument in the
            call function) is included in `args`. Defaults to `False`.
          pop_kwarg_if_none: If the new value is `None`, and this is `True`,
            then the argument is deleted from `kwargs`.

        Returns:
          The updated `(args, kwargs)`.
        """
    def split_out_first_arg(self, args, kwargs):
        """Splits (args, kwargs) into (inputs, args, kwargs)."""

def warmstart_embedding_matrix(base_vocabulary, new_vocabulary, base_embeddings, new_embeddings_initializer: str = 'uniform'):
    '''Warm start embedding matrix with changing vocab.

    This util can be used to warmstart the embedding layer matrix when
    vocabulary changes between previously saved checkpoint and model.
    Vocabulary change could mean, the size of the new vocab is different or the
    vocabulary is reshuffled or new vocabulary has been added to old vocabulary.
    If the vocabulary size changes, size of the embedding layer matrix also
    changes. This util remaps the old vocabulary embeddings to the new embedding
    layer matrix.

    Example:
    Here is an example that demonstrates how to use the
    `warmstart_embedding_matrix` util.
    >>> import keras
    >>> vocab_base = tf.convert_to_tensor(["unk", "a", "b", "c"])
    >>> vocab_new = tf.convert_to_tensor(
    ...        ["unk", "unk", "a", "b", "c", "d", "e"])
    >>> vectorized_vocab_base = np.random.rand(vocab_base.shape[0], 3)
    >>> vectorized_vocab_new = np.random.rand(vocab_new.shape[0], 3)
    >>> warmstarted_embedding_matrix = warmstart_embedding_matrix(
    ...       base_vocabulary=vocab_base,
    ...       new_vocabulary=vocab_new,
    ...       base_embeddings=vectorized_vocab_base,
    ...       new_embeddings_initializer=keras.initializers.Constant(
    ...         vectorized_vocab_new))

    Here is an example that demonstrates how to get vocabulary and embedding
    weights from layers, use the `warmstart_embedding_matrix` util to remap the
    layer embeddings and continue with model training.
    ```
    # get old and new vocabulary by using layer.get_vocabulary()
    # for example assume TextVectorization layer is used
    base_vocabulary = old_text_vectorization_layer.get_vocabulary()
    new_vocabulary = new_text_vectorization_layer.get_vocabulary()
    # get previous embedding layer weights
    embedding_weights_base = model.get_layer(\'embedding\').get_weights()[0]
    warmstarted_embedding = keras.utils.warmstart_embedding_matrix(
                                  base_vocabulary,
                                  new_vocabulary,
                                  base_embeddings=embedding_weights_base,
                                  new_embeddings_initializer="uniform")
    updated_embedding_variable = tf.Variable(warmstarted_embedding)

    # update embedding layer weights
    model.layers[1].embeddings = updated_embedding_variable
    model.fit(..)
    # continue with model training

    ```

    Args:
        base_vocabulary: The list of vocabulary terms that
          the preexisting embedding matrix `base_embeddings` represents.
          It can be either a 1D array/tensor or a tuple/list of vocabulary
          terms (strings), or a path to a vocabulary text file. If passing a
           file path, the file should contain one line per term in the
           vocabulary.
        new_vocabulary: The list of vocabulary terms for the new vocabulary
           (same format as above).
        base_embeddings: NumPy array or tensor representing the preexisting
          embedding matrix.
        new_embeddings_initializer: Initializer for embedding vectors for
          previously unseen terms to be added to the new embedding matrix (see
          `keras.initializers`). Defaults to "uniform". new_embedding matrix
          needs to be specified with "constant" initializer.
          matrix. Default value is None.

    Returns:
      tf.tensor of remapped embedding layer matrix

    '''
def convert_vocab_to_list(vocab):
    """Convert input vacabulary to list."""

from _typeshed import Incomplete
from collections.abc import Generator
from keras import backend as backend, layers as layers, models as models
from keras.engine import base_layer_utils as base_layer_utils
from keras.utils import tf_contextlib as tf_contextlib, tf_inspect as tf_inspect

def string_test(actual, expected) -> None: ...
def numeric_test(actual, expected) -> None: ...
def get_test_data(train_samples, test_samples, input_shape, num_classes, random_seed: Incomplete | None = None):
    """Generates test data to train a model on.

    Args:
      train_samples: Integer, how many training samples to generate.
      test_samples: Integer, how many test samples to generate.
      input_shape: Tuple of integers, shape of the inputs.
      num_classes: Integer, number of classes for the data and targets.
      random_seed: Integer, random seed used by numpy to generate data.

    Returns:
      A tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
    """
def layer_test(layer_cls, kwargs: Incomplete | None = None, input_shape: Incomplete | None = None, input_dtype: Incomplete | None = None, input_data: Incomplete | None = None, expected_output: Incomplete | None = None, expected_output_dtype: Incomplete | None = None, expected_output_shape: Incomplete | None = None, validate_training: bool = True, adapt_data: Incomplete | None = None, custom_objects: Incomplete | None = None, test_harness: Incomplete | None = None, supports_masking: Incomplete | None = None):
    """Test routine for a layer with a single input and single output.

    Args:
      layer_cls: Layer class object.
      kwargs: Optional dictionary of keyword arguments for instantiating the
        layer.
      input_shape: Input shape tuple.
      input_dtype: Data type of the input data.
      input_data: Numpy array of input data.
      expected_output: Numpy array of the expected output.
      expected_output_dtype: Data type expected for the output.
      expected_output_shape: Shape tuple for the expected shape of the output.
      validate_training: Whether to attempt to validate training on this layer.
        This might be set to False for non-differentiable layers that output
        string or integer values.
      adapt_data: Optional data for an 'adapt' call. If None, adapt() will not
        be tested for this layer. This is only relevant for PreprocessingLayers.
      custom_objects: Optional dictionary mapping name strings to custom objects
        in the layer class. This is helpful for testing custom layers.
      test_harness: The Tensorflow test, if any, that this function is being
        called in.
      supports_masking: Optional boolean to check the `supports_masking`
        property of the layer. If None, the check will not be performed.

    Returns:
      The output data (Numpy array) returned by the layer, for additional
      checks to be done by the calling code.

    Raises:
      ValueError: if `input_shape is None`.
    """
def model_type_scope(value) -> Generator[Incomplete, None, None]:
    """Provides a scope within which the model type to test is equal to `value`.

    The model type gets restored to its original value upon exiting the scope.

    Args:
       value: model type value

    Yields:
      The provided value.
    """
def run_eagerly_scope(value) -> Generator[Incomplete, None, None]:
    """Provides a scope within which we compile models to run eagerly or not.

    The boolean gets restored to its original value upon exiting the scope.

    Args:
       value: Bool specifying if we should run models eagerly in the active
         test. Should be True or False.

    Yields:
      The provided value.
    """
def should_run_eagerly():
    """Returns whether the models we are testing should be run eagerly."""
def saved_model_format_scope(value, **kwargs) -> Generator[None, None, None]:
    """Provides a scope within which the savde model format to test is `value`.

    The saved model format gets restored to its original value upon exiting the
    scope.

    Args:
       value: saved model format value
       **kwargs: optional kwargs to pass to the save function.

    Yields:
      The provided value.
    """
def get_save_format(): ...
def get_save_kwargs(): ...
def get_model_type():
    """Gets the model type that should be tested."""
def get_small_sequential_mlp(num_hidden, num_classes, input_dim: Incomplete | None = None): ...
def get_small_functional_mlp(num_hidden, num_classes, input_dim): ...

class SmallSubclassMLP(models.Model):
    """A subclass model based small MLP."""
    num_hidden: Incomplete
    num_classes: Incomplete
    use_bn: Incomplete
    use_dp: Incomplete
    layer_a: Incomplete
    layer_b: Incomplete
    dp: Incomplete
    bn: Incomplete
    def __init__(self, num_hidden, num_classes, use_bn: bool = False, use_dp: bool = False, **kwargs) -> None: ...
    def call(self, inputs, **kwargs): ...
    def get_config(self): ...

class _SmallSubclassMLPCustomBuild(models.Model):
    """A subclass model small MLP that uses a custom build method."""
    layer_a: Incomplete
    layer_b: Incomplete
    num_hidden: Incomplete
    num_classes: Incomplete
    def __init__(self, num_hidden, num_classes) -> None: ...
    def build(self, input_shape) -> None: ...
    def call(self, inputs, **kwargs): ...

def get_small_subclass_mlp(num_hidden, num_classes): ...
def get_small_subclass_mlp_with_custom_build(num_hidden, num_classes): ...
def get_small_mlp(num_hidden, num_classes, input_dim):
    """Get a small mlp of the model type specified by `get_model_type`."""

class _SubclassModel(models.Model):
    """A Keras subclass model."""
    num_layers: Incomplete
    def __init__(self, model_layers, *args, **kwargs) -> None:
        """Instantiate a model.

        Args:
          model_layers: a list of layers to be added to the model.
          *args: Model's args
          **kwargs: Model's keyword args, at most one of input_tensor -> the
            input tensor required for ragged/sparse input.
        """
    def call(self, inputs, **kwargs): ...
    def get_config(self) -> None: ...

class _SubclassModelCustomBuild(models.Model):
    """A Keras subclass model that uses a custom build method."""
    all_layers: Incomplete
    def __init__(self, layer_generating_func, *args, **kwargs) -> None: ...
    def build(self, input_shape) -> None: ...
    def call(self, inputs, **kwargs): ...

def get_model_from_layers(model_layers, input_shape: Incomplete | None = None, input_dtype: Incomplete | None = None, name: Incomplete | None = None, input_ragged: Incomplete | None = None, input_sparse: Incomplete | None = None, model_type: Incomplete | None = None):
    '''Builds a model from a sequence of layers.

    Args:
      model_layers: The layers used to build the network.
      input_shape: Shape tuple of the input or \'TensorShape\' instance.
      input_dtype: Datatype of the input.
      name: Name for the model.
      input_ragged: Boolean, whether the input data is a ragged tensor.
      input_sparse: Boolean, whether the input data is a sparse tensor.
      model_type: One of "subclass", "subclass_custom_build", "sequential", or
        "functional". When None, defaults to `get_model_type`.

    Returns:
      A Keras model.
    '''

class Bias(layers.Layer):
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...

class _MultiIOSubclassModel(models.Model):
    """Multi IO Keras subclass model."""
    def __init__(self, branch_a, branch_b, shared_input_branch: Incomplete | None = None, shared_output_branch: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def call(self, inputs, **kwargs): ...

class _MultiIOSubclassModelCustomBuild(models.Model):
    """Multi IO Keras subclass model that uses a custom build method."""
    def __init__(self, branch_a_func, branch_b_func, shared_input_branch_func: Incomplete | None = None, shared_output_branch_func: Incomplete | None = None) -> None: ...
    def build(self, input_shape) -> None: ...
    def call(self, inputs, **kwargs): ...

def get_multi_io_model(branch_a, branch_b, shared_input_branch: Incomplete | None = None, shared_output_branch: Incomplete | None = None):
    """Builds a multi-io model that contains two branches.

    The produced model will be of the type specified by `get_model_type`.

    To build a two-input, two-output model:
      Specify a list of layers for branch a and branch b, but do not specify any
      shared input branch or shared output branch. The resulting model will
      apply each branch to a different input, to produce two outputs.

      The first value in branch_a must be the Keras 'Input' layer for branch a,
      and the first value in branch_b must be the Keras 'Input' layer for
      branch b.

      example usage:
      ```
      branch_a = [Input(shape=(2,), name='a'), Dense(), Dense()]
      branch_b = [Input(shape=(3,), name='b'), Dense(), Dense()]

      model = get_multi_io_model(branch_a, branch_b)
      ```

    To build a two-input, one-output model:
      Specify a list of layers for branch a and branch b, and specify a
      shared output branch. The resulting model will apply
      each branch to a different input. It will then apply the shared output
      branch to a tuple containing the intermediate outputs of each branch,
      to produce a single output. The first layer in the shared_output_branch
      must be able to merge a tuple of two tensors.

      The first value in branch_a must be the Keras 'Input' layer for branch a,
      and the first value in branch_b must be the Keras 'Input' layer for
      branch b.

      example usage:
      ```
      input_branch_a = [Input(shape=(2,), name='a'), Dense(), Dense()]
      input_branch_b = [Input(shape=(3,), name='b'), Dense(), Dense()]
      shared_output_branch = [Concatenate(), Dense(), Dense()]

      model = get_multi_io_model(input_branch_a, input_branch_b,
                                 shared_output_branch=shared_output_branch)
      ```
    To build a one-input, two-output model:
      Specify a list of layers for branch a and branch b, and specify a
      shared input branch. The resulting model will take one input, and apply
      the shared input branch to it. It will then respectively apply each branch
      to that intermediate result in parallel, to produce two outputs.

      The first value in the shared_input_branch must be the Keras 'Input' layer
      for the whole model. Branch a and branch b should not contain any Input
      layers.

      example usage:
      ```
      shared_input_branch = [Input(shape=(2,), name='in'), Dense(), Dense()]
      output_branch_a = [Dense(), Dense()]
      output_branch_b = [Dense(), Dense()]


      model = get_multi_io_model(output__branch_a, output_branch_b,
                                 shared_input_branch=shared_input_branch)
      ```

    Args:
      branch_a: A sequence of layers for branch a of the model.
      branch_b: A sequence of layers for branch b of the model.
      shared_input_branch: An optional sequence of layers to apply to a single
        input, before applying both branches to that intermediate result. If
        set, the model will take only one input instead of two. Defaults to
        None.
      shared_output_branch: An optional sequence of layers to merge the
        intermediate results produced by branch a and branch b. If set,
        the model will produce only one output instead of two. Defaults to None.

    Returns:
      A multi-io model of the type specified by `get_model_type`, specified
      by the different branches.
    """
def get_v2_optimizer(name, **kwargs):
    """Get the v2 optimizer requested.

    This is only necessary until v2 are the default, as we are testing in Eager,
    and Eager + v1 optimizers fail tests. When we are in v2, the strings alone
    should be sufficient, and this mapping can theoretically be removed.

    Args:
      name: string name of Keras v2 optimizer.
      **kwargs: any kwargs to pass to the optimizer constructor.

    Returns:
      Initialized Keras v2 optimizer.

    Raises:
      ValueError: if an unknown name was passed.
    """
def get_expected_metric_variable_names(var_names, name_suffix: str = ''):
    """Returns expected metric variable names given names and prefix/suffix."""
def enable_v2_dtype_behavior(fn):
    """Decorator for enabling the layer V2 dtype behavior on a test."""
def disable_v2_dtype_behavior(fn):
    """Decorator for disabling the layer V2 dtype behavior on a test."""
def device(should_use_gpu) -> Generator[None, None, None]:
    """Uses gpu when requested and available."""
def use_gpu() -> Generator[None, None, None]:
    """Uses gpu when requested and available."""
def for_all_test_methods(decorator, *args, **kwargs):
    """Generate class-level decorator from given method-level decorator.

    It is expected for the given decorator to take some arguments and return
    a method that is then called on the test method to produce a decorated
    method.

    Args:
      decorator: The decorator to apply.
      *args: Positional arguments
      **kwargs: Keyword arguments
    Returns: Function that will decorate a given classes test methods with the
      decorator.
    """
def run_without_tensor_float_32(description):
    """Execute test with TensorFloat-32 disabled.

    While almost every real-world deep learning model runs fine with
    TensorFloat-32, many tests use assertAllClose or similar methods.
    TensorFloat-32 matmuls typically will cause such methods to fail with the
    default tolerances.

    Args:
      description: A description used for documentation purposes, describing why
        the test requires TensorFloat-32 to be disabled.

    Returns:
      Decorator which runs a test with TensorFloat-32 disabled.
    """
def run_all_without_tensor_float_32(description):
    """Execute all tests in a class with TensorFloat-32 disabled."""
def run_v2_only(obj: Incomplete | None = None):
    """Execute the decorated test only if running in v2 mode.

    This function is intended to be applied to tests that exercise v2 only
    functionality. If the test is run in v1 mode it will simply be skipped.

    See go/tf-test-decorator-cheatsheet for the decorators to use in different
    v1/v2/eager/graph combinations.

    Args:
      obj: function to be annotated. If None, return a
        decorator the can be applied to a function or class. If `obj` is not
        None, return the decorator applied to `obj`.

    Returns:
      Returns a decorator that will conditionally skip the decorated test
      method.
    """
def generate_combinations_with_testcase_name(**kwargs):
    """Generate combinations based on its keyword arguments using combine().

    This function calls combine() and appends a testcase name to the list of
    dictionaries returned. The 'testcase_name' key is a required for named
    parameterized tests.

    Args:
      **kwargs: keyword arguments of form `option=[possibilities, ...]` or
        `option=the_only_possibility`.

    Returns:
      a list of dictionaries for each combination. Keys in the dictionaries are
      the keyword argument names.  Each key has one value - one of the
      corresponding keyword argument values.
    """

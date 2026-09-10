import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from absl.testing import parameterized
from keras.testing_infra import test_utils as test_utils

KERAS_MODEL_TYPES: Incomplete

class TestCase(tf.test.TestCase, parameterized.TestCase):
    def tearDown(self) -> None: ...

def run_with_all_saved_model_formats(test_or_class: Incomplete | None = None, exclude_formats: Incomplete | None = None):
    '''Execute the decorated test with all Keras saved model formats).

    This decorator is intended to be applied either to individual test methods
    in a `test_combinations.TestCase` class, or directly to a test class that
    extends it. Doing so will cause the contents of the individual test method
    (or all test methods in the class) to be executed multiple times - once for
    each Keras saved model format.

    The Keras saved model formats include:
    1. HDF5: \'h5\'
    2. SavedModel: \'tf\'

    Note: if stacking this decorator with absl.testing\'s parameterized
    decorators, those should be at the bottom of the stack.

    Various methods in `testing_utils` to get file path for saved models will
    auto-generate a string of the two saved model formats. This allows unittests
    to confirm the equivalence between the two Keras saved model formats.

    For example, consider the following unittest:

    ```python
    class MyTests(test_utils.KerasTestCase):

      @test_utils.run_with_all_saved_model_formats
      def test_foo(self):
        save_format = test_utils.get_save_format()
        saved_model_dir = \'/tmp/saved_model/\'
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(2, input_shape=(3,)))
        model.add(keras.layers.Dense(3))
        model.compile(loss=\'mse\', optimizer=\'sgd\', metrics=[\'acc\'])

        keras.models.save_model(model, saved_model_dir, save_format=save_format)
        model = keras.models.load_model(saved_model_dir)

    if __name__ == "__main__":
      tf.test.main()
    ```

    This test tries to save the model into the formats of \'hdf5\', \'h5\', \'keras\',
    \'tensorflow\', and \'tf\'.

    We can also annotate the whole class if we want this to apply to all tests
    in the class:
    ```python
    @test_utils.run_with_all_saved_model_formats
    class MyTests(test_utils.KerasTestCase):

      def test_foo(self):
        save_format = test_utils.get_save_format()
        saved_model_dir = \'/tmp/saved_model/\'
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(2, input_shape=(3,)))
        model.add(keras.layers.Dense(3))
        model.compile(loss=\'mse\', optimizer=\'sgd\', metrics=[\'acc\'])

        keras.models.save_model(model, saved_model_dir, save_format=save_format)
        model = tf.keras.models.load_model(saved_model_dir)

    if __name__ == "__main__":
      tf.test.main()
    ```

    Args:
      test_or_class: test method or class to be annotated. If None,
        this method returns a decorator that can be applied to a test method or
        test class. If it is not None this returns the decorator applied to the
        test or class.
      exclude_formats: A collection of Keras saved model formats to not run.
        (May also be a single format not wrapped in a collection).
        Defaults to None.

    Returns:
      Returns a decorator that will run the decorated test method multiple
      times: once for each desired Keras saved model format.

    Raises:
      ImportError: If abseil parameterized is not installed or not included as
        a target dependency.
    '''
def run_with_all_weight_formats(test_or_class: Incomplete | None = None, exclude_formats: Incomplete | None = None):
    """Runs all tests with the supported formats for saving weights."""
def run_with_all_model_types(test_or_class: Incomplete | None = None, exclude_models: Incomplete | None = None):
    '''Execute the decorated test with all Keras model types.

    This decorator is intended to be applied either to individual test methods
    in a `test_combinations.TestCase` class, or directly to a test class that
    extends it. Doing so will cause the contents of the individual test method
    (or all test methods in the class) to be executed multiple times - once for
    each Keras model type.

    The Keras model types are: [\'functional\', \'subclass\', \'sequential\']

    Note: if stacking this decorator with absl.testing\'s parameterized
    decorators, those should be at the bottom of the stack.

    Various methods in `testing_utils` to get models will auto-generate a model
    of the currently active Keras model type. This allows unittests to confirm
    the equivalence between different Keras models.

    For example, consider the following unittest:

    ```python
    class MyTests(test_utils.KerasTestCase):

      @test_utils.run_with_all_model_types(
        exclude_models = [\'sequential\'])
      def test_foo(self):
        model = test_utils.get_small_mlp(1, 4, input_dim=3)
        optimizer = RMSPropOptimizer(learning_rate=0.001)
        loss = \'mse\'
        metrics = [\'mae\']
        model.compile(optimizer, loss, metrics=metrics)

        inputs = np.zeros((10, 3))
        targets = np.zeros((10, 4))
        dataset = dataset_ops.Dataset.from_tensor_slices((inputs, targets))
        dataset = dataset.repeat(100)
        dataset = dataset.batch(10)

        model.fit(dataset, epochs=1, steps_per_epoch=2, verbose=1)

    if __name__ == "__main__":
      tf.test.main()
    ```

    This test tries building a small mlp as both a functional model and as a
    subclass model.

    We can also annotate the whole class if we want this to apply to all tests
    in the class:
    ```python
    @test_utils.run_with_all_model_types(exclude_models = [\'sequential\'])
    class MyTests(test_utils.KerasTestCase):

      def test_foo(self):
        model = test_utils.get_small_mlp(1, 4, input_dim=3)
        optimizer = RMSPropOptimizer(learning_rate=0.001)
        loss = \'mse\'
        metrics = [\'mae\']
        model.compile(optimizer, loss, metrics=metrics)

        inputs = np.zeros((10, 3))
        targets = np.zeros((10, 4))
        dataset = dataset_ops.Dataset.from_tensor_slices((inputs, targets))
        dataset = dataset.repeat(100)
        dataset = dataset.batch(10)

        model.fit(dataset, epochs=1, steps_per_epoch=2, verbose=1)

    if __name__ == "__main__":
      tf.test.main()
    ```


    Args:
      test_or_class: test method or class to be annotated. If None,
        this method returns a decorator that can be applied to a test method or
        test class. If it is not None this returns the decorator applied to the
        test or class.
      exclude_models: A collection of Keras model types to not run.
        (May also be a single model type not wrapped in a collection).
        Defaults to None.

    Returns:
      Returns a decorator that will run the decorated test method multiple
      times: once for each desired Keras model type.

    Raises:
      ImportError: If abseil parameterized is not installed or not included as
        a target dependency.
    '''
def run_all_keras_modes(test_or_class: Incomplete | None = None, config: Incomplete | None = None, always_skip_v1: bool = False, always_skip_eager: bool = False, **kwargs):
    '''Execute the decorated test with all keras execution modes.

    This decorator is intended to be applied either to individual test methods
    in a `test_combinations.TestCase` class, or directly to a test class that
    extends it. Doing so will cause the contents of the individual test method
    (or all test methods in the class) to be executed multiple times - once
    executing in legacy graph mode, once running eagerly and with
    `should_run_eagerly` returning True, and once running eagerly with
    `should_run_eagerly` returning False.

    If Tensorflow v2 behavior is enabled, legacy graph mode will be skipped, and
    the test will only run twice.

    Note: if stacking this decorator with absl.testing\'s parameterized
    decorators, those should be at the bottom of the stack.

    For example, consider the following unittest:

    ```python
    class MyTests(test_utils.KerasTestCase):

      @test_utils.run_all_keras_modes
      def test_foo(self):
        model = test_utils.get_small_functional_mlp(1, 4, input_dim=3)
        optimizer = RMSPropOptimizer(learning_rate=0.001)
        loss = \'mse\'
        metrics = [\'mae\']
        model.compile(
            optimizer, loss, metrics=metrics,
            run_eagerly=test_utils.should_run_eagerly())

        inputs = np.zeros((10, 3))
        targets = np.zeros((10, 4))
        dataset = dataset_ops.Dataset.from_tensor_slices((inputs, targets))
        dataset = dataset.repeat(100)
        dataset = dataset.batch(10)

        model.fit(dataset, epochs=1, steps_per_epoch=2, verbose=1)

    if __name__ == "__main__":
      tf.test.main()
    ```

    This test will try compiling & fitting the small functional mlp using all
    three Keras execution modes.

    Args:
      test_or_class: test method or class to be annotated. If None,
        this method returns a decorator that can be applied to a test method or
        test class. If it is not None this returns the decorator applied to the
        test or class.
      config: An optional config_pb2.ConfigProto to use to configure the
        session when executing graphs.
      always_skip_v1: If True, does not try running the legacy graph mode even
        when Tensorflow v2 behavior is not enabled.
      always_skip_eager: If True, does not execute the decorated test
        with eager execution modes.
      **kwargs: Additional kwargs for configuring tests for
       in-progress Keras behaviors/ refactorings that we haven\'t fully
       rolled out yet

    Returns:
      Returns a decorator that will run the decorated test method multiple
      times.

    Raises:
      ImportError: If abseil parameterized is not installed or not included as
        a target dependency.
    '''
def keras_mode_combinations(mode: Incomplete | None = None, run_eagerly: Incomplete | None = None):
    """Returns the default test combinations for tf.keras tests.

    Note that if tf2 is enabled, then v1 session test will be skipped.

    Args:
      mode: List of modes to run the tests. The valid options are 'graph' and
        'eager'. Default to ['graph', 'eager'] if not specified. If a empty list
        is provide, then the test will run under the context based on tf's
        version, eg graph for v1 and eager for v2.
      run_eagerly: List of `run_eagerly` value to be run with the tests.
        Default to [True, False] if not specified. Note that for `graph` mode,
        run_eagerly value will only be False.

    Returns:
      A list contains all the combinations to be used to generate test cases.
    """
def keras_model_type_combinations(): ...

class KerasModeCombination(tf.__internal__.test.combinations.TestCombination):
    """Combination for Keras test mode.

    It by default includes v1_session, v2_eager and v2_tf_function.
    """
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

class KerasModelTypeCombination(tf.__internal__.test.combinations.TestCombination):
    """Combination for Keras model types when doing model test.

    It by default includes 'functional', 'subclass', 'sequential'.

    Various methods in `testing_utils` to get models will auto-generate a model
    of the currently active Keras model type. This allows unittests to confirm
    the equivalence between different Keras models.
    """
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

generate: Incomplete
combine: Incomplete
times: Incomplete
NamedObject: Incomplete

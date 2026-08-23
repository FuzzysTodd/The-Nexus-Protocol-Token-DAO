from _typeshed import Incomplete
from absl.testing import parameterized
from tensorflow.python import keras as keras, tf2 as tf2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import testing_utils as testing_utils
from tensorflow.python.platform import test as test
from tensorflow.python.util import nest as nest

class TestCase(test.TestCase, parameterized.TestCase):
    def tearDown(self) -> None: ...

def run_with_all_saved_model_formats(test_or_class: Incomplete | None = None, exclude_formats: Incomplete | None = None):
    '''Execute the decorated test with all Keras saved model formats).

  This decorator is intended to be applied either to individual test methods in
  a `keras_parameterized.TestCase` class, or directly to a test class that
  extends it. Doing so will cause the contents of the individual test
  method (or all test methods in the class) to be executed multiple times - once
  for each Keras saved model format.

  The Keras saved model formats include:
  1. HDF5: \'h5\'
  2. SavedModel: \'tf\'

  Note: if stacking this decorator with absl.testing\'s parameterized decorators,
  those should be at the bottom of the stack.

  Various methods in `testing_utils` to get file path for saved models will
  auto-generate a string of the two saved model formats. This allows unittests
  to confirm the equivalence between the two Keras saved model formats.

  For example, consider the following unittest:

  ```python
  class MyTests(testing_utils.KerasTestCase):

    @testing_utils.run_with_all_saved_model_formats
    def test_foo(self):
      save_format = testing_utils.get_save_format()
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

  We can also annotate the whole class if we want this to apply to all tests in
  the class:
  ```python
  @testing_utils.run_with_all_saved_model_formats
  class MyTests(testing_utils.KerasTestCase):

    def test_foo(self):
      save_format = testing_utils.get_save_format()
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
    Returns a decorator that will run the decorated test method multiple times:
    once for each desired Keras saved model format.

  Raises:
    ImportError: If abseil parameterized is not installed or not included as
      a target dependency.
  '''
def run_with_all_weight_formats(test_or_class: Incomplete | None = None, exclude_formats: Incomplete | None = None):
    """Runs all tests with the supported formats for saving weights."""
def run_with_all_model_types(test_or_class: Incomplete | None = None, exclude_models: Incomplete | None = None):
    '''Execute the decorated test with all Keras model types.

  This decorator is intended to be applied either to individual test methods in
  a `keras_parameterized.TestCase` class, or directly to a test class that
  extends it. Doing so will cause the contents of the individual test
  method (or all test methods in the class) to be executed multiple times - once
  for each Keras model type.

  The Keras model types are: [\'functional\', \'subclass\', \'sequential\']

  Note: if stacking this decorator with absl.testing\'s parameterized decorators,
  those should be at the bottom of the stack.

  Various methods in `testing_utils` to get models will auto-generate a model
  of the currently active Keras model type. This allows unittests to confirm
  the equivalence between different Keras models.

  For example, consider the following unittest:

  ```python
  class MyTests(testing_utils.KerasTestCase):

    @testing_utils.run_with_all_model_types(
      exclude_models = [\'sequential\'])
    def test_foo(self):
      model = testing_utils.get_small_mlp(1, 4, input_dim=3)
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

  We can also annotate the whole class if we want this to apply to all tests in
  the class:
  ```python
  @testing_utils.run_with_all_model_types(exclude_models = [\'sequential\'])
  class MyTests(testing_utils.KerasTestCase):

    def test_foo(self):
      model = testing_utils.get_small_mlp(1, 4, input_dim=3)
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
    Returns a decorator that will run the decorated test method multiple times:
    once for each desired Keras model type.

  Raises:
    ImportError: If abseil parameterized is not installed or not included as
      a target dependency.
  '''
def run_all_keras_modes(test_or_class: Incomplete | None = None, config: Incomplete | None = None, always_skip_v1: bool = False, always_skip_eager: bool = False, **kwargs):
    '''Execute the decorated test with all keras execution modes.

  This decorator is intended to be applied either to individual test methods in
  a `keras_parameterized.TestCase` class, or directly to a test class that
  extends it. Doing so will cause the contents of the individual test
  method (or all test methods in the class) to be executed multiple times -
  once executing in legacy graph mode, once running eagerly and with
  `should_run_eagerly` returning True, and once running eagerly with
  `should_run_eagerly` returning False.

  If Tensorflow v2 behavior is enabled, legacy graph mode will be skipped, and
  the test will only run twice.

  Note: if stacking this decorator with absl.testing\'s parameterized decorators,
  those should be at the bottom of the stack.

  For example, consider the following unittest:

  ```python
  class MyTests(testing_utils.KerasTestCase):

    @testing_utils.run_all_keras_modes
    def test_foo(self):
      model = testing_utils.get_small_functional_mlp(1, 4, input_dim=3)
      optimizer = RMSPropOptimizer(learning_rate=0.001)
      loss = \'mse\'
      metrics = [\'mae\']
      model.compile(
          optimizer, loss, metrics=metrics,
          run_eagerly=testing_utils.should_run_eagerly())

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
    Returns a decorator that will run the decorated test method multiple times.

  Raises:
    ImportError: If abseil parameterized is not installed or not included as
      a target dependency.
  '''

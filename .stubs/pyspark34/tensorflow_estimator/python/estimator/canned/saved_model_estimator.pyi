from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import estimator as estimator_lib
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.export import export_lib as export_lib
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class SavedModelEstimator(estimator_lib.EstimatorV2):
    """Create an Estimator from a SavedModel.

  Only SavedModels exported with
  `tf.estimator.Estimator.experimental_export_all_saved_models()` or
  `tf.estimator.Estimator.export_saved_model()` are supported for this class.

  Example with `tf.estimator.DNNClassifier`:

  **Step 1: Create and train DNNClassifier.**

  ```python
  feature1 = tf.feature_column.embedding_column(
      tf.feature_column.categorical_column_with_vocabulary_list(
          key='feature1', vocabulary_list=('green', 'yellow')), dimension=1)
  feature2 = tf.feature_column.numeric_column(key='feature2', default_value=0.0)

  classifier = tf.estimator.DNNClassifier(
      hidden_units=[4,2], feature_columns=[feature1, feature2])

  def input_fn():
    features = {'feature1': tf.constant(['green', 'green', 'yellow']),
                'feature2': tf.constant([3.5, 4.2, 6.1])}
    label = tf.constant([1., 0., 0.])
    return tf.data.Dataset.from_tensors((features, label)).repeat()

  classifier.train(input_fn=input_fn, steps=10)
  ```

  **Step 2: Export classifier.**
  First, build functions that specify the expected inputs.

  ```python
  # During train and evaluation, both the features and labels should be defined.
  supervised_input_receiver_fn = (
      tf.estimator.experimental.build_raw_supervised_input_receiver_fn(
          {'feature1': tf.placeholder(dtype=tf.string, shape=[None]),
           'feature2': tf.placeholder(dtype=tf.float32, shape=[None])},
          tf.placeholder(dtype=tf.float32, shape=[None])))

  # During predict mode, expect to receive a `tf.Example` proto, so a parsing
  # function is used.
  serving_input_receiver_fn = (
      tf.estimator.export.build_parsing_serving_input_receiver_fn(
          tf.feature_column.make_parse_example_spec([feature1, feature2])))
  ```

  Next, export the model as a SavedModel. A timestamped directory will be
  created (for example `/tmp/export_all/1234567890`).

  ```python
  # Option 1: Save all modes (train, eval, predict)
  export_dir = classifier.experimental_export_all_saved_models(
      '/tmp/export_all',
      {tf.estimator.ModeKeys.TRAIN: supervised_input_receiver_fn,
       tf.estimator.ModeKeys.EVAL: supervised_input_receiver_fn,
       tf.estimator.ModeKeys.PREDICT: serving_input_receiver_fn})

  # Option 2: Only export predict mode
  export_dir = classifier.export_saved_model(
      '/tmp/export_predict', serving_input_receiver_fn)
  ```

  **Step 3: Create a SavedModelEstimator from the exported SavedModel.**

  ```python
  est = tf.estimator.experimental.SavedModelEstimator(export_dir)

  # If all modes were exported, you can immediately evaluate and predict, or
  # continue training. Otherwise only predict is available.
  eval_results = est.evaluate(input_fn=input_fn, steps=1)
  print(eval_results)

  est.train(input_fn=input_fn, steps=20)

  def predict_input_fn():
    example = tf.train.Example()
    example.features.feature['feature1'].bytes_list.value.extend(['yellow'])
    example.features.feature['feature2'].float_list.value.extend([1.])
    return {'inputs':tf.constant([example.SerializeToString()])}

  predictions = est.predict(predict_input_fn)
  print(next(predictions))
  ```
  """
    saved_model_dir: Incomplete
    saved_model_loader: Incomplete
    def __init__(self, saved_model_dir, model_dir: Incomplete | None = None) -> None:
        """Initialize a SavedModelEstimator.

    The SavedModelEstimator loads its model function and variable values from
    the graphs defined in the SavedModel. There is no option to pass in
    `RunConfig` or `params` arguments, because the model function graph is
    defined statically in the SavedModel.

    Args:
      saved_model_dir: Directory containing SavedModel protobuf and subfolders.
      model_dir: Directory to save new checkpoints during training.

    Raises:
      NotImplementedError: If a DistributionStrategy is defined in the config.
        Unless the SavedModelEstimator is subclassed, this shouldn't happen.
    """
    def latest_checkpoint(self):
        """Returns the filename of the latest saved checkpoint.

    Returns:
      Filename of latest checkpoint in `model_dir`. If no checkpoints are found
      in `model_dir`, then the path to the SavedModel checkpoint is returned.
    """

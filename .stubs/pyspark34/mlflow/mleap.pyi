from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.utils import reraise as reraise
from mlflow.utils.annotations import deprecated as deprecated, keyword_only as keyword_only
from mlflow.utils.file_utils import path_to_local_file_uri as path_to_local_file_uri

FLAVOR_NAME: str

def log_model(spark_model, sample_input, artifact_path, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, metadata: Incomplete | None = None):
    '''
    Log a Spark MLLib model in MLeap format as an MLflow artifact
    for the current run. The logged model will have the MLeap flavor.

    NOTE:

        You cannot load the MLeap model flavor in Python; you must download it using the
        Java API method ``downloadArtifacts(String runId)`` and load the model
        using the method ``MLeapLoader.loadPipeline(String modelRootPath)``.

    :param spark_model: Spark PipelineModel to be saved. This model must be MLeap-compatible and
                        cannot contain any custom transformers.
    :param sample_input: Sample PySpark DataFrame input that the model can evaluate. This is
                         required by MLeap for data schema inference.
    :param artifact_path: Run-relative artifact path.
    :param registered_model_name: If given, create a model version under
                                  ``registered_model_name``, also creating a registered model if one
                                  with the given name does not exist.

    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        train = df.drop_column("target_label")
                        predictions = ...  # compute model predictions
                        signature = infer_signature(train, predictions)
    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.


    .. code-block:: python
        :caption: Example

        import mlflow
        import mlflow.mleap
        import pyspark
        from pyspark.ml import Pipeline
        from pyspark.ml.classification import LogisticRegression
        from pyspark.ml.feature import HashingTF, Tokenizer

        # training DataFrame
        training = spark.createDataFrame(
            [
                (0, "a b c d e spark", 1.0),
                (1, "b d", 0.0),
                (2, "spark f g h", 1.0),
                (3, "hadoop mapreduce", 0.0),
            ],
            ["id", "text", "label"],
        )
        # testing DataFrame
        test_df = spark.createDataFrame(
            [(4, "spark i j k"), (5, "l m n"), (6, "spark hadoop spark"), (7, "apache hadoop")],
            ["id", "text"],
        )
        # Create an MLlib pipeline
        tokenizer = Tokenizer(inputCol="text", outputCol="words")
        hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
        lr = LogisticRegression(maxIter=10, regParam=0.001)
        pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])
        model = pipeline.fit(training)
        # log parameters
        mlflow.log_param("max_iter", 10)
        mlflow.log_param("reg_param", 0.001)
        # log the Spark MLlib model in MLeap format
        mlflow.mleap.log_model(
            spark_model=model, sample_input=test_df, artifact_path="mleap-model"
        )
    '''
def save_model(spark_model, sample_input, path, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, metadata: Incomplete | None = None):
    '''
    Save a Spark MLlib PipelineModel in MLeap format at a local path.
    The saved model will have the MLeap flavor.

    NOTE:

        You cannot load the MLeap model flavor in Python; you must download it using the
        Java API method ``downloadArtifacts(String runId)`` and load the model
        using the method ``MLeapLoader.loadPipeline(String modelRootPath)``.

    :param spark_model: Spark PipelineModel to be saved. This model must be MLeap-compatible and
                  cannot contain any custom transformers.
    :param sample_input: Sample PySpark DataFrame input that the model can evaluate. This is
                         required by MLeap for data schema inference.
    :param path: Local path where the model is to be saved.
    :param mlflow_model: :py:mod:`mlflow.models.Model` to which this flavor is being added.

    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset) and valid
                      model output (e.g. model predictions generated on the training dataset),
                      for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        train = df.drop_column("target_label")
                        signature = infer_signature(train, model.predict(train))
    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.

    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        train = df.drop_column("target_label")
                        predictions = ...  # compute model predictions
                        signature = infer_signature(train, predictions)
    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    '''
def add_to_model(mlflow_model, path, spark_model, sample_input) -> None:
    """
    Add the MLeap flavor to an existing MLflow model.

    :param mlflow_model: :py:mod:`mlflow.models.Model` to which this flavor is being added.
    :param path: Path of the model to which this flavor is being added.
    :param spark_model: Spark PipelineModel to be saved. This model must be MLeap-compatible and
                        cannot contain any custom transformers.
    :param sample_input: Sample PySpark DataFrame input that the model can evaluate. This is
                         required by MLeap for data schema inference.
    """

class MLeapSerializationException(MlflowException):
    """Exception thrown when a model or DataFrame cannot be serialized in MLeap format."""

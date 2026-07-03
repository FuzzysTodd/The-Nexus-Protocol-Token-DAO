from _typeshed import Incomplete
from mlflow import environment_variables as environment_variables, mleap as mleap, pyfunc as pyfunc
from mlflow.environment_variables import MLFLOW_DFS_TMP as MLFLOW_DFS_TMP
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature, infer_signature as infer_signature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.store.artifact.databricks_artifact_repo import DatabricksArtifactRepository as DatabricksArtifactRepository
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils import databricks_utils as databricks_utils
from mlflow.utils.autologging_utils import autologging_integration as autologging_integration, safe_patch as safe_patch
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import TempDir as TempDir, shutil_copytree_without_file_permissions as shutil_copytree_without_file_permissions, write_to as write_to
from mlflow.utils.uri import append_to_uri_path as append_to_uri_path, dbfs_hdfs_uri_to_fuse_path as dbfs_hdfs_uri_to_fuse_path, generate_tmp_dfs_path as generate_tmp_dfs_path, get_databricks_profile_uri_from_artifact_uri as get_databricks_profile_uri_from_artifact_uri, is_databricks_acled_artifacts_uri as is_databricks_acled_artifacts_uri, is_local_uri as is_local_uri, is_valid_dbfs_uri as is_valid_dbfs_uri
from typing import Any, Dict

FLAVOR_NAME: str

def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at minimum, contains these requirements.
    """
def get_default_conda_env():
    """
    :return: The default Conda environment for MLflow Models produced by calls to
             :func:`save_model()` and :func:`log_model()`. This Conda environment
             contains the current version of PySpark that is installed on the caller's
             system. ``dev`` versions of PySpark are replaced with stable versions in
             the resulting Conda environment (e.g., if you are running PySpark version
             ``2.4.5.dev0``, invoking this method produces a Conda environment with a
             dependency on PySpark version ``2.4.5``).
    """
def log_model(spark_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, dfs_tmpdir: Incomplete | None = None, sample_input: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Log a Spark MLlib model as an MLflow artifact for the current run. This uses the
    MLlib persistence format and produces an MLflow Model with the Spark flavor.

    Note: If no run is active, it will instantiate a run to obtain a run_id.

    :param spark_model: Spark model to be saved - MLflow can only save descendants of
                        pyspark.ml.Model or pyspark.ml.Transformer which implement
                        MLReadable and MLWritable.
    :param artifact_path: Run relative artifact path.
    :param conda_env: Either a dictionary representation of a Conda environment or the path to a
                      Conda environment yaml file. If provided, this decsribes the environment
                      this model should be run in. At minimum, it should specify the dependencies
                      contained in :func:`get_default_conda_env()`. If `None`, the default
                      :func:`get_default_conda_env()` environment is added to the model.
                      The following is an *example* dictionary representation of a Conda
                      environment::

                        {
                            \'name\': \'mlflow-env\',
                            \'channels\': [\'defaults\'],
                            \'dependencies\': [
                                \'python=3.8.15\',
                                \'pyspark=2.3.0\'
                            ]
                        }
    :param dfs_tmpdir: Temporary directory path on Distributed (Hadoop) File System (DFS) or local
                       filesystem if running in local mode. The model is written in this
                       destination and then copied into the model\'s artifact directory. This is
                       necessary as Spark ML models read from and write to DFS if running on a
                       cluster. If this operation completes successfully, all temporary files
                       created on the DFS are removed. Defaults to ``/tmp/mlflow``.
    :param sample_input: A sample input used to add the MLeap flavor to the model.
                         This must be a PySpark DataFrame that the model can evaluate. If
                         ``sample_input`` is ``None``, the MLeap flavor is not added.
    :param registered_model_name: If given, create a model version under
                                  ``registered_model_name``, also creating a registered model if one
                                  with the given name does not exist.
    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param await_registration_for: Number of seconds to wait for the model version to finish
                            being created and is in ``READY`` status. By default, the function
                            waits for five minutes. Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.

    .. code-block:: python
        :caption: Example

        from pyspark.ml import Pipeline
        from pyspark.ml.classification import LogisticRegression
        from pyspark.ml.feature import HashingTF, Tokenizer

        training = spark.createDataFrame(
            [
                (0, "a b c d e spark", 1.0),
                (1, "b d", 0.0),
                (2, "spark f g h", 1.0),
                (3, "hadoop mapreduce", 0.0),
            ],
            ["id", "text", "label"],
        )
        tokenizer = Tokenizer(inputCol="text", outputCol="words")
        hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
        lr = LogisticRegression(maxIter=10, regParam=0.001)
        pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])
        model = pipeline.fit(training)
        mlflow.spark.log_model(model, "spark-model")
    '''

class _HadoopFileSystem:
    """
    Interface to org.apache.hadoop.fs.FileSystem.

    Spark ML models expect to read from and write to Hadoop FileSystem when running on a cluster.
    Since MLflow works on local directories, we need this interface to copy the files between
    the current DFS and local dir.
    """
    def __init__(self) -> None: ...
    @classmethod
    def copy_to_local_file(cls, src, dst, remove_src) -> None: ...
    @classmethod
    def copy_from_local_file(cls, src, dst, remove_src) -> None: ...
    @classmethod
    def qualified_local_path(cls, path): ...
    @classmethod
    def maybe_copy_from_local_file(cls, src, dst):
        """
        Conditionally copy the file to the Hadoop DFS.
        The file is copied iff the configuration has distributed filesystem.

        :return: If copied, return new target location, otherwise return (absolute) source path.
        """
    @classmethod
    def maybe_copy_from_uri(cls, src_uri, dst_path, local_model_path: Incomplete | None = None):
        """
        Conditionally copy the file to the Hadoop DFS from the source uri.
        In case the file is already on the Hadoop DFS do nothing.

        :return: If copied, return new target location, otherwise return source uri.
        """
    @classmethod
    def delete(cls, path) -> None: ...
    @classmethod
    def is_filesystem_available(cls, scheme): ...

def save_model(spark_model, path, mlflow_model: Incomplete | None = None, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, dfs_tmpdir: Incomplete | None = None, sample_input: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Save a Spark MLlib Model to a local path.

    By default, this function saves models using the Spark MLlib persistence mechanism.
    Additionally, if a sample input is specified using the ``sample_input`` parameter, the model
    is also serialized in MLeap format and the MLeap flavor is added.

    :param spark_model: Spark model to be saved - MLflow can only save descendants of
                        pyspark.ml.Model or pyspark.ml.Transformer which implement
                        MLReadable and MLWritable.
    :param path: Local path where the model is to be saved.
    :param mlflow_model: MLflow model config this flavor is being added to.
    :param conda_env: Either a dictionary representation of a Conda environment or the path to a
                      Conda environment yaml file. If provided, this decsribes the environment
                      this model should be run in. At minimum, it should specify the dependencies
                      contained in :func:`get_default_conda_env()`. If `None`, the default
                      :func:`get_default_conda_env()` environment is added to the model.
                      The following is an *example* dictionary representation of a Conda
                      environment::

                        {
                            \'name\': \'mlflow-env\',
                            \'channels\': [\'defaults\'],
                            \'dependencies\': [
                                \'python=3.8.15\',
                                \'pyspark=2.3.0\'
                            ]
                        }
    :param dfs_tmpdir: Temporary directory path on Distributed (Hadoop) File System (DFS) or local
                       filesystem if running in local mode. The model is be written in this
                       destination and then copied to the requested local path. This is necessary
                       as Spark ML models read from and write to DFS if running on a cluster. All
                       temporary files created on the DFS are removed if this operation
                       completes successfully. Defaults to ``/tmp/mlflow``.
    :param sample_input: A sample input that is used to add the MLeap flavor to the model.
                         This must be a PySpark DataFrame that the model can evaluate. If
                         ``sample_input`` is ``None``, the MLeap flavor is not added.

    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    .. code-block:: python
        :caption: Example

        from mlflow import spark
        from pyspark.ml.pipeline import PipelineModel

        # your pyspark.ml.pipeline.PipelineModel type
        model = ...
        mlflow.spark.save_model(model, "spark-model")
    '''
def load_model(model_uri, dfs_tmpdir: Incomplete | None = None, dst_path: Incomplete | None = None):
    '''
    Load the Spark MLlib model from the path.

    :param model_uri: The location, in URI format, of the MLflow model, for example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.
    :param dfs_tmpdir: Temporary directory path on Distributed (Hadoop) File System (DFS) or local
                       filesystem if running in local mode. The model is loaded from this
                       destination. Defaults to ``/tmp/mlflow``.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.
    :return: pyspark.ml.pipeline.PipelineModel

    .. code-block:: python
        :caption: Example

        from mlflow import spark

        model = mlflow.spark.load_model("spark-model")
        # Prepare test documents, which are unlabeled (id, text) tuples.
        test = spark.createDataFrame(
            [(4, "spark i j k"), (5, "l m n"), (6, "spark hadoop spark"), (7, "apache hadoop")],
            ["id", "text"],
        )
        # Make predictions on test documents
        prediction = model.transform(test)
    '''

class _PyFuncModelWrapper:
    """
    Wrapper around Spark MLlib PipelineModel providing interface for scoring pandas DataFrame.
    """
    spark: Incomplete
    spark_model: Incomplete
    def __init__(self, spark, spark_model) -> None: ...
    def predict(self, pandas_df, params: Dict[str, Any] | None = None):
        """
        Generate predictions given input data in a pandas DataFrame.

        :param pandas_df: pandas DataFrame containing input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: List with model predictions.
        """

def autolog(disable: bool = False, silent: bool = False) -> None:
    '''
    Enables (or disables) and configures logging of Spark datasource paths, versions
    (if applicable), and formats when they are read. This method is not threadsafe and assumes a
    `SparkSession
    <https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.SparkSession>`_
    already exists with the
    `mlflow-spark JAR
    <http://mlflow.org/docs/latest/tracking.html#automatic-logging-from-spark-experimental>`_
    attached. It should be called on the Spark driver, not on the executors (i.e. do not call
    this method within a function parallelized by Spark). This API requires Spark 3.0 or above.

    Datasource information is cached in memory and logged to all subsequent MLflow runs,
    including the active MLflow run (if one exists when the data is read). Note that autologging of
    Spark ML (MLlib) models is not currently supported via this API. Datasource autologging is
    best-effort, meaning that if Spark is under heavy load or MLflow logging fails for any reason
    (e.g., if the MLflow server is unavailable), logging may be dropped.

    For any unexpected issues with autologging, check Spark driver and executor logs in addition
    to stderr & stdout generated from your MLflow code - datasource information is pulled from
    Spark, so logs relevant to debugging may show up amongst the Spark logs.

    .. code-block:: python
        :caption: Example

        import mlflow.spark
        import os
        import shutil
        from pyspark.sql import SparkSession

        # Create and persist some dummy data
        # Note: On environments like Databricks with pre-created SparkSessions,
        # ensure the org.mlflow:mlflow-spark:1.11.0 is attached as a library to
        # your cluster
        spark = (
            SparkSession.builder.config("spark.jars.packages", "org.mlflow:mlflow-spark:1.11.0")
            .master("local[*]")
            .getOrCreate()
        )
        df = spark.createDataFrame(
            [(4, "spark i j k"), (5, "l m n"), (6, "spark hadoop spark"), (7, "apache hadoop")],
            ["id", "text"],
        )
        import tempfile

        tempdir = tempfile.mkdtemp()
        df.write.csv(os.path.join(tempdir, "my-data-path"), header=True)
        # Enable Spark datasource autologging.
        mlflow.spark.autolog()
        loaded_df = spark.read.csv(
            os.path.join(tempdir, "my-data-path"), header=True, inferSchema=True
        )
        # Call toPandas() to trigger a read of the Spark datasource. Datasource info
        # (path and format) is logged to the current active run, or the
        # next-created MLflow run if no run is currently active
        with mlflow.start_run() as active_run:
            pandas_df = loaded_df.toPandas()

    :param disable: If ``True``, disables the Spark datasource autologging integration.
                    If ``False``, enables the Spark datasource autologging integration.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during Spark
                   datasource autologging. If ``False``, show all events and warnings during Spark
                   datasource autologging.
    '''

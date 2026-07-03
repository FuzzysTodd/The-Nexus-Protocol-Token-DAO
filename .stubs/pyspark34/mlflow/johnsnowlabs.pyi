from _typeshed import Incomplete
from mlflow import mleap as mleap, pyfunc as pyfunc
from mlflow.environment_variables import MLFLOW_DFS_TMP as MLFLOW_DFS_TMP
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.models.signature import ModelSignature as ModelSignature
from mlflow.models.utils import ModelInputExample as ModelInputExample
from mlflow.store.artifact.databricks_artifact_repo import DatabricksArtifactRepository as DatabricksArtifactRepository
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils import databricks_utils as databricks_utils
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import TempDir as TempDir, shutil_copytree_without_file_permissions as shutil_copytree_without_file_permissions, write_to as write_to
from mlflow.utils.uri import append_to_uri_path as append_to_uri_path, dbfs_hdfs_uri_to_fuse_path as dbfs_hdfs_uri_to_fuse_path, generate_tmp_dfs_path as generate_tmp_dfs_path, get_databricks_profile_uri_from_artifact_uri as get_databricks_profile_uri_from_artifact_uri, is_local_uri as is_local_uri, is_valid_dbfs_uri as is_valid_dbfs_uri
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
             :func:`save_model()` and :func:`log_model()`.
    """
def log_model(spark_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, dfs_tmpdir: Incomplete | None = None, sample_input: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, store_license: bool = False):
    '''
    Log a ``Johnsnowlabs NLUPipeline`` created via `nlp.load()
    <https://nlp.johnsnowlabs.com/docs/en/jsl/load_api>`_, as an MLflow artifact for the current
    run. This uses the MLlib persistence format and produces an MLflow Model with the
    ``johnsnowlabs`` flavor.

    Note: If no run is active, it will instantiate a run to obtain a run_id.

    :param spark_model: NLUPipeline obtained via `nlp.load()
                        <https://nlp.johnsnowlabs.com/docs/en/jsl/load_api>`_
    :param store_license: If True, the license will be stored with the model and used and re-loading
                          it.
    :param artifact_path: Run relative artifact path.
    :param conda_env: Either a dictionary representation of a Conda environment or the path to a
                      Conda environment yaml file. If provided, this describes the environment
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
                                \'johnsnowlabs\'
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

    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models.signature import infer_signature

                        train = df.drop_column("target_label")
                        predictions = ...  # compute model predictions
                        signature = infer_signature(train, predictions)
    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.
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

        import os
        import json
        import pandas as pd
        import mlflow
        from johnsnowlabs import nlp

        # Write your raw license.json string into the \'JOHNSNOWLABS_LICENSE_JSON\' env variable
        creds = {
            "AWS_ACCESS_KEY_ID": "...",
            "AWS_SECRET_ACCESS_KEY": "...",
            "SPARK_NLP_LICENSE": "...",
            "SECRET": "...",
        }
        os.environ["JOHNSNOWLABS_LICENSE_JSON"] = json.dumps(creds)

        # Download & Install Jars/Wheels if missing and Start a spark Session
        nlp.start()

        # For more details on trainable models and parameterization like embedding choice see
        # https://nlp.johnsnowlabs.com/docs/en/jsl/training
        trainable_classifier = nlp.load("train.classifier")

        # Create a sample training dataset
        data = pd.DataFrame(
            {"text": ["I hate covid ", "I love covid"], "y": ["negative", "positive"]}
        )

        # Fit and get a trained classifier
        trained_classifier = trainable_classifier.fit(data)
        trained_classifier.predict("He hates covid")

        # Log it
        mlflow.johnsnowlabs.log_model(trained_classifier, "my_trained_model")
    '''
def save_model(spark_model, path, mlflow_model: Incomplete | None = None, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, dfs_tmpdir: Incomplete | None = None, sample_input: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, store_license: bool = False):
    '''
    Save a Spark johnsnowlabs Model to a local path.

    By default, this function saves models using the Spark MLlib persistence mechanism.
    Additionally, if a sample input is specified using the ``sample_input`` parameter, the model
    is also serialized in MLeap format and the MLeap flavor is added.

    :param store_license: If True, the license will be stored with the model and used and
                          re-loading it.
    :param spark_model: Either a pyspark.ml.pipeline.PipelineModel or nlu.NLUPipeline object to be
                        saved. `Every johnsnowlabs model <https://nlp.johnsnowlabs.com/models>`_
                        is a PipelineModel and loadable as nlu.NLUPipeline.
    :param path: Local path where the model is to be saved.
    :param mlflow_model: MLflow model config this flavor is being added to.
    :param conda_env: Either a dictionary representation of a Conda environment or the path to a
                      Conda environment yaml file. If provided, this describes the environment
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
                                \'johnsnowlabs\'
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

    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models.signature import infer_signature

                        train = df.drop_column("target_label")
                        predictions = ...  # compute model predictions
                        signature = infer_signature(train, predictions)
    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    .. code-block:: python
        :caption: Example

        from johnsnowlabs import nlp
        import mlflow
        import os

        # Write your raw license.json string into the \'JOHNSNOWLABS_LICENSE_JSON\' env variable
        creds = {
            "AWS_ACCESS_KEY_ID": "...",
            "AWS_SECRET_ACCESS_KEY": "...",
            "SPARK_NLP_LICENSE": "...",
            "SECRET": "...",
        }
        os.environ["JOHNSNOWLABS_LICENSE_JSON"] = json.dumps(creds)

        # Download & Install Jars/Wheels if missing and Start a spark Session
        nlp.start()

        # load a model
        model = nlp.load("en.classify.bert_sequence.covid_sentiment")
        model.predict(["I hate covid", "I love covid"])

        # Save model as pyfunc and johnsnowlabs format
        mlflow.johnsnowlabs.save_model(model, "saved_model")
        model = mlflow.johnsnowlabs.load_model("saved_model")
        # Predict with reloaded model,
        # supports datatypes defined in https://nlp.johnsnowlabs.com/docs/en/jsl/predict_api#supported-data-types
        model.predict(["I hate covid", "I love covid"])
    '''
def load_model(model_uri, dfs_tmpdir: Incomplete | None = None, dst_path: Incomplete | None = None, **kwargs):
    '''
    Load the Johnsnowlabs MlFlow model from the path.

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
    :return: `nlu.NLUPipeline <https://nlp.johnsnowlabs.com/docs/en/jsl/predict_api>`_

    .. code-block:: python
        :caption: Example

        import mlflow
        from johnsnowlabs import nlp
        import os

        # Write your raw license.json string into the \'JOHNSNOWLABS_LICENSE_JSON\' env variable
        creds = {
            "AWS_ACCESS_KEY_ID": "...",
            "AWS_SECRET_ACCESS_KEY": "...",
            "SPARK_NLP_LICENSE": "...",
            "SECRET": "...",
        }
        os.environ["JOHNSNOWLABS_LICENSE_JSON"] = json.dumps(creds)

        # start a spark session
        nlp.start()
        # Load you MlFlow Model
        model = mlflow.johnsnowlabs.load_model("johnsnowlabs_model")

        # Make predictions on test documents
        # supports datatypes defined in https://nlp.johnsnowlabs.com/docs/en/jsl/predict_api#supported-data-types
        prediction = model.transform(["I love Covid", "I hate Covid"])
    '''

class _PyFuncModelWrapper:
    """
    Wrapper around NLUPipeline providing interface for scoring pandas DataFrame.
    """
    spark: Incomplete
    spark_model: Incomplete
    def __init__(self, spark_model, spark: Incomplete | None = None) -> None: ...
    def predict(self, text, params: Dict[str, Any] | None = None):
        """
        Generate predictions given input data in a pandas DataFrame.

        :param text: pandas DataFrame containing input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.
        :return: List with model predictions.
        """

import pandas as pd
from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.environment_variables import MLFLOW_DFS_TMP as MLFLOW_DFS_TMP
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import shutil_copytree_without_file_permissions as shutil_copytree_without_file_permissions, write_to as write_to
from mlflow.utils.uri import dbfs_hdfs_uri_to_fuse_path as dbfs_hdfs_uri_to_fuse_path, generate_tmp_dfs_path as generate_tmp_dfs_path
from typing import Any, Dict

FLAVOR_NAME: str

def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced with the ``Diviner``
             flavor. Calls to :py:func:`save_model()` and :py:func:`log_model()` produce a pip
             environment that, at a minimum, contains these requirements.
    """
def get_default_conda_env():
    """
    :return: The default Conda environment for MLflow Models produced with the ``Diviner`` flavor
             that is produced by calls to :py:func:`save_model()` and :py:func:`log_model()`.
    """
def save_model(diviner_model, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Save a ``Diviner`` model object to a path on the local file system.

    :param diviner_model: ``Diviner`` model that has been ``fit`` on a grouped temporal
                          ``DataFrame``.
    :param path: Local path destination for the serialized model is to be saved.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: :py:mod:`mlflow.models.Model` the flavor that this model is being added to.
    :param signature: :py:class:`Model Signature <mlflow.models.ModelSignature>` describes model
                      input and output :py:class:`Schema <mlflow.types.Schema>`. The model
                      signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        model = diviner.GroupedProphet().fit(data, ("region", "state"))
                        predictions = model.predict(prediction_config)
                        signature = infer_signature(data, predictions)

    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a ``Pandas DataFrame`` and
                          then serialized to json using the ``Pandas`` split-oriented format.
                          Bytes are base64-encoded.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    :param kwargs: Optional configurations for Spark DataFrame storage iff the model has
                   been fit in Spark.

                   Current supported options:

                   - `partition_by` for setting a (or several) partition columns as a list of                    column names. Must be a list of strings of grouping key column(s).
                   - `partition_count` for setting the number of part files to write from a                    repartition per `partition_by` group. The default part file count is 200.
                   - `dfs_tmpdir` for specifying the DFS temporary location where the model will                    be stored while copying from a local file system to a Spark-supported "dbfs:/"                    scheme.
    '''
def load_model(model_uri, dst_path: Incomplete | None = None, **kwargs):
    '''
    Load a ``Diviner`` object from a local file or a run.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``mlflow-artifacts:/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/tracking.html#
                      artifact-locations>`_.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist if provided. If unspecified, a local output
                     path will be created.
    :param kwargs: Optional configuration options for loading of a Diviner model. For models
                   that have been fit and saved using Spark, if a specific DFS temporary directory
                   is desired for loading of Diviner models, use the keyword argument
                   `"dfs_tmpdir"` to define the loading temporary path for the model during loading.

    :return: A ``Diviner`` model instance
    '''
def log_model(diviner_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Log a ``Diviner`` object as an MLflow artifact for the current run.

    :param diviner_model: ``Diviner`` model that has been ``fit`` on a grouped temporal
                          ``DataFrame``.
    :param artifact_path: Run-relative artifact path to save the model instance to.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param registered_model_name: This argument may change or be removed in a
                                  future release without warning. If given, create a model
                                  version under ``registered_model_name``, also creating a
                                  registered model if one with the given name does not exist.
    :param signature: :py:class:`Model Signature <mlflow.models.ModelSignature>` describes model
                      input and output :py:class:`Schema <mlflow.types.Schema>`. The model
                      signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        auto_arima_obj = AutoARIMA(out_of_sample_size=60, maxiter=100)
                        base_auto_arima = GroupedPmdarima(model_template=auto_arima_obj).fit(
                            df=training_data,
                            group_key_columns=("region", "state"),
                            y_col="y",
                            datetime_col="ds",
                            silence_warnings=True,
                        )
                        predictions = model.predict(n_periods=30, alpha=0.05, return_conf_int=True)
                        signature = infer_signature(data, predictions)

    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a ``Pandas DataFrame`` and
                          then serialized to json using the ``Pandas`` split-oriented format.
                          Bytes are base64-encoded.
    :param await_registration_for: Number of seconds to wait for the model version
                                   to finish being created and is in ``READY`` status.
                                   By default, the function waits for five minutes.
                                   Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param kwargs: Additional arguments for :py:class:`mlflow.models.model.Model`
                   Additionally, for models that have been fit in Spark, the following supported
                   configuration options are available to set.
                   Current supported options:

                   - `partition_by` for setting a (or several) partition columns as a list of                    column names. Must be a list of strings of grouping key column(s).
                   - `partition_count` for setting the number of part files to write from a                    repartition per `partition_by` group. The default part file count is 200.
                   - `dfs_tmpdir` for specifying the DFS temporary location where the model will                    be stored while copying from a local file system to a Spark-supported "dbfs:/"                    scheme.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.
    '''

class _DivinerModelWrapper:
    diviner_model: Incomplete
    def __init__(self, diviner_model) -> None: ...
    def predict(self, dataframe, params: Dict[str, Any] | None = None) -> pd.DataFrame:
        '''
        A method that allows a pyfunc implementation of this flavor to generate forecasted values
        from the end of a trained Diviner model\'s training series per group.

        The implementation here encapsulates a config-based switch of method calling. In short:
          *  If the ``DataFrame`` supplied to this method contains a column ``groups`` whose
             first row of data is of type List[tuple[str]] (containing the series-identifying
             group keys that were generated to identify a single underlying model during training),
             the caller will resolve to the method ``predict_groups()`` in each of the underlying
             wrapped libraries (i.e., ``GroupedProphet.predict_groups()``).
          *  If the ``DataFrame`` supplied does not contain the column name ``groups``, then the
             specific forecasting method that is primitive-driven (for ``GroupedProphet``, the
             ``predict()`` method mirrors that of ``Prophet``\'s, requiring a ``DataFrame``
             submitted with explicit datetime values per group which is not a tenable
             implementation for pyfunc or RESTful serving) is utilized. For ``GroupedProphet``,
             this is the ``.forecast()`` method, while for ``GroupedPmdarima``, this is the
             ``.predict()`` method.

        :param dataframe: A ``pandas.DataFrame`` that contains the required configuration for the
                          appropriate ``Diviner`` type.

                          For example, for ``GroupedProphet.forecast()``:

                          - horizon : int
                          - frequency: str

                          predict_conf = pd.DataFrame({"horizon": 30, "frequency": "D"}, index=[0])
                          forecast = pyfunc.load_pyfunc(model_uri=model_path).predict(predict_conf)

                          Will generate 30 days of forecasted values for each group that the model
                          was trained on.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: A Pandas DataFrame containing the forecasted values for each group key that was
                 either trained or declared as a subset with a ``groups`` entry in the ``dataframe``
                 configuration argument.
        '''

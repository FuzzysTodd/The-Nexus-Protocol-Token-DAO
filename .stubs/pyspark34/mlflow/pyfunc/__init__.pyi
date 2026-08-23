from _typeshed import Incomplete
from mlflow.environment_variables import MLFLOW_OPENAI_RETRIES_ENABLED as MLFLOW_OPENAI_RETRIES_ENABLED, MLFLOW_SCORING_SERVER_REQUEST_TIMEOUT as MLFLOW_SCORING_SERVER_REQUEST_TIMEOUT
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.flavor_backend_registry import get_flavor_backend as get_flavor_backend
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.models.utils import PyFuncInput as PyFuncInput, PyFuncOutput as PyFuncOutput
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.pyfunc.model import PythonModel as PythonModel, PythonModelContext as PythonModelContext, get_default_conda_env as get_default_conda_env, get_default_pip_requirements as get_default_pip_requirements
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils import PYTHON_VERSION as PYTHON_VERSION, check_port_connectivity as check_port_connectivity, find_free_port as find_free_port, get_major_minor_py_version as get_major_minor_py_version
from mlflow.utils.annotations import deprecated as deprecated, experimental as experimental
from mlflow.utils.databricks_utils import is_in_databricks_runtime as is_in_databricks_runtime
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import get_or_create_nfs_tmp_dir as get_or_create_nfs_tmp_dir, get_or_create_tmp_dir as get_or_create_tmp_dir, write_to as write_to
from mlflow.utils.nfs_on_spark import get_nfs_cache_root_dir as get_nfs_cache_root_dir
from typing import Any, Dict

FLAVOR_NAME: str
MAIN: str
CODE: str
DATA: str
ENV: str

class EnvType:
    CONDA: str
    VIRTUALENV: str
    def __init__(self) -> None: ...

PY_VERSION: str

def add_to_model(model, loader_module, data: Incomplete | None = None, code: Incomplete | None = None, conda_env: Incomplete | None = None, python_env: Incomplete | None = None, **kwargs):
    """
    Add a ``pyfunc`` spec to the model configuration.

    Defines ``pyfunc`` configuration schema. Caller can use this to create a valid ``pyfunc`` model
    flavor out of an existing directory structure. For example, other model flavors can use this to
    specify how to use their output as a ``pyfunc``.

    NOTE:

        All paths are relative to the exported model root directory.

    :param model: Existing model.
    :param loader_module: The module to be used to load the model.
    :param data: Path to the model data.
    :param code: Path to the code dependencies.
    :param conda_env: Conda environment.
    :param python_env: Python environment.
    :param req: pip requirements file.
    :param kwargs: Additional key-value pairs to include in the ``pyfunc`` flavor specification.
                   Values must be YAML-serializable.
    :return: Updated model configuration.
    """

class PyFuncModel:
    """
    MLflow 'python function' model.

    Wrapper around model implementation and metadata. This class is not meant to be constructed
    directly. Instead, instances of this class are constructed and returned from
    :py:func:`load_model() <mlflow.pyfunc.load_model>`.

    ``model_impl`` can be any Python object that implements the `Pyfunc interface
    <https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#pyfunc-inference-api>`_, and is
    returned by invoking the model's ``loader_module``.

    ``model_meta`` contains model metadata loaded from the MLmodel file.
    """
    def __init__(self, model_meta: Model, model_impl: Any, predict_fn: str = 'predict') -> None: ...
    def predict(self, data: PyFuncInput, params: Dict[str, Any] | None = None) -> PyFuncOutput:
        '''
        Generate model predictions.

        If the model contains signature, enforce the input schema first before calling the model
        implementation with the sanitized input. If the pyfunc model does not include model schema,
        the input is passed to the model implementation as is. See `Model Signature Enforcement
        <https://www.mlflow.org/docs/latest/models.html#signature-enforcement>`_ for more details."

        :param data: Model input as one of pandas.DataFrame, numpy.ndarray,
                     scipy.sparse.(csc.csc_matrix | csr.csr_matrix), List[Any], or
                     Dict[str, numpy.ndarray].
                     For model signatures with tensor spec inputs
                     (e.g. the Tensorflow core / Keras model), the input data type must be one of
                     `numpy.ndarray`, `List[numpy.ndarray]`, `Dict[str, numpy.ndarray]` or
                     `pandas.DataFrame`. If data is of `pandas.DataFrame` type and the model
                     contains a signature with tensor spec inputs, the corresponding column values
                     in the pandas DataFrame will be reshaped to the required shape with \'C\' order
                     (i.e. read / write the elements using C-like index order), and DataFrame
                     column values will be cast as the required tensor spec type.

        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions as one of pandas.DataFrame, pandas.Series, numpy.ndarray or list.
        '''
    def unwrap_python_model(self):
        '''
        Unwrap the underlying Python model object.

        This method is useful for accessing custom model functions, while still being able to
        leverage the MLflow designed workflow through the `predict()` method.

        :return: The underlying wrapped model object

        .. test-code-block:: python
            :caption: Example

            import mlflow


            # define a custom model
            class MyModel(mlflow.pyfunc.PythonModel):
                def predict(self, context, model_input, params=None):
                    return self.my_custom_function(model_input, params)

                def my_custom_function(self, model_input, params=None):
                    # do something with the model input
                    return 0


            some_input = 1
            # save the model
            my_model = MyModel()
            with mlflow.start_run():
                model_info = mlflow.pyfunc.log_model(artifact_path="model", python_model=my_model)

            # load the model
            loaded_model = mlflow.pyfunc.load_model(model_uri=model_info.model_uri)
            print(type(loaded_model))  # <class \'mlflow.pyfunc.model.PyFuncModel\'>

            unwrapped_model = loaded_model.unwrap_python_model()
            print(type(unwrapped_model))  # <class \'__main__.MyModel\'>

            # does not work, only predict() is exposed
            # print(loaded_model.my_custom_function(some_input))

            print(unwrapped_model.my_custom_function(some_input))  # works

            print(loaded_model.predict(some_input))  # works

            # works, but None is needed for context arg
            print(unwrapped_model.predict(None, some_input))

        '''
    def __eq__(self, other): ...
    @property
    def metadata(self):
        """Model metadata."""

def load_model(model_uri: str, suppress_warnings: bool = False, dst_path: str = None) -> PyFuncModel:
    """
    Load a model stored in Python function format.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``
                      - ``mlflow-artifacts:/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.
    :param suppress_warnings: If ``True``, non-fatal warning messages associated with the model
                              loading process will be suppressed. If ``False``, these warning
                              messages will be emitted.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.
    """

class _ServedPyFuncModel(PyFuncModel):
    def __init__(self, model_meta: Model, client: Any, server_pid: int) -> None: ...
    def predict(self, data, params: Incomplete | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """
    @property
    def pid(self): ...

def get_model_dependencies(model_uri, format: str = 'pip'):
    '''
    :param model_uri: The uri of the model to get dependencies from.
    :param format: The format of the returned dependency file. If the ``"pip"`` format is
                   specified, the path to a pip ``requirements.txt`` file is returned.
                   If the ``"conda"`` format is specified, the path to a ``"conda.yaml"``
                   file is returned . If the ``"pip"`` format is specified but the model
                   was not saved with a ``requirements.txt`` file, the ``pip`` section
                   of the model\'s ``conda.yaml`` file is extracted instead, and any
                   additional conda dependencies are ignored. Default value is ``"pip"``.
    :return: The local filesystem path to either a pip ``requirements.txt`` file
             (if ``format="pip"``) or a ``conda.yaml`` file (if ``format="conda"``)
             specifying the model\'s dependencies.
    '''
def load_pyfunc(model_uri, suppress_warnings: bool = False):
    """
    Load a model stored in Python function format.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``
                      - ``mlflow-artifacts:/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.

    :param suppress_warnings: If ``True``, non-fatal warning messages associated with the model
                              loading process will be suppressed. If ``False``, these warning
                              messages will be emitted.
    """
def spark_udf(spark, model_uri, result_type: Incomplete | None = None, env_manager=..., params: Dict[str, Any] | None = None):
    '''
    A Spark UDF that can be used to invoke the Python function formatted model.

    Parameters passed to the UDF are forwarded to the model as a DataFrame where the column names
    are ordinals (0, 1, ...). On some versions of Spark (3.0 and above), it is also possible to
    wrap the input in a struct. In that case, the data will be passed as a DataFrame with column
    names given by the struct definition (e.g. when invoked as my_udf(struct(\'x\', \'y\')), the model
    will get the data as a pandas DataFrame with 2 columns \'x\' and \'y\').

    If a model contains a signature with tensor spec inputs, you will need to pass a column of
    array type as a corresponding UDF argument. The column values of which must be one dimensional
    arrays. The UDF will reshape the column values to the required shape with \'C\' order
    (i.e. read / write the elements using C-like index order) and cast the values as the required
    tensor spec type.

    If a model contains a signature, the UDF can be called without specifying column name
    arguments. In this case, the UDF will be called with column names from signature, so the
    evaluation dataframe\'s column names must match the model signature\'s column names.

    The predictions are filtered to contain only the columns that can be represented as the
    ``result_type``. If the ``result_type`` is string or array of strings, all predictions are
    converted to string. If the result type is not an array type, the left most column with
    matching type is returned.

    NOTE: Inputs of type ``pyspark.sql.types.DateType`` are not supported on earlier versions of
    Spark (2.4 and below).

    .. code-block:: python
        :caption: Example

        from pyspark.sql.functions import struct

        predict = mlflow.pyfunc.spark_udf(spark, "/my/local/model")
        df.withColumn("prediction", predict(struct("name", "age"))).show()

    :param spark: A SparkSession object.
    :param model_uri: The location, in URI format, of the MLflow model with the
                      :py:mod:`mlflow.pyfunc` flavor. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``
                      - ``mlflow-artifacts:/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.

    :param result_type: the return type of the user-defined function. The value can be either a
        ``pyspark.sql.types.DataType`` object or a DDL-formatted type string. Only a primitive
        type, an array ``pyspark.sql.types.ArrayType`` of primitive type, or a struct type
        containing fields of above 2 kinds of types are allowed.
        If unspecified, it tries to infer result type from model signature
        output schema, if model output schema is not available, it fallbacks to use ``double``
        type.

        The following classes of result type are supported:

        - "int" or ``pyspark.sql.types.IntegerType``: The leftmost integer that can fit in an
          ``int32`` or an exception if there is none.

        - "long" or ``pyspark.sql.types.LongType``: The leftmost long integer that can fit in an
          ``int64`` or an exception if there is none.

        - ``ArrayType(IntegerType|LongType)``: All integer columns that can fit into the requested
          size.

        - "float" or ``pyspark.sql.types.FloatType``: The leftmost numeric result cast to
          ``float32`` or an exception if there is none.

        - "double" or ``pyspark.sql.types.DoubleType``: The leftmost numeric result cast to
          ``double`` or an exception if there is none.

        - ``ArrayType(FloatType|DoubleType)``: All numeric columns cast to the requested type or
          an exception if there are no numeric columns.

        - "string" or ``pyspark.sql.types.StringType``: The leftmost column converted to ``string``.

        - "boolean" or "bool" or ``pyspark.sql.types.BooleanType``: The leftmost column converted
          to ``bool`` or an exception if there is none.

        - ``ArrayType(StringType)``: All columns converted to ``string``.

        - "field1 FIELD1_TYPE, field2 FIELD2_TYPE, ...": A struct type containing multiple fields
          separated by comma, each field type must be one of types listed above.

    :param env_manager: The environment manager to use in order to create the python environment
                        for model inference. Note that environment is only restored in the context
                        of the PySpark UDF; the software environment outside of the UDF is
                        unaffected. Default value is ``local``, and the following values are
                        supported:

                         - ``virtualenv``: Use virtualenv to restore the python environment that
                           was used to train the model.
                         - ``conda``: (Recommended) Use Conda to restore the software environment
                           that was used to train the model.
                         - ``local``: Use the current Python environment for model inference, which
                           may differ from the environment used to train the model and may lead to
                           errors or invalid predictions.

    :param params: Additional parameters to pass to the model for inference.

                   .. Note:: Experimental: This parameter may change or be removed in a future
                                           release without warning.

    :return: Spark UDF that applies the model\'s ``predict`` method to the data and returns a
             type specified by ``result_type``, which by default is a double.
    '''
def save_model(path, loader_module: Incomplete | None = None, data_path: Incomplete | None = None, code_path: Incomplete | None = None, conda_env: Incomplete | None = None, mlflow_model: Incomplete | None = None, python_model: Incomplete | None = None, artifacts: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    save_model(path, loader_module=None, data_path=None, code_path=None, conda_env=None,               mlflow_model=Model(), python_model=None, artifacts=None)

    Save a Pyfunc model with custom inference logic and optional data dependencies to a path on the
    local filesystem.

    For information about the workflows that this method supports, please see :ref:`"workflows for
    creating custom pyfunc models" <pyfunc-create-custom-workflows>` and
    :ref:`"which workflow is right for my use case?" <pyfunc-create-custom-selecting-workflow>`.
    Note that the parameters for the second workflow: ``loader_module``, ``data_path`` and the
    parameters for the first workflow: ``python_model``, ``artifacts``, cannot be
    specified together.

    :param path: The path to which to save the Python model.
    :param loader_module: The name of the Python module that is used to load the model
                          from ``data_path``. This module must define a method with the prototype
                          ``_load_pyfunc(data_path)``. If not ``None``, this module and its
                          dependencies must be included in one of the following locations:

                          - The MLflow library.
                          - Package(s) listed in the model\'s Conda environment, specified by
                            the ``conda_env`` parameter.
                          - One or more of the files specified by the ``code_path`` parameter.

    :param data_path: Path to a file or directory containing model data.
    :param code_path: A list of local filesystem paths to Python file dependencies (or directories
                      containing file dependencies). These files are *prepended* to the system
                      path before the model is loaded.
    :param conda_env: {{ conda_env }}
    :param mlflow_model: :py:mod:`mlflow.models.Model` configuration to which to add the
                         **python_function** flavor.
    :param python_model:
        An instance of a subclass of :class:`~PythonModel` or a callable object with a single
        argument (see the examples below). The passed-in object is serialized using the CloudPickle
        library. Any dependencies of the class should be included in one of the following locations:

        - The MLflow library.
        - Package(s) listed in the model\'s Conda environment, specified by the ``conda_env``
          parameter.
        - One or more of the files specified by the ``code_path`` parameter.

        Note: If the class is imported from another module, as opposed to being defined in the
        ``__main__`` scope, the defining module should also be included in one of the listed
        locations.

        **Examples**

        Class model

        .. code-block:: python

            from typing import List, Dict
            import mlflow


            class MyModel(mlflow.pyfunc.PythonModel):
                def predict(self, context, model_input: List[str], params=None) -> List[str]:
                    return [i.upper() for i in model_input]


            mlflow.pyfunc.save_model("model", python_model=MyModel(), input_example=["a"])
            model = mlflow.pyfunc.load_model("model")
            print(model.predict(["a", "b", "c"]))  # -> ["A", "B", "C"]

        Functional model

        .. note::
            Experimental: Functional model support is experimental and may change or be removed in
            a future release without warning.

        .. code-block:: python

            from typing import List
            import mlflow


            def predict(model_input: List[str]) -> List[str]:
                return [i.upper() for i in model_input]


            mlflow.pyfunc.save_model("model", python_model=predict, input_example=["a"])
            model = mlflow.pyfunc.load_model("model")
            print(model.predict(["a", "b", "c"]))  # -> ["A", "B", "C"]

        If the `predict` method or function has type annotations, MLflow automatically constructs
        a model signature based on the type annotations (unless the ``signature`` argument is
        explicitly specified), and converts the input value to the specified type before passing
        it to the function. Currently, the following type annotations are supported:

            - ``List[str]``
            - ``List[Dict[str, str]]``

    :param artifacts: A dictionary containing ``<name, artifact_uri>`` entries. Remote artifact URIs
                      are resolved to absolute filesystem paths, producing a dictionary of
                      ``<name, absolute_path>`` entries. ``python_model`` can reference these
                      resolved entries as the ``artifacts`` property of the ``context`` parameter
                      in :func:`PythonModel.load_context() <mlflow.pyfunc.PythonModel.load_context>`
                      and :func:`PythonModel.predict() <mlflow.pyfunc.PythonModel.predict>`.
                      For example, consider the following ``artifacts`` dictionary::

                        {
                            "my_file": "s3://my-bucket/path/to/my/file"
                        }

                      In this case, the ``"my_file"`` artifact is downloaded from S3. The
                      ``python_model`` can then refer to ``"my_file"`` as an absolute filesystem
                      path via ``context.artifacts["my_file"]``.

                      If ``None``, no artifacts are added to the model.

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
                          model. The given example can be a Pandas DataFrame where the given
                          example will be serialized to json using the Pandas split-oriented
                          format, or a numpy array where the example will be serialized to json
                          by converting it to a list. Bytes are base64-encoded.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    '''
def log_model(artifact_path, loader_module: Incomplete | None = None, data_path: Incomplete | None = None, code_path: Incomplete | None = None, conda_env: Incomplete | None = None, python_model: Incomplete | None = None, artifacts: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Log a Pyfunc model with custom inference logic and optional data dependencies as an MLflow
    artifact for the current run.

    For information about the workflows that this method supports, see :ref:`Workflows for
    creating custom pyfunc models <pyfunc-create-custom-workflows>` and
    :ref:`Which workflow is right for my use case? <pyfunc-create-custom-selecting-workflow>`.
    You cannot specify the parameters for the second workflow: ``loader_module``, ``data_path``
    and the parameters for the first workflow: ``python_model``, ``artifacts`` together.

    :param artifact_path: The run-relative artifact path to which to log the Python model.
    :param loader_module: The name of the Python module that is used to load the model
                          from ``data_path``. This module must define a method with the prototype
                          ``_load_pyfunc(data_path)``. If not ``None``, this module and its
                          dependencies must be included in one of the following locations:

                          - The MLflow library.
                          - Package(s) listed in the model\'s Conda environment, specified by
                            the ``conda_env`` parameter.
                          - One or more of the files specified by the ``code_path`` parameter.

    :param data_path: Path to a file or directory containing model data.
    :param code_path: A list of local filesystem paths to Python file dependencies (or directories
                      containing file dependencies). These files are *prepended* to the system
                      path before the model is loaded.
    :param conda_env: {{ conda_env }}
    :param python_model:
        An instance of a subclass of :class:`~PythonModel` or a callable object with a single
        argument (see the examples below). The passed-in object is serialized using the CloudPickle
        library. Any dependencies of the class should be included in one of the following locations:

        - The MLflow library.
        - Package(s) listed in the model\'s Conda environment, specified by the ``conda_env``
          parameter.
        - One or more of the files specified by the ``code_path`` parameter.

        Note: If the class is imported from another module, as opposed to being defined in the
        ``__main__`` scope, the defining module should also be included in one of the listed
        locations.

        **Examples**

        Class model

        .. code-block:: python

            from typing import List, Dict
            import mlflow


            class MyModel(mlflow.pyfunc.PythonModel):
                def predict(self, context, model_input: List[str], params=None) -> List[str]:
                    return [i.upper() for i in model_input]


            mlflow.pyfunc.save_model("model", python_model=MyModel(), input_example=["a"])
            model = mlflow.pyfunc.load_model("model")
            print(model.predict(["a", "b", "c"]))  # -> ["A", "B", "C"]

        Functional model

        .. note::
            Experimental: Functional model support is experimental and may change or be removed in
            a future release without warning.

        .. code-block:: python

            from typing import List
            import mlflow


            def predict(model_input: List[str]) -> List[str]:
                return [i.upper() for i in model_input]


            mlflow.pyfunc.save_model("model", python_model=predict, input_example=["a"])
            model = mlflow.pyfunc.load_model("model")
            print(model.predict(["a", "b", "c"]))  # -> ["A", "B", "C"]

        If the `predict` method or function has type annotations, MLflow automatically constructs
        a model signature based on the type annotations (unless the ``signature`` argument is
        explicitly specified), and converts the input value to the specified type before passing
        it to the function. Currently, the following type annotations are supported:

            - ``List[str]``
            - ``List[Dict[str, str]]``

    :param artifacts: A dictionary containing ``<name, artifact_uri>`` entries. Remote artifact URIs
                      are resolved to absolute filesystem paths, producing a dictionary of
                      ``<name, absolute_path>`` entries. ``python_model`` can reference these
                      resolved entries as the ``artifacts`` property of the ``context`` parameter
                      in :func:`PythonModel.load_context() <mlflow.pyfunc.PythonModel.load_context>`
                      and :func:`PythonModel.predict() <mlflow.pyfunc.PythonModel.predict>`.
                      For example, consider the following ``artifacts`` dictionary::

                        {
                            "my_file": "s3://my-bucket/path/to/my/file"
                        }

                      In this case, the ``"my_file"`` artifact is downloaded from S3. The
                      ``python_model`` can then refer to ``"my_file"`` as an absolute filesystem
                      path via ``context.artifacts["my_file"]``.

                      If ``None``, no artifacts are added to the model.
    :param registered_model_name: This argument may change or be removed in a
                                  future release without warning. If given, create a model
                                  version under ``registered_model_name``, also creating a
                                  registered model if one with the given name does not exist.

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
                          model. The given example can be a Pandas DataFrame where the given
                          example will be serialized to json using the Pandas split-oriented
                          format, or a numpy array where the example will be serialized to json
                          by converting it to a list. Bytes are base64-encoded.
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
    '''

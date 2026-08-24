import numpy as np
import pandas as pd
from _typeshed import Incomplete
from mlflow.exceptions import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, MlflowException as MlflowException
from mlflow.models import Model as Model
from mlflow.store.artifact.utils.models import get_model_name_and_version as get_model_name_and_version
from mlflow.types import DataType as DataType, ParamSchema as ParamSchema, ParamSpec as ParamSpec, Schema as Schema, TensorSpec as TensorSpec
from mlflow.types.utils import TensorsNotSupportedException as TensorsNotSupportedException, clean_tensor_type as clean_tensor_type
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.proto_json_utils import NumpyEncoder as NumpyEncoder, dataframe_from_raw_json as dataframe_from_raw_json, parse_tf_serving_input as parse_tf_serving_input
from mlflow.utils.uri import get_databricks_profile_uri_from_artifact_uri as get_databricks_profile_uri_from_artifact_uri

HAS_SCIPY: bool
ModelInputExample: Incomplete
PyFuncInput: Incomplete
PyFuncOutput = pd.DataFrame | pd.Series | np.ndarray | list | str

class _Example:
    '''
    Represents an input example for MLflow model.

    Contains jsonable data that can be saved with the model and meta data about the exported format
    that can be saved with :py:class:`Model <mlflow.models.Model>`.

    The _Example is created from example data provided by user. The example(s) can be provided as
    pandas.DataFrame, numpy.ndarray, python dictionary or python list. The assumption is that the
    example contains jsonable elements (see storage format section below).

    NOTE: If the example is 1 dimensional (e.g. dictionary of str -> scalar, or a list of scalars),
    the assumption is that it is a single row of data (rather than a single column).

    Metadata:

    The _Example metadata contains the following information:
        - artifact_path: Relative path to the serialized example within the model directory.
        - type: Type of example data provided by the user. E.g. dataframe, ndarray.
        - One of the following metadata based on the `type`:
            - pandas_orient: For dataframes, this attribute specifies how is the dataframe encoded
                             in json. For example, "split" value signals that the data is stored as
                             object with columns and data attributes.
            - format: For tensors, this attribute specifies the standard being used to store an
                      input example. MLflow uses a JSON-formatted string representation of T
                      F serving input.

    Storage Format:

    The examples are stored as json for portability and readability. Therefore, the contents of the
    example(s) must be jsonable. Mlflow will make the following conversions automatically on behalf
    of the user:

        - binary values: :py:class:`bytes` or :py:class:`bytearray` are converted to base64
          encoded strings.
        - numpy types: Numpy types are converted to the corresponding python types or their closest
          equivalent.
        - csc/csr matrix: similar to 2 dims numpy array, csc/csr matrix are converted to
          corresponding python types or their closest equivalent.
    '''
    data: Incomplete
    info: Incomplete
    def __init__(self, input_example: ModelInputExample) -> None: ...
    def save(self, parent_dir_path: str):
        """Save the example as json at ``parent_dir_path``/`self.info['artifact_path']`."""
    @property
    def inference_data(self):
        """
        Returns the input example in a form that PyFunc wrapped models can score.
        """

def plot_lines(data_series, xlabel, ylabel, legend_loc: Incomplete | None = None, line_kwargs: Incomplete | None = None, title: Incomplete | None = None): ...
def validate_schema(data: PyFuncInput, expected_schema: Schema) -> None:
    """
    Validate that the input data has the expected schema.

    :param data: Input data to be validated. Supported types are:

                 - pandas.DataFrame
                 - pandas.Series
                 - numpy.ndarray
                 - scipy.sparse.csc_matrix
                 - scipy.sparse.csr_matrix
                 - List[Any]
                 - Dict[str, Any]
                 - str
    :param expected_schema: Expected :py:class:`Schema <mlflow.types.Schema>` of the input data.
    :raises: A :py:class:`mlflow.exceptions.MlflowException`. when the input data does
             not match the schema.

    .. code-block:: python
        :caption: Example usage of validate_schema

        import mlflow.models

        # Suppose you've already got a model_uri
        model_info = mlflow.models.get_model_info(model_uri)
        # Get model signature directly
        model_signature = model_info.signature
        # validate schema
        mlflow.models.validate_schema(input_data, model_signature.inputs)
    """
def add_libraries_to_model(model_uri, run_id: Incomplete | None = None, registered_model_name: Incomplete | None = None):
    '''
    Given a registered model_uri (e.g. models:/<model_name>/<model_version>), this utility
    re-logs the model along with all the required model libraries back to the Model Registry.
    The required model libraries are stored along with the model as model artifacts. In
    addition, supporting files to the model (e.g. conda.yaml, requirements.txt) are modified
    to use the added libraries.

    By default, this utility creates a new model version under the same registered model specified
    by ``model_uri``. This behavior can be overridden by specifying the ``registered_model_name``
    argument.

    :param model_uri: A registered model uri in the Model Registry of the form
                      models:/<model_name>/<model_version/stage/latest>
    :param run_id: The ID of the run to which the model with libraries is logged. If None, the model
                   with libraries is logged to the source run corresponding to model version
                   specified by ``model_uri``; if the model version does not have a source run, a
                   new run created.
    :param registered_model_name: The new model version (model with its libraries) is
                                  registered under the inputted registered_model_name. If None, a
                                  new version is logged to the existing model in the Model Registry.

    .. note::
        This utility only operates on a model that has been registered to the Model Registry.

    .. note::
        The libraries are only compatible with the platform on which they are added. Cross platform
        libraries are not supported.

    .. code-block:: python
        :caption: Example

        # Create and log a model to the Model Registry

        import pandas as pd
        from sklearn import datasets
        from sklearn.ensemble import RandomForestClassifier
        import mlflow
        import mlflow.sklearn
        from mlflow.models import infer_signature

        with mlflow.start_run():
            iris = datasets.load_iris()
            iris_train = pd.DataFrame(iris.data, columns=iris.feature_names)
            clf = RandomForestClassifier(max_depth=7, random_state=0)
            clf.fit(iris_train, iris.target)
            signature = infer_signature(iris_train, clf.predict(iris_train))
            mlflow.sklearn.log_model(
                clf, "iris_rf", signature=signature, registered_model_name="model-with-libs"
            )

        # model uri for the above model
        model_uri = "models:/model-with-libs/1"

        # Import utility
        from mlflow.models.utils import add_libraries_to_model

        # Log libraries to the original run of the model
        add_libraries_to_model(model_uri)

        # Log libraries to some run_id
        existing_run_id = "21df94e6bdef4631a9d9cb56f211767f"
        add_libraries_to_model(model_uri, run_id=existing_run_id)

        # Log libraries to a new run
        with mlflow.start_run():
            add_libraries_to_model(model_uri)

        # Log libraries to a new registered model named \'new-model\'
        with mlflow.start_run():
            add_libraries_to_model(model_uri, registered_model_name="new-model")
    '''
def get_model_version_from_model_uri(model_uri):
    """
    Helper function to fetch a model version from a model uri of the form
    models:/<model_name>/<model_version/stage/latest>.
    """

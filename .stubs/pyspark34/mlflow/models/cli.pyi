from _typeshed import Incomplete
from mlflow.models.flavor_backend_registry import get_flavor_backend as get_flavor_backend
from mlflow.utils import cli_args as cli_args

def commands() -> None:
    """
    Deploy MLflow models locally.

    To deploy a model associated with a run on a tracking server, set the MLFLOW_TRACKING_URI
    environment variable to the URL of the desired server.
    """
def serve(model_uri, port, host, timeout, workers, env_manager: Incomplete | None = None, no_conda: bool = False, install_mlflow: bool = False, enable_mlserver: bool = False):
    '''
    Serve a model saved with MLflow by launching a webserver on the specified host and port.
    The command supports models with the ``python_function`` or ``crate`` (R Function) flavor.
    For information about the input data formats accepted by the webserver, see the following
    documentation: https://www.mlflow.org/docs/latest/models.html#built-in-deployment-tools.

    .. warning::

        Models built using MLflow 1.x will require adjustments to the endpoint request payload
        if executed in an environment that has MLflow 2.x installed. In 1.x, a request payload
        was in the format: ``{\'columns\': [str], \'data\': [[...]]}``. 2.x models require
        payloads that are defined by the structural-defining keys of either ``dataframe_split``,
        ``instances``, ``inputs`` or ``dataframe_records``. See the examples below for
        demonstrations of the changes to the invocation API endpoint in 2.0.

    .. note::

        Requests made in pandas DataFrame structures can be made in either `split` or `records`
        oriented formats.
        See https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html for
        detailed information on orientation formats for converting a pandas DataFrame to json.

    Example:

    .. code-block:: bash

        $ mlflow models serve -m runs:/my-run-id/model-path &

        # records orientation input format for serializing a pandas DataFrame
        $ curl http://127.0.0.1:5000/invocations -H \'Content-Type: application/json\' -d \'{
            "dataframe_records": [{"a":1, "b":2}, {"a":3, "b":4}, {"a":5, "b":6}]
        }\'

        # split orientation input format for serializing a pandas DataFrame
        $ curl http://127.0.0.1:5000/invocations -H \'Content-Type: application/json\' -d \'{
            "dataframe_split": {"columns": ["a", "b"],
                                "index": [0, 1, 2],
                                "data": [[1, 2], [3, 4], [5, 6]]}
        }\'

        # inputs format for List submission of array, tensor, or DataFrame data
        $ curl http://127.0.0.1:5000/invocations -H \'Content-Type: application/json\' -d \'{
            "inputs": [[1, 2], [3, 4], [5, 6]]
        }\'

        # instances format for submission of Tensor data
        curl http://127.0.0.1:5000/invocations -H \'Content-Type: application/json\' -d \'{
            "instances": [
                {"a": "t1", "b": [1, 2, 3]},
                {"a": "t2", "b": [4, 5, 6]},
                {"a": "t3", "b": [7, 8, 9]}
            ]
        }\'

    '''
def predict(model_uri, input_path, output_path, content_type, env_manager, install_mlflow):
    """
    Generate predictions in json format using a saved MLflow model. For information about the input
    data formats accepted by this function, see the following documentation:
    https://www.mlflow.org/docs/latest/models.html#built-in-deployment-tools.
    """
def prepare_env(model_uri, env_manager, install_mlflow):
    """
    Performs any preparation necessary to predict or serve the model, for example
    downloading dependencies or initializing a conda environment. After preparation,
    calling predict or serve should be fast.
    """
def generate_dockerfile(model_uri, output_directory, env_manager, mlflow_home, install_mlflow, enable_mlserver) -> None:
    """
    Generates a directory with Dockerfile whose default entrypoint serves an MLflow model at port
    8080 using the python_function flavor. The generated Dockerfile is written to the specified
    output directory, along with the model (if specified). This Dockerfile defines an image that
    is equivalent to the one produced by ``mlflow models build-docker``.
    """
def build_docker(model_uri, name, env_manager, mlflow_home, install_mlflow, enable_mlserver) -> None:
    '''
    Builds a Docker image whose default entrypoint serves an MLflow model at port 8080, using the
    python_function flavor. The container serves the model referenced by ``--model-uri``, if
    specified when ``build-docker`` is called. If ``--model-uri`` is not specified when build_docker
    is called, an MLflow Model directory must be mounted as a volume into the /opt/ml/model
    directory in the container.

    Building a Docker image with ``--model-uri``:

    .. code:: bash

        # Build a Docker image named \'my-image-name\' that serves the model from run \'some-run-uuid\'
        # at run-relative artifact path \'my-model\'
        mlflow models build-docker --model-uri "runs:/some-run-uuid/my-model" --name "my-image-name"
        # Serve the model
        docker run -p 5001:8080 "my-image-name"

    Building a Docker image without ``--model-uri``:

    .. code:: bash

        # Build a generic Docker image named \'my-image-name\'
        mlflow models build-docker --name "my-image-name"
        # Mount the model stored in \'/local/path/to/artifacts/model\' and serve it
        docker run --rm -p 5001:8080 -v /local/path/to/artifacts/model:/opt/ml/model "my-image-name"

    .. warning::

        The image built without ``--model-uri`` doesn\'t support serving models with RFunc / Java
        MLeap model server.

    NB: by default, the container will start nginx and gunicorn processes. If you don\'t need the
    nginx process to be started (for instance if you deploy your container to Google Cloud Run),
    you can disable it via the DISABLE_NGINX environment variable:

    .. code:: bash

        docker run -p 5001:8080 -e DISABLE_NGINX=true "my-image-name"

    See https://www.mlflow.org/docs/latest/python_api/mlflow.pyfunc.html for more information on the
    \'python_function\' flavor.
    '''

from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils import PYTHON_VERSION as PYTHON_VERSION
from mlflow.version import VERSION as VERSION

class _PythonEnv:
    BUILD_PACKAGES: Incomplete
    python: Incomplete
    build_dependencies: Incomplete
    dependencies: Incomplete
    def __init__(self, python: Incomplete | None = None, build_dependencies: Incomplete | None = None, dependencies: Incomplete | None = None) -> None:
        """
        Represents environment information for MLflow Models and Projects.

        :param python: Python version for the environment. If unspecified, defaults to the current
                       Python version.
        :param build_dependencies: List of build dependencies for the environment that must
                                   be installed before installing ``dependencies``. If unspecified,
                                   defaults to an empty list.
        :param dependencies: List of dependencies for the environment. If unspecified, defaults to
                             an empty list.
        """
    @classmethod
    def current(cls): ...
    @staticmethod
    def get_current_build_dependencies(): ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, dct): ...
    def to_yaml(self, path) -> None: ...
    @classmethod
    def from_yaml(cls, path): ...
    @staticmethod
    def get_dependencies_from_conda_yaml(path): ...
    @classmethod
    def from_conda_yaml(cls, path): ...

def infer_pip_requirements(model_uri, flavor, fallback: Incomplete | None = None):
    '''
    Infers the pip requirements of the specified model by creating a subprocess and loading
    the model in it to determine which packages are imported.

    :param model_uri: The URI of the model.
    :param flavor: The flavor name of the model.
    :param fallback: If provided, an unexpected error during the inference procedure is swallowed
                     and the value of ``fallback`` is returned. Otherwise, the error is raised.
    :return: A list of inferred pip requirements (e.g. ``["scikit-learn==0.24.2", ...]``).
    '''

class Environment:
    def __init__(self, activate_cmd, extra_env: Incomplete | None = None) -> None: ...
    def get_activate_command(self): ...
    def execute(self, command, command_env: Incomplete | None = None, preexec_fn: Incomplete | None = None, capture_output: bool = False, stdout: Incomplete | None = None, stderr: Incomplete | None = None, stdin: Incomplete | None = None, synchronous: bool = True): ...

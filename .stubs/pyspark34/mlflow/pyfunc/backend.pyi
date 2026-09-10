from _typeshed import Incomplete
from mlflow.models import FlavorBackend as FlavorBackend
from mlflow.models.container import ENABLE_MLSERVER as ENABLE_MLSERVER
from mlflow.models.docker_utils import DISABLE_ENV_CREATION as DISABLE_ENV_CREATION, SETUP_MINICONDA as SETUP_MINICONDA, SETUP_PYENV_AND_VIRTUALENV as SETUP_PYENV_AND_VIRTUALENV
from mlflow.pyfunc import ENV as ENV, mlserver as mlserver, scoring_server as scoring_server
from mlflow.utils.conda import get_conda_bin_executable as get_conda_bin_executable, get_or_create_conda_env as get_or_create_conda_env
from mlflow.utils.environment import Environment as Environment
from mlflow.utils.file_utils import get_or_create_nfs_tmp_dir as get_or_create_nfs_tmp_dir, get_or_create_tmp_dir as get_or_create_tmp_dir, path_to_local_file_uri as path_to_local_file_uri
from mlflow.utils.nfs_on_spark import get_nfs_cache_root_dir as get_nfs_cache_root_dir
from mlflow.utils.process import cache_return_value_per_process as cache_return_value_per_process
from mlflow.version import VERSION as VERSION

class PyFuncBackend(FlavorBackend):
    """
    Flavor backend implementation for the generic python models.
    """
    def __init__(self, config, workers: int = 1, env_manager=..., install_mlflow: bool = False, create_env_root_dir: bool = False, env_root_dir: Incomplete | None = None, **kwargs) -> None:
        '''
        :param env_root_dir: Root path for conda env. If None, use Conda\'s default environments
                             directory. Note if this is set, conda package cache path becomes
                             "{env_root_dir}/conda_cache_pkgs" instead of the global package cache
                             path, and pip package cache path becomes
                             "{env_root_dir}/pip_cache_pkgs" instead of the global package cache
                             path.
        '''
    def prepare_env(self, model_uri, capture_output: bool = False): ...
    def predict(self, model_uri, input_path, output_path, content_type):
        """
        Generate predictions using generic python model saved with MLflow. The expected format of
        the input JSON is the Mlflow scoring format.
        Return the prediction results as a JSON.
        """
    def serve(self, model_uri, port, host, timeout, enable_mlserver, synchronous: bool = True, stdout: Incomplete | None = None, stderr: Incomplete | None = None):
        """
        Serve pyfunc model locally.
        """
    def serve_stdin(self, model_uri, stdout: Incomplete | None = None, stderr: Incomplete | None = None): ...
    def can_score_model(self): ...
    def generate_dockerfile(self, model_uri, output_path: str = 'mlflow-dockerfile', install_mlflow: bool = False, mlflow_home: Incomplete | None = None, enable_mlserver: bool = False) -> None: ...
    def build_image(self, model_uri, image_name, install_mlflow: bool = False, mlflow_home: Incomplete | None = None, enable_mlserver: bool = False) -> None: ...
    def copy_model_into_container_wrapper(self, model_uri, install_mlflow, enable_mlserver): ...

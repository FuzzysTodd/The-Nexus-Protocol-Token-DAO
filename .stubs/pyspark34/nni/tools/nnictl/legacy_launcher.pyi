from .command_utils import check_output_command as check_output_command, kill_command as kill_command
from .common_utils import detect_port as detect_port, get_json_content as get_json_content, get_user as get_user, get_yml_content as get_yml_content, print_error as print_error, print_normal as print_normal
from .config_utils import Config as Config, Experiments as Experiments
from .constants import ERROR_INFO as ERROR_INFO, EXPERIMENT_SUCCESS_INFO as EXPERIMENT_SUCCESS_INFO, LOG_HEADER as LOG_HEADER, NNI_HOME_DIR as NNI_HOME_DIR, REST_TIME_OUT as REST_TIME_OUT
from .launcher_utils import validate_all_content as validate_all_content
from .nnictl_utils import update_experiment as update_experiment
from .rest_utils import check_response as check_response, check_rest_server as check_rest_server, rest_post as rest_post, rest_put as rest_put
from .url_utils import cluster_metadata_url as cluster_metadata_url, experiment_url as experiment_url, get_local_urls as get_local_urls, set_prefix_url as set_prefix_url
from _typeshed import Incomplete
from nni.experiment.config import ExperimentConfig as ExperimentConfig, convert as convert
from nni.tools.annotation import expand_annotations as expand_annotations, generate_search_space as generate_search_space
from nni.tools.package_utils.tuner_factory import get_builtin_module_class_name as get_builtin_module_class_name
from subprocess import STDOUT as STDOUT

k8s_training_services: Incomplete

def get_log_path(experiment_id):
    """generate stdout and stderr log path"""
def print_log_content(config_file_name) -> None:
    """print log information"""
def start_rest_server(port, platform, mode, experiment_id, foreground: bool = False, log_dir: Incomplete | None = None, log_level: Incomplete | None = None, url_prefix: Incomplete | None = None):
    """Run nni manager process"""
def set_trial_config(experiment_config, port, config_file_name):
    """set trial configuration"""
def set_adl_config(experiment_config, port, config_file_name):
    """set adl configuration"""
def validate_response(response, config_file_name) -> None: ...
def set_V1_common_config(experiment_config, port, config_file_name) -> None: ...
def setNNIManagerIp(experiment_config, port, config_file_name):
    """set nniManagerIp"""
def set_kubeflow_config(experiment_config, port, config_file_name):
    """set kubeflow configuration"""
def set_frameworkcontroller_config(experiment_config, port, config_file_name):
    """set kubeflow configuration"""
def set_shared_storage(experiment_config, port, config_file_name): ...
def set_experiment_v1(experiment_config, mode, port, config_file_name):
    """Call startExperiment (rest POST /experiment) with yaml file content"""
def set_experiment_v2(experiment_config, mode, port, config_file_name):
    """Call startExperiment (rest POST /experiment) with yaml file content"""
def set_platform_config(platform, experiment_config, port, config_file_name, rest_process) -> None:
    """call set_cluster_metadata for specific platform"""
def launch_experiment(args, experiment_config, mode, experiment_id, config_version) -> None:
    """follow steps to start rest server and start experiment"""
def create_experiment(args) -> None:
    """start a new experiment"""
def manage_stopped_experiment(args, mode) -> None:
    """view a stopped experiment"""
def view_experiment(args) -> None:
    """view a stopped experiment"""
def resume_experiment(args) -> None:
    """resume an experiment"""
def manage_external_experiment(args, mode) -> None:
    """view a experiment from external path"""

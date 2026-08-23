from .command_utils import check_output_command as check_output_command, kill_command as kill_command
from .common_utils import detect_process as detect_process, generate_temp_dir as generate_temp_dir, get_yml_content as get_yml_content, print_error as print_error, print_green as print_green, print_normal as print_normal, print_warning as print_warning
from .config_utils import Config as Config, Experiments as Experiments
from .constants import EXPERIMENT_DETAIL_FORMAT as EXPERIMENT_DETAIL_FORMAT, EXPERIMENT_INFORMATION_FORMAT as EXPERIMENT_INFORMATION_FORMAT, EXPERIMENT_MONITOR_INFO as EXPERIMENT_MONITOR_INFO, NNI_HOME_DIR as NNI_HOME_DIR, REST_TIME_OUT as REST_TIME_OUT, TRIAL_MONITOR_CONTENT as TRIAL_MONITOR_CONTENT, TRIAL_MONITOR_HEAD as TRIAL_MONITOR_HEAD, TRIAL_MONITOR_TAIL as TRIAL_MONITOR_TAIL
from .rest_utils import check_response as check_response, check_rest_server_quick as check_rest_server_quick, rest_delete as rest_delete, rest_get as rest_get
from .ssh_utils import create_ssh_sftp_client as create_ssh_sftp_client, remove_remote_directory as remove_remote_directory
from .url_utils import experiment_url as experiment_url, export_data_url as export_data_url, metric_data_url as metric_data_url, trial_job_id_url as trial_job_id_url, trial_jobs_url as trial_jobs_url
from _typeshed import Incomplete
from nni.tools.annotation import expand_annotations as expand_annotations

def get_experiment_time(port):
    """get the startTime and endTime of an experiment"""
def get_experiment_status(port):
    """get the status of an experiment"""
def update_experiment() -> None:
    """Update the experiment status in config file"""
def check_experiment_id(args, update: bool = True):
    """check if the id is valid
    """
def parse_ids(args):
    """Parse the arguments for nnictl stop
    1.If port is provided and id is not specified, return the id who owns the port
    2.If both port and id are provided, return the id if it owns the port, otherwise fail
    3.If there is an id specified, return the corresponding id
    4.If there is no id specified, and there is an experiment running, return the id, or return Error
    5.If the id matches an experiment, nnictl will return the id.
    6.If the id ends with ``*``, nnictl will match all ids matchs the regular
    7.If the id does not exist but match the prefix of an experiment id, nnictl will return the matched id
    8.If the id does not exist but match multiple prefix of the experiment ids, nnictl will give id information
    """
def get_config_filename(args):
    """get the file name of config file"""
def get_experiment_port(args):
    """get the port of experiment"""
def convert_time_stamp_to_date(content):
    """Convert time stamp to date time format"""
def check_rest(args):
    """check if restful server is running"""
def stop_experiment(args) -> None:
    """Stop the experiment which is running"""
def trial_ls(args):
    """List trial"""
def trial_kill(args):
    """List trial"""
def trial_codegen(args) -> None:
    """Generate code for a specific trial"""
def list_experiment(args):
    """Get experiment information"""
def experiment_status(args):
    """Show the status of experiment"""
def log_internal(args, filetype) -> None:
    """internal function to call get_log_content"""
def log_stdout(args) -> None:
    """get stdout log"""
def log_stderr(args) -> None:
    """get stderr log"""
def log_trial_adl_helper(args, experiment_id) -> None: ...
def log_trial(args) -> None:
    """'get trial log path"""
def get_config(args) -> None:
    """get config info"""
def webui_url(args) -> None:
    """show the url of web ui"""
def local_clean(directory) -> None:
    """clean up local data"""
def remote_clean(machine_list, experiment_id: Incomplete | None = None) -> None:
    """clean up remote data"""
def experiment_clean(args) -> None:
    """clean up the experiment data"""
def get_platform_dir(config_content):
    """get the dir list to be deleted"""
def platform_clean(args) -> None:
    """clean up the experiment data"""
def experiment_list(args):
    """get the information of all experiments"""
def get_time_interval(time1, time2):
    """get the interval of two times"""
def show_experiment_info() -> None:
    """show experiment information in monitor"""
def set_monitor(auto_exit, time_interval, port: Incomplete | None = None, pid: Incomplete | None = None) -> None:
    """set the experiment monitor engine"""
def monitor_experiment(args) -> None:
    """monitor the experiment"""
def export_trials_data(args):
    """export experiment metadata and intermediate results to json or csv
    """
def search_space_auto_gen(args) -> None:
    """dry run trial code to generate search space file"""
def save_experiment(args) -> None:
    """save experiment data to a zip file"""
def load_experiment(args) -> None:
    """load experiment data"""

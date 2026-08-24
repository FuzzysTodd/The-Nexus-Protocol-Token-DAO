BASE_URL: str
API_ROOT_URL: str
EXPERIMENT_API: str
CLUSTER_METADATA_API: str
IMPORT_DATA_API: str
CHECK_STATUS_API: str
TRIAL_JOBS_API: str
EXPORT_DATA_API: str
TENSORBOARD_API: str
METRIC_DATA_API: str

def format_url_path(path): ...
def set_prefix_url(prefix_path) -> None: ...
def metric_data_url(port):
    """get metric_data url"""
def check_status_url(port):
    """get check_status url"""
def cluster_metadata_url(port):
    """get cluster_metadata_url"""
def import_data_url(port):
    """get import_data_url"""
def experiment_url(port):
    """get experiment_url"""
def trial_jobs_url(port):
    """get trial_jobs url"""
def trial_job_id_url(port, job_id):
    """get trial_jobs with id url"""
def export_data_url(port):
    """get export_data url"""
def tensorboard_url(port):
    """get tensorboard url"""
def get_local_urls(port, prefix):
    """get urls of local machine"""

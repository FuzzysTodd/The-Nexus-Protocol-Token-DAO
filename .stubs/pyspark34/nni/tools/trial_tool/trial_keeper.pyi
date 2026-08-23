from .constants import LOG_DIR as LOG_DIR, MULTI_PHASE as MULTI_PHASE, NNI_EXP_ID as NNI_EXP_ID, NNI_PLATFORM as NNI_PLATFORM, NNI_SYS_DIR as NNI_SYS_DIR, NNI_TRIAL_JOB_ID as NNI_TRIAL_JOB_ID
from .hdfsClientUtility import copyDirectoryToHdfs as copyDirectoryToHdfs, copyHdfsDirectoryToLocal as copyHdfsDirectoryToLocal, copyHdfsFileToLocal as copyHdfsFileToLocal
from .log_utils import LogType as LogType, RemoteLogger as RemoteLogger, StdOutputType as StdOutputType, nni_log as nni_log
from .rest_utils import rest_get as rest_get, rest_post as rest_post
from .url_utils import gen_parameter_meta_url as gen_parameter_meta_url, gen_send_version_url as gen_send_version_url
from _typeshed import Incomplete

logger: Incomplete
regular: Incomplete

def get_hdfs_client(args): ...
def main_loop(args) -> None:
    """main loop logic for trial keeper"""
def trial_keeper_help_info(*args) -> None: ...
def check_version(args) -> None: ...
def is_multi_phase(): ...
def download_parameter(meta_list, args) -> None:
    '''
    Download parameter file to local working directory.
    meta_list format is defined in paiJobRestServer.ts
    example meta_list:
    [
        {"experimentId":"yWFJarYa","trialId":"UpPkl","filePath":"/chec/nni/experiments/yWFJarYa/trials/UpPkl/parameter_1.cfg"},
        {"experimentId":"yWFJarYa","trialId":"aIUMA","filePath":"/chec/nni/experiments/yWFJarYa/trials/aIUMA/parameter_1.cfg"}
    ]
    '''
def fetch_parameter_file(args) -> None: ...

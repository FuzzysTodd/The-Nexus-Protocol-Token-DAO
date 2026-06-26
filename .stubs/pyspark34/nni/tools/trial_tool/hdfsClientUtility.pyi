from .log_utils import LogType as LogType, nni_log as nni_log

def copyHdfsDirectoryToLocal(hdfsDirectory, localDirectory, hdfsClient) -> None:
    """Copy directory from HDFS to local"""
def copyHdfsFileToLocal(hdfsFilePath, localFilePath, hdfsClient, override: bool = True) -> None:
    """Copy file from HDFS to local"""
def copyDirectoryToHdfs(localDirectory, hdfsDirectory, hdfsClient):
    """Copy directory from local to HDFS"""
def copyFileToHdfs(localFilePath, hdfsFilePath, hdfsClient, override: bool = True):
    """Copy a local file to HDFS directory"""

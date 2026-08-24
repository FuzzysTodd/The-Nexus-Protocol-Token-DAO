from .logging import get_logger as get_logger
from _typeshed import Incomplete
from apache_beam.pipeline import Pipeline

CHUNK_SIZE: Incomplete
logger: Incomplete

class BeamPipeline(Pipeline):
    """Wrapper over `apache_beam.pipeline.Pipeline` for convenience"""
    def is_local(self): ...

def upload_local_to_remote(local_file_path, remote_file_path, force_upload: bool = False) -> None:
    """Use the Beam Filesystems to upload to a remote directory on gcs/s3/hdfs..."""
def download_remote_to_local(remote_file_path, local_file_path, force_download: bool = False) -> None:
    """Use the Beam Filesystems to download from a remote directory on gcs/s3/hdfs..."""

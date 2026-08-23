__all__ = ['NNI_BLOB', 'load_or_download_file', 'upload_file', 'nni_cache_home']

NNI_BLOB: str

def nni_cache_home() -> str: ...
def load_or_download_file(local_path: str, download_url: str, download: bool = False, progress: bool = True) -> None:
    """Download the ``download_url`` to ``local_path``, and check its hash.

    If ``local_path`` already exists, and hash is checked, do nothing.
    """
def upload_file(local_path: str, destination_path: str, sas_token: str) -> str:
    """For NNI maintainers to add updated static files to the Azure blob easily.
    In most cases, you don't need to calculate the hash on your own, it will be automatically inserted.
    For example, if you write ``https://xxx.com/myfile.zip``, the uploaded file will look like
    ``https://xxx.com/myfile-da5f43b7.zip``.

    Need to have `azcopy installed <https://docs.microsoft.com/en-us/azure/storage/common/storage-ref-azcopy>`_,
    and a SAS token for the destination storage (``?`` should be included as prefix of token).

    Returns a string which is the uploaded path.
    """

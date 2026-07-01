from _typeshed import Incomplete
from nni.common.blob_utils import NNI_BLOB as NNI_BLOB, load_or_download_file as load_or_download_file, nni_cache_home as nni_cache_home

PRETRAINED_WEIGHT_URLS: Incomplete

def load_pretrained_weight(name: str, **kwargs) -> str: ...

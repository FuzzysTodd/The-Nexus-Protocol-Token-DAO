from ...utils import logging as logging
from .image_processing_dpt import DPTImageProcessor as DPTImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class DPTFeatureExtractor(DPTImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

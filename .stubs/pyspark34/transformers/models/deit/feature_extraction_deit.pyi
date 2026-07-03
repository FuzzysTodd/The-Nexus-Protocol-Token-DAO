from ...utils import logging as logging
from .image_processing_deit import DeiTImageProcessor as DeiTImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class DeiTFeatureExtractor(DeiTImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

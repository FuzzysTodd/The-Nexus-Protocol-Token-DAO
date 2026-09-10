from ...utils import logging as logging
from .image_processing_detr import DetrImageProcessor as DetrImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class DetrFeatureExtractor(DetrImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

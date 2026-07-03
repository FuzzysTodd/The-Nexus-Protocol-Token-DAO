from ...utils import logging as logging
from .image_processing_flava import FlavaImageProcessor as FlavaImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class FlavaFeatureExtractor(FlavaImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

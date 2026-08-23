from ...utils import logging as logging
from .image_processing_convnext import ConvNextImageProcessor as ConvNextImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class ConvNextFeatureExtractor(ConvNextImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

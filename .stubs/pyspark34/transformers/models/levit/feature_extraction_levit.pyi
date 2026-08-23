from ...utils import logging as logging
from .image_processing_levit import LevitImageProcessor as LevitImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class LevitFeatureExtractor(LevitImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

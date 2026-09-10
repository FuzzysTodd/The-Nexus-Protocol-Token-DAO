from ...utils import logging as logging
from .image_processing_donut import DonutImageProcessor as DonutImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class DonutFeatureExtractor(DonutImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

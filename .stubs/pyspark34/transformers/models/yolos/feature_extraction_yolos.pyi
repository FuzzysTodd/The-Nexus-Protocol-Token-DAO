from ...utils import logging as logging
from .image_processing_yolos import YolosImageProcessor as YolosImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class YolosFeatureExtractor(YolosImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

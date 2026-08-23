from ...utils import logging as logging
from .image_processing_mobilevit import MobileViTImageProcessor as MobileViTImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class MobileViTFeatureExtractor(MobileViTImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

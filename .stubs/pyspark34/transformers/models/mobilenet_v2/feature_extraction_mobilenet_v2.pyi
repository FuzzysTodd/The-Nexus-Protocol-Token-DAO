from ...utils import logging as logging
from .image_processing_mobilenet_v2 import MobileNetV2ImageProcessor as MobileNetV2ImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class MobileNetV2FeatureExtractor(MobileNetV2ImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

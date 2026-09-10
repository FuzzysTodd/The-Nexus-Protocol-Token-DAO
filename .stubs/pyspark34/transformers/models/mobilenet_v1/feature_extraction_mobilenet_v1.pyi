from ...utils import logging as logging
from .image_processing_mobilenet_v1 import MobileNetV1ImageProcessor as MobileNetV1ImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class MobileNetV1FeatureExtractor(MobileNetV1ImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

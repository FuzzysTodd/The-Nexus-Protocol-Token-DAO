from ...utils import logging as logging
from .image_processing_layoutlmv2 import LayoutLMv2ImageProcessor as LayoutLMv2ImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class LayoutLMv2FeatureExtractor(LayoutLMv2ImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

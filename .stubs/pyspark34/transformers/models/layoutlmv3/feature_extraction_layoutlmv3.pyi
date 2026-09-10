from ...utils import logging as logging
from .image_processing_layoutlmv3 import LayoutLMv3ImageProcessor as LayoutLMv3ImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class LayoutLMv3FeatureExtractor(LayoutLMv3ImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

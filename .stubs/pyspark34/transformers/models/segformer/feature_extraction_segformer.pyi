from ...utils import logging as logging
from .image_processing_segformer import SegformerImageProcessor as SegformerImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class SegformerFeatureExtractor(SegformerImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

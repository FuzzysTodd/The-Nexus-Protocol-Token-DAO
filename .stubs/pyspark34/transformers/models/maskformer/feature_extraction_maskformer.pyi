from .image_processing_maskformer import MaskFormerImageProcessor as MaskFormerImageProcessor
from _typeshed import Incomplete
from transformers.utils import logging as logging

logger: Incomplete

class MaskFormerFeatureExtractor(MaskFormerImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

from ...utils import logging as logging
from .image_processing_conditional_detr import ConditionalDetrImageProcessor as ConditionalDetrImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class ConditionalDetrFeatureExtractor(ConditionalDetrImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

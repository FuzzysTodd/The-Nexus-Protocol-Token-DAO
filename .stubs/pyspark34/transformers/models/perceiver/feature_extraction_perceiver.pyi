from ...utils import logging as logging
from .image_processing_perceiver import PerceiverImageProcessor as PerceiverImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class PerceiverFeatureExtractor(PerceiverImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

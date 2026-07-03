from ...utils import logging as logging
from .image_processing_vilt import ViltImageProcessor as ViltImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class ViltFeatureExtractor(ViltImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

from ...utils import logging as logging
from .image_processing_clip import CLIPImageProcessor as CLIPImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class CLIPFeatureExtractor(CLIPImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

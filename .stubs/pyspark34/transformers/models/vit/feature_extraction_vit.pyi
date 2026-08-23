from ...utils import logging as logging
from .image_processing_vit import ViTImageProcessor as ViTImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class ViTFeatureExtractor(ViTImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

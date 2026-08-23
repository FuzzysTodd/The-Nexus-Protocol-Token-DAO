from ...utils import logging as logging
from .image_processing_owlvit import OwlViTImageProcessor as OwlViTImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class OwlViTFeatureExtractor(OwlViTImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

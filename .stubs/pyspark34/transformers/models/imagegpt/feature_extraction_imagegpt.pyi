from ...utils import logging as logging
from .image_processing_imagegpt import ImageGPTImageProcessor as ImageGPTImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class ImageGPTFeatureExtractor(ImageGPTImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

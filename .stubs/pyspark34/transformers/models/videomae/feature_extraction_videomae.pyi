from ...utils import logging as logging
from .image_processing_videomae import VideoMAEImageProcessor as VideoMAEImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class VideoMAEFeatureExtractor(VideoMAEImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

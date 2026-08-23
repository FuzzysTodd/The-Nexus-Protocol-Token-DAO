from ...utils import logging as logging
from .image_processing_chinese_clip import ChineseCLIPImageProcessor as ChineseCLIPImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class ChineseCLIPFeatureExtractor(ChineseCLIPImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

from ...utils import logging as logging
from .image_processing_beit import BeitImageProcessor as BeitImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class BeitFeatureExtractor(BeitImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

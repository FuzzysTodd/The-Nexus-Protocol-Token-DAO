from ...utils import logging as logging
from .image_processing_poolformer import PoolFormerImageProcessor as PoolFormerImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class PoolFormerFeatureExtractor(PoolFormerImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

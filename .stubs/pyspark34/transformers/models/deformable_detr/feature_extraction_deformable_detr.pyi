from ...utils import logging as logging
from .image_processing_deformable_detr import DeformableDetrImageProcessor as DeformableDetrImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class DeformableDetrFeatureExtractor(DeformableDetrImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

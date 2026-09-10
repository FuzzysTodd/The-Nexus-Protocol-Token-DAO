from ...utils import logging as logging
from .image_processing_glpn import GLPNImageProcessor as GLPNImageProcessor
from _typeshed import Incomplete

logger: Incomplete

class GLPNFeatureExtractor(GLPNImageProcessor):
    def __init__(self, *args, **kwargs) -> None: ...

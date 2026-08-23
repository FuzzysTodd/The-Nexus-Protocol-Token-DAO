from ..constants import ENDPOINT as ENDPOINT
from ..utils import build_hf_headers as build_hf_headers, get_session as get_session, hf_raise_for_status as hf_raise_for_status, is_aiohttp_available as is_aiohttp_available, is_numpy_available as is_numpy_available, is_pillow_available as is_pillow_available
from ._text_generation import TextGenerationStreamResponse as TextGenerationStreamResponse
from _typeshed import Incomplete
from aiohttp import ClientResponse as ClientResponse, ClientSession as ClientSession
from dataclasses import dataclass
from pathlib import Path
from requests import HTTPError
from typing import BinaryIO

UrlT = str
PathT = str | Path
BinaryT = bytes | BinaryIO
ContentT = BinaryT | PathT | UrlT
TASKS_EXPECTING_IMAGES: Incomplete
logger: Incomplete

@dataclass
class ModelStatus:
    """
    This Dataclass represents the the model status in the Hugging Face Inference API.

    Args:
        loaded (`bool`):
            If the model is currently loaded.
        state (`str`):
            The current state of the model. This can be 'Loaded', 'Loadable', 'TooBig'
        compute_type (`str`):
            The type of compute resource the model is using or will use, such as 'gpu' or 'cpu'.
        framework (`str`):
            The name of the framework that the model was built with, such as 'transformers'
            or 'text-generation-inference'.
    """
    loaded: bool
    state: str
    compute_type: str
    framework: str
    def __init__(self, loaded, state, compute_type, framework) -> None: ...

class InferenceTimeoutError(HTTPError, TimeoutError):
    """Error raised when a model is unavailable or the request times out."""

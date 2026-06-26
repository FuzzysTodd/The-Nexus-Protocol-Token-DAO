from .constants import INFERENCE_ENDPOINT as INFERENCE_ENDPOINT
from .hf_api import HfApi as HfApi
from .utils import build_hf_headers as build_hf_headers, get_session as get_session, is_pillow_available as is_pillow_available, logging as logging, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import Incomplete
from typing import Any, Dict, List

logger: Incomplete
ALL_TASKS: Incomplete

class InferenceApi:
    '''Client to configure requests and make calls to the HuggingFace Inference API.

    Example:

    ```python
    >>> from huggingface_hub.inference_api import InferenceApi

    >>> # Mask-fill example
    >>> inference = InferenceApi("bert-base-uncased")
    >>> inference(inputs="The goal of life is [MASK].")
    [{\'sequence\': \'the goal of life is life.\', \'score\': 0.10933292657136917, \'token\': 2166, \'token_str\': \'life\'}]

    >>> # Question Answering example
    >>> inference = InferenceApi("deepset/roberta-base-squad2")
    >>> inputs = {
    ...     "question": "What\'s my name?",
    ...     "context": "My name is Clara and I live in Berkeley.",
    ... }
    >>> inference(inputs)
    {\'score\': 0.9326569437980652, \'start\': 11, \'end\': 16, \'answer\': \'Clara\'}

    >>> # Zero-shot example
    >>> inference = InferenceApi("typeform/distilbert-base-uncased-mnli")
    >>> inputs = "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!"
    >>> params = {"candidate_labels": ["refund", "legal", "faq"]}
    >>> inference(inputs, params)
    {\'sequence\': \'Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!\', \'labels\': [\'refund\', \'faq\', \'legal\'], \'scores\': [0.9378499388694763, 0.04914155602455139, 0.013008488342165947]}

    >>> # Overriding configured task
    >>> inference = InferenceApi("bert-base-uncased", task="feature-extraction")

    >>> # Text-to-image
    >>> inference = InferenceApi("stabilityai/stable-diffusion-2-1")
    >>> inference("cat")
    <PIL.PngImagePlugin.PngImageFile image (...)>

    >>> # Return as raw response to parse the output yourself
    >>> inference = InferenceApi("mio/amadeus")
    >>> response = inference("hello world", raw_response=True)
    >>> response.headers
    {"Content-Type": "audio/flac", ...}
    >>> response.content # raw bytes from server
    b\'(...)\'
    ```
    '''
    options: Incomplete
    headers: Incomplete
    task: Incomplete
    api_url: Incomplete
    def __init__(self, repo_id: str, task: str | None = None, token: str | None = None, gpu: bool = False) -> None:
        """Inits headers and API call information.

        Args:
            repo_id (``str``):
                Id of repository (e.g. `user/bert-base-uncased`).
            task (``str``, `optional`, defaults ``None``):
                Whether to force a task instead of using task specified in the
                repository.
            token (`str`, `optional`):
                The API token to use as HTTP bearer authorization. This is not
                the authentication token. You can find the token in
                https://huggingface.co/settings/token. Alternatively, you can
                find both your organizations and personal API tokens using
                `HfApi().whoami(token)`.
            gpu (`bool`, `optional`, defaults `False`):
                Whether to use GPU instead of CPU for inference(requires Startup
                plan at least).
        """
    def __call__(self, inputs: str | Dict | List[str] | List[List[str]] | None = None, params: Dict | None = None, data: bytes | None = None, raw_response: bool = False) -> Any:
        """Make a call to the Inference API.

        Args:
            inputs (`str` or `Dict` or `List[str]` or `List[List[str]]`, *optional*):
                Inputs for the prediction.
            params (`Dict`, *optional*):
                Additional parameters for the models. Will be sent as `parameters` in the
                payload.
            data (`bytes`, *optional*):
                Bytes content of the request. In this case, leave `inputs` and `params` empty.
            raw_response (`bool`, defaults to `False`):
                If `True`, the raw `Response` object is returned. You can parse its content
                as preferred. By default, the content is parsed into a more practical format
                (json dictionary or PIL Image for example).
        """

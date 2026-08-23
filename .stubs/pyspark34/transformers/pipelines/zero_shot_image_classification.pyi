from ..image_utils import load_image as load_image
from ..tf_utils import stable_softmax as stable_softmax
from ..utils import add_end_docstrings as add_end_docstrings, is_tf_available as is_tf_available, is_torch_available as is_torch_available, is_vision_available as is_vision_available, logging as logging, requires_backends as requires_backends
from .base import ChunkPipeline as ChunkPipeline, PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS
from PIL import Image as Image
from _typeshed import Incomplete
from collections.abc import Generator
from typing import List, Union

logger: Incomplete

class ZeroShotImageClassificationPipeline(ChunkPipeline):
    '''
    Zero shot image classification pipeline using `CLIPModel`. This pipeline predicts the class of an image when you
    provide an image and a set of `candidate_labels`.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> classifier = pipeline(model="openai/clip-vit-large-patch14")
    >>> classifier(
    ...     "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png",
    ...     candidate_labels=["animals", "humans", "landscape"],
    ... )
    [{\'score\': 0.965, \'label\': \'animals\'}, {\'score\': 0.03, \'label\': \'humans\'}, {\'score\': 0.005, \'label\': \'landscape\'}]

    >>> classifier(
    ...     "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png",
    ...     candidate_labels=["black and white", "photorealist", "painting"],
    ... )
    [{\'score\': 0.996, \'label\': \'black and white\'}, {\'score\': 0.003, \'label\': \'photorealist\'}, {\'score\': 0.0, \'label\': \'painting\'}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This image classification pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"zero-shot-image-classification"`.

    See the list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=zero-shot-image-classification).
    '''
    def __init__(self, **kwargs) -> None: ...
    def __call__(self, images: Union[str, List[str], 'Image', List['Image']], **kwargs):
        '''
        Assign labels to the image(s) passed as inputs.

        Args:
            images (`str`, `List[str]`, `PIL.Image` or `List[PIL.Image]`):
                The pipeline handles three types of images:

                - A string containing a http link pointing to an image
                - A string containing a local path to an image
                - An image loaded in PIL directly

            candidate_labels (`List[str]`):
                The candidate labels for this image

            hypothesis_template (`str`, *optional*, defaults to `"This is a photo of {}"`):
                The sentence used in cunjunction with *candidate_labels* to attempt the image classification by
                replacing the placeholder with the candidate_labels. Then likelihood is estimated by using
                logits_per_image

        Return:
            A list of dictionaries containing result, one dictionary per proposed label. The dictionaries contain the
            following keys:

            - **label** (`str`) -- The label identified by the model. It is one of the suggested `candidate_label`.
            - **score** (`float`) -- The score attributed by the model for that label (between 0 and 1).
        '''
    def preprocess(self, image, candidate_labels: Incomplete | None = None, hypothesis_template: str = 'This is a photo of {}.') -> Generator[Incomplete, None, None]: ...
    def postprocess(self, model_outputs): ...

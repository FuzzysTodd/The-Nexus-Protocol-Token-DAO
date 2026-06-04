from ..image_utils import load_image as load_image
from ..models.auto.modeling_auto import MODEL_FOR_VISION_2_SEQ_MAPPING as MODEL_FOR_VISION_2_SEQ_MAPPING
from ..models.auto.modeling_tf_auto import TF_MODEL_FOR_VISION_2_SEQ_MAPPING as TF_MODEL_FOR_VISION_2_SEQ_MAPPING
from ..utils import add_end_docstrings as add_end_docstrings, is_tf_available as is_tf_available, is_torch_available as is_torch_available, is_vision_available as is_vision_available, logging as logging, requires_backends as requires_backends
from .base import PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline
from PIL import Image as Image
from _typeshed import Incomplete
from typing import List, Union

logger: Incomplete

class ImageToTextPipeline(Pipeline):
    '''
    Image To Text pipeline using a `AutoModelForVision2Seq`. This pipeline predicts a caption for a given image.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> captioner = pipeline(model="ydshieh/vit-gpt2-coco-en")
    >>> captioner("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
    [{\'generated_text\': \'two birds are standing next to each other \'}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This image to text pipeline can currently be loaded from pipeline() using the following task identifier:
    "image-to-text".

    See the list of available models on
    [huggingface.co/models](https://huggingface.co/models?pipeline_tag=image-to-text).
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, images: Union[str, List[str], 'Image.Image', List['Image.Image']], **kwargs):
        """
        Assign labels to the image(s) passed as inputs.

        Args:
            images (`str`, `List[str]`, `PIL.Image` or `List[PIL.Image]`):
                The pipeline handles three types of images:

                - A string containing a HTTP(s) link pointing to an image
                - A string containing a local path to an image
                - An image loaded in PIL directly

                The pipeline accepts either a single image or a batch of images.

            max_new_tokens (`int`, *optional*):
                The amount of maximum tokens to generate. By default it will use `generate` default.

            generate_kwargs (`Dict`, *optional*):
                Pass it to send all of these arguments directly to `generate` allowing full control of this function.

        Return:
            A list or a list of list of `dict`: Each result comes as a dictionary with the following key:

            - **generated_text** (`str`) -- The generated text.
        """
    def preprocess(self, image): ...
    def postprocess(self, model_outputs): ...

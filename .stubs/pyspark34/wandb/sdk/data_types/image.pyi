import numpy as np
from ..wandb_run import Run as LocalRun
from ._private import MEDIA_TMP as MEDIA_TMP
from .base_types.media import BatchableMedia as BatchableMedia, Media as Media
from .helper_types.bounding_boxes_2d import BoundingBoxes2D as BoundingBoxes2D
from .helper_types.classes import Classes as Classes
from .helper_types.image_mask import ImageMask as ImageMask
from PIL.Image import Image as PILImage
from _typeshed import Incomplete
from typing import Any, Dict, List, Sequence
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import hashutil as hashutil, runid as runid
from wandb.sdk.lib.paths import LogicalPath as LogicalPath

ImageDataType: Incomplete
ImageDataOrPathType: Incomplete
TorchTensorType: Incomplete

class Image(BatchableMedia):
    '''Format images for logging to W&B.

    Arguments:
        data_or_path: (numpy array, string, io) Accepts numpy array of
            image data, or a PIL image. The class attempts to infer
            the data format and converts it.
        mode: (string) The PIL mode for an image. Most common are "L", "RGB",
            "RGBA". Full explanation at https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes.
        caption: (string) Label for display of image.

    Note : When logging a `torch.Tensor` as a `wandb.Image`, images are normalized. If you do not want to normalize your images, please convert your tensors to a PIL Image.

    Examples:
        ### Create a wandb.Image from a numpy array
        <!--yeadoc-test:log-image-numpy-->
        ```python
        import numpy as np
        import wandb

        wandb.init()
        examples = []
        for i in range(3):
            pixels = np.random.randint(low=0, high=256, size=(100, 100, 3))
            image = wandb.Image(pixels, caption=f"random field {i}")
            examples.append(image)
        wandb.log({"examples": examples})
        ```

        ### Create a wandb.Image from a PILImage
        <!--yeadoc-test:log-image-pillow-->
        ```python
        import numpy as np
        from PIL import Image as PILImage
        import wandb

        wandb.init()
        examples = []
        for i in range(3):
            pixels = np.random.randint(low=0, high=256, size=(100, 100, 3), dtype=np.uint8)
            pil_image = PILImage.fromarray(pixels, mode="RGB")
            image = wandb.Image(pil_image, caption=f"random field {i}")
            examples.append(image)
        wandb.log({"examples": examples})
        ```
    '''
    MAX_ITEMS: int
    MAX_DIMENSION: int
    format: str | None
    def __init__(self, data_or_path: ImageDataOrPathType, mode: str | None = None, caption: str | None = None, grouping: int | None = None, classes: Classes | Sequence[dict] | None = None, boxes: Dict[str, 'BoundingBoxes2D'] | Dict[str, dict] | None = None, masks: Dict[str, 'ImageMask'] | Dict[str, dict] | None = None) -> None: ...
    @classmethod
    def from_json(cls, json_obj: dict, source_artifact: Artifact) -> Image: ...
    @classmethod
    def get_media_subdir(cls) -> str: ...
    def bind_to_run(self, run: LocalRun, key: int | str, step: int | str, id_: int | str | None = None, ignore_copy_err: bool | None = None) -> None: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict: ...
    def guess_mode(self, data: np.ndarray) -> str:
        """Guess what type of image the np.array is representing."""
    @classmethod
    def to_uint8(cls, data: np.ndarray) -> np.ndarray:
        """Convert image data to uint8.

        Convert floating point image on the range [0,1] and integer images on the range
        [0,255] to uint8, clipping if necessary.
        """
    @classmethod
    def seq_to_json(cls, seq: Sequence['BatchableMedia'], run: LocalRun, key: str, step: int | str) -> dict:
        """Combine a list of images into a meta dictionary object describing the child images."""
    @classmethod
    def all_masks(cls, images: Sequence['Image'], run: LocalRun, run_key: str, step: int | str) -> List[dict | None] | bool: ...
    @classmethod
    def all_boxes(cls, images: Sequence['Image'], run: LocalRun, run_key: str, step: int | str) -> List[dict | None] | bool: ...
    @classmethod
    def all_captions(cls, images: Sequence['Media']) -> bool | Sequence[str | None]: ...
    def __ne__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def to_data_array(self) -> List[Any]: ...
    @property
    def image(self) -> PILImage | None: ...

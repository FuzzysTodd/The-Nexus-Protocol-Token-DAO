from ...wandb_run import Run as LocalRun
from .._private import MEDIA_TMP as MEDIA_TMP
from ..base_types.media import Media as Media
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import runid as runid

class ImageMask(Media):
    '''Format image masks or overlays for logging to W&B.

    Arguments:
        val: (dictionary)
            One of these two keys to represent the image:
                mask_data : (2D numpy array) The mask containing an integer class label
                    for each pixel in the image
                path : (string) The path to a saved image file of the mask
            class_labels : (dictionary of integers to strings, optional) A mapping of the
                integer class labels in the mask to readable class names. These will default
                to class_0, class_1, class_2, etc.

        key: (string)
            The readable name or id for this mask type (e.g. predictions, ground_truth)

    Examples:
        ### Logging a single masked image
        <!--yeadoc-test:log-image-mask-->
        ```python
        import numpy as np
        import wandb

        wandb.init()
        image = np.random.randint(low=0, high=256, size=(100, 100, 3), dtype=np.uint8)
        predicted_mask = np.empty((100, 100), dtype=np.uint8)
        ground_truth_mask = np.empty((100, 100), dtype=np.uint8)

        predicted_mask[:50, :50] = 0
        predicted_mask[50:, :50] = 1
        predicted_mask[:50, 50:] = 2
        predicted_mask[50:, 50:] = 3

        ground_truth_mask[:25, :25] = 0
        ground_truth_mask[25:, :25] = 1
        ground_truth_mask[:25, 25:] = 2
        ground_truth_mask[25:, 25:] = 3

        class_labels = {0: "person", 1: "tree", 2: "car", 3: "road"}

        masked_image = wandb.Image(
            image,
            masks={
                "predictions": {"mask_data": predicted_mask, "class_labels": class_labels},
                "ground_truth": {"mask_data": ground_truth_mask, "class_labels": class_labels},
            },
        )
        wandb.log({"img_with_masks": masked_image})
        ```

        ### Log a masked image inside a Table
        <!--yeadoc-test:log-image-mask-table-->
        ```python
        import numpy as np
        import wandb

        wandb.init()
        image = np.random.randint(low=0, high=256, size=(100, 100, 3), dtype=np.uint8)
        predicted_mask = np.empty((100, 100), dtype=np.uint8)
        ground_truth_mask = np.empty((100, 100), dtype=np.uint8)

        predicted_mask[:50, :50] = 0
        predicted_mask[50:, :50] = 1
        predicted_mask[:50, 50:] = 2
        predicted_mask[50:, 50:] = 3

        ground_truth_mask[:25, :25] = 0
        ground_truth_mask[25:, :25] = 1
        ground_truth_mask[:25, 25:] = 2
        ground_truth_mask[25:, 25:] = 3

        class_labels = {0: "person", 1: "tree", 2: "car", 3: "road"}

        class_set = wandb.Classes(
            [
                {"name": "person", "id": 0},
                {"name": "tree", "id": 1},
                {"name": "car", "id": 2},
                {"name": "road", "id": 3},
            ]
        )

        masked_image = wandb.Image(
            image,
            masks={
                "predictions": {"mask_data": predicted_mask, "class_labels": class_labels},
                "ground_truth": {"mask_data": ground_truth_mask, "class_labels": class_labels},
            },
            classes=class_set,
        )

        table = wandb.Table(columns=["image"])
        table.add_data(masked_image)
        wandb.log({"random_field": table})
        ```
    '''
    def __init__(self, val: dict, key: str) -> None:
        """Initialize an ImageMask object.

        Arguments:
            val: (dictionary) One of these two keys to represent the image:
                mask_data : (2D numpy array) The mask containing an integer class label
                    for each pixel in the image
                path : (string) The path to a saved image file of the mask
                class_labels : (dictionary of integers to strings, optional) A mapping
                    of the integer class labels in the mask to readable class names.
                    These will default to class_0, class_1, class_2, etc.

        key: (string)
            The readable name or id for this mask type (e.g. predictions, ground_truth)
        """
    def bind_to_run(self, run: LocalRun, key: int | str, step: int | str, id_: int | str | None = None, ignore_copy_err: bool | None = None) -> None: ...
    @classmethod
    def get_media_subdir(cls) -> str: ...
    @classmethod
    def from_json(cls, json_obj: dict, source_artifact: Artifact) -> ImageMask: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict: ...
    @classmethod
    def type_name(cls) -> str: ...
    def validate(self, val: dict) -> bool: ...

import torch
import wandb
from typing import Any, Dict, List, Tuple
from ultralytics.engine.results import Results as Results
from ultralytics.models.yolo.detect import DetectionPredictor as DetectionPredictor

def scale_bounding_box_to_original_image_shape(box: torch.Tensor, resized_image_shape: Tuple, original_image_shape: Tuple, ratio_pad: bool) -> List[int]:
    """YOLOv8 resizes images during training and the label values are normalized based on this resized shape.

    This function rescales the bounding box labels to the original
    image shape.

    Reference: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/yolo/utils/callbacks/comet.py#L105
    """
def get_ground_truth_bbox_annotations(img_idx: int, image_path: str, batch: Dict, class_name_map: Dict = None) -> List[Dict[str, Any]]:
    """Get ground truth bounding box annotation data in the form required for `wandb.Image` overlay system."""
def get_mean_confidence_map(classes: List, confidence: List, class_id_to_label: Dict) -> Dict[str, float]:
    """Get Mean-confidence map from the predictions to be logged into a `wandb.Table`."""
def get_boxes(result: Results) -> Tuple[Dict, Dict]:
    """Convert an ultralytics prediction result into metadata for the `wandb.Image` overlay system."""
def plot_predictions(result: Results, model_name: str, table: wandb.Table | None = None) -> wandb.Table | Tuple[wandb.Image, Dict, Dict]:
    """Plot the images with the W&B overlay system. The `wandb.Image` is either added to a `wandb.Table` or returned."""
def plot_validation_results(dataloader: Any, class_label_map: Dict, model_name: str, predictor: DetectionPredictor, table: wandb.Table, max_validation_batches: int, epoch: int | None = None) -> wandb.Table:
    """Plot validation results in a table."""

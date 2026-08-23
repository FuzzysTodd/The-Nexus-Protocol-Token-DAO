from _typeshed import Incomplete
from typing import Callable, Dict
from ultralytics.models import YOLO as YOLO
from ultralytics.models.yolo.classify import ClassificationPredictor, ClassificationTrainer, ClassificationValidator
from ultralytics.models.yolo.detect import DetectionPredictor, DetectionTrainer, DetectionValidator
from ultralytics.models.yolo.pose import PosePredictor, PoseTrainer, PoseValidator
from ultralytics.models.yolo.segment import SegmentationPredictor, SegmentationTrainer, SegmentationValidator
from wandb.integration.ultralytics.bbox_utils import plot_predictions as plot_predictions, plot_validation_results as plot_validation_results
from wandb.integration.ultralytics.classification_utils import plot_classification_predictions as plot_classification_predictions, plot_classification_validation_results as plot_classification_validation_results
from wandb.integration.ultralytics.mask_utils import plot_mask_predictions as plot_mask_predictions, plot_mask_validation_results as plot_mask_validation_results
from wandb.integration.ultralytics.pose_utils import plot_pose_predictions as plot_pose_predictions, plot_pose_validation_results as plot_pose_validation_results
from wandb.sdk.lib import telemetry as telemetry

TRAINER_TYPE = ClassificationTrainer | DetectionTrainer | SegmentationTrainer | PoseTrainer
VALIDATOR_TYPE = ClassificationValidator | DetectionValidator | SegmentationValidator | PoseValidator
PREDICTOR_TYPE = ClassificationPredictor | DetectionPredictor | SegmentationPredictor | PosePredictor

class WandBUltralyticsCallback:
    '''Stateful callback for logging to W&B.

    In particular, it will log model checkpoints, predictions, and
    ground-truth annotations with interactive overlays for bounding boxes
    to Weights & Biases Tables during training, validation and prediction
    for a `ultratytics` workflow.

    **Usage:**

    ```python
    from ultralytics.yolo.engine.model import YOLO
    from wandb.yolov8 import add_wandb_callback

    # initialize YOLO model
    model = YOLO("yolov8n.pt")

    # add wandb callback
    add_wandb_callback(model, max_validation_batches=2, enable_model_checkpointing=True)

    # train
    model.train(data="coco128.yaml", epochs=5, imgsz=640)

    # validate
    model.val()

    # perform inference
    model(["img1.jpeg", "img2.jpeg"])
    ```

    Args:
        model: YOLO Model of type `:class:ultralytics.yolo.engine.model.YOLO`.
        max_validation_batches: maximum number of validation batches to log to
            a table per epoch.
        enable_model_checkpointing: enable logging model checkpoints as
            artifacts at the end of eveny epoch if set to `True`.
        visualize_skeleton: visualize pose skeleton by drawing lines connecting
            keypoints for human pose.
    '''
    max_validation_batches: Incomplete
    enable_model_checkpointing: Incomplete
    visualize_skeleton: Incomplete
    task: Incomplete
    task_map: Incomplete
    model_name: Incomplete
    supported_tasks: Incomplete
    def __init__(self, model: YOLO, max_validation_batches: int = 1, enable_model_checkpointing: bool = False, visualize_skeleton: bool = False) -> None: ...
    def on_train_start(self, trainer: TRAINER_TYPE): ...
    device: Incomplete
    model: Incomplete
    train_validation_table: Incomplete
    def on_fit_epoch_end(self, trainer: TRAINER_TYPE): ...
    def on_train_end(self, trainer: TRAINER_TYPE): ...
    validation_table: Incomplete
    def on_val_end(self, trainer: VALIDATOR_TYPE): ...
    prediction_table: Incomplete
    def on_predict_end(self, predictor: PREDICTOR_TYPE): ...
    @property
    def callbacks(self) -> Dict[str, Callable]:
        """Property contains all the relevant callbacks to add to the YOLO model for the Weights & Biases logging."""

def add_wandb_callback(model: YOLO, enable_model_checkpointing: bool = False, enable_train_validation_logging: bool = True, enable_validation_logging: bool = True, enable_prediction_logging: bool = True, max_validation_batches: int | None = 1, visualize_skeleton: bool | None = True):
    '''Function to add the `WandBUltralyticsCallback` callback to the `YOLO` model.

    **Usage:**

    ```python
    from ultralytics.yolo.engine.model import YOLO
    from wandb.yolov8 import add_wandb_callback

    # initialize YOLO model
    model = YOLO("yolov8n.pt")

    # add wandb callback
    add_wandb_callback(model, max_validation_batches=2, enable_model_checkpointing=True)

    # train
    model.train(data="coco128.yaml", epochs=5, imgsz=640)

    # validate
    model.val()

    # perform inference
    model(["img1.jpeg", "img2.jpeg"])
    ```

    Args:
        model: YOLO Model of type `:class:ultralytics.yolo.engine.model.YOLO`.
        enable_model_checkpointing: enable logging model checkpoints as
            artifacts at the end of eveny epoch if set to `True`.
        enable_train_validation_logging: enable logging the predictions and
            ground-truths as interactive image overlays on the images from
            the validation dataloader to a `wandb.Table` along with
            mean-confidence of the predictions per-class at the end of each
            training epoch.
        enable_validation_logging: enable logging the predictions and
            ground-truths as interactive image overlays on the images from the
            validation dataloader to a `wandb.Table` along with
            mean-confidence of the predictions per-class at the end of
            validation.
        enable_prediction_logging: enable logging the predictions and
            ground-truths as interactive image overlays on the images from the
            validation dataloader to a `wandb.Table` along with mean-confidence
            of the predictions per-class at the end of each prediction.
        max_validation_batches: maximum number of validation batches to log to
            a table per epoch.
        visualize_skeleton: visualize pose skeleton by drawing lines connecting
            keypoints for human pose.
    '''

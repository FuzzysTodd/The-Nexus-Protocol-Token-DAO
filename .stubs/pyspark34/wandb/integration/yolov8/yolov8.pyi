from _typeshed import Incomplete
from typing import Any, Callable, Dict, List
from ultralytics.yolo.engine.model import YOLO as YOLO
from ultralytics.yolo.engine.trainer import BaseTrainer as BaseTrainer
from wandb.sdk.lib import telemetry as telemetry

class WandbCallback:
    '''An internal YOLO model wrapper that tracks metrics, and logs models to Weights & Biases.

    Usage:
    ```python
    from wandb.integration.yolov8.yolov8 import WandbCallback

    model = YOLO("yolov8n.pt")
    wandb_logger = WandbCallback(
        model,
    )
    for event, callback_fn in wandb_logger.callbacks.items():
        model.add_callback(event, callback_fn)
    ```
    '''
    yolo: Incomplete
    run_name: Incomplete
    project: Incomplete
    tags: Incomplete
    resume: Incomplete
    kwargs: Incomplete
    def __init__(self, yolo: YOLO, run_name: str | None = None, project: str | None = None, tags: List[str] | None = None, resume: str | None = None, **kwargs: Any | None) -> None:
        '''A utility class to manage wandb run and various callbacks for the ultralytics YOLOv8 framework.

        Args:
            yolo: A YOLOv8 model that\'s inherited from `:class:ultralytics.yolo.engine.model.YOLO`
            run_name, str: The name of the Weights & Biases run, defaults to an auto generated run_name if `trainer.args.name` is not defined.
            project, str: The name of the Weights & Biases project, defaults to `"YOLOv8"` if `trainer.args.project` is not defined.
            tags, List[str]: A list of tags to be added to the Weights & Biases run, defaults to `["YOLOv8"]`.
            resume, str: Whether to resume a previous run on Weights & Biases, defaults to `None`.
            **kwargs: Additional arguments to be passed to `wandb.init()`.
        '''
    run: Incomplete
    def on_pretrain_routine_start(self, trainer: BaseTrainer) -> None:
        """Starts a new wandb run to track the training process and log to Weights & Biases.

        Args:
            trainer: A task trainer that's inherited from `:class:ultralytics.yolo.engine.trainer.BaseTrainer`
                    that contains the model training and optimization routine.
        """
    def on_pretrain_routine_end(self, trainer: BaseTrainer) -> None: ...
    def on_train_epoch_start(self, trainer: BaseTrainer) -> None:
        """On train epoch start we only log epoch number to the Weights & Biases run."""
    def on_train_epoch_end(self, trainer: BaseTrainer) -> None:
        """On train epoch end we log all the metrics to the Weights & Biases run."""
    def on_fit_epoch_end(self, trainer: BaseTrainer) -> None:
        """On fit epoch end we log all the best metrics and model detail to Weights & Biases run summary."""
    def on_train_end(self, trainer: BaseTrainer) -> None:
        """On train end we log all the media, including plots, images and best model artifact to Weights & Biases."""
    def on_model_save(self, trainer: BaseTrainer) -> None:
        """On model save we log the model as an artifact to Weights & Biases."""
    def teardown(self, _trainer: BaseTrainer) -> None:
        """On teardown, we finish the Weights & Biases run and set it to None."""
    @property
    def callbacks(self) -> Dict[str, Callable]:
        """Property contains all the relevant callbacks to add to the YOLO model for the Weights & Biases logging."""

def add_callbacks(yolo: YOLO, run_name: str | None = None, project: str | None = None, tags: List[str] | None = None, resume: str | None = None, **kwargs: Any | None) -> YOLO:
    '''A YOLO model wrapper that tracks metrics, and logs models to Weights & Biases.

    Args:
        yolo: A YOLOv8 model that\'s inherited from `:class:ultralytics.yolo.engine.model.YOLO`
        run_name, str: The name of the Weights & Biases run, defaults to an auto generated name if `trainer.args.name` is not defined.
        project, str: The name of the Weights & Biases project, defaults to `"YOLOv8"` if `trainer.args.project` is not defined.
        tags, List[str]: A list of tags to be added to the Weights & Biases run, defaults to `["YOLOv8"]`.
        resume, str: Whether to resume a previous run on Weights & Biases, defaults to `None`.
        **kwargs: Additional arguments to be passed to `wandb.init()`.

    Usage:
    ```python
    from wandb.integration.yolov8 import add_callbacks as add_wandb_callbacks

    model = YOLO("yolov8n.pt")
    add_wandb_callbacks(
        model,
    )
    model.train(
        data="coco128.yaml",
        epochs=3,
        imgsz=640,
    )
    ```
    '''

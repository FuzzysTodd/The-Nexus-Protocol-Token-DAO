import wandb
from typing import Any
from ultralytics.engine.results import Results as Results
from ultralytics.models.yolo.classify import ClassificationPredictor as ClassificationPredictor

def plot_classification_predictions(result: Results, model_name: str, table: wandb.Table | None = None):
    """Plot classification prediction results to a `wandb.Table` if the table is passed otherwise return the data."""
def plot_classification_validation_results(dataloader: Any, model_name: str, predictor: ClassificationPredictor, table: wandb.Table, max_validation_batches: int, epoch: int | None = None):
    """Plot classification results to a `wandb.Table`."""

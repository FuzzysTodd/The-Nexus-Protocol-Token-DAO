from . import SentenceEvaluator as SentenceEvaluator
from ..util import batch_to_device as batch_to_device
from _typeshed import Incomplete
from torch.utils.data import DataLoader as DataLoader

logger: Incomplete

class LabelAccuracyEvaluator(SentenceEvaluator):
    """
    Evaluate a model based on its accuracy on a labeled dataset

    This requires a model with LossFunction.SOFTMAX

    The results are written in a CSV. If a CSV already exists, then values are appended.
    """
    dataloader: Incomplete
    name: Incomplete
    softmax_model: Incomplete
    write_csv: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    def __init__(self, dataloader: DataLoader, name: str = '', softmax_model: Incomplete | None = None, write_csv: bool = True) -> None:
        """
        Constructs an evaluator for the given dataset

        :param dataloader:
            the data for the evaluation
        """
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...

from ...utils import logging as logging
from .utils import DataProcessor as DataProcessor, InputExample as InputExample
from _typeshed import Incomplete

logger: Incomplete

class XnliProcessor(DataProcessor):
    """
    Processor for the XNLI dataset. Adapted from
    https://github.com/google-research/bert/blob/f39e881b169b9d53bea03d2d341b31707a6c052b/run_classifier.py#L207
    """
    language: Incomplete
    train_language: Incomplete
    def __init__(self, language, train_language: Incomplete | None = None) -> None: ...
    def get_train_examples(self, data_dir):
        """See base class."""
    def get_test_examples(self, data_dir):
        """See base class."""
    def get_labels(self):
        """See base class."""

xnli_processors: Incomplete
xnli_output_modes: Incomplete
xnli_tasks_num_labels: Incomplete

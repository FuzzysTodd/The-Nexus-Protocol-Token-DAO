from _typeshed import Incomplete
from keras import backend as backend

class PartialBatchPaddingHandler:
    """A container that holds info about partial batches for `predict()`."""
    padded_batch_size: int
    padding_mask: Incomplete
    output_shape: Incomplete
    def __init__(self, output_shape) -> None: ...
    def get_real_batch_size(self, dataset_batch):
        """Returns the number of elements in a potentially partial batch."""
    def update_mask(self, padding_mask, dataset_batch):
        """Calculate and cache the amount of padding required for a batch."""
    def pad_batch(self, *dataset_batch_elements):
        """Pads the batch dimension of a tensor to the complete batch size."""
    def apply_mask(self, prediction_result):
        """Removes prediction output that corresponds to padded input."""

from _typeshed import Incomplete
from tensorflow import keras

__all__ = ['TqdmCallback']

class TqdmCallback(keras.callbacks.Callback):
    """Keras callback for epoch and batch progress."""
    @staticmethod
    def bar2callback(bar, pop: Incomplete | None = None, delta=...): ...
    tqdm_class: Incomplete
    epoch_bar: Incomplete
    on_epoch_end: Incomplete
    batches: Incomplete
    verbose: Incomplete
    batch_bar: Incomplete
    on_batch_end: Incomplete
    def __init__(self, epochs: Incomplete | None = None, data_size: Incomplete | None = None, batch_size: Incomplete | None = None, verbose: int = 1, tqdm_class=..., **tqdm_kwargs) -> None:
        """
        Parameters
        ----------
        epochs  : int, optional
        data_size  : int, optional
            Number of training pairs.
        batch_size  : int, optional
            Number of training pairs per batch.
        verbose  : int
            0: epoch, 1: batch (transient), 2: batch. [default: 1].
            Will be set to `0` unless both `data_size` and `batch_size`
            are given.
        tqdm_class  : optional
            `tqdm` class to use for bars [default: `tqdm.auto.tqdm`].
        tqdm_kwargs  : optional
            Any other arguments used for all bars.
        """
    def on_train_begin(self, *_, **__) -> None: ...
    def on_epoch_begin(self, epoch, *_, **__): ...
    def on_train_end(self, *_, **__) -> None: ...
    def display(self) -> None:
        """Displays in the current cell in Notebooks."""

from pytorch_lightning.trainer.supporters import CombinedLoader, CombinedLoaderIterator
from typing import Any

__all__ = ['ConcatLoader']

class ConcatLoader(CombinedLoader):
    '''This loader is same as CombinedLoader in PyTorch-Lightning, but concatenate sub-loaders
    instead of loading them in parallel.

    Parameters
    ----------
    loaders
        For example, ::

            {
                "train": DataLoader(train_dataset),
                "val": DataLoader(val_dataset)
            }

        In this example, the loader will first produce the batches from "train", then "val".

    mode
        Only support "min_size" for now.
    '''
    def __init__(self, loaders: dict[str, Any], mode: str = 'min_size') -> None: ...
    def __iter__(self) -> Any:
        """Replace the super-class iterator with ours."""
    def __len__(self) -> int: ...

class ConcatLoaderIterator(CombinedLoaderIterator):
    """Similar to CombinedLoaderIterator in Lightning, but in a concat manner."""
    def __next__(self) -> Any:
        """Fetches the next batch from multiple data loaders,
        by looking for the first iterator that isn't exhausted yet.
        """

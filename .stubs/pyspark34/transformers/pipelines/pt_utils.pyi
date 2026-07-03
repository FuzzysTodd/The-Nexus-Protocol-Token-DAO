from _typeshed import Incomplete
from torch.utils.data import Dataset, IterableDataset
from transformers.utils.generic import ModelOutput as ModelOutput

class PipelineDataset(Dataset):
    dataset: Incomplete
    process: Incomplete
    params: Incomplete
    def __init__(self, dataset, process, params) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...

class PipelineIterator(IterableDataset):
    loader: Incomplete
    infer: Incomplete
    params: Incomplete
    loader_batch_size: Incomplete
    def __init__(self, loader, infer, params, loader_batch_size: Incomplete | None = None) -> None:
        """
        Roughly equivalent to

        ```
        for item in loader:
            yield infer(item, **params)
        ```

                Arguments:
                    loader (`torch.utils.data.DataLoader` or any iterator):
                        The iterator that will be used to apply `infer` on.
                    infer (any function):
                        The function to apply of each element of `loader`.
                    params (`dict`):
                        The parameters passed to `infer` along with every item
                    loader_batch_size (`int`, *optional*):
                        If specified, the items of `loader` are supposed to come as batch, and are loader_batched here
                        making it roughly behave as


        ```
        for items in loader:
            for i in loader_batch_size:
                item = items[i]
                yield infer(item, **params)
        ```"""
    def __len__(self) -> int: ...
    iterator: Incomplete
    def __iter__(self): ...
    def loader_batch_item(self):
        """
        Return item located at `loader_batch_index` within the current `loader_batch_data`.
        """
    def __next__(self): ...

class PipelineChunkIterator(PipelineIterator):
    def __init__(self, loader, infer, params, loader_batch_size: Incomplete | None = None) -> None:
        """
        Roughly equivalent to

        ```
        for iterator in loader:
            for item in iterator:
                yield infer(item, **params)
        ```

                Arguments:
                    loader (`torch.utils.data.DataLoader` or any iterator):
                        The iterator that will be used to apply `infer` on.
                    infer (any function):
                        The function to apply of each element of `loader`.
                    params (`dict`):
                        The parameters passed to `infer` along with every item
        """
    iterator: Incomplete
    subiterator: Incomplete
    def __iter__(self): ...
    def __next__(self): ...

class PipelinePackIterator(PipelineIterator):
    '''
    Roughly equivalent to

    ```
    packed =  []
    for item in loader:
        packed.append(item)
        if item["is_last"]:
            yield packed
            packed = []
    ```

        but it also handles cases where `item` are batched (meaning it\'s a dict of Tensor with first dimension > 1. In
        that case it does

    ```
    packed =  []
    for batch in loader:
        # item is batched
        for item in batch:
            packed.append(item)
            if item["is_last"]:
                yield packed
                packed = []
    ```

        Arguments:
            loader (`torch.utils.data.DataLoader` or any iterator):
                The iterator that will be used to apply `infer` on.
            infer (any function):
                The function to apply of each element of `loader`.
            params (`dict`):
                The parameters passed to `infer` along with every item
            loader_batch_size (`int`, *optional*):
                If specified, the items of `loader` are supposed to come as batch, and are loader_batched here making
                it roughly behave as


    ```
    for items in loader:
        for i in loader_batch_size:
            item = items[i]
            yield infer(item, **params)
    ```'''
    iterator: Incomplete
    def __iter__(self): ...
    loader_batch_size: Incomplete
    def __next__(self): ...

class KeyDataset(Dataset):
    dataset: Incomplete
    key: Incomplete
    def __init__(self, dataset: Dataset, key: str) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...

class KeyPairDataset(Dataset):
    dataset: Incomplete
    key1: Incomplete
    key2: Incomplete
    def __init__(self, dataset: Dataset, key1: str, key2: str) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...

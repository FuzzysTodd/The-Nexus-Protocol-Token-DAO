from _typeshed import Incomplete
from torch.utils.data import DataLoader

def to_device(obj, device):
    """
    Move a tensor, tuple, list, or dict onto device.
    """
def to_list(arr): ...

class AverageMeterGroup:
    """
    Average meter group for multiple average meters.
    """
    meters: Incomplete
    def __init__(self) -> None: ...
    def update(self, data) -> None:
        """
        Update the meter group with a dict of metrics.
        Non-exist average meters will be automatically created.
        """
    def __getattr__(self, item): ...
    def __getitem__(self, item): ...
    def summary(self):
        """
        Return a summary string of group data.
        """

class AverageMeter:
    """
    Computes and stores the average and current value.

    Parameters
    ----------
    name : str
        Name to display.
    fmt : str
        Format string to print the values.
    """
    name: Incomplete
    fmt: Incomplete
    def __init__(self, name, fmt: str = ':f') -> None: ...
    val: int
    avg: int
    sum: int
    count: int
    def reset(self) -> None:
        """
        Reset the meter.
        """
    def update(self, val, n: int = 1) -> None:
        """
        Update with value and weight.

        Parameters
        ----------
        val : float or int
            The new value to be accounted in.
        n : int
            The weight of the new value.
        """
    def summary(self): ...

def replace_layer_choice(root_module, init_fn, modules: Incomplete | None = None):
    """
    Replace layer choice modules with modules that are initiated with init_fn.

    Parameters
    ----------
    root_module : nn.Module
        Root module to traverse.
    init_fn : Callable
        Initializing function.
    modules : dict, optional
        Update the replaced modules into the dict and check duplicate if provided.

    Returns
    -------
    list[tuple[str, nn.Module]]
        A list from layer choice keys (names) and replaced modules.
    """
def replace_input_choice(root_module, init_fn, modules: Incomplete | None = None):
    """
    Replace input choice modules with modules that are initiated with init_fn.

    Parameters
    ----------
    root_module : nn.Module
        Root module to traverse.
    init_fn : Callable
        Initializing function.
    modules : dict, optional
        Update the replaced modules into the dict and check duplicate if provided.

    Returns
    -------
    list[tuple[str, nn.Module]]
        A list from layer choice keys (names) and replaced modules.
    """

class InterleavedTrainValDataLoader(DataLoader):
    """
    Dataloader that yields both train data and validation data in a batch, with an order of (train_batch, val_batch). The shorter
    one will be upsampled (repeated) to the length of the longer one, and the tail of the last repeat will be dropped. This enables
    users to train both model parameters and architecture parameters in parallel in an epoch.

    Some NAS algorithms, i.e. DARTS and Proxyless, require this type of dataloader.

    Parameters
    ----------
    train_data : DataLoader
        training dataloader
    val_data : DataLoader
        validation dataloader

    Example
    --------
    Fit your dataloaders into a parallel one.

    >>> para_loader = InterleavedTrainValDataLoader(train_dataloader, val_dataloader)

    Then you can use the ``para_loader`` as a normal training loader.
    """
    train_loader: Incomplete
    val_loader: Incomplete
    equal_len: Incomplete
    train_longer: Incomplete
    def __init__(self, train_dataloader: DataLoader, val_dataloader: DataLoader | list[DataLoader]) -> None: ...
    train_iter: Incomplete
    val_iter: Incomplete
    def __iter__(self): ...
    def __next__(self): ...
    def __len__(self) -> int: ...

class ConcatenateTrainValDataLoader(DataLoader):
    """
    Dataloader that yields validation data after training data in an epoch. You will get a batch with the form of (batch, source) in the
    training step, where ``source`` is a string which is either 'train' or 'val', indicating which dataloader the batch comes from. This
    enables users to train model parameters first in an epoch, and then train architecture parameters.

    Some NAS algorithms, i.e. ENAS, may require this type of dataloader.

    Parameters
    ----------
    train_data : DataLoader
        training dataloader
    val_data : DataLoader
        validation dataloader

    Warnings
    ----------
    If you set ``limit_train_batches`` of the trainer, the validation batches may be skipped.
    Consider downsampling the train dataset and the validation dataset instead if you want to shorten the length of data.

    Example
    --------
    Fit your dataloaders into a concatenated one.

    >>> concat_loader = ConcatenateTrainValDataLoader(train_dataloader, val_datalodaer)

    Then you can use the ``concat_loader`` as a normal training loader.
    """
    train_loader: Incomplete
    val_loader: Incomplete
    def __init__(self, train_dataloader: DataLoader, val_dataloader: DataLoader | list[DataLoader]) -> None: ...
    cur_iter: Incomplete
    source: str
    def __iter__(self): ...
    def __next__(self): ...
    def __len__(self) -> int: ...

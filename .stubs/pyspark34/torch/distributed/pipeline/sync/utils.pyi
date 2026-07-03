from torch import nn
from typing import List

__all__ = ['partition_model']

def partition_model(module: nn.Sequential, balance: List[int], devices: List[int] = None):
    """
    Given an :class:`nn.Sequential <torch.nn.Sequential>` module, partitions
    the model across multiple GPU devices according the provided ``balance``
    and ``devices``.

    Args:
        module (:class:`nn.Sequential <torch.nn.Sequential>`):
            Sequential model representing the pipe.
        balance (List[int]):
            List indicating the number of layers in each partition.
        devices (List[int], optional):
            List indicating the device to use for each partition. Defaults to
            ``range(len(balance))``
    """

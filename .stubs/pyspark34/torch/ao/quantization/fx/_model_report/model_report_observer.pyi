from _typeshed import Incomplete
from torch.ao.quantization.observer import ObserverBase as ObserverBase

class ModelReportObserver(ObserverBase):
    """This observer is used to record additional information regarding keeping track
    of S = average_batch_activation_range/epoch_activation_range.

    The purpose of this information is to prepare a report to present to users on whether
    Dynamic or Static Quantization is more appropriate for their model given the general
    distributions of their data.

    Args:
        ch_axis (int, optional): The channel axis for which the range and outlier stats are computed
            Default: 1
        comp_percentile (float, optional): The percentile to compare against 100 percentile to find outliers
            Should be between 0 and 1 exclusive
            Default: 0.9

    * :attr:`num_batches_tracked` specifies number of batches passed through the observer

    * :attr:`average_batch_activation_range` defines average across the ranges of each batch passed through

    * :attr:`epoch_activation_min` defines the minimum value passed through the observer

    * :attr:`epoch_activation_max` defines the maximum value passed through the observer

    * :attr:`ch_axis` defines the channel being used to compute per channel min max stats

    * :attr:`min_val` defines the per channel minimum values passed through

    * :attr:`max_val` defines the per channel maximum values passed through

    * :attr:`comp_percentile` defines comparison percentile to find outliers

    * :attr:`average_percentile_ratio` defines the per channel average percentile ratios

    * :attr:`percentile_batches_tracked` defines the number of percentile batches tracked for each channel

    * :attr:`constant_channels` defines the number of batches that aren't constant channels per channel

    Note: this tool is meant for FX Graph Mode Quantization
    """
    num_batches_tracked: int
    average_batch_activation_range: Incomplete
    epoch_activation_min: Incomplete
    epoch_activation_max: Incomplete
    ch_axis: Incomplete
    min_val: Incomplete
    max_val: Incomplete
    comp_percentile: Incomplete
    average_percentile_ratio: Incomplete
    percentile_batches_tracked: Incomplete
    constant_channels: Incomplete
    def __init__(self, ch_axis: int = 1, comp_percentile: float = 0.9) -> None: ...
    def forward(self, x): ...
    def get_batch_to_epoch_ratio(self): ...
    def reset_batch_and_epoch_values(self) -> None: ...
    def calculate_qparams(self) -> None: ...

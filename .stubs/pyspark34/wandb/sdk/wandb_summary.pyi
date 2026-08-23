import abc
import typing as t
from .interface.summary_record import SummaryItem as SummaryItem, SummaryRecord as SummaryRecord
from _typeshed import Incomplete

class SummaryDict(metaclass=abc.ABCMeta):
    """dict-like wrapper for the nested dictionaries in a SummarySubDict.

    Triggers self._root._callback on property changes.
    """
    def keys(self): ...
    def get(self, key, default: Incomplete | None = None): ...
    def __getitem__(self, key): ...
    __getattr__ = __getitem__
    def __setitem__(self, key, val) -> None: ...
    __setattr__ = __setitem__
    def __delattr__(self, key) -> None: ...
    __delitem__ = __delattr__
    def update(self, d: t.Dict): ...

class Summary(SummaryDict):
    '''Track single values for each metric for each run.

    By default, a metric\'s summary is the last value of its History.

    For example, `wandb.log({\'accuracy\': 0.9})` will add a new step to History and
    update Summary to the latest value. In some cases, it\'s more useful to have
    the maximum or minimum of a metric instead of the final value. You can set
    history manually `(wandb.summary[\'accuracy\'] = best_acc)`.

    In the UI, summary metrics appear in the table to compare across runs.
    Summary metrics are also used in visualizations like the scatter plot and
    parallel coordinates chart.

    After training has completed, you may want to save evaluation metrics to a
    run. Summary can handle numpy arrays and PyTorch/TensorFlow tensors. When
    you save one of these types to Summary, we persist the entire tensor in a
    binary file and store high level metrics in the summary object, such as min,
    mean, variance, and 95th percentile.

    Examples:
        ```python
        wandb.init(config=args)

        best_accuracy = 0
        for epoch in range(1, args.epochs + 1):
            test_loss, test_accuracy = test()
            if test_accuracy > best_accuracy:
                wandb.run.summary["best_accuracy"] = test_accuracy
                best_accuracy = test_accuracy
        ```
    '''
    def __init__(self, get_current_summary_callback: t.Callable) -> None: ...

class SummarySubDict(SummaryDict):
    """Non-root node of the summary data structure.

    Contains a path to itself from the root.
    """
    def __init__(self) -> None: ...

import logging
from _typeshed import Incomplete
from pyspark import cloudpickle as cloudpickle
from pyspark.context import SparkContext as SparkContext
from pyspark.ml.torch.log_communication import LogStreamingClient as LogStreamingClient, LogStreamingServer as LogStreamingServer, get_driver_host as get_driver_host
from pyspark.sql import SparkSession as SparkSession
from pyspark.taskcontext import BarrierTaskContext as BarrierTaskContext
from typing import Any, Callable, List

def get_conf_boolean(sc: SparkContext, key: str, default_value: str) -> bool:
    '''Get the conf "key" from the given spark context,
    or return the default value if the conf is not set.
    This expects the conf value to be a boolean or string;
    if the value is a string, this checks for all capitalization
    patterns of "true" and "false" to match Scala.

    Parameters
    ----------
    sc : :class:`SparkContext`
        The :class:`SparkContext` for the distributor.
    key : str
        string for conf name
    default_value : str
        default value for the conf value for the given key

    Returns
    -------
    bool
        Returns the boolean value that corresponds to the conf

    Raises
    ------
    ValueError
        Thrown when the conf value is not a valid boolean
    '''
def get_logger(name: str) -> logging.Logger:
    """
    Gets a logger by name, or creates and configures it for the first time.
    """
def get_gpus_owned(context: SparkContext | BarrierTaskContext) -> List[str]:
    """Gets the number of GPUs that Spark scheduled to the calling task.

    Parameters
    ----------
    context : :class:`SparkContext` or :class:`BarrierTaskContext`
        The :class:`SparkContext` or :class:`BarrierTaskContext` that has GPUs available.

    Returns
    -------
    list
        The correct mapping of addresses to workers.

    Raises
    ------
    ValueError
        Raised if the input addresses were not found.
    """

class Distributor:
    """
    The parent class for TorchDistributor. This class shouldn't be instantiated directly.
    """
    logger: Incomplete
    num_processes: Incomplete
    local_mode: Incomplete
    use_gpu: Incomplete
    spark: Incomplete
    sc: Incomplete
    num_tasks: Incomplete
    ssl_conf: Incomplete
    def __init__(self, num_processes: int = 1, local_mode: bool = True, use_gpu: bool = True) -> None: ...

class TorchDistributor(Distributor):
    '''
    A class to support distributed training on PyTorch and PyTorch Lightning using PySpark.

    .. versionadded:: 3.4.0

    Parameters
    ----------
    num_processes : int, optional
        An integer that determines how many different concurrent
        tasks are allowed. We expect spark.task.gpus = 1 for GPU-enabled training. Default
        should be 1; we don\'t want to invoke multiple cores/gpus without explicit mention.
    local_mode : bool, optional
        A boolean that determines whether we are using the driver
        node for training. Default should be false; we don\'t want to invoke executors without
        explicit mention.
    use_gpu : bool, optional
        A boolean that indicates whether or not we are doing training
        on the GPU. Note that there are differences in how GPU-enabled code looks like and
        how CPU-specific code looks like.

    Examples
    --------
    Run PyTorch Training locally on GPU (using a PyTorch native function)

    >>> def train(learning_rate):
    ...     import torch.distributed
    ...     torch.distributed.init_process_group(backend="nccl")
    ...     # ...
    ...     torch.destroy_process_group()
    ...     return model # or anything else
    >>> distributor = TorchDistributor(
    ...     num_processes=2,
    ...     local_mode=True,
    ...     use_gpu=True)
    >>> model = distributor.run(train, 1e-3)

    Run PyTorch Training on GPU (using a file with PyTorch code)

    >>> distributor = TorchDistributor(
    ...     num_processes=2,
    ...     local_mode=False,
    ...     use_gpu=True)
    >>> distributor.run("/path/to/train.py", "--learning-rate=1e-3")

    Run PyTorch Lightning Training on GPU

    >>> num_proc = 2
    >>> def train():
    ...     from pytorch_lightning import Trainer
    ...     # ...
    ...     # required to set devices = 1 and num_nodes = num_processes for multi node
    ...     # required to set devices = num_processes and num_nodes = 1 for single node multi GPU
    ...     trainer = Trainer(accelerator="gpu", devices=1, num_nodes=num_proc, strategy="ddp")
    ...     trainer.fit()
    ...     # ...
    ...     return trainer
    >>> distributor = TorchDistributor(
    ...     num_processes=num_proc,
    ...     local_mode=True,
    ...     use_gpu=True)
    >>> trainer = distributor.run(train)
    '''
    ssl_conf: str
    input_params: Incomplete
    def __init__(self, num_processes: int = 1, local_mode: bool = True, use_gpu: bool = True) -> None:
        """Initializes the distributor.

        Parameters
        ----------
        num_processes : int, optional
            An integer that determines how many different concurrent
            tasks are allowed. We expect spark.task.gpus = 1 for GPU-enabled training. Default
            should be 1; we don't want to invoke multiple cores/gpus without explicit mention.
        local_mode : bool, optional
            A boolean that determines whether we are using the driver
            node for training. Default should be false; we don't want to invoke executors without
            explicit mention.
        use_gpu : bool, optional
            A boolean that indicates whether or not we are doing training
            on the GPU. Note that there are differences in how GPU-enabled code looks like and
            how CPU-specific code looks like.

        Raises
        ------
        ValueError
            If any of the parameters are incorrect.
        RuntimeError
            If an active SparkSession is unavailable.
        """
    def run(self, train_object: Callable | str, *args: Any) -> Any | None:
        '''Runs distributed training.

        Parameters
        ----------
        train_object : callable object or str
            Either a PyTorch function, PyTorch Lightning function, or the path to a python file
            that launches distributed training.
        args :
            If train_object is a python function and not a path to a python file, args need
            to be the input parameters to that function. It would look like

            >>> model = distributor.run(train, 1e-3, 64)

            where train is a function and 1e-3 is a regular numeric input to the function.

            If train_object is a python file, then args would be the command-line arguments for
            that python file which are all in the form of strings. An example would be

            >>> distributor.run("/path/to/train.py", "--learning-rate=1e-3", "--batch-size=64")

            where since the input is a path, all of the parameters are strings that can be
            handled by argparse in that python file.

        Returns
        -------
            Returns the output of train_object called with args if the train_object is a
            Callable with an expected output. Returns None if train_object is a file.
        '''

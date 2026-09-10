from _typeshed import Incomplete

logger: Incomplete
logger_formatter: Incomplete

def check_spark():
    """Check if Spark is installed and running.
    Result of the function will be cached since test once is enough. As lru_cache will not
    cache exceptions, we don't raise exceptions here but only log a warning message.

    Returns:
        Return (True, None) if the check passes, otherwise log the exception message and
        return (False, Exception(msg)). The exception can be raised by the caller.
    """
def get_n_cpus(node: str = 'driver'):
    """Get the number of CPU cores of the given type of node.

    Args:
        node: string | The type of node to get the number of cores. Can be 'driver' or 'executor'.
            Default is 'driver'.

    Returns:
        An int of the number of CPU cores.
    """
def with_parameters(trainable, **kwargs):
    '''Wrapper for trainables to pass arbitrary large data objects.

    This wrapper function will store all passed parameters in the Spark
    Broadcast variable.

    Args:
        trainable: Trainable to wrap.
        **kwargs: parameters to store in object store.

    Returns:
        A new function with partial application of the given arguments
        and keywords. The given arguments and keywords will be broadcasted
        to all the executors.


    ```python
    import pyspark
    import flaml
    from sklearn.datasets import load_iris
    def train(config, data=None):
        if isinstance(data, pyspark.broadcast.Broadcast):
            data = data.value
        print(config, data)

    data = load_iris()
    with_parameters_train = flaml.tune.spark.utils.with_parameters(train, data=data)
    with_parameters_train(config=1)
    train(config={"metric": "accuracy"})
    ```
    '''
def broadcast_code(custom_code: str = '', file_name: str = 'mylearner'):
    '''Write customized learner/metric code contents to a file for importing.
    It is necessary for using the customized learner/metric in spark backend.
    The path of the learner/metric file will be returned.

    Args:
        custom_code: str, default="" | code contents of the custom learner/metric.
        file_name: str, default="mylearner" | file name of the custom learner/metric.

    Returns:
        The path of the custom code file.
    ```python
    from flaml.tune.spark.utils import broadcast_code
    from flaml.automl.model import LGBMEstimator

    custom_code = \'\'\'
    from flaml.automl.model import LGBMEstimator
    from flaml import tune

    class MyLargeLGBM(LGBMEstimator):
        @classmethod
        def search_space(cls, **params):
            return {
                "n_estimators": {
                    "domain": tune.lograndint(lower=4, upper=32768),
                    "init_value": 32768,
                    "low_cost_init_value": 4,
                },
                "num_leaves": {
                    "domain": tune.lograndint(lower=4, upper=32768),
                    "init_value": 32768,
                    "low_cost_init_value": 4,
                },
            }
    \'\'\'

    broadcast_code(custom_code=custom_code)
    from flaml.tune.spark.mylearner import MyLargeLGBM
    assert isinstance(MyLargeLGBM(), LGBMEstimator)
    ```
    '''
def get_broadcast_data(broadcast_data):
    """Get the broadcast data from the broadcast variable.

    Args:
        broadcast_data: pyspark.broadcast.Broadcast | the broadcast variable.

    Returns:
        The broadcast data.
    """

class PySparkOvertimeMonitor:
    """A context manager class to monitor if the PySpark job is overtime.
    Example:

    ```python
    with PySparkOvertimeMonitor(time_start, time_budget_s, force_cancel, parallel=parallel):
        results = parallel(
            delayed(evaluation_function)(trial_to_run.config)
            for trial_to_run in trials_to_run
        )
    ```

    """
    sc: Incomplete
    def __init__(self, start_time, time_budget_s, force_cancel: bool = False, cancel_func: Incomplete | None = None, parallel: Incomplete | None = None, sc: Incomplete | None = None) -> None:
        """Constructor.

        Specify the time budget and start time of the PySpark job, and specify how to cancel them.

        Args:
            Args relate to monitoring:
                start_time: float | The start time of the PySpark job.
                time_budget_s: float | The time budget of the PySpark job in seconds.
                force_cancel: boolean, default=False | Whether to forcely cancel the PySpark job if overtime.

            Args relate to how to cancel the PySpark job:
            (Only one of the following args will work. Priorities from top to bottom)
                cancel_func: function | A function to cancel the PySpark job.
                parallel: joblib.parallel.Parallel | Specify this if using joblib_spark as a parallel backend. It will call parallel._backend.terminate() to cancel the jobs.
                sc: pyspark.SparkContext object | You can pass a specific SparkContext.

                If all three args is None, the monitor will call pyspark.SparkContext.getOrCreate().cancelAllJobs() to cancel the jobs.


        """
    def __enter__(self) -> None:
        """Enter the context manager.
        This will start a monitor thread if spark is available and force_cancel is True.
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_traceback: types.TracebackType | None):
        """Exit the context manager.
        This will wait for the monitor thread to nicely exit."""

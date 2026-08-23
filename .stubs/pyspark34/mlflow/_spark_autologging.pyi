from _typeshed import Incomplete
from mlflow import MlflowClient as MlflowClient
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.spark import FLAVOR_NAME as FLAVOR_NAME
from mlflow.tracking.context.abstract_context import RunContextProvider as RunContextProvider
from mlflow.utils.autologging_utils import ExceptionSafeClass as ExceptionSafeClass, autologging_is_disabled as autologging_is_disabled
from mlflow.utils.validation import MAX_TAG_VAL_LENGTH as MAX_TAG_VAL_LENGTH

def add_table_info_to_context_provider(path, version, data_format) -> None: ...

class PythonSubscriber(metaclass=ExceptionSafeClass):
    """
    Subscriber, intended to be instantiated once per Python process, that logs Spark table
    information propagated from Java to the current MLflow run, starting a run if necessary.
    class implements a Java interface (org.mlflow.spark.autologging.MlflowAutologEventSubscriber,
    defined in the mlflow-spark package) that's called-into by autologging logic in the JVM in order
    to propagate Spark datasource read events to Python.

    This class leverages the Py4j callback mechanism to receive callbacks from the JVM, see
    https://www.py4j.org/advanced_topics.html#implementing-java-interfaces-from-python-callback for
    more information.
    """
    def __init__(self) -> None: ...
    def toString(self): ...
    def ping(self) -> None: ...
    def notify(self, path, version, data_format) -> None: ...
    def replId(self): ...
    class Java:
        implements: Incomplete

class SparkAutologgingContext(RunContextProvider):
    """
    Context provider used when there's no active run. Accumulates datasource read information,
    then logs that information to the next-created run & clears the accumulated information.
    """
    def in_context(self): ...
    def tags(self): ...

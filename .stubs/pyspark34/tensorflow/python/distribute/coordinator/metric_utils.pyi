from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.eager import monitoring as monitoring
from tensorflow.python.util import tf_contextlib as tf_contextlib

enable_metrics: bool

def monitored_timer(metric_name, state_tracker: Incomplete | None = None) -> Generator[None, None, None]:
    """Monitor the execution time and collect it into the specified metric."""
def get_metric_summary(metric_name):
    """Get summary for the specified metric."""

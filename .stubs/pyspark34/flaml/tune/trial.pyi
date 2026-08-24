from _typeshed import Incomplete

def flatten_dict(dt, delimiter: str = '/', prevent_delimiter: bool = False): ...
def unflatten_dict(dt, delimiter: str = '/'):
    """Unflatten dict. Does not support unflattening lists."""

class Trial:
    """A trial object holds the state for one model training run.
    Trials are themselves managed by the TrialRunner class, which implements
    the event loop for submitting trial runs to a Ray cluster.
    Trials start in the PENDING state, and transition to RUNNING once started.
    On error it transitions to ERROR, otherwise TERMINATED on success.
    Attributes:
        trainable_name (str): Name of the trainable object to be executed.
        config (dict): Provided configuration dictionary with evaluated params.
        trial_id (str): Unique identifier for the trial.
        local_dir (str): Local_dir as passed to tune.run.
        logdir (str): Directory where the trial logs are saved.
        evaluated_params (dict): Evaluated parameters by search algorithm,
        experiment_tag (str): Identifying trial name to show in the console.
        resources (Resources): Amount of resources that this trial will use.
        status (str): One of PENDING, RUNNING, PAUSED, TERMINATED, ERROR/
        error_file (str): Path to the errors that this trial has raised.
    """
    PENDING: str
    RUNNING: str
    PAUSED: str
    TERMINATED: str
    ERROR: str
    @classmethod
    def generate_id(cls): ...
    last_result: Incomplete
    last_update_time: Incomplete
    def update_last_result(self, result) -> None: ...
    status: Incomplete
    start_time: Incomplete
    def set_status(self, status) -> None:
        """Sets the status of the trial."""
    def is_finished(self): ...

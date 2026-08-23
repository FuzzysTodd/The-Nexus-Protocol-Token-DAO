from _typeshed import Incomplete

__all__ = ['get_advisor', 'register_advisor', 'send_trial', 'receive_trial_parameters', 'get_experiment_id', '_advisor']

_advisor: Incomplete

def get_advisor(): ...
def register_advisor(advisor) -> None: ...
def send_trial(parameters: dict, placement_constraint: Incomplete | None = None) -> int:
    """
    Send a new trial. Executed on tuner end.
    Return a ID that is the unique identifier for this trial.
    """
def receive_trial_parameters() -> dict:
    """
    Received a new trial. Executed on trial end.
    Reload with our json loads because NNI didn't use Retiarii serializer to load the data.
    """
def get_experiment_id() -> str: ...

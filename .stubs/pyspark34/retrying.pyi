from _typeshed import Incomplete

MAX_WAIT: int

def retry(*dargs, **dkw):
    """
    Decorator function that instantiates the Retrying object
    @param *dargs: positional arguments passed to Retrying object
    @param **dkw: keyword arguments passed to the Retrying object
    """

class Retrying:
    stop: Incomplete
    wait: Incomplete
    def __init__(self, stop: Incomplete | None = None, wait: Incomplete | None = None, stop_max_attempt_number: Incomplete | None = None, stop_max_delay: Incomplete | None = None, wait_fixed: Incomplete | None = None, wait_random_min: Incomplete | None = None, wait_random_max: Incomplete | None = None, wait_incrementing_start: Incomplete | None = None, wait_incrementing_increment: Incomplete | None = None, wait_exponential_multiplier: Incomplete | None = None, wait_exponential_max: Incomplete | None = None, retry_on_exception: Incomplete | None = None, retry_on_result: Incomplete | None = None, wrap_exception: bool = False, stop_func: Incomplete | None = None, wait_func: Incomplete | None = None, wait_jitter_max: Incomplete | None = None) -> None: ...
    def stop_after_attempt(self, previous_attempt_number, delay_since_first_attempt_ms):
        """Stop after the previous attempt >= stop_max_attempt_number."""
    def stop_after_delay(self, previous_attempt_number, delay_since_first_attempt_ms):
        """Stop after the time from the first attempt >= stop_max_delay."""
    def no_sleep(self, previous_attempt_number, delay_since_first_attempt_ms):
        """Don't sleep at all before retrying."""
    def fixed_sleep(self, previous_attempt_number, delay_since_first_attempt_ms):
        """Sleep a fixed amount of time between each retry."""
    def random_sleep(self, previous_attempt_number, delay_since_first_attempt_ms):
        """Sleep a random amount of time between wait_random_min and wait_random_max"""
    def incrementing_sleep(self, previous_attempt_number, delay_since_first_attempt_ms):
        """
        Sleep an incremental amount of time after each attempt, starting at
        wait_incrementing_start and incrementing by wait_incrementing_increment
        """
    def exponential_sleep(self, previous_attempt_number, delay_since_first_attempt_ms): ...
    def never_reject(self, result): ...
    def always_reject(self, result): ...
    def should_reject(self, attempt): ...
    def call(self, fn, *args, **kwargs): ...

class Attempt:
    """
    An Attempt encapsulates a call to a target function that may end as a
    normal return value from the function or an Exception depending on what
    occurred during the execution.
    """
    value: Incomplete
    attempt_number: Incomplete
    has_exception: Incomplete
    def __init__(self, value, attempt_number, has_exception) -> None: ...
    def get(self, wrap_exception: bool = False):
        """
        Return the return value of this Attempt instance or raise an Exception.
        If wrap_exception is true, this Attempt is wrapped inside of a
        RetryError before being raised.
        """

class RetryError(Exception):
    """
    A RetryError encapsulates the last Attempt instance right before giving up.
    """
    last_attempt: Incomplete
    def __init__(self, last_attempt) -> None: ...

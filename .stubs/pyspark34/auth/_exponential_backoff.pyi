class ExponentialBackoff:
    """An exponential backoff iterator. This can be used in a for loop to
    perform requests with exponential backoff.

    Args:
        total_attempts Optional[int]:
            The maximum amount of retries that should happen.
            The default value is 3 attempts.
        initial_wait_seconds Optional[int]:
            The amount of time to sleep in the first backoff. This parameter
            should be in seconds.
            The default value is 1 second.
        randomization_factor Optional[float]:
            The amount of jitter that should be in each backoff. For example,
            a value of 0.1 will introduce a jitter range of 10% to the
            current backoff period.
            The default value is 0.1.
        multiplier Optional[float]:
            The backoff multipler. This adjusts how much each backoff will
            increase. For example a value of 2.0 leads to a 200% backoff
            on each attempt. If the initial_wait is 1.0 it would look like
            this sequence [1.0, 2.0, 4.0, 8.0].
            The default value is 2.0.
    """
    def __init__(self, total_attempts=..., initial_wait_seconds=..., randomization_factor=..., multiplier=...) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    @property
    def total_attempts(self):
        """The total amount of backoff attempts that will be made."""
    @property
    def backoff_count(self):
        """The current amount of backoff attempts that have been made."""

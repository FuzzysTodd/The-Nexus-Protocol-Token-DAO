import abc
from _typeshed import Incomplete
from tenacity import RetryCallState as RetryCallState, _utils

class wait_base(abc.ABC, metaclass=abc.ABCMeta):
    """Abstract base class for wait strategies."""
    @abc.abstractmethod
    def __call__(self, retry_state: RetryCallState) -> float: ...
    def __add__(self, other: wait_base) -> wait_combine: ...
    def __radd__(self, other: wait_base) -> wait_combine | wait_base: ...

WaitBaseT: Incomplete

class wait_fixed(wait_base):
    """Wait strategy that waits a fixed amount of time between each retry."""
    wait_fixed: Incomplete
    def __init__(self, wait: _utils.time_unit_type) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> float: ...

class wait_none(wait_fixed):
    """Wait strategy that doesn't wait at all before retrying."""
    def __init__(self) -> None: ...

class wait_random(wait_base):
    """Wait strategy that waits a random amount of time between min/max."""
    wait_random_min: Incomplete
    wait_random_max: Incomplete
    def __init__(self, min: _utils.time_unit_type = 0, max: _utils.time_unit_type = 1) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> float: ...

class wait_combine(wait_base):
    """Combine several waiting strategies."""
    wait_funcs: Incomplete
    def __init__(self, *strategies: wait_base) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> float: ...

class wait_chain(wait_base):
    '''Chain two or more waiting strategies.

    If all strategies are exhausted, the very last strategy is used
    thereafter.

    For example::

        @retry(wait=wait_chain(*[wait_fixed(1) for i in range(3)] +
                               [wait_fixed(2) for j in range(5)] +
                               [wait_fixed(5) for k in range(4)))
        def wait_chained():
            print("Wait 1s for 3 attempts, 2s for 5 attempts and 5s
                   thereafter.")
    '''
    strategies: Incomplete
    def __init__(self, *strategies: wait_base) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> float: ...

class wait_incrementing(wait_base):
    """Wait an incremental amount of time after each attempt.

    Starting at a starting value and incrementing by a value for each attempt
    (and restricting the upper limit to some maximum value).
    """
    start: Incomplete
    increment: Incomplete
    max: Incomplete
    def __init__(self, start: _utils.time_unit_type = 0, increment: _utils.time_unit_type = 100, max: _utils.time_unit_type = ...) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> float: ...

class wait_exponential(wait_base):
    """Wait strategy that applies exponential backoff.

    It allows for a customized multiplier and an ability to restrict the
    upper and lower limits to some maximum and minimum value.

    The intervals are fixed (i.e. there is no jitter), so this strategy is
    suitable for balancing retries against latency when a required resource is
    unavailable for an unknown duration, but *not* suitable for resolving
    contention between multiple processes for a shared resource. Use
    wait_random_exponential for the latter case.
    """
    multiplier: Incomplete
    min: Incomplete
    max: Incomplete
    exp_base: Incomplete
    def __init__(self, multiplier: int | float = 1, max: _utils.time_unit_type = ..., exp_base: int | float = 2, min: _utils.time_unit_type = 0) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> float: ...

class wait_random_exponential(wait_exponential):
    '''Random wait with exponentially widening window.

    An exponential backoff strategy used to mediate contention between multiple
    uncoordinated processes for a shared resource in distributed systems. This
    is the sense in which "exponential backoff" is meant in e.g. Ethernet
    networking, and corresponds to the "Full Jitter" algorithm described in
    this blog post:

    https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/

    Each retry occurs at a random time in a geometrically expanding interval.
    It allows for a custom multiplier and an ability to restrict the upper
    limit of the random interval to some maximum value.

    Example::

        wait_random_exponential(multiplier=0.5,  # initial window 0.5s
                                max=60)          # max 60s timeout

    When waiting for an unavailable resource to become available again, as
    opposed to trying to resolve contention for a shared resource, the
    wait_exponential strategy (which uses a fixed interval) may be preferable.

    '''
    def __call__(self, retry_state: RetryCallState) -> float: ...

class wait_exponential_jitter(wait_base):
    """Wait strategy that applies exponential backoff and jitter.

    It allows for a customized initial wait, maximum wait and jitter.

    This implements the strategy described here:
    https://cloud.google.com/storage/docs/retry-strategy

    The wait time is min(initial * 2**n + random.uniform(0, jitter), maximum)
    where n is the retry count.
    """
    initial: Incomplete
    max: Incomplete
    exp_base: Incomplete
    jitter: Incomplete
    def __init__(self, initial: float = 1, max: float = ..., exp_base: float = 2, jitter: float = 1) -> None: ...
    def __call__(self, retry_state: RetryCallState) -> float: ...

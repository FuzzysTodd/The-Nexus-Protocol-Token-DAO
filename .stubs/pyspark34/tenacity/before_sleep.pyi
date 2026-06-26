import logging
import typing
from tenacity import RetryCallState as RetryCallState

def before_sleep_nothing(retry_state: RetryCallState) -> None:
    """Before call strategy that does nothing."""
def before_sleep_log(logger: logging.Logger, log_level: int, exc_info: bool = False) -> typing.Callable[[RetryCallState], None]:
    """Before call strategy that logs to some logger the attempt."""

from _typeshed import Incomplete
from backoff._jitter import full_jitter as full_jitter

def on_predicate(wait_gen, predicate=..., max_tries: Incomplete | None = None, max_time: Incomplete | None = None, jitter=..., on_success: Incomplete | None = None, on_backoff: Incomplete | None = None, on_giveup: Incomplete | None = None, logger: str = 'backoff', backoff_log_level=..., giveup_log_level=..., **wait_gen_kwargs):
    '''Returns decorator for backoff and retry triggered by predicate.

    Args:
        wait_gen: A generator yielding successive wait times in
            seconds.
        predicate: A function which when called on the return value of
            the target function will trigger backoff when considered
            truthily. If not specified, the default behavior is to
            backoff on falsey return values.
        max_tries: The maximum number of attempts to make before giving
            up. In the case of failure, the result of the last attempt
            will be returned. The default value of None means there
            is no limit to the number of tries. If a callable is passed,
            it will be evaluated at runtime and its return value used.
        max_time: The maximum total amount of time to try for before
            giving up. If this time expires, the result of the last
            attempt will be returned. If a callable is passed, it will
            be evaluated at runtime and its return value used.
        jitter: A function of the value yielded by wait_gen returning
            the actual time to wait. This distributes wait times
            stochastically in order to avoid timing collisions across
            concurrent clients. Wait times are jittered by default
            using the full_jitter function. Jittering may be disabled
            altogether by passing jitter=None.
        on_success: Callable (or iterable of callables) with a unary
            signature to be called in the event of success. The
            parameter is a dict containing details about the invocation.
        on_backoff: Callable (or iterable of callables) with a unary
            signature to be called in the event of a backoff. The
            parameter is a dict containing details about the invocation.
        on_giveup: Callable (or iterable of callables) with a unary
            signature to be called in the event that max_tries
            is exceeded.  The parameter is a dict containing details
            about the invocation.
        logger: Name of logger or Logger object to log to. Defaults to
            \'backoff\'.
        backoff_log_level: log level for the backoff event. Defaults to "INFO"
        giveup_log_level: log level for the give up event. Defaults to "ERROR"
        **wait_gen_kwargs: Any additional keyword args specified will be
            passed to wait_gen when it is initialized.  Any callable
            args will first be evaluated and their return values passed.
            This is useful for runtime configuration.
    '''
def on_exception(wait_gen, exception, max_tries: Incomplete | None = None, max_time: Incomplete | None = None, jitter=..., giveup=..., on_success: Incomplete | None = None, on_backoff: Incomplete | None = None, on_giveup: Incomplete | None = None, logger: str = 'backoff', backoff_log_level=..., giveup_log_level=..., **wait_gen_kwargs):
    '''Returns decorator for backoff and retry triggered by exception.

    Args:
        wait_gen: A generator yielding successive wait times in
            seconds.
        exception: An exception type (or tuple of types) which triggers
            backoff.
        max_tries: The maximum number of attempts to make before giving
            up. Once exhausted, the exception will be allowed to escape.
            The default value of None means there is no limit to the
            number of tries. If a callable is passed, it will be
            evaluated at runtime and its return value used.
        max_time: The maximum total amount of time to try for before
            giving up. Once expired, the exception will be allowed to
            escape. If a callable is passed, it will be
            evaluated at runtime and its return value used.
        jitter: A function of the value yielded by wait_gen returning
            the actual time to wait. This distributes wait times
            stochastically in order to avoid timing collisions across
            concurrent clients. Wait times are jittered by default
            using the full_jitter function. Jittering may be disabled
            altogether by passing jitter=None.
        giveup: Function accepting an exception instance and
            returning whether or not to give up. Optional. The default
            is to always continue.
        on_success: Callable (or iterable of callables) with a unary
            signature to be called in the event of success. The
            parameter is a dict containing details about the invocation.
        on_backoff: Callable (or iterable of callables) with a unary
            signature to be called in the event of a backoff. The
            parameter is a dict containing details about the invocation.
        on_giveup: Callable (or iterable of callables) with a unary
            signature to be called in the event that max_tries
            is exceeded.  The parameter is a dict containing details
            about the invocation.
        logger: Name or Logger object to log to. Defaults to \'backoff\'.
        backoff_log_level: log level for the backoff event. Defaults to "INFO"
        giveup_log_level: log level for the give up event. Defaults to "ERROR"
        **wait_gen_kwargs: Any additional keyword args specified will be
            passed to wait_gen when it is initialized.  Any callable
            args will first be evaluated and their return values passed.
            This is useful for runtime configuration.
    '''

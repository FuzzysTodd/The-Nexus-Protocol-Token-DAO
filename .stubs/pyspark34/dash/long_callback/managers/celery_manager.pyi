from _typeshed import Incomplete
from dash._callback_context import context_value as context_value
from dash._utils import AttributeDict as AttributeDict
from dash.exceptions import PreventUpdate as PreventUpdate
from dash.long_callback.managers import BaseLongCallbackManager as BaseLongCallbackManager

class CeleryManager(BaseLongCallbackManager):
    """Manage background execution of callbacks with a celery queue."""
    handle: Incomplete
    expire: Incomplete
    def __init__(self, celery_app, cache_by: Incomplete | None = None, expire: Incomplete | None = None) -> None:
        """
        Long callback manager that runs callback logic on a celery task queue,
        and stores results using a celery result backend.

        :param celery_app:
            A celery.Celery application instance that must be configured with a
            result backend. See the celery documentation for information on
            configuration options.
        :param cache_by:
            A list of zero-argument functions.  When provided, caching is enabled and
            the return values of these functions are combined with the callback
            function's input arguments and source code to generate cache keys.
        :param expire:
            If provided, a cache entry will be removed when it has not been accessed
            for ``expire`` seconds.  If not provided, the lifetime of cache entries
            is determined by the default behavior of the celery result backend.
        """
    def terminate_job(self, job) -> None: ...
    def terminate_unhealthy_job(self, job): ...
    def job_running(self, job): ...
    def make_job_fn(self, fn, progress, key: Incomplete | None = None): ...
    def get_task(self, job): ...
    def clear_cache_entry(self, key) -> None: ...
    def call_job_fn(self, key, job_fn, args, context): ...
    def get_progress(self, key): ...
    def result_ready(self, key): ...
    def get_result(self, key, job): ...

class CeleryLongCallbackManager(CeleryManager):
    """Deprecated: use `from dash import CeleryManager` instead."""

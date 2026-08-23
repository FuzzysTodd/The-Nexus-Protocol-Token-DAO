from . import BaseLongCallbackManager as BaseLongCallbackManager
from ..._callback_context import context_value as context_value
from ..._utils import AttributeDict as AttributeDict
from ...exceptions import PreventUpdate as PreventUpdate
from _typeshed import Incomplete

class DiskcacheManager(BaseLongCallbackManager):
    """Manage the background execution of callbacks with subprocesses and a diskcache result backend."""
    handle: Incomplete
    expire: Incomplete
    def __init__(self, cache: Incomplete | None = None, cache_by: Incomplete | None = None, expire: Incomplete | None = None) -> None:
        """
        Long callback manager that runs callback logic in a subprocess and stores
        results on disk using diskcache

        :param cache:
            A diskcache.Cache or diskcache.FanoutCache instance. See the diskcache
            documentation for information on configuration options. If not provided,
            a diskcache.Cache instance will be created with default values.
        :param cache_by:
            A list of zero-argument functions.  When provided, caching is enabled and
            the return values of these functions are combined with the callback
            function's input arguments and source code to generate cache keys.
        :param expire:
            If provided, a cache entry will be removed when it has not been accessed
            for ``expire`` seconds.  If not provided, the lifetime of cache entries
            is determined by the default behavior of the ``cache`` instance.
        """
    def terminate_job(self, job) -> None: ...
    def terminate_unhealthy_job(self, job): ...
    def job_running(self, job): ...
    def make_job_fn(self, fn, progress, key: Incomplete | None = None): ...
    def clear_cache_entry(self, key) -> None: ...
    def call_job_fn(self, key, job_fn, args, context): ...
    def get_progress(self, key): ...
    def result_ready(self, key): ...
    def get_result(self, key, job): ...

class DiskcacheLongCallbackManager(DiskcacheManager):
    """Deprecated: use `from dash import DiskcacheManager` instead."""

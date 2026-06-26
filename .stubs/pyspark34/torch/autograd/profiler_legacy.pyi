from _typeshed import Incomplete

__all__ = ['profile']

class profile:
    """DEPRECATED: use torch.profiler instead"""
    enabled: Incomplete
    use_cuda: Incomplete
    function_events: Incomplete
    entered: bool
    record_shapes: Incomplete
    with_flops: Incomplete
    profile_memory: Incomplete
    with_stack: Incomplete
    with_modules: Incomplete
    profiler_kind: Incomplete
    def __init__(self, enabled: bool = True, *, use_cuda: bool = False, record_shapes: bool = False, with_flops: bool = False, profile_memory: bool = False, with_stack: bool = False, with_modules: bool = False) -> None: ...
    def config(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...
    def table(self, sort_by: Incomplete | None = None, row_limit: int = 100, max_src_column_width: int = 75, max_name_column_width: int = 55, max_shapes_column_width: int = 80, header: Incomplete | None = None, top_level_events_only: bool = False): ...
    def export_chrome_trace(self, path): ...
    def export_stacks(self, path: str, metric: str = 'self_cpu_time_total'): ...
    def key_averages(self, group_by_input_shape: bool = False, group_by_stack_n: int = 0): ...
    def total_average(self): ...
    @property
    def self_cpu_time_total(self):
        """ Returns total time spent on CPU obtained as a sum of
        all self times across all the events.
        """

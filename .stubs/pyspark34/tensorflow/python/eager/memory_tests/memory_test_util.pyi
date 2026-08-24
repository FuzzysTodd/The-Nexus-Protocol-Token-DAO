from tensorflow.python.eager import context as context

def assert_no_leak(f, num_iters: int = 100000, increase_threshold_absolute_mb: int = 10) -> None:
    """Assert memory usage doesn't increase beyond given threshold for f."""
def memory_profiler_is_available(): ...

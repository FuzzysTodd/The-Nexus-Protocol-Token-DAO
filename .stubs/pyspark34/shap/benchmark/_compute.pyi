from ._result import BenchmarkResult as BenchmarkResult

class ComputeTime:
    """ Extracts a runtime benchmark result from the passed Explanation.
    """
    def __call__(self, explanation, name): ...

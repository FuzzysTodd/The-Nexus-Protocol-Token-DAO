from _typeshed import Incomplete

class LazyEvaluate:
    """This is used for formatting strings with values that need to be updated
    at that time, such as the current time or working directory."""
    func: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, func, *args, **kwargs) -> None: ...
    def __call__(self, **kwargs): ...
    def __format__(self, format_spec) -> str: ...

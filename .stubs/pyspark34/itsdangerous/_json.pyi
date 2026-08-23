import typing as _t

class _CompactJSON:
    """Wrapper around json module that strips whitespace."""
    @staticmethod
    def loads(payload: str | bytes) -> _t.Any: ...
    @staticmethod
    def dumps(obj: _t.Any, **kwargs: _t.Any) -> str: ...

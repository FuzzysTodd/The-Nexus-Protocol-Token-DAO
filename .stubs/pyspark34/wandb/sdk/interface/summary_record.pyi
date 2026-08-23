import typing as t

class SummaryRecord:
    """Encodes a diff -- analogous to the SummaryRecord protobuf message."""
    update: t.List['SummaryItem']
    remove: t.List['SummaryItem']
    def __init__(self) -> None: ...

class SummaryItem:
    """Analogous to the SummaryItem protobuf message."""
    key: t.Tuple[str]
    value: t.Any
    def __init__(self) -> None: ...

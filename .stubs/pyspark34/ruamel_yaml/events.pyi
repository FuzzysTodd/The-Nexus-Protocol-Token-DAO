from _typeshed import Incomplete
from typing import Any

def CommentCheck() -> None: ...

class Event:
    start_mark: Incomplete
    end_mark: Incomplete
    comment: Incomplete
    def __init__(self, start_mark: Any = None, end_mark: Any = None, comment: Any = ...) -> None: ...

class NodeEvent(Event):
    anchor: Incomplete
    def __init__(self, anchor: Any, start_mark: Any = None, end_mark: Any = None, comment: Any = None) -> None: ...

class CollectionStartEvent(NodeEvent):
    tag: Incomplete
    implicit: Incomplete
    flow_style: Incomplete
    nr_items: Incomplete
    def __init__(self, anchor: Any, tag: Any, implicit: Any, start_mark: Any = None, end_mark: Any = None, flow_style: Any = None, comment: Any = None, nr_items: int | None = None) -> None: ...

class CollectionEndEvent(Event): ...

class StreamStartEvent(Event):
    encoding: Incomplete
    def __init__(self, start_mark: Any = None, end_mark: Any = None, encoding: Any = None, comment: Any = None) -> None: ...

class StreamEndEvent(Event): ...

class DocumentStartEvent(Event):
    explicit: Incomplete
    version: Incomplete
    tags: Incomplete
    def __init__(self, start_mark: Any = None, end_mark: Any = None, explicit: Any = None, version: Any = None, tags: Any = None, comment: Any = None) -> None: ...

class DocumentEndEvent(Event):
    explicit: Incomplete
    def __init__(self, start_mark: Any = None, end_mark: Any = None, explicit: Any = None, comment: Any = None) -> None: ...

class AliasEvent(NodeEvent): ...

class ScalarEvent(NodeEvent):
    tag: Incomplete
    implicit: Incomplete
    value: Incomplete
    style: Incomplete
    def __init__(self, anchor: Any, tag: Any, implicit: Any, value: Any, start_mark: Any = None, end_mark: Any = None, style: Any = None, comment: Any = None) -> None: ...

class SequenceStartEvent(CollectionStartEvent): ...
class SequenceEndEvent(CollectionEndEvent): ...
class MappingStartEvent(CollectionStartEvent): ...
class MappingEndEvent(CollectionEndEvent): ...

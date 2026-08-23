from _typeshed import Incomplete
from greenlet import greenlet

__all__ = ['TrackedRawGreenlet', 'SwitchOutGreenletWithLoop']

class TrackedRawGreenlet(greenlet):
    spawning_greenlet: Incomplete
    spawn_tree_locals: Incomplete
    def __init__(self, function, parent) -> None: ...

class SwitchOutGreenletWithLoop(TrackedRawGreenlet):
    def switch(self): ...
    def switch_out(self) -> None: ...

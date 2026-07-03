from .utils import ExactWeakKeyDictionary as ExactWeakKeyDictionary
from _typeshed import Incomplete
from torch.nn import Module as Module

class MutationTracker:
    db: Incomplete
    mutation_count: int
    watchers: Incomplete
    def __init__(self) -> None: ...
    def on_mutation(self, name) -> None: ...
    def track(self, guarded_code) -> None: ...

def watch(obj, guarded_code) -> None:
    """invalidate guarded_code when obj is mutated"""
def ensure_patched(cls): ...

class GenerationTracker:
    generation: int
    dynamic_classes: Incomplete
    generation_values: Incomplete
    @classmethod
    def tag(cls, obj) -> None: ...
    @staticmethod
    def mark_class_dynamic(cls) -> None: ...
    @classmethod
    def get_generation_value(cls, obj): ...
    @classmethod
    def check(cls, obj): ...

def is_dynamic_nn_module(obj):
    """Check for nn.Modules() created dynamically or mutated"""
def install_generation_tagging_init() -> None:
    """
    Monkey patch torch.nn.Module.__init__ and torch.nn.Module.__setstate__
    so we can detect nn.Module instances created dynamically inside forward methods.
    """

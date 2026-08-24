from mypy.nodes import FakeInfo as FakeInfo, Node as Node
from mypy.types import Type as Type
from mypy.util import get_class_descriptors as get_class_descriptors

def collect_memory_stats() -> tuple[dict[str, int], dict[str, int]]:
    """Return stats about memory use.

    Return a tuple with these items:
      - Dict from object kind to number of instances of that kind
      - Dict from object kind to total bytes used by all instances of that kind
    """
def print_memory_profile(run_gc: bool = True) -> None: ...
def find_recursive_objects(objs: list[object]) -> None:
    """Find additional objects referenced by objs and append them to objs.

    We use this since gc.get_objects() does not return objects without pointers
    in them such as strings.
    """

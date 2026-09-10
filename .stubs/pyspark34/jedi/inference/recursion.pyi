from _typeshed import Incomplete
from collections.abc import Generator
from jedi import debug as debug
from jedi.inference.base_value import NO_VALUES as NO_VALUES

recursion_limit: int
total_function_execution_limit: int
per_function_execution_limit: int
per_function_recursion_limit: int

class RecursionDetector:
    pushed_nodes: Incomplete
    def __init__(self) -> None: ...

def execution_allowed(inference_state, node) -> Generator[Incomplete, None, None]:
    """
    A decorator to detect recursions in statements. In a recursion a statement
    at the same place, in the same module may not be executed two times.
    """
def execution_recursion_decorator(default=...): ...

class ExecutionRecursionDetector:
    """
    Catches recursions of executions.
    """
    def __init__(self, inference_state) -> None: ...
    def pop_execution(self) -> None: ...
    def push_execution(self, execution): ...

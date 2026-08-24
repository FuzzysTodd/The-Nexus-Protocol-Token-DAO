from ..sample import Categorical as Categorical, Domain as Domain, RandomState as RandomState
from _typeshed import Incomplete
from typing import Any, Dict, Generator, List, Tuple

RayDomain = Domain
logger: Incomplete

class TuneError(Exception):
    """General error class raised by ray.tune."""

def generate_variants(unresolved_spec: Dict, constant_grid_search: bool = False, random_state: RandomState = None) -> Generator[Tuple[Dict, Dict], None, None]:
    '''Generates variants from a spec (dict) with unresolved values.
    There are two types of unresolved values:
        Grid search: These define a grid search over values. For example, the
        following grid search values in a spec will produce six distinct
        variants in combination:
            "activation": grid_search(["relu", "tanh"])
            "learning_rate": grid_search([1e-3, 1e-4, 1e-5])
        Lambda functions: These are evaluated to produce a concrete value, and
        can express dependencies or conditional distributions between values.
        They can also be used to express random search (e.g., by calling
        into the `random` or `np` module).
            "cpu": lambda spec: spec.config.num_workers
            "batch_size": lambda spec: random.uniform(1, 1000)
    Finally, to support defining specs in plain JSON / YAML, grid search
    and lambda functions can also be defined alternatively as follows:
        "activation": {"grid_search": ["relu", "tanh"]}
        "cpu": {"eval": "spec.config.num_workers"}
    Use `format_vars` to format the returned dict of hyperparameters.
    Yields:
        (Dict of resolved variables, Spec object)
    '''
def grid_search(values: List) -> Dict[str, List]:
    """Convenience method for specifying grid search over a value.
    Arguments:
        values: An iterable whose parameters will be gridded.
    """
def parse_spec_vars(spec: Dict) -> Tuple[List[Tuple[Tuple, Any]], List[Tuple[Tuple, Any]], List[Tuple[Tuple, Any]]]: ...
def assign_value(spec: Dict, path: Tuple, value: Any): ...
def has_unresolved_values(spec: Dict) -> bool: ...

class _UnresolvedAccessGuard(dict):
    __dict__: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def __getattribute__(self, item): ...

class RecursiveDependencyError(Exception):
    def __init__(self, msg: str) -> None: ...

from . import sample as sample
from .searcher.variant_generator import generate_variants as generate_variants
from _typeshed import Incomplete
from typing import Any, Dict, Generator, List, Tuple

logger: Incomplete

def generate_variants_compatible(unresolved_spec: Dict, constant_grid_search: bool = False, random_state: Incomplete | None = None) -> Generator[Tuple[Dict, Dict], None, None]: ...
def is_constant(space: Dict | List) -> bool:
    """Whether the search space is all constant.

    Returns:
        A bool of whether the search space is all constant.
    """
def define_by_run_func(trial, space: Dict, path: str = '') -> Dict[str, Any] | None:
    """Define-by-run function to create the search space.

    Returns:
        A dict with constant values.
    """
def unflatten_hierarchical(config: Dict, space: Dict) -> Tuple[Dict, Dict]:
    """Unflatten hierarchical config."""
def add_cost_to_space(space: Dict, low_cost_point: Dict, choice_cost: Dict):
    """Update the space in place by adding low_cost_point and choice_cost.

    Returns:
        A dict with constant values.
    """
def normalize(config: Dict, space: Dict, reference_config: Dict, normalized_reference_config: Dict, recursive: bool = False):
    """Normalize config in space according to reference_config.

    Normalize each dimension in config to [0,1].
    """
def denormalize(config: Dict, space: Dict, reference_config: Dict, normalized_reference_config: Dict, random_state): ...
def equal(config, const) -> bool: ...
def indexof(domain: Dict, config: Dict) -> int:
    """Find the index of config in domain.categories."""
def complete_config(partial_config: Dict, space: Dict, flow2, disturb: bool = False, lower: Dict | None = None, upper: Dict | None = None) -> Tuple[Dict, Dict]:
    """Complete partial config in space.

    Returns:
        config, space.
    """

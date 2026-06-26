from typing import Any, Callable, Dict, TypeVar

FuncT = TypeVar('FuncT', bound=Callable[..., Any])
requirement_env_var_mapping: Dict[str, str]

def requires(requirement: str) -> FuncT:
    """Decorate functions to gate features with wandb.require."""

class RequiresMixin:
    requirement: str
    def __init__(self) -> None: ...
    def __post_init__(self) -> None: ...

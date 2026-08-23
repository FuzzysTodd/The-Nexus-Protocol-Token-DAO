from .registry import CollectorRegistry as CollectorRegistry, REGISTRY as REGISTRY
from typing import Callable

def make_asgi_app(registry: CollectorRegistry = ..., disable_compression: bool = False) -> Callable:
    """Create a ASGI app which serves the metrics from a registry."""

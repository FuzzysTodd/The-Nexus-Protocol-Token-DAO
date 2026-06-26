from jupyter_core.utils import ensure_async as ensure_async, run_sync as run_sync
from typing import Any, Callable

async def run_hook(hook: Callable | None, **kwargs: Any) -> None:
    """Run a hook callback."""

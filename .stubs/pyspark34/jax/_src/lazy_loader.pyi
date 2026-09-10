from collections.abc import Sequence
from typing import Any, Callable

def attach(package_name: str, submodules: Sequence[str]) -> tuple[Callable[[str], Any], Callable[[], list[str]], list[str]]:
    '''Lazily loads submodules of a package.

  Example use:
  ```
  __getattr__, __dir__, __all__ = lazy_loader.attach(__name__, ["sub1", "sub2"])
  ```
  '''

from pathlib import Path
from typing import Callable, Generator

yaml_dump: Callable[..., str]

def SoftTemporaryDirectory(suffix: str | None = None, prefix: str | None = None, dir: Path | str | None = None, **kwargs) -> Generator[str, None, None]:
    """
    Context manager to create a temporary directory and safely delete it.

    If tmp directory cannot be deleted normally, we set the WRITE permission and retry.
    If cleanup still fails, we give up but don't raise an exception. This is equivalent
    to  `tempfile.TemporaryDirectory(..., ignore_cleanup_errors=True)` introduced in
    Python 3.10.

    See https://www.scivision.dev/python-tempfile-permission-error-windows/.
    """

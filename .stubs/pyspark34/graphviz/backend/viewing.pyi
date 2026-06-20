import os

__all__ = ['view']

def view(filepath: os.PathLike | str, quiet: bool = False) -> None:
    """Open filepath with its default viewing application (platform-specific).

    Args:
        filepath: Path to the file to open in viewer.
        quiet: Suppress ``stderr`` output
            from the viewer process (ineffective on Windows).

    Raises:
        RuntimeError: If the current platform is not supported.

    Note:
        There is no option to wait for the application to close,
        and no way to retrieve the application's exit status.
    """
